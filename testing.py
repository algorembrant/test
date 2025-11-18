import json
import requests
from pathlib import Path
import re

# ----------------------------
# GitHub raw README URL
# ----------------------------
readme_url = "https://raw.githubusercontent.com/algorembrant/test/main/README.md"

# Notebook path (local file)
notebook_path = Path("Market Profile (volumedata ver).ipynb")

# ----------------------------
# Download README.md
# ----------------------------
response = requests.get(readme_url)
if response.status_code != 200:
    raise Exception("Could not download README.md from GitHub")

readme_content = response.text

# ----------------------------
# Count notebook code lines
# ----------------------------
with open(notebook_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

code_lines = 0
for cell in nb["cells"]:
    if cell["cell_type"] == "code":
        for item in cell["source"]:
            code_lines += item.count("\n") + 1

# ----------------------------
# Embed stats
# ----------------------------
md_snippet = f"""### Project Code Statistics

- **Notebook:** {notebook_path.name}
- **Lines of code:** {code_lines}
"""

pattern = r"(<!-- CODE_STATS_START -->)(.*?)(<!-- CODE_STATS_END -->)"
new_content = re.sub(pattern, rf"\1\n{md_snippet}\3", readme_content, flags=re.DOTALL)

# ----------------------------
# Save updated README locally
# ----------------------------
with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)

print("README.md has been created with updated stats.")
