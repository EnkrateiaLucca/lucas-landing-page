# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Lucas Soares' personal blog and landing page built with MkDocs and Material theme. Features technical articles on AI, machine learning, and software engineering.

## Commands

### Development
```bash
# Install dependencies
pip install mkdocs-material

# Start development server with live reload
mkdocs serve

# Development server on custom port
mkdocs serve -a localhost:8001
```

### Build & Deploy
```bash
# Build static site to site/ directory
mkdocs build

# Deploy to GitHub Pages (gh-pages branch)
mkdocs gh-deploy

# Force push deployment
mkdocs gh-deploy --force
```

## Architecture

### Tech Stack
- **Static Site Generator**: MkDocs with Material theme
- **Hosting**: GitHub Pages (gh-pages branch)
- **Content Format**: Markdown with YAML front matter

### Project Structure
```
docs/
├── blog/
│   ├── posts/          # Blog posts (YYYY-MM-DD-title.md format)
│   └── assets/         # Shared images and resources
├── courses/
│   └── index.md        # Courses listing page
├── about.md
├── index.md
└── style.css           # Custom CSS overrides (typography/spacing)

mkdocs.yml              # Main configuration
```

### Blog Post Front Matter
```yaml
---
title: Post Title
date: YYYY-MM-DD
slug: url-slug          # Optional, defaults to filename
categories:
  - Category Name
tags:
  - tag1
excerpt: One-line summary shown in post listings
---

<!-- more -->           # Required: marks excerpt boundary
```

The `excerpt:` field and `<!-- more -->` are both used — `excerpt` is metadata, `<!-- more -->` marks the content split. Both are needed.

### Active Content Categories
- AI Best Practices
- LLM Development
- Technical Guides
- Machine Learning Fundamentals
- Learning Resources
- Software Engineering
- Personal Updates

### Key Configuration (mkdocs.yml)

**Plugins:** `blog` (date-based URLs `YYYY/MM/DD/{slug}/`), `search`

**Notable markdown extensions:** `admonition`, `footnotes`, `pymdownx.arithmatex` (math), `pymdownx.superfences` (code blocks), `pymdownx.tabbed`, `pymdownx.tasklist`

### Development Notes

- Site navigation is defined in `mkdocs.yml` under `nav:` — add new top-level sections there
- Images go in `docs/blog/assets/`; reference with relative paths: `../assets/image.png`
- Site builds to `site/` (gitignored)
- URL format: `YYYY/MM/DD/{slug}/` — changing a slug or date breaks existing links
