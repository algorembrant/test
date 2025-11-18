from pathlib import Path
import re

# Base folder
base = Path(__file__).parent  # ensures script works from anywhere
statistics_folder = base / "statistics"

# Scan all files recursively, exclude testme.md
files = [f for f in statistics_folder.rglob("*") if f.is_file() and f.name != "testme.md"]

# Build Markdown snippet
md_snippet = "### Project File Size (Bytes)\n\n"
for file in files:
    size = file.stat().st_size
    # Make path relative to statistics folder
    rel_path = file.relative_to(statistics_folder)
    md_snippet += f"- **{rel_path}**: `{size}` bytes\n"

# Read testme.md
readme_path = statistics_folder / "testme.md"
if readme_path.exists():
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace content between markers
    pattern = r"(<!-- CODE_STATS_START -->)(.*?)(<!-- CODE_STATS_END -->)"
    if re.search(pattern, content, flags=re.DOTALL):
        new_content = re.sub(pattern, rf"\1\n{md_snippet}\n\3", content, flags=re.DOTALL)
    else:
        # If markers don't exist, append at the end
        new_content = content + f"\n<!-- CODE_STATS_START -->\n{md_snippet}\n<!-- CODE_STATS_END -->\n"

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("testme.md updated with file sizes!")
else:
    print("testme.md not found!")
