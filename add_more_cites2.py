import os

cites = {
    "ch3.tex": [
        ("cosmological constant problem:", "cosmological constant problem~\\cite{Weinberg1989}:"),
    ]
}

def apply_cites():
    for fname, replacements in cites.items():
        path = os.path.join("/Users/anandkrishnapv/Desktop/Cosmology_Book", fname)
        if not os.path.exists(path):
            continue
        with open(path, "r") as f:
            content = f.read()
        
        modified = False
        for old, new in replacements:
            if old in content and new not in content:
                content = content.replace(old, new, 1)
                modified = True
                print(f"Replaced in {fname}: {old}")
            
        if modified:
            with open(path, "w") as f:
                f.write(content)
            
apply_cites()
print("Injected final citation.")
