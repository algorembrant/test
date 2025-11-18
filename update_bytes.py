from pathlib import Path
import re

# Base folder
base = Path.cwd() / "statistics"

# Scan all files recursively
files = [f for f in base.rglob("*") if f.is_file() and f.name != "testme.md"]

# Build Markdown snippet
md_snippet = "### Project File Size (Bytes)\n\n"

for file in files:
    size = file.stat().st_size
    # Make path relative to statistics folder
    rel_path = file.relative_to(base)
    md_snippet += f"- **{rel_path}**: `{size}` bytes\n"

# Read testme.md
readme_path = base / "testme.md"
if readme_path.exists():
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace between markers
    pattern = r"(<!-- CODE_STATS_START -->)(.*?)(<!-- CODE_STATS_END -->)"
    new_content = re.sub(pattern, rf"\1\n{md_snippet}\n\3", content, flags=re.DOTALL)

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("testme.md updated with file sizes!")
else:
    print("testme.md not found!")
