import json
from pathlib import Path
import re

# ----------------------------
# PATH SETUP  (all inside the same folder)
# ----------------------------
base = Path(__file__).parent  # directory of testing.py

notebook_path = base / "Market Profile (volumedata ver).ipynb"
readme_path = base / "testme.md"

# ----------------------------
# COUNT LINES IN NOTEBOOK
# ----------------------------
with open(notebook_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

code_lines = 0
for cell in nb["cells"]:
    if cell["cell_type"] == "code":
        for item in cell["source"]:
            code_lines += item.count("\n") + 1

print(f"Total lines of code in notebook: {code_lines}")

# ----------------------------
# GENERATE MARKDOWN SNIPPET
# ----------------------------
md_snippet = f"""### Project Code Statistics

- **Notebook:** {notebook_path.name}
- **Lines of code:** {code_lines}
"""

# ----------------------------
# READ testme.md
# ----------------------------
with open(readme_path, "r", encoding="utf-8") as f:
    readme_content = f.read()

# ----------------------------
# REPLACE SECTION IN testme.md
# ----------------------------
pattern = r"(<!-- CODE_STATS_START -->)(.*?)(<!-- CODE_STATS_END -->)"
replacement = rf"\1\n{md_snippet}\n\3"
new_content = re.sub(pattern, replacement, readme_content, flags=re.DOTALL)

# ----------------------------
# WRITE BACK TO testme.md
# ----------------------------
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("testme.md updated successfully!")
