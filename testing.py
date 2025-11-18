import json
from pathlib import Path

# ----------------------------
# Configuration
# ----------------------------
notebook_path = Path("Market Profile (volumedata ver).ipynb")
readme_path = Path("README.md")

# ----------------------------
# Count lines in notebook
# ----------------------------
with open(notebook_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

code_lines = 0
for cell in nb["cells"]:
    if cell["cell_type"] == "code":
        for item in cell["source"]:
            code_lines += item.count("\n") + 1

# ----------------------------
# Generate Markdown snippet
# ----------------------------
md_snippet = f"""### Project Code Statistics

- **Notebook:** [{notebook_path.name}]({notebook_path})
- **Lines of code:** {code_lines}
"""

# ----------------------------
# Update README.md
# ----------------------------
with open(readme_path, "r", encoding="utf-8") as f:
    readme_content = f.read()

# Replace between the markers
import re
pattern = r"(<!-- CODE_STATS_START -->)(.*?)(<!-- CODE_STATS_END -->)"
new_content = re.sub(pattern, rf"\1\n{md_snippet}\3", readme_content, flags=re.DOTALL)

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("README.md updated with code stats!")
print(md_snippet)
