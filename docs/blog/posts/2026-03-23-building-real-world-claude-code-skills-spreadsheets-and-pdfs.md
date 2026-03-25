---
date: 2026-03-23
slug: building-real-world-claude-code-skills-spreadsheets-and-pdfs
title: "Building Real-World Claude Code Skills: Spreadsheets and PDFs"
categories:
  - AI Best Practices
  - Technical Guides
  - LLM Development
tags:
  - claude-code
  - agent-skills
  - context-engineering
  - python
  - automation
excerpt: "A hands-on look at two Claude Code skills I built for my LinkedIn Learning course—an expense categorizer for spreadsheets and a PDF extraction toolkit. Here's what I learned about progressive disclosure, composability, and making AI agents actually reliable."
---

# Building Real-World Claude Code Skills: Spreadsheets and PDFs

Agent skills sound great in theory. But what does it actually look like to build one that handles messy, real-world data? For my upcoming LinkedIn Learning course on Claude Code skills, I built two production-grade skills from scratch: an **expense categorizer** for bank CSV exports and a **PDF extraction and transformation toolkit**. Both taught me things about skill architecture that I didn't expect.

This post walks through what each skill does, the design decisions that made them reliable, and the patterns that emerged across both.

<!-- more -->

## The Spreadsheet Skill: Categorizing Expenses from Any CSV

The first skill I built solves a common problem: you export transactions from your bank or credit card, and you want them categorized into spending buckets with a summary. Simple enough—until you realize every bank exports CSVs differently.

### What It Does

Given any bank/credit card CSV export, the skill:

1. **Reads and interprets the CSV** — detecting columns by inspecting headers, never assuming positions
2. **Categorizes every transaction** into one of 10 spending categories (Housing, Utilities, Groceries, Dining, Transport, Software, Shopping, Health, Entertainment, Travel) plus Income and Uncategorized
3. **Produces two outputs** — a clean categorized CSV and a markdown spending summary table with totals, percentages, and transaction counts
4. **Validates everything** — checks that every row has a category, totals sum correctly (within $0.01), and dates converted properly

### The Interesting Part: Handling Messy Data

The clean-path CSV is easy. The real test was `sample-messy.csv` — a file I designed to break naive parsing:

```
transaction_date;merchant_name;debit;credit
15-Jan-2026;COSTCO WHSE #1234;$127.43;
22-Jan-2026;trader joes;$89.17;
03-Feb-2026;TGT*TARGET.COM;$234.56;
10-Feb-2026;AMZN Mktp US*2K8;$67.89;
15-Feb-2026;;$45.00;
```

Semicolons instead of commas. Debit and credit in separate columns. Currency symbols with comma separators. Dates in `DD-Mon-YYYY` format. Mixed-case merchant names. Truncated identifiers like `TGT*TARGET.COM`. And a completely **blank merchant name** that the skill maps to "UNKNOWN MERCHANT" → Uncategorized.

All of this is handled through the instructions in `SKILL.md` — Claude reads the header row, infers the structure, and adapts. No hardcoded parsing logic required.

### The Category Table as Embedded Knowledge

Rather than relying on Claude's general knowledge to categorize merchants, the skill embeds a **keyword-matching table** directly in the SKILL.md:

| Category | Keywords |
|----------|----------|
| Groceries | grocery, supermarket, whole foods, trader joe, aldi, costco |
| Dining | restaurant, cafe, starbucks, uber eats, doordash, chipotle |
| Software | subscription, saas, github, aws, openai, adobe, notion, figma |
| Transport | uber, lyft, gas station, parking, transit, metro, fuel |

This is a key context engineering pattern: **don't rely on the model's training data when you can provide explicit mappings**. The skill also points to a `references/categories.md` file for customization, keeping the core instructions stable while the reference layer evolves.

## The PDF Skill: Extract, Merge, Split, Create, and Fill

The PDF skill is significantly more ambitious. It covers five capability areas, backed by two Python helper scripts and a documented failure-modes reference.

### Five Operations, Fully Composable

The skill handles:

- **Extract** — Pull structured invoice data (vendor, amounts, line items, dates) from any PDF
- **Merge** — Combine multiple PDFs into one with a source attribution map
- **Split** — Extract specific pages or page ranges into separate files
- **Create** — Generate new PDFs from extracted JSON data
- **Fill Forms** — Read, fill, and flatten interactive PDF form fields

What makes this powerful is **composability**. You can merge five vendor invoices into one PDF, then extract structured data from the merged result, then attribute each invoice back to its source using the source map. This chaining of operations is what elevates a skill beyond a script.

### Confidence Scoring as a First-Class Output

Every extracted field comes with confidence metadata:

```json
{
  "vendor_name": "Apex Manufacturing",
  "_confidence": {
    "vendor_name": {
      "score": "high",
      "reason": "Single occurrence in document header"
    },
    "total": {
      "score": "high",
      "reason": "Single 'Total' label, matches subtotal + tax"
    }
  },
  "_validation": {
    "line_item_sum_check": "pass",
    "date_sanity_check": "pass",
    "required_fields_check": "pass",
    "warnings": []
  }
}
```

This isn't just for debugging. **Confidence is the trigger for escalation.** If any required field has confidence "low" or "unresolved," the skill flags it for human review rather than silently guessing. This is the difference between a demo and something you'd actually trust with real invoices.

### The Fallback Chain Pattern

When extracting a "Total" value from a PDF, the skill follows a defined fallback chain:

1. Look for a field labeled "Total" at the bottom of a table
2. Try alternate labels: "Grand Total", "Amount Due", "Balance Due"
3. Look for a prominently displayed monetary amount near the top
4. **Sum line item totals** and report the calculated sum with a warning flag

Each step is explicit in the SKILL.md. Claude doesn't improvise — it follows the chain and reports which level it reached. This makes behavior predictable and debuggable.

### 10 Documented Failure Modes

The `references/known-failure-modes.md` file catalogs real problems the skill might encounter:

| Failure | Mitigation |
|---------|-----------|
| Dual total values | Check which equals line item sum vs. sum + tax |
| Rotated text | Use bounding boxes to detect tall/narrow blocks |
| Merged table cells | Compare cell count per row to header row |
| Watermarks obscuring text | Detect diagonal text, strip known fragments |
| OCR artifacts | Apply common substitutions: rn→m, $S→$5 |
| Currency symbol confusion | Check vendor address for country disambiguation |

This reference document is a knowledge layer that Claude consults when confidence drops. The skill doesn't need to handle every edge case in its core instructions — it can defer to the reference and adapt.

### Python Scripts via `uv run`

Both PDF operations (extract and merge/split) use Python helper scripts with [PEP 723 inline metadata](https://peps.python.org/pep-0723/):

```python
# /// script
# requires-python = ">=3.12"
# dependencies = ["pymupdf>=1.25.0"]
# ///
```

This means `uv run extract_pdf.py invoice.pdf` just works — no virtual environment setup, no requirements.txt. The scripts use **pymupdf** specifically because it doesn't re-encode PDF content, preserving fonts, layout, and table structures that the extraction depends on.

## Patterns That Emerged Across Both Skills

Building these two skills back-to-back revealed patterns I now consider essential for any serious skill:

### 1. The `references/` Folder as a Plugin Layer

Both skills separate **stable instructions** (SKILL.md) from **extensible knowledge** (references/). The spreadsheet skill has `categories.md`; the PDF skill has `vendor-schemas.yaml` and `known-failure-modes.md`. This lets you evolve the knowledge layer without touching the core workflow.

### 2. Never Silently Lose Data

The spreadsheet skill states this explicitly as "The Golden Rule." The PDF skill encodes it through the `_validation.warnings` array. Either way, the principle is the same: **problematic data gets flagged and returned, never dropped**. If a merchant can't be categorized, it goes to "Uncategorized" and gets flagged for review. If a PDF total doesn't match the line items, both values are reported with a warning.

### 3. Validation as a Required Step

Both skills include explicit validation before presenting results. The spreadsheet skill checks that category totals sum correctly and row counts match. The PDF skill runs four validation checks (line item sums, date sanity, required fields, monetary sanity). This isn't optional — it's baked into the workflow.

### 4. Progressive Disclosure in Practice

The skills only load what's needed. The SKILL.md is always loaded when triggered. The references folder? Only consulted when Claude encounters an edge case or needs to look up a vendor schema. Python scripts? Only executed when the operation requires them. This keeps the context window lean for simple tasks while enabling deep capability for complex ones.

## What I'd Tell Someone Building Their First Skill

After building these two skills across 10 video lessons, here's what I'd pass along:

**Start with the SKILL.md, not the code.** The natural instinct is to write Python first. Resist it. Write the instructions that teach Claude the workflow. You'll be surprised how much you can accomplish with instructions alone before needing any scripts.

**Design for the messy case from day one.** The clean CSV test passes easily. It's the semicolon-delimited, mixed-case, blank-field, currency-formatted mess that reveals whether your skill is robust. Build your adversarial test data early.

**Embed domain knowledge explicitly.** Don't assume the model knows that `TGT*TARGET.COM` means Target or that `AMZN Mktp` means Amazon. Put the keyword mappings in your skill. You'll get consistent results instead of probabilistic ones.

**Make confidence visible.** If your skill produces structured outputs, include confidence scores. They give users (and downstream systems) a clear signal about when to trust the output and when to verify manually.

If you want to see these skills built step by step, the full course is available on LinkedIn Learning. Each chapter walks through the design decisions, the edge cases, and the testing approach that makes a skill production-ready.

---

[Subscribe to my Newsletter](https://automata-learning-lab.kit.com/ccd5287996){ .md-button .md-button--primary }
[Subscribe to my YouTube](https://www.youtube.com/@automatalearninglab){ .md-button .md-button--secondary }
