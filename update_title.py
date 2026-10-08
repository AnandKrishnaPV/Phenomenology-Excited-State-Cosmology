import os

filepath = "/Users/anandkrishnapv/Desktop/Cosmology_Book/main.tex"
with open(filepath, "r") as f:
    lines = f.readlines()

with open(filepath, "w") as f:
    in_title = False
    for line in lines:
        if r"\title{" in line:
            f.write(r"\title{Phenomenology of an excited-state cosmological framework: Dark matter and CMB constraints}" + "\n")
            # If the closing brace isn't on the same line, skip lines until we find it
            if "}" not in line[line.find(r"\title{"): ]:
                in_title = True
        elif in_title:
            if "}" in line:
                in_title = False
        else:
            f.write(line)

print("Title updated.")
