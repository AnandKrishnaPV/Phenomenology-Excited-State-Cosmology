import os
import re

def replace_in_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    original_content = content

    # 1. "rigorously formalizes" -> "theoretically models"
    content = content.replace("rigorously formalized", "theoretically modeled")
    
    # 2. "fundamentally invalidates" -> "challenges"
    content = content.replace("fundamentally invalidates", "challenges")
    
    # 3. "rigorously understood" -> "understood"
    content = content.replace("rigorously understood", "understood")
    
    # 4. "rigorous mathematical derivation" -> "mathematical derivation"
    content = content.replace("rigorous mathematical derivation", "mathematical derivation")
    
    # 5. "profound proof of concept" -> "compelling demonstration"
    content = content.replace("profound proof of concept", "compelling demonstration")
    
    # 6. "To prove that" -> "To demonstrate mathematically within this framework that"
    content = content.replace("To prove that this shared phase coherence", "To demonstrate mathematically within this framework that this shared phase coherence")
    
    # 7. "demonstrate rigorously" -> "suggest mathematically"
    content = content.replace("demonstrate rigorously", "suggest mathematically")
    
    # 8. "rigorously provided" -> "provided"
    content = content.replace("rigorously provided", "provided")

    if original_content != content:
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Updated {filepath}")

for filename in os.listdir('.'):
    if filename.startswith('ch') and filename.endswith('.tex'):
        replace_in_file(filename)
    elif filename == 'main.tex':
        replace_in_file(filename)
