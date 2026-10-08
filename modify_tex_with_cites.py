import os

cites = {
    "ch1.tex": [
        ("inflationary epoch", "inflationary epoch~\\cite{Guth1981}"),
    ],
    "ch2.tex": [
        ("Einstein Field Equations", "Einstein Field Equations~\\cite{Einstein1916GR}"),
    ],
    "ch3.tex": [
        ("spontaneous emission", "spontaneous emission~\\cite{Weisskopf1930}"),
    ],
    "ch4.tex": [
        ("Einstein A-Coefficient", "Einstein A-Coefficient~\\cite{Einstein1916Rad}"),
    ],
    "ch5.tex": [
        ("CMB anisotropies", "CMB anisotropies~\\cite{Planck2018}"),
    ],
    "ch6.tex": [
        ("Schrödinger-Newton", "Schrödinger-Newton~\\cite{Hu2000}"),
    ],
    "ch7.tex": [
        ("AdS/CFT correspondence", "AdS/CFT correspondence~\\cite{Maldacena1997}"),
        ("Ryu-Takayanagi", "Ryu-Takayanagi~\\cite{Ryu2006}"),
    ],
    "ch8.tex": [
        ("Bell's inequalities", "Bell's inequalities~\\cite{Bell1964, CHSH1969}"),
    ],
    "ch10.tex": [
        ("Bekenstein-Hawking", "Bekenstein-Hawking~\\cite{Bekenstein1973, Hawking1975}"),
    ]
}

def apply_cites():
    for fname, replacements in cites.items():
        path = os.path.join("/Users/anandkrishnapv/Desktop/Cosmology_Book", fname)
        if not os.path.exists(path):
            continue
        with open(path, "r") as f:
            content = f.read()
        
        # Count if replacement occurred
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
print("Injected citations.")
