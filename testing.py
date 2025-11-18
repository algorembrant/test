import json
from pathlib import Path

# --- Notebook path ---
notebook_path = Path("Market Profile (volumedata ver).ipynb")

# --- Count code lines ---
with open(notebook_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

code_lines = sum(len(cell["source"]) for cell in nb["cells"] if cell["cell_type"] == "code")

# --- Generate Markdown snippet ---
md_snippet = f"""
### Project Code Statistics

- **Notebook:** [{notebook_path.name}]({notebook_path})
- **Lines of code:** {code_lines}
"""

# Save to a file (optional)
with open("CODE_STATS.md", "w", encoding="utf-8") as f:
    f.write(md_snippet)

print(md_snippet)
