"""
MkDocs hook: strip headerlink anchors from RSS feeds.

MkDocs Material adds ¶ permalink anchors to every heading via `toc.permalink: true`.
These bleed into the RSS feed as broken relative links (e.g. href="#some-heading").
This hook removes them from the generated XML files after each build.
"""

import os
import re


def on_post_build(config, **kwargs):
    site_dir = config["site_dir"]

    for feed_file in ("feed_rss_created.xml", "feed_rss_updated.xml"):
        feed_path = os.path.join(site_dir, feed_file)
        if not os.path.exists(feed_path):
            continue

        with open(feed_path, "r", encoding="utf-8") as f:
            content = f.read()

        # The RSS description content is HTML-escaped inside XML, so < > " appear as
        # &lt; &gt; &#34; / &quot;.  The headerlink pattern looks like:
        #   &lt;a class=&#34;headerlink&#34; href=&#34;#slug&#34; title=...&gt;&amp;para;&lt;/a&gt;
        #
        # Tempered greedy token (?:(?!&gt;).)* matches "any char not starting &gt;"
        # so we stay inside the opening tag without crossing into its body.
        cleaned = re.sub(
            r'&lt;a\b(?:(?!&gt;).)*?headerlink(?:(?!&gt;).)*?&gt;.*?&lt;/a&gt;',
            "",
            content,
            flags=re.DOTALL,
        )

        removed = content.count("headerlink") - cleaned.count("headerlink")

        with open(feed_path, "w", encoding="utf-8") as f:
            f.write(cleaned)

        print(f"[rss-cleanup] {feed_file}: removed {removed} headerlink anchor(s)")
