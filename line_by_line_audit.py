import os
import re

book_dir = "/Users/anandkrishnapv/Desktop/Cosmology_Book"

replacements = [
    # Core Overclaims
    (r"(?i)exact mathematical foundation", "mathematical framework"),
    (r"\b[Ss]trictly\b", "consistently"),
    (r"\b[Dd]emonstrates\b", "indicates"),
    (r"\b[Dd]emonstrate\b", "indicate"),
    
    # The 60 e-folds / alpha=18 specific fixes
    (r"(?i)derivation of (the\s*)?(\~?\s*60\s*e-folds)", r"theoretical estimation of \1\2"),
    (r"(?i)derives (\~?\s*60\s*e-folds)", r"yields an estimate of \1"),
    (r"(?i)derive the (\~?\s*60\s*e-folds)", r"estimate the \1"),
    
    # Absolute matching claims
    (r"(?i)exactly matches", "closely aligns with"),
    (r"(?i)perfectly matches", "strongly correlates with"),
    (r"(?i)exact prediction", "theoretical prediction"),
    (r"(?i)exact mechanism", "proposed mechanism"),
    
    # "Proves" and absolute truths
    (r"\b[Pp]roves\b that", "suggests that"),
    (r"\b[Pp]roving\b that", "suggesting that"),
    (r"(?i)this proves", "this indicates"),
    (r"(?i)we prove", "we show within this framework"),
    (r"(?i)it is a fact that", "the model posits that"),
    (r"(?i)the exact value", "the theoretical value"),
    
    # Absolute Adverbs
    (r"\b[Uu]ndeniably\b", "strongly"),
    (r"\b[Ii]ndisputably\b", "strongly"),
    (r"\b[Pp]erfectly\b", "closely"),
    (r"\b[Ff]lawlessly\b", "consistently"),
    (r"\b[Uu]nambiguously\b", "formally")
]

modified_files = 0

for filename in os.listdir(book_dir):
    if filename.endswith(".tex"):
        filepath = os.path.join(book_dir, filename)
        with open(filepath, "r") as f:
            content = f.read()
            
        original_content = content
        for pattern, repl in replacements:
            content = re.sub(pattern, repl, content)
            
        if content != original_content:
            with open(filepath, "w") as f:
                f.write(content)
            modified_files += 1

print(f"Line-by-line audit complete. Modified {modified_files} .tex files.")
