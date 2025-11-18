import json
from pathlib import Path

# Notebook path
notebook_path = Path("Market Profile (volumedata ver).ipynb")

# Load notebook
with open(notebook_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

# Count lines in code cells
code_lines = 0
for cell in nb["cells"]:
    if cell["cell_type"] == "code":
        # Each item in cell["source"] may contain multiple lines
        for item in cell["source"]:
            code_lines += item.count("\n") + 1  # +1 for last line if no newline

# Generate Markdown snippet
md_snippet = f"""
### Project Code Statistics

- **Notebook:** [{notebook_path.name}]({notebook_path})
- **Lines of code:** {code_lines}
"""

# Save to a file (optional)
with open("CODE_STATS.md", "w", encoding="utf-8") as f:
    f.write(md_snippet)

print(md_snippet)
