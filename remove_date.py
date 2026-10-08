import re

filepath = "/Users/anandkrishnapv/Desktop/Cosmology_Book/main.tex"
with open(filepath, "r") as f:
    content = f.read()

# If a date command already exists, empty it. Otherwise, add an empty date command before maketitle.
if r"\date" in content:
    content = re.sub(r"\\date\{[^\}]*\}", r"\\date{}", content)
else:
    content = content.replace(r"\maketitle", "\\date{}\n\\maketitle")

with open(filepath, "w") as f:
    f.write(content)

print("Date removed.")
