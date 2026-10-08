import os

for i in range(1, 11):
    fname = f"ch{i}.tex"
    fig_name = f"fig_ch{i}.pdf"
    
    # Check if the figure exists
    if not os.path.exists(fig_name):
        print(f"Warning: {fig_name} not found.")
        continue
        
    # Read content
    with open(fname, "r") as f:
        content = f.read()
        
    # Find the appropriate place to inject (e.g., end of file)
    injection = f"""

\\begin{{figure}}[H]
\\centering
\\includegraphics[width=0.85\\textwidth]{{{fig_name}}}
\\caption{{Mathematical visualization of the principles derived in Section {i}.}}
\\end{{figure}}
"""
    
    with open(fname, "a") as f:
        f.write(injection)

print("Injected images successfully.")
