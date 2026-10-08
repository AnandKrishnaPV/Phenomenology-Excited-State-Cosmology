import re

with open("main.tex", "r") as f:
    content = f.read()

# Change the title to a Q1 standard academic title
old_title_pattern = r"\\title\{.*?\}"
new_title = r"\title{\Large \textbf{Cosmological Dynamics via Higher-Dimensional Spontaneous Emission: A Unified Framework for Inflation, Dark Energy, and Holographic Entropy}}"
content = re.sub(old_title_pattern, new_title, content, flags=re.DOTALL)

# Remove table of contents
content = content.replace("\\tableofcontents", "")

with open("main.tex", "w") as f:
    f.write(content)
