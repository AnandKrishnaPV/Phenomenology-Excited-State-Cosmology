import os

cites = {
    "ch5.tex": [
        ("anisotropies in the CMB", "anisotropies in the CMB~\\cite{Planck2018}"),
    ],
    "ch8.tex": [
        ("Bell's subsequent theorem", "Bell's subsequent theorem~\\cite{Bell1964, CHSH1969}"),
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
            else:
                print(f"NOT FOUND or ALREADY REPLACED in {fname}: {old}")
            
        if modified:
            with open(path, "w") as f:
                f.write(content)
            
apply_cites()
print("Injected remaining citations.")
