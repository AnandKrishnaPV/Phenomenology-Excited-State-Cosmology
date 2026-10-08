import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp
import os

# Set global style to B&W / grayscale for scientific purity
plt.style.use('grayscale')
plt.rcParams.update({
    'font.size': 12,
    'lines.linewidth': 2,
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'legend.fontsize': 12,
    'figure.figsize': (8, 5),
    'figure.autolayout': True,
    'text.usetex': False
})

out_dir = "/Users/anandkrishnapv/Desktop/Cosmology_Book"

# --- Ch1: Hydrogen Radial Probabilities (Big Bang) ---
fig, ax = plt.subplots()
r = np.linspace(0, 15, 500)
R10 = 2 * np.exp(-r)
P10 = r**2 * R10**2
R21 = (1/np.sqrt(24)) * r * np.exp(-r/2)
P21 = r**2 * R21**2

ax.plot(r, P10, 'k--', label=r'$1s$ state (Pre-Inflation Vacuum)')
ax.plot(r, P21, 'k-', label=r'$2p$ state (Post-Inflation Universe)')
ax.set_xlabel(r'Hyper-Radial Coordinate (Units of $a_0$)')
ax.set_ylabel(r'Radial Probability Density $P(r)$')
ax.set_title(r'Hyper-Electron State Transition (The Big Bang)')
ax.legend()
plt.savefig(os.path.join(out_dir, 'fig_ch1.pdf'))
plt.close()

# --- Ch2: Schwarzschild Time Dilation ---
fig, ax = plt.subplots()
r = np.linspace(1.00001, 3, 500)
gamma = 1 / np.sqrt(1 - 1/r)
ax.plot(r, np.log10(gamma), 'k-')
ax.set_xlabel(r'Radial Distance $r / r_s$')
ax.set_ylabel(r'$\log_{10}(\gamma)$ (Time Dilation Factor)')
ax.set_title(r'Relativistic Hang-Time Dilation near the Hyper-Horizon')
ax.grid(True, linestyle=':', color='0.6')
plt.savefig(os.path.join(out_dir, 'fig_ch2.pdf'))
plt.close()

# --- Ch3: Wigner-Weisskopf Decay (Dark Energy) ---
fig, ax = plt.subplots()
t = np.linspace(0, 5, 500)
gamma_decay = 1.0
P_surv = np.exp(-gamma_decay * t)
ax.plot(t, P_surv, 'k-')
ax.fill_between(t, 0, P_surv, color='0.9')
ax.set_xlabel(r'Time $t / \tau_{univ}$')
ax.set_ylabel(r'Survival Probability $|\langle e_n(t) | e_n(0) \rangle|^2$')
ax.set_title(r'Spontaneous Emission Probability (Vacuum Instability)')
plt.savefig(os.path.join(out_dir, 'fig_ch3.pdf'))
plt.close()

# --- Ch4: Density of States ---
fig, ax = plt.subplots()
omega = np.linspace(0, 10, 500)
rho = omega**2
ax.plot(omega, rho, 'k-')
ax.axvline(x=5, color='k', linestyle='--', label=r'Transition Frequency $\omega_0$')
ax.set_xlabel(r'Hyper-Photon Frequency $\omega$')
ax.set_ylabel(r'Density of States $\rho(\omega) \propto \omega^2$')
ax.set_title(r'Vacuum Mode Density for Cosmic Collapse')
ax.legend()
plt.savefig(os.path.join(out_dir, 'fig_ch4.pdf'))
plt.close()

# --- Ch5: CMB Angular Covariance (Legendre Polynomials) ---
fig, ax = plt.subplots()
theta = np.linspace(0, np.pi, 500)
x = np.cos(theta)
for l in [1, 2, 4]:
    Pl = sp.eval_legendre(l, x)
    ax.plot(theta, Pl, label=rf'$P_{{{l}}}(\cos\theta)$')
ax.set_xlabel(r'Separation Angle $\theta$ (Radians)')
ax.set_ylabel(r'Angular Correlation Function $C(\theta)$')
ax.set_title(r'Transition Radiation Angular Harmonics (CMB)')
ax.legend()
plt.savefig(os.path.join(out_dir, 'fig_ch5.pdf'))
plt.close()

# --- Ch6: Solitonic Dark Matter Core ---
fig, ax = plt.subplots()
r = np.linspace(0, 5, 500)
rho_c = 1.0 / (1 + 0.091 * (r)**2)**8
ax.plot(r, rho_c, 'k-', label=r'Solitonic Interference Core')
# Safe NFW plot for r > 0
r_nfw = np.linspace(0.1, 5, 500)
ax.plot(r_nfw, 1/(r_nfw*(1+r_nfw)**2), 'k--', label=r'NFW Classical Profile')
ax.set_ylim(0, 1.1)
ax.set_xlabel(r'Radius $r / r_c$')
ax.set_ylabel(r'Probability Density $\rho(r)$')
ax.set_title(r'Schrödinger-Newton Probability Nodes (Dark Matter)')
ax.legend()
plt.savefig(os.path.join(out_dir, 'fig_ch6.pdf'))
plt.close()

# --- Ch7: Holographic Ryu-Takayanagi Geodesics ---
fig, ax = plt.subplots(figsize=(8,4))
x = np.linspace(-2, 2, 500)
for r_val in [0.5, 1.0, 1.5]:
    z = np.sqrt(np.clip(r_val**2 - x**2, 0, None))
    mask = z > 0
    ax.plot(x[mask], z[mask], 'k-')
ax.axhline(y=0, color='k', linewidth=3, label=r'Conformal Boundary (Orbital Shell)')
ax.set_xlabel(r'Boundary Coordinate $x$')
ax.set_ylabel(r'Bulk Holographic Depth $z$')
ax.set_title(r'$AdS_3$ Bulk Entanglement Geodesics')
ax.invert_yaxis()
ax.legend()
plt.savefig(os.path.join(out_dir, 'fig_ch7.pdf'))
plt.close()

# --- Ch8: Quantum Entanglement CHSH Correlation ---
fig, ax = plt.subplots()
theta = np.linspace(0, 2*np.pi, 500)
E = np.cos(2*theta)
ax.plot(theta, E, 'k-', label=r'Quantum Phase Correlation')
ax.axhline(y=0.5, color='k', linestyle=':', label=r'Classical Bound')
ax.axhline(y=-0.5, color='k', linestyle=':')
ax.set_xlabel(r'Measurement Angle Difference $(a-b)$')
ax.set_ylabel(r'Expectation Value $E(a,b)$')
ax.set_title(r'Bell Inequality Violation via Global Holonomy')
ax.legend()
plt.savefig(os.path.join(out_dir, 'fig_ch8.pdf'))
plt.close()

# --- Ch9: Phase vs Group Velocity Dispersion ---
fig, ax = plt.subplots()
k = np.linspace(0.1, 5, 500)
c = 1.0
omega_c = 1.0
omega = np.sqrt((c*k)**2 + omega_c**2)
vp = omega / k
vg = (c**2 * k) / omega
ax.plot(k, vp, 'k-', label=r'Phase Velocity $v_p$ (Manifold Update Rate)')
ax.plot(k, vg, 'k--', label=r'Group Velocity $v_g$ (Kinematic Motion)')
ax.axhline(y=c, color='k', linestyle=':', label=r'Speed of Light $c$')
ax.set_xlabel(r'Wave Vector $k$')
ax.set_ylabel(r'Velocity')
ax.set_title(r'Superluminal Phase Updates of the Hyper-Dirac Field')
ax.legend()
plt.savefig(os.path.join(out_dir, 'fig_ch9.pdf'))
plt.close()

# --- Ch10: Bekenstein-Hawking Entropy Scaling ---
fig, ax = plt.subplots()
Rc = np.linspace(0, 10, 500)
S = Rc**2
ax.plot(Rc, S, 'k-', label=r'Holographic Entropy bound $S \propto R_c^2$')
ax.plot(Rc, Rc**3, 'k:', label=r'Classical Volume Scaling $S \propto R_c^3$')
ax.set_ylim(0, 100)
ax.set_xlabel(r'Hubble Radius $R_c$')
ax.set_ylabel(r'Internal Entropy $\text{Tr}(\rho_{int} \ln \rho_{int})$')
ax.set_title(r'Cosmological Area Law')
ax.legend()
plt.savefig(os.path.join(out_dir, 'fig_ch10.pdf'))
plt.close()

print("Generated all 10 scientific plots successfully.")
