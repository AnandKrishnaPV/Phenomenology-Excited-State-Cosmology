import re

with open("all_chapters.tex") as f:
    text = f.read()

# find all citations
cites = re.findall(r'\\cite{([^}]+)}', text)
print("Citations found:", cites)

# check for broken latex commands
broken = re.findall(r'\\[a-zA-Z]*{?\w+?[^}]*$', text, re.MULTILINE)
# wait, a better way is just to search for missing figures
figs = re.findall(r'\\includegraphics\[.*?\]{(.*?)}', text)
print("Figures included:", figs)

import os
for fig in figs:
    if not os.path.exists(fig):
        print("MISSING FIGURE:", fig)

with open("refs.bib") as f:
    refs = f.read()

print("Refs keys:")
print(re.findall(r'@\w+{([^,]+)', refs))
