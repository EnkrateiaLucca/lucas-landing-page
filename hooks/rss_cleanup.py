"""
MkDocs hook: clean code blocks and headerlinks from RSS feeds.

Problems solved:
  1. MkDocs Material adds ¶ permalink anchors to headings → broken relative links in RSS.
  2. Pygments syntax-highlight <span> tags clutter code blocks with CSS-class markup
     that is meaningless without an external stylesheet (e.g. Gmail / ConvertKit).
  3. The RSS plugin's Jinja2 template strips all newlines, collapsing code to one line.
  4. <pre> tags have no inline styles → email clients don't apply monospace/pre-wrap.

Strategy (two-phase):
  Phase 1 — on_page_content (priority 0, runs before RSS plugin at priority -75):
    • Clean the rendered page HTML.
    • Strip Pygments <span> tags from code blocks.
    • Add inline styles to <pre> tags (survives Gmail's CSS stripping).
    • Replace \\n inside code blocks with ##RSS_NL## so they survive the RSS
      plugin's newline-stripping Jinja2 pass.
    • Store the result in page.meta["rss"]["feed_description"] — the RSS plugin
      reads this field and skips its own content processing.
    • Return the original output unchanged (site pages are NOT affected).

  Phase 2 — on_post_build:
    • Replace every ##RSS_NL## placeholder with a real newline character.
    • Strip any remaining headerlinks as a safety net.
"""

import os
import re
from urllib.parse import urljoin

# Gmail strips external stylesheets; inline styles are the only reliable option.
PRE_STYLE = (
    "font-family:'Courier New',Courier,monospace;"
    "font-size:13px;"
    "line-height:1.6;"
    "background-color:#f6f8fa;"
    "padding:16px;"
    "border-radius:6px;"
    "white-space:pre-wrap;"
    "border:1px solid #e1e4e8;"
    "display:block;"
    "overflow-x:auto;"
)

TABLE_STYLE = (
    "border-collapse:collapse;"
    "width:100%;"
    "margin:16px 0;"
    "font-size:14px;"
    "border:1px solid #e1e4e8;"
)

TH_STYLE = (
    "background-color:#f6f8fa;"
    "border:1px solid #e1e4e8;"
    "padding:8px 12px;"
    "text-align:left;"
    "font-weight:600;"
)

TD_STYLE = (
    "border:1px solid #e1e4e8;"
    "padding:8px 12px;"
    "vertical-align:top;"
)

IMG_STYLE = (
    "max-width:100%;"
    "height:auto;"
    "display:block;"
    "margin:16px 0;"
)

# Placeholder that survives the RSS plugin's newline-stripping Jinja2 pass.
# Contains no XML/HTML special characters, so it passes through escaping unchanged.
_NL = "##RSS_NL##"


def _add_style(tag, style):
    """Inject an inline style attribute into an HTML opening tag string."""
    # If the tag already has a style attribute, prepend to it
    if re.search(r'\bstyle\s*=', tag):
        return re.sub(r'style\s*=\s*"', f'style="{style}', tag)
    # Otherwise insert before the closing >
    return re.sub(r'\s*/?>', f' style="{style}">', tag, count=1)


def _style_tables(html):
    """Add inline styles to table elements so Gmail renders them correctly."""
    html = re.sub(r'<table\b[^>]*>', lambda m: _add_style(m.group(0), TABLE_STYLE), html)
    html = re.sub(r'<th\b[^>]*>', lambda m: _add_style(m.group(0), TH_STYLE), html)
    html = re.sub(r'<td\b[^>]*>', lambda m: _add_style(m.group(0), TD_STYLE), html)
    return html


def _fix_images(html, page_url):
    """Convert relative img src paths to absolute URLs and add responsive inline styles."""
    def _process_img(match):
        tag = match.group(0)
        # Resolve relative src to absolute URL
        src_match = re.search(r'src=["\']([^"\']+)["\']', tag)
        if src_match:
            src = src_match.group(1)
            if not src.startswith(("http://", "https://", "//")):
                abs_src = urljoin(page_url, src)
                tag = tag.replace(src_match.group(1), abs_src)
        # Add responsive inline styles
        tag = _add_style(tag, IMG_STYLE)
        return tag

    return re.sub(r'<img\b[^>]*/?>', _process_img, html)


def _process_code_block(match):
    """Strip Pygments spans, add inline styles, encode newlines as placeholder."""
    block = match.group(0)
    # Remove Pygments syntax-highlight span tags (keep text content and \n between them)
    block = re.sub(r"<span[^>]*>", "", block)
    block = block.replace("</span>", "")
    # Style the <pre> tag for email clients
    block = block.replace("<pre>", f'<pre style="{PRE_STYLE}">')
    # Encode newlines so they survive the RSS plugin's compression pass
    block = block.replace("\n", _NL)
    return block


def _clean_for_rss(html, page_url):
    """Return cleaned HTML suitable for RSS description content."""
    # 1. Remove headerlink anchors (the ¶ permalink symbols added by toc.permalink)
    html = re.sub(
        r'<a[^>]*class="headerlink"[^>]*>.*?</a>',
        "",
        html,
        flags=re.DOTALL,
    )
    # 2. Process code blocks: strip spans, add inline styles, preserve newlines
    html = re.sub(
        r'<div class="highlight">.*?</div>',
        _process_code_block,
        html,
        flags=re.DOTALL,
    )
    # 3. Style tables with inline CSS for email clients
    html = _style_tables(html)
    # 4. Fix images: resolve relative src paths and add responsive styles
    html = _fix_images(html, page_url)
    # 5. Remove the <!-- more --> excerpt marker (MkDocs artifact, noise in email)
    html = html.replace("<!-- more -->", "")
    return html


def on_page_content(output, page, config, **kwargs):
    """
    Intercept page HTML before the RSS plugin processes it.

    Our hook runs at default priority 0; the RSS plugin runs at -75 (lower = later).
    By setting page.meta["rss"]["feed_description"] here, the RSS plugin will use
    our pre-cleaned HTML and skip its own content extraction entirely.

    The original `output` is returned unchanged so site pages are unaffected.
    """
    # Only process pages included in the RSS feed
    if not re.search(r"blog/posts/", page.file.src_path):
        return output

    # Respect any feed_description the author set manually in front matter
    if page.meta.get("rss", {}).get("feed_description"):
        return output

    cleaned = _clean_for_rss(output, page.canonical_url)
    page.meta.setdefault("rss", {})["feed_description"] = cleaned
    return output  # site page is untouched


def on_post_build(config, **kwargs):
    """
    After the RSS plugin generates the XML files, restore newlines inside code
    blocks and strip any remaining headerlinks.
    """
    site_dir = config["site_dir"]

    for feed_file in ("feed_rss_created.xml", "feed_rss_updated.xml"):
        feed_path = os.path.join(site_dir, feed_file)
        if not os.path.exists(feed_path):
            continue

        with open(feed_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Restore encoded newlines inside code blocks
        nl_count = content.count(_NL)
        content = content.replace(_NL, "\n")

        # Safety net: strip headerlinks that slipped through (escaped HTML form)
        hl_count = content.count("headerlink")
        content = re.sub(
            r"&lt;a\b(?:(?!&gt;).)*?headerlink(?:(?!&gt;).)*?&gt;.*?&lt;/a&gt;",
            "",
            content,
            flags=re.DOTALL,
        )

        with open(feed_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(
            f"[rss-cleanup] {feed_file}: "
            f"restored {nl_count} newlines in code blocks, "
            f"removed {hl_count} headerlinks"
        )
