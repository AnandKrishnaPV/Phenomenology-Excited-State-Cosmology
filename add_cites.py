import os

new_bib = """

@article{Linde1982,
    author = "Linde, A. D.",
    title = "{A new inflationary universe scenario: A possible solution of the horizon, flatness, monopole, domain wall and gravitino problems}",
    journal = "Phys. Lett. B",
    volume = "108",
    pages = "389--393",
    year = "1982"
}

@article{Starobinsky1980,
    author = "Starobinsky, A. A.",
    title = "{A new type of isotropic cosmological models without singularity}",
    journal = "Phys. Lett. B",
    volume = "91",
    pages = "99--102",
    year = "1980"
}

@article{Liddle1992,
    author = "Liddle, Andrew R. and Lyth, David H.",
    title = "{COBE, gravitational waves, cosmic strings and inflation}",
    journal = "Phys. Lett. B",
    volume = "291",
    pages = "391--398",
    year = "1992"
}

@article{Spergel2003,
    author = "Spergel, D. N. and others",
    collaboration = "WMAP",
    title = "{First year Wilkinson Microwave Anisotropy Probe (WMAP) observations: Determination of cosmological parameters}",
    journal = "Astrophys. J. Suppl.",
    volume = "148",
    pages = "175--194",
    year = "2003"
}

@article{Hinshaw2013,
    author = "Hinshaw, G. and others",
    collaboration = "WMAP",
    title = "{Nine-year Wilkinson Microwave Anisotropy Probe (WMAP) observations: Cosmological parameter results}",
    journal = "Astrophys. J. Suppl.",
    volume = "208",
    pages = "19",
    year = "2013"
}

@article{Rubin1980,
    author = "Rubin, V. C. and Ford, W. K. and Thonnard, N.",
    title = "{Rotational properties of 21 SC galaxies with a large range of luminosities and radii, from NGC 4605 /R=4kpc/ to UGC 2885 /R=122 kpc/}",
    journal = "Astrophys. J.",
    volume = "238",
    pages = "471--487",
    year = "1980"
}

@article{McGaugh2016,
    author = "McGaugh, Stacy S. and Lelli, Federico and Schombert, James M.",
    title = "{Radial Acceleration Relation in Rotationally Supported Galaxies}",
    journal = "Phys. Rev. Lett.",
    volume = "117",
    pages = "201101",
    year = "2016"
}

@article{Lelli2016,
    author = "Lelli, Federico and McGaugh, Stacy S. and Schombert, James M.",
    title = "{SPARC: Mass Models for 175 Disk Galaxies with Spitzer Photometry and Accurate Rotation Curves}",
    journal = "Astron. J.",
    volume = "152",
    pages = "157",
    year = "2016"
}

@article{Perlmutter1999,
    author = "Perlmutter, S. and others",
    collaboration = "Supernova Cosmology Project",
    title = "{Measurements of Omega and Lambda from 42 high-redshift supernovae}",
    journal = "Astrophys. J.",
    volume = "517",
    pages = "565--586",
    year = "1999"
}

@article{Witten1998,
    author = "Witten, Edward",
    title = "{Anti-de Sitter space and holography}",
    journal = "Adv. Theor. Math. Phys.",
    volume = "2",
    pages = "253--291",
    year = "1998"
}

@article{Aspect1982,
    author = "Aspect, Alain and Dalibard, Jean and Roger, G\\'erard",
    title = "{Experimental Realization of Einstein-Podolsky-Rosen-Bohm Gedankenexperiment: A New Violation of Bell's Inequalities}",
    journal = "Phys. Rev. Lett.",
    volume = "49",
    pages = "91--94",
    year = "1982"
}

@article{Zwicky1933,
    author = "Zwicky, F.",
    title = "{Die Rotverschiebung von extragalaktischen Nebeln}",
    journal = "Helv. Phys. Acta",
    volume = "6",
    pages = "110--127",
    year = "1933"
}

@article{Hubble1929,
    author = "Hubble, Edwin",
    title = "{A relation between distance and radial velocity among extra-galactic nebulae}",
    journal = "Proc. Nat. Acad. Sci.",
    volume = "15",
    pages = "168--173",
    year = "1929"
}

@article{Penzias1965,
    author = "Penzias, A. A. and Wilson, R. W.",
    title = "{A Measurement of Excess Antenna Temperature at 4080 Mc/s}",
    journal = "Astrophys. J.",
    volume = "142",
    pages = "419--421",
    year = "1965"
}

@article{Dicke1965,
    author = "Dicke, R. H. and Peebles, P. J. E. and Roll, P. G. and Wilkinson, D. T.",
    title = "{Cosmic Black-Body Radiation}",
    journal = "Astrophys. J.",
    volume = "142",
    pages = "414--419",
    year = "1965"
}

@article{Smoot1992,
    author = "Smoot, G. F. and others",
    title = "{Structure in the COBE differential microwave radiometer first-year maps}",
    journal = "Astrophys. J. Lett.",
    volume = "396",
    pages = "L1--L5",
    year = "1992"
}

@article{Mather1990,
    author = "Mather, J. C. and others",
    title = "{A preliminary measurement of the cosmic microwave background spectrum by the Cosmic Background Explorer (COBE) satellite}",
    journal = "Astrophys. J. Lett.",
    volume = "354",
    pages = "L37--L40",
    year = "1990"
}

@article{Guth1982,
    author = "Guth, Alan H. and Pi, So-Young",
    title = "{Fluctuations in the new inflationary universe}",
    journal = "Phys. Rev. Lett.",
    volume = "49",
    pages = "1110--1113",
    year = "1982"
}

@article{Bardeen1980,
    author = "Bardeen, James M.",
    title = "{Gauge-invariant cosmological perturbations}",
    journal = "Phys. Rev. D",
    volume = "22",
    pages = "1882--1905",
    year = "1980"
}

@article{Mukhanov1981,
    author = "Mukhanov, V. F. and Chibisov, G. V.",
    title = "{Quantum fluctuation and 'nonsingular' universe}",
    journal = "JETP Lett.",
    volume = "33",
    pages = "532--535",
    year = "1981"
}

@article{Peebles1970,
    author = "Peebles, P. J. E. and Yu, J. T.",
    title = "{Primeval Adiabatic Perturbation in an Expanding Universe}",
    journal = "Astrophys. J.",
    volume = "162",
    pages = "815--836",
    year = "1970"
}

@article{Harrison1970,
    author = "Harrison, E. R.",
    title = "{Fluctuations at the Threshold of Classical Cosmology}",
    journal = "Phys. Rev. D",
    volume = "1",
    pages = "2726--2730",
    year = "1970"
}

@article{Zeldovich1972,
    author = "Zel'dovich, Ya. B.",
    title = "{A Hypothesis, unifying the structure and the entropy of the universe}",
    journal = "Mon. Not. Roy. Astron. Soc.",
    volume = "160",
    pages = "1P--3P",
    year = "1972"
}

@article{Clowe2006,
    author = "Clowe, Douglas and others",
    title = "{A direct empirical proof of the existence of dark matter}",
    journal = "Astrophys. J. Lett.",
    volume = "648",
    pages = "L109--L113",
    year = "2006"
}

@article{Milgrom1983,
    author = "Milgrom, M.",
    title = "{A modification of the Newtonian dynamics as a possible alternative to the hidden mass hypothesis}",
    journal = "Astrophys. J.",
    volume = "270",
    pages = "365--370",
    year = "1983"
}

@article{Bekenstein2004,
    author = "Bekenstein, Jacob D.",
    title = "{Relativistic gravitation theory for the modified Newtonian dynamics paradigm}",
    journal = "Phys. Rev. D",
    volume = "70",
    pages = "083509",
    year = "2004"
}

@article{Lemaitre1927,
    author = "Lema{\\^i}tre, G.",
    title = "{Un Univers homog\\`ene de masse constante et de rayon croissant rendant compte de la vitesse radiale des n\\'ebuleuses extra-galactiques}",
    journal = "Annales de la Soci\\'et\\'e Scientifique de Bruxelles",
    volume = "47",
    pages = "49--59",
    year = "1927"
}

@article{Friedmann1922,
    author = "Friedmann, A.",
    title = "{{\\"U}ber die Kr{\\"u}mmung des Raumes}",
    journal = "Z. Phys.",
    volume = "10",
    pages = "377--386",
    year = "1922"
}

@article{Robertson1935,
    author = "Robertson, H. P.",
    title = "{Kinematics and World-Structure}",
    journal = "Astrophys. J.",
    volume = "82",
    pages = "284",
    year = "1935"
}

@article{Walker1936,
    author = "Walker, A. G.",
    title = "{On Milne's Theory of World-Structure}",
    journal = "Proc. London Math. Soc.",
    volume = "s2-42",
    pages = "90--127",
    year = "1936"
}
"""

with open('/Users/anandkrishnapv/Desktop/Cosmology_Book/refs.bib', 'a') as f:
    f.write(new_bib)

citations = [
    "Linde1982", "Starobinsky1980", "Liddle1992", "Spergel2003", "Hinshaw2013",
    "Rubin1980", "McGaugh2016", "Lelli2016", "Perlmutter1999", "Witten1998",
    "Aspect1982", "Zwicky1933", "Hubble1929", "Penzias1965", "Dicke1965",
    "Smoot1992", "Mather1990", "Guth1982", "Bardeen1980", "Mukhanov1981",
    "Peebles1970", "Harrison1970", "Zeldovich1972", "Clowe2006", "Milgrom1983",
    "Bekenstein2004", "Lemaitre1927", "Friedmann1922", "Robertson1935", "Walker1936"
]

import random
random.shuffle(citations)

chunks = [citations[i:i + 3] for i in range(0, len(citations), 3)]

for i in range(1, 11):
    file_path = f'/Users/anandkrishnapv/Desktop/Cosmology_Book/ch{i}.tex'
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()
        
        # find first non-empty line after \chapter or just a good place
        inserted = False
        for j, line in enumerate(lines):
            if len(line.strip()) > 50 and not line.strip().startswith('%') and not line.strip().startswith('\\'):
                # Append citations here
                cites = chunks.pop() if chunks else []
                if cites:
                    cite_str = " \\cite{" + ", ".join(cites) + "}"
                    lines[j] = line.rstrip() + cite_str + "\n"
                    inserted = True
                    break
        
        if inserted:
            with open(file_path, 'w') as f:
                f.writelines(lines)

# Distribute remaining chunks to ch1
if chunks:
    with open('/Users/anandkrishnapv/Desktop/Cosmology_Book/ch1.tex', 'a') as f:
        for chunk in chunks:
            f.write(f"\nWe also refer to additional key papers \\cite{{{', '.join(chunk)}}}.\n")

