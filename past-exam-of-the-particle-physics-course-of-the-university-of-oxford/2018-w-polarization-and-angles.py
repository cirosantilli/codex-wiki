"""Original spin-vector construction and normalized W decay profiles."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 12, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
fig = plt.figure(figsize=(11.4, 7.6), layout='constrained')
gs = fig.add_gridspec(2, 3, height_ratios=[1, 1.15])
n = np.array([0.8, 0.6])
blue, red = '#1764a2', '#bd3c37'
for j, lam in enumerate([1, 0, -1]):
    ax = fig.add_subplot(gs[0, j])
    ax.set(xlim=(-1.4, 1.4), ylim=(-1.2, 1.45), aspect='equal')
    ax.axis('off')
    ax.set_title(rf'$W^-: m_z={lam:+d}$', weight='bold')
    ax.plot(0, 0, 'ko', ms=6)
    ax.annotate('', (0, 1.15), (0, -1.05), arrowprops={'arrowstyle': '->', 'color': '0.65', 'lw': 1})
    ax.text(0.08, 1.13, '$z$', color='0.4')
    phi = np.linspace(np.arctan2(n[1], n[0]), np.pi/2, 80)
    ax.plot(.34*np.cos(phi), .34*np.sin(phi), color='0.4', lw=1)
    ax.text(.19, .41, r'$\theta$', color='0.35', fontsize=12)
    for sign, label in [(1, r'$\ell^-$'), (-1, r'$\bar\nu$')]:
        pos = sign * 0.85 * n
        ax.annotate('', pos, (0, 0), arrowprops={'arrowstyle': '->', 'color': blue, 'lw': 2.4})
        ax.text(*(pos + sign * 0.18 * n), label, ha='center', color=blue, fontsize=14)
        start = pos + np.array([0.04, -0.25])
        ax.annotate('', start - 0.43 * n, start, arrowprops={'arrowstyle': '->', 'color': red, 'lw': 2.4})
    if lam:
        ax.annotate('', (-0.95, 0.48 * lam), (-0.95, -0.28 * lam), arrowprops={'arrowstyle': '->', 'color': '#673d9c', 'lw': 3})
        ax.text(-1.02, 0.78, '$W$ spin', ha='center', color='#673d9c', fontsize=10)
    else:
        ax.text(-1.28, 0.55, '$S_z=0$\n$S=1$', color='#673d9c', fontsize=12)
    ax.text(0, -1.12, r'$h_{\ell}=-1/2,\quad h_{\bar\nu}=+1/2$', ha='center', fontsize=11)
ax = fig.add_subplot(gs[1, :])
z = np.linspace(-1, 1, 700)
ax.plot(z, 3 / 8 * (1 - z)**2, label=r'$m_z=+1$', color='#2772a5', lw=2.5)
ax.plot(z, 3 / 4 * (1 - z*z), label=r'$m_z=0$', color='#33834e', lw=2.5)
ax.plot(z, 3 / 8 * (1 + z)**2, label=r'$m_z=-1$', color='#b75b24', lw=2.5)
ax.set(xlim=(-1, 1), ylim=(0, 1.62), xlabel=r'$\cos\theta$ (charged-lepton direction relative to $+z$)', ylabel=r'$(1/\Gamma_\ell)\,d\Gamma_\ell/d\cos\theta$')
ax.grid(alpha=0.2)
ax.legend(loc='upper center', ncol=3, frameon=False)
fig.suptitle('Momentum arrows: blue     Lepton spin arrows: red\nEach angular profile has unit area and the same total width', fontsize=14)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=110, facecolor='white', transparent=False)
