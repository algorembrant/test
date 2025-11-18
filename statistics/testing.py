from pathlib import Path
import re

base = Path.cwd() / "statistics"

files = [
    base / "testing.py",
    base / "testme.md",
    base / "Market Profile (volumedata ver).ipynb"
]

md_snippet = "### Project File Size (Bytes)\n\n"

for file in files:
    if file.exists():
        size = file.stat().st_size
        md_snippet += f"- **{file.name}**: `{size}` bytes\n"
    else:
        md_snippet += f"- **{file.name}**: *File not found*\n"

readme_path = base / "testme.md"
if readme_path.exists():
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = r"(<!-- CODE_STATS_START -->)(.*?)(<!-- CODE_STATS_END -->)"
    new_content = re.sub(pattern, rf"\1\n{md_snippet}\n\3", content, flags=re.DOTALL)

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("testme.md updated with file sizes!")
    print(md_snippet)
else:
    print("testme.md not found!")
