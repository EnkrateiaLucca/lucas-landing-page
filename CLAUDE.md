# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is Lucas Soares' personal blog and landing page built with MkDocs and Material theme. The site features technical articles on AI, machine learning, and software engineering, with a focus on educational content and documentation.

## Commands

### Development
```bash
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
- **Static Site Generator**: MkDocs 1.6.1
- **Theme**: Material for MkDocs 9.5.45
- **Hosting**: GitHub Pages (gh-pages branch)
- **Content Format**: Markdown with YAML front matter

### Project Structure
```
docs/                     # All content files
├── blog/                # Blog system
│   ├── posts/          # Blog posts (YYYY-MM-DD-title.md format)
│   ├── assets/         # Shared images and resources
│   └── .authors.yml    # Author metadata
├── about.md            # About page
├── index.md            # Homepage content
└── style.css           # Custom CSS overrides

mkdocs.yml              # Main configuration
requirements.txt        # Python dependencies
```

### Blog Post Structure
Posts require specific front matter:
```yaml
---
authors:
  - lucassoares
date: YYYY-MM-DD
slug: url-slug
title: Post Title
categories:
  - Category Name
tags:
  - tag1
  - tag2
image: blog/assets/image.png  # Optional
---
```

Posts must include `<!-- more -->` to mark the excerpt boundary.

### Content Categories
- AI Best Practices
- Technical Guides
- Machine Learning Fundamentals
- Learning Resources
- Software Engineering
- Personal Updates

### Key Configuration (mkdocs.yml)

**Plugins Enabled:**
- `blog`: Handles blog functionality with date-based URLs
- `search`: Site-wide search
- `meta`: Process meta tags
- `glightbox`: Image lightbox functionality

**Blog Configuration:**
- Posts per page: 10
- URL format: `YYYY/MM/DD/{slug}/`
- Archives enabled with yearly/monthly views
- Categories and tags enabled
- Pagination enabled

### Development Notes

- All blog images should be placed in `docs/blog/assets/` and referenced relatively
- Site builds to `site/` directory (gitignored)
- Custom styling in `docs/style.css` - mainly typography and spacing adjustments
- Navigation defined in mkdocs.yml - includes auto-generated blog sections
- Author information centralized in `docs/blog/.authors.yml`

### Asset Management
- Images: Store in `docs/blog/assets/` with descriptive names
- Use relative paths in Markdown: `![Alt text](../assets/image.png)`
- Optimize images before committing (prefer WebP/PNG for diagrams, JPEG for photos)