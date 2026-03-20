---
skill: write-blog-post
description: Write a first draft of a new blog post following Lucas's style, structure, and conventions
---

# Blog Post Writing Skill

This skill helps you write a first draft of a blog post for Lucas Soares' personal blog, following his established style, structure, and conventions.

## Overview

When the user invokes this skill, you will:
1. Ask clarifying questions about the blog post topic and scope
2. Create a new blog post file with proper naming and front matter
3. Write a first draft following Lucas's writing style
4. Start the MkDocs dev server so the user can preview the post
5. Open the post in the browser for review

## File Structure & Naming

**Blog posts location:** `docs/blog/posts/`

**File naming convention:** `YYYY-MM-DD-title-with-hyphens.md`
- Date should be today's date (2026-01-30)
- Title should be lowercase with hyphens between words
- Example: `2026-01-30-building-ai-agents-with-langgraph.md`

## Front Matter Templates

### Minimal Front Matter (Default)
Use this for most posts:

```yaml
---
title: Your Post Title Here
date: YYYY-MM-DD

# Your Post Title Here
---
```

### Extended Front Matter (Optional)
Use this for posts where you want to specify categories and a custom excerpt:

```yaml
---
title: Your Post Title Here
date: YYYY-MM-DD
categories:
  - Category Name
  - Another Category
excerpt: A brief description of what this post is about (1-2 sentences)
---
```

**Common categories:**
- AI Best Practices
- LLM Development
- Technical Guides
- Building Agents
- Learning Resources
- Software Engineering
- Personal Updates

## Post Structure

### Required Elements

1. **Front Matter** (see templates above)
2. **Excerpt Marker** - Always include `<!-- more -->` immediately after front matter
3. **Title as H1** - Repeat the title as a level 1 heading after the excerpt marker
4. **Content** - Your main blog post content
5. **CTAs** - Include newsletter/YouTube subscription buttons at the end

### Standard Structure Template

```markdown
---
title: Your Post Title
date: YYYY-MM-DD

# Your Post Title
---

<!-- more -->

# Your Post Title

[Opening paragraph that hooks the reader and sets context. Usually 2-3 sentences introducing the topic and why it matters.]

## Main Section 1

[Content organized with clear headings and subheadings]

### Subsection

[Detailed explanation with examples]

## Main Section 2

[Continue with your content...]

## Conclusion (optional)

[Wrap up the key points]

---

[Subscribe to my Newsletter](https://automata-learning-lab.kit.com/ccd5287996){ .md-button .md-button--primary }

---

## Sources and Further Reading (if applicable)
[List of references, links, etc.]
```

## Writing Style Guide

### Voice & Tone

**Core characteristics:**
- **Conversational and personal** - Write like you're explaining to a friend
- **Educational but accessible** - Teach complex topics without being condescating
- **Reflective** - Share personal experiences and the learning journey
- **Pragmatic** - Focus on practical applications, not just theory
- **Honest and humble** - Admit gaps, share failures, invite discussion

**Common phrases to use:**
- "The way I like to think about..."
- "Let me break this down..."
- "I've found that..."
- "Here's what I mean by that..."
- "In my experience..."
- "To put it simply..."
- "The interesting thing is..."

**Tone indicators:**
- Use first person ("I think", "I've noticed", "In my view")
- Ask rhetorical questions to engage readers
- Use concrete examples and scenarios
- Include personal anecdotes when relevant
- Acknowledge complexity while making it understandable

### Content Organization

**Opening patterns:**
- Start with personal context or motivation
- Set up the "why" before the "what"
- Hook with a relatable problem or observation
- Keep it conversational and engaging

**Body patterns:**
- Use hierarchical headings (H2, H3, H4) for structure
- Break complex ideas into digestible chunks
- Include concrete examples and code snippets
- Use bullet points for lists and key takeaways
- Add visual aids when helpful (images, diagrams)
- Use collapsible sections for supplementary details

**Conclusion patterns:**
- Summarize key takeaways (optional - many posts don't have explicit conclusions)
- Reinforce practical applications
- Invite further exploration

### Formatting Conventions

**Emphasis:**
- Use **bold** for key concepts and important terms
- Use *italics* for emphasis or to highlight nuances
- Use `inline code` for technical terms, commands, file names

**Code blocks:**
```python
# Always include language identifier
# Add comments to explain what's happening
# Keep examples practical and runnable
```

**Links:**
- Use descriptive link text (not "click here")
- Inline links naturally in the flow
- Link to authoritative sources
- **IMPORTANT - Inline Citations**: When making specific claims, statistics, or quotes that come from sources, hyperlink them directly inline using `[claim or statement](source-url)`. This validates claims and provides readers immediate access to sources.
  - Example: `[Anthropic's engineering team measured this waste: **150,000 tokens reduced to 2,000 tokens**](https://anthropic.com/engineering/...)`
  - Example: `[Using Claude-generated skills, some open models saw +45% accuracy improvements](https://huggingface.co/blog/...)`
  - Apply to: specific statistics, direct quotes, surprising claims, performance metrics, study results
  - Don't overdo it: General knowledge or commonly understood facts don't need inline citations

**Source Quality Guidelines - CRITICAL**:
- **For validating claims** (technical statements, research findings, performance metrics, quotes):
  - ✅ USE: Papers, scientific resources, official company engineering blogs (e.g., Anthropic, Google, OpenAI), reputable tech journalism (e.g., VentureBeat, The New Stack), technical documentation from authoritative sources
  - ❌ AVOID: Medium articles, LinkedIn posts, GitHub repos, personal blogs (unless if from reputable engineers and/or authors)

- **For basic information** (tool availability, project stats, observable facts):
  - ✅ USE: GitHub repos (for repo stats, tool references), marketplace sites (for their own stats), community resources
  - ✅ ACCEPTABLE: Medium articles, LinkedIn posts (only for describing observable facts, not validating claims)

- **Examples**:
  - ❌ BAD: `[Key insight: "Context windows are constrained by attention mechanics"](https://github.com/user/repo)` - Technical claim should not cite GitHub repo
  - ✅ GOOD: `[The anthropics/skills GitHub repository has 58.8k stars](https://github.com/anthropics/skills)` - Repo stats can cite GitHub
  - ❌ BAD: `[Models achieve 45% improvement](https://linkedin.com/posts/...)` - Research finding should not cite LinkedIn
  - ✅ GOOD: `[Models achieve 45% improvement](https://huggingface.co/blog/...)` - Research finding from authoritative technical source

**Collapsible sections (use when appropriate):**
```markdown
??? note "Expandable Section Title"
    Content that can be expanded/collapsed
    Use for supplementary details or advanced topics
```

**Images:**
- Store in `docs/blog/assets/` directory
- Reference with relative paths: `![Alt text](../assets/image-name.png)`
- Include descriptive alt text
- Credit AI-generated images: `*[Image generated with GPT-4o](https://chatgpt.com/)*`

**Block quotes:**
> Use for highlighting important concepts or key takeaways
> Keep them concise and impactful

**Lists:**
- Use unordered lists (bullets) for non-sequential items
- Use ordered lists for step-by-step instructions
- Nest bullets for hierarchical information

## Common Content Patterns

### Technical Explanations
- Define terms clearly when first introduced
- Build from simple to complex
- Use analogies to make abstract concepts concrete
- Provide practical examples alongside theory

### Code Examples
- Keep them focused and relevant
- Add inline comments for clarity
- Show both the code and what it does
- Prefer complete, runnable examples

### Tutorials/How-To
- Clear step-by-step instructions
- Numbered lists for sequential steps
- Include expected outcomes
- Mention common pitfalls

### Opinion/Analysis Pieces
- Acknowledge different perspectives
- Support claims with examples or evidence
- Use personal experience to illustrate points
- Invite discussion and alternative views

## Required CTAs (Call-to-Action)

**CRITICAL**: Always include the newsletter subscription button at the end of every post, BEFORE any "Sources" or reference sections.

Format:
```markdown
---

[Subscribe to my Newsletter](https://automata-learning-lab.kit.com/ccd5287996){ .md-button .md-button--primary }

---

## Sources and Further Reading
[rest of content...]
```

The newsletter button must be:
1. Placed after the conclusion/final paragraph
2. Surrounded by `---` separators above and below
3. Before any "Sources", "References", or "Further Reading" sections

## MkDocs Commands

After creating the post, use these commands:

**Start development server:**
```bash
mkdocs serve
```
This starts a live-reload server at `http://127.0.0.1:8000/`

**Start on custom port:**
```bash
mkdocs serve -a localhost:8001
```

**Build static site:**
```bash
mkdocs build
```

**Deploy to GitHub Pages:**
```bash
mkdocs gh-deploy
```

## Workflow

When the user invokes this skill:

1. **Ask clarifying questions:**
   - What's the topic of the blog post?
   - What's the target length? (short note ~500 words, medium article ~2000 words, comprehensive guide ~5000+ words)
   - Are there specific points or sections to include?
   - Any specific examples or resources to reference?
   - Should this use minimal or extended front matter?

2. **Create the blog post file:**
   - Use today's date (2026-01-30)
   - Create filename following convention
   - Add appropriate front matter
   - Include `<!-- more -->` excerpt marker
   - Write the first draft following style guidelines

3. **Start the dev server:**
   - Run `mkdocs serve` in the background
   - Wait for it to start successfully

4. **Open in browser:**
   - Navigate to the blog post URL in the default browser
   - URL format: `http://127.0.0.1:8000/blog/YYYY/MM/DD/post-slug/`
   - Example: `http://127.0.0.1:8000/blog/2026/01/30/building-ai-agents-with-langgraph/`

5. **Inform the user:**
   - Confirm the post has been created
   - Show the file path
   - Confirm the dev server is running
   - Provide the browser URL
   - Remind them they can edit and see live changes

## Example Interaction

```
User: /write-blog-post

Assistant: I'll help you write a blog post\! Let me ask a few clarifying questions first.

What's the topic of your blog post?

User: I want to write about using Claude Code skills to automate blogging workflows.

Assistant: Great topic\! A few more questions:
- Target length? (short note ~500 words, medium article ~2000 words, or comprehensive guide ~5000+ words)
- Any specific points or sections you want to include?
- Should I use minimal or extended front matter with categories?

User: Medium article, around 2000 words. Focus on practical examples. Use extended front matter.

Assistant: Perfect\! I'll create a medium-length article about Claude Code skills for blogging automation. Creating the post now...

[Creates file: docs/blog/posts/2026-01-30-automating-blog-workflows-with-claude-code-skills.md]
[Writes first draft with proper structure and style]
[Starts mkdocs serve in background]
[Opens browser to http://127.0.0.1:8000/blog/2026/01/30/automating-blog-workflows-with-claude-code-skills/]

Done\! I've created your blog post at:
docs/blog/posts/2026-01-30-automating-blog-workflows-with-claude-code-skills.md

The MkDocs dev server is now running at http://127.0.0.1:8000/
Your post is viewable at: http://127.0.0.1:8000/blog/2026/01/30/automating-blog-workflows-with-claude-code-skills/

I've opened it in your browser. The server has live reload enabled, so any edits you make will automatically refresh the page. Feel free to review and edit as needed\!
```

## Additional Notes

- **Placeholders**: Always use today's date (2026-01-30) when creating new posts
- **Slug generation**: The slug is automatically derived from the filename (everything after the date)
- **Live reload**: The dev server watches for file changes and auto-refreshes the browser
- **Draft posts**: It's okay to create incomplete posts - they can be filled in later
- **Assets**: If the post needs images, create them in `docs/blog/assets/` with descriptive names
- **Port conflicts**: If port 8000 is in use, the skill should try `mkdocs serve -a localhost:8001`

## Style Tips Reminder

- Lead with "why" not "what"
- Use concrete examples over abstract theory
- Break complex topics into digestible sections
- Include code snippets that are practical and runnable
- Use collapsible sections for advanced/optional content
- End every post with the standard CTAs
- Keep the tone conversational but authoritative
- Share personal experiences and learnings
- Acknowledge complexity but make it approachable
