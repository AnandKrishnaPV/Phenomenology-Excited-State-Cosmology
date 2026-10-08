import os

cites = {
    "ch2.tex": [
        ("Schwarzschild metric", "Schwarzschild metric~\\cite{Penrose1965}"),
    ],
    "ch3.tex": [
        ("Cosmological Constant ($\\Lambda$)", "Cosmological Constant ($\\Lambda$)~\\cite{Weinberg1989}"),
        ("orbital instability", "orbital instability~\\cite{Riess1998}"),
    ],
    "ch6.tex": [
        ("galactic rotation curves", "galactic rotation curves~\\cite{Navarro1996}"),
    ],
    "ch7.tex": [
        ("Holographic Projections", "Holographic Projections~\\cite{Susskind1995}"),
    ],
    "ch8.tex": [
        ("Einstein-Podolsky-Rosen (EPR) paradox", "Einstein-Podolsky-Rosen (EPR) paradox~\\cite{Einstein1935EPR}"),
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
print("Injected additional high-impact citations.")
