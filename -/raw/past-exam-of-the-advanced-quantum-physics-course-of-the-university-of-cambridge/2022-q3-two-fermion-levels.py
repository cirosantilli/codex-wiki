"""Original first-order spectrum; Python 3.14, numpy 2.3.5, matplotlib 3.10.7.

Run from the mirrored _media directory. Energies are in hbar*omega.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

b = np.linspace(-0.2, 0.2, 401)
u = 0.12
fig, ax = plt.subplots(figsize=(7.4, 4.5), layout='constrained')
ax.plot(b, np.full_like(b, 1 + u), color='#9244a0', lw=2.2, label=r'singlet $(N,n)=(0,0)$')
ax.plot(b, np.full_like(b, 2 + u), color='#9244a0', lw=2.2, ls='--', label=r'singlet $(N,n)=(1,0)$')
for m, color in [(-1, '#d97706'), (0, '#177c65'), (1, '#236bc0')]:
    ax.plot(b, 2 + m*b, color=color, lw=2, label=fr'triplet $M={m}$')
ax.axvline(0, color='0.65', lw=0.7, zorder=0)
ax.set(xlim=(-0.2, 0.2), ylim=(1.02, 2.28), xlabel=r'$b=2\mu_B B_z/(\hbar\omega)$', ylabel=r'$E/(\hbar\omega)$', title=r'Weak contact interaction: $U=0.12\hbar\omega$')
ax.set_xticks([-0.2, -0.1, 0, 0.1, 0.2])
ax.grid(alpha=0.18)
ax.legend(loc='center left', fontsize=9, framealpha=0.95)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=150, facecolor='white')
plt.close(fig)
