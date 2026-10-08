filepath = "/Users/anandkrishnapv/Desktop/Cosmology_Book/main.tex"
with open(filepath, "r") as f:
    content = f.read()

content = content.replace(r"\date{} \today}", r"\date{}")

with open(filepath, "w") as f:
    f.write(content)

