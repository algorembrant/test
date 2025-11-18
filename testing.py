import json
from pathlib import Path

def count_py_lines(path):
    return sum(1 for _ in open(path, "r", encoding="utf-8"))

def count_ipynb_lines(path):
    with open(path, "r", encoding="utf-8") as f:
        nb = json.load(f)
    return sum(len(cell["source"]) for cell in nb["cells"] if cell["cell_type"] == "code")

# Example usage
py_lines = count_py_lines("sample.py")
nb_lines = count_ipynb_lines("Market Profile (volumedata ver).ipynb")

print(f"Python lines: {py_lines}")
print(f"Notebook lines: {nb_lines}")
