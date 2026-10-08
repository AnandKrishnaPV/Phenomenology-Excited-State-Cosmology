import os
import re

def replace_in_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    original_content = content

    content = content.replace("To rigorously ground", "To mathematically ground")
    content = content.replace("we rigorously derive", "we derive")
    content = content.replace("To rigorously describe", "To describe")
    content = content.replace("To rigorously formalize", "To formalize")
    content = content.replace("rigorously isolate", "isolate")
    content = content.replace("are rigorously \pm 1", "are strictly \pm 1")

    if original_content != content:
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Updated {filepath}")

for filename in os.listdir('.'):
    if filename.startswith('ch') and filename.endswith('.tex'):
        replace_in_file(filename)
    elif filename == 'main.tex':
        replace_in_file(filename)
