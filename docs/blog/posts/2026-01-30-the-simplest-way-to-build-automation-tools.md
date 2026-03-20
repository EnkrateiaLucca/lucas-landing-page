---

title: The Simplest Way to Build Automation Tools
date: 2026-01-30

---

<!-- more -->

# The Simplest Way to Build Personal Automation Tools

Yesterday I taught my O'Reilly live course about how to automate tasks with Python and AI and I discussed this really cool recipe that I think is worth sharing here about how to create simple Python automation scripts with UV, Python, and a little bit of AI chatbots.

## The Recipe

1. **Install UV** (one command, one time)
2. **Use AI to generate your script** with a simple prompt
3. **Run it with `uv run`** (no virtual environment needed)
4. **Create an alias** to make it a custom command
5. **Done.** You now have a personal automation tool.

## Step 1: Install UV

[UV](https://docs.astral.sh/uv/) is a fast Python package manager that handles everything for you. Install it once:

**macOS/Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

That's it. No messing with Python versions, virtual environments, or pip installations.

## Step 2: Use AI to Generate Your Script

Here's where it gets really powerful: instead of writing the script yourself, you can use AI to generate it with the exact format you need.

### Use This Prompt Template

Copy this prompt and replace `[YOUR TASK]` with what you want to automate:

```
Write a Python automation script that [YOUR TASK].

Requirements:
- Include UV inline script metadata at the top (# /// script format)
- List all required dependencies in the metadata
- Make it a simple CLI tool that accepts input via sys.argv[1]
- Keep it focused and single-purpose
- Include minimal error handling

Example format:
# /// script
# requires-python = ">=3.10"
# dependencies = ["package1", "package2"]
# ///
```

**Example:** "Write a Python automation script that downloads a PDF from a URL and summarizes it using OpenAI's API"

The AI will generate a properly formatted script with:

- UV inline metadata already configured
- All dependencies declared
- Simple command-line interface using `sys.argv[1]`
- Ready to run with `uv run`

### What You Get

Here's the magic: UV lets you declare dependencies right in your Python file using [inline script metadata](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies). The AI-generated script will look like this:

```python
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "openai",
#     "pymupdf",
# ]
# ///

import sys
from openai import OpenAI
import fitz

def summarize_pdf(filepath):
    # Extract text from PDF
    doc = fitz.open(filepath)
    text = "".join(page.get_text() for page in doc)

    # Summarize with AI
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{
            "role": "user",
            "content": f"Summarize this into bullet points:\n\n{text}"
        }]
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    summary = summarize_pdf(sys.argv[1])
    print(summary)
```

Save this as `~/scripts/summarize_pdf.py`.

## Step 3: Run It

```bash
uv run ~/scripts/summarize_pdf.py paper.pdf
```

UV automatically:

- Creates an isolated environment
- Installs the exact dependencies you specified
- Runs your script
- Cleans up after itself

No `pip install`. No `requirements.txt`. No virtual environment activation. Just run it.

## Step 4: Create an Alias

Make it a custom command you can run from anywhere:

**macOS/Linux** - Add to `~/.zshrc`, `~/.bashrc`, or `~/.aliases`:

```bash
# Simple alias (no arguments)
alias summarize='uv run ~/scripts/summarize_pdf.py'

# Or as a function to accept arguments using "$@"
summarize() { uv run ~/scripts/summarize_pdf.py "$@"; }
```

**Windows** - Add to your PowerShell profile (`notepad $PROFILE`):

```powershell
function summarize { uv run C:\scripts\summarize_pdf.py @args }
```

Reload your shell and you're done:
```bash
summarize research_paper.pdf
```

## Why This Works

**AI does the heavy lifting:** You describe what you want, AI generates the properly formatted script. No need to remember syntax or look up package names.

**No dependency hell:** Each script declares exactly what it needs. No conflicts between projects.

**No setup ceremony:** Someone else can run your script with just `uv run script.py`. UV handles everything.

**No maintenance:** Dependencies are locked to what works. Scripts keep working months later.

**No barriers:** Describe your task to AI, test the script once, alias it, use it forever.

## Real Examples

In my [O'Reilly course on automating tasks with Python + AI](https://learning.oreilly.com/live-events/using-ai-tools-and-python-to-automate-tasks/0642572011642/), students have built automation tools for:

- **PDF processing**: Download ArXiv papers, extract data, summarize with AI
- **File organization**: Categorize images using vision AI, organize downloads by type
- **Data extraction**: Pull structured data from receipts, invoices, emails
- **Web automation**: Add movies to watchlists, scrape data, fill forms
- **Report generation**: Analyze data, create charts, generate presentations

Each one is just a Python script with inline dependencies, aliased to a custom command.

## The Power of Simplicity

Instead of building complex applications, you create single-purpose tools that do exactly what you need. With AI generating the scripts and UV handling dependencies, each automation tool is:

- **AI-generated** - describe your task in plain English, get working code
- **Self-contained** - dependencies declared inline
- **Instantly runnable** - just `uv run`
- **Easily shareable** - send someone a file, they can run it
- **Permanently useful** - alias it once, use it forever

This is how you build a personal toolkit of automation superpowers.

## Resources

- [UV Documentation](https://docs.astral.sh/uv/)
- [UV Script Guide](https://docs.astral.sh/uv/guides/scripts/)
- [O'Reilly Course: Automate Tasks with Python + AI](https://learning.oreilly.com/live-events/using-ai-tools-and-python-to-automate-tasks/0642572011642/)
- [PEP 723 - Inline Script Metadata](https://peps.python.org/pep-0723/)

[Subscribe to my Newsletter](https://automata-learning-lab.kit.com/ccd5287996){ .md-button .md-button--primary }
[Subscribe to my YouTube](https://www.youtube.com/@automatalearninglab){ .md-button .md-button--secondary }
