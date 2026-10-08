import os
import re

book_dir = "/Users/anandkrishnapv/Desktop/Cosmology_Book"

# 1. Create Chapter 13
ch13_content = r"""\chapter{Conditions for Falsifiability}

The purpose of this section is to make the framework scientifically falsifiable by identifying observations that could rule out specific realizations of the model. The Excited-State Cosmology framework is intended as a testable theoretical proposal rather than a definitive replacement for the standard cosmological model. Its validity therefore depends on whether its quantitative predictions remain consistent with independent observations. The framework would be disfavored or falsified if future observations systematically contradict predictions that follow from its fixed parameter set.

\section{Galactic dynamics}
The Schr\"{o}dinger--Newton formulation predicts a specific radial mass-density structure and corresponding rotation-velocity profile. If sufficiently precise and independently analyzed galaxy rotation-curve data systematically exclude the predicted velocity profiles across a representative galaxy sample, without permitting additional unconstrained halo parameters, the dark-matter interpretation proposed here would be falsified.

\section{CMB temperature and polarization spectra}
The model predicts a specific angular power spectrum $C_\ell$ arising from the internal hyper-orbital structure. Future high-precision measurements of the CMB temperature and polarization spectra that produce statistically significant deviations from the predicted $C_\ell$, beyond observational and foreground uncertainties, would falsify the corresponding CMB realization of the framework. Experiments such as the Simons Observatory provide relevant future tests through precision measurements of CMB temperature and polarization.

\section{Primordial gravitational-wave signatures}
The inflationary interpretation of the $1s\rightarrow2p$ transition makes predictions concerning primordial perturbations. A robust detection of a primordial tensor signal whose amplitude, scale dependence, or polarization properties are incompatible with the model's predicted perturbation spectrum would rule out that realization of Excited-State Cosmology. Conversely, a non-detection would place quantitative upper bounds on the allowed parameter space rather than constitute a direct confirmation of the framework.

\section{Cosmological expansion history}
The framework predicts an effective Friedmann evolution through $G_{\rm eff}$, $\Lambda_{\rm eff}$, and the internal excitation dynamics. Future measurements of $H(z)$, baryon acoustic oscillations, Type-Ia supernovae, and other distance-redshift observables that produce a statistically significant incompatibility with this predicted expansion history would disfavor the model.

\section{Parameter consistency across independent datasets}
A particularly stringent test is cross-dataset consistency. Parameters determined from one observational sector, such as the CMB, should be used without re-fitting in independent sectors such as galaxy dynamics or late-time expansion. If a common parameter set cannot simultaneously reproduce these observations within their uncertainties, the framework would be falsified as a unified cosmological model.

Thus, the principal empirical criterion is not whether Excited-State Cosmology can reproduce an individual observation, but whether a single theoretically motivated parameter set can survive independent and increasingly precise observational tests.
"""

with open(os.path.join(book_dir, "ch13.tex"), "w") as f:
    f.write(ch13_content)

# 2. Epistemological Sweep
replacements = {
    r"(?i)mathematically proves": "mathematically derives",
    r"(?i)exactly explains": "provides an explanation for",
    r"(?i)strictly resolves": "offers a resolution to",
    r"(?i)rigorously proves": "demonstrates mathematically within this framework",
    r"(?i)proves mathematically": "demonstrates mathematically",
    r"(?i)proof of scientific validity": "demonstration of empirical consistency",
    r"(?i)definitively solves": "proposes a solution to",
    r"(?i)perfectly matches": "strongly correlates with"
}

for filename in os.listdir(book_dir):
    if filename.endswith(".tex"):
        filepath = os.path.join(book_dir, filename)
        with open(filepath, "r") as f:
            content = f.read()
            
        original_content = content
        for pattern, replacement in replacements.items():
            content = re.sub(pattern, replacement, content)
            
        if filename == "main.tex" and r"\include{ch13}" not in content:
            # Inject ch13 before the bibliography or end of document
            if r"\bibliographystyle" in content:
                content = content.replace(r"\bibliographystyle", "\\include{ch13}\n\\bibliographystyle")
            elif r"\end{document}" in content:
                content = content.replace(r"\end{document}", "\\include{ch13}\n\\end{document}")
                
        if content != original_content:
            with open(filepath, "w") as f:
                f.write(content)

print("Chapter 13 added and epistemological sweep completed.")
