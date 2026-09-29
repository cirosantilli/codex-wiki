"""Original model comparisons; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Write the PNG basename to the caller's working directory. Honor MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False})
fig, ax = plt.subplots(1, 3, figsize=(11.2, 4.0), facecolor='white', layout='constrained')
s = np.geomspace(0.01, 100, 400)
ax[0].loglog(s, s + np.expm1(-s), label='Thermal initial velocity', color='#174c84', lw=2)
ax[0].loglog(s[s < 1], s[s < 1] ** 2 / 2, '--', color='#ca6b1e', label=r'Ballistic: $s^2/2$')
ax[0].loglog(s[s > 1], s[s > 1], ':', color='#198754', label='Diffusive: s')
ax[0].set(xlabel=r'$s=t/\tau$', ylabel=r'$\langle x^2\rangle/(2D\tau)$', title='Thermal displacement')
ax[0].legend(fontsize=8, loc='upper left')
s = np.linspace(0, 4, 400)
ax[1].plot(s, -np.expm1(-s), label='Kelvin-Voigt (parallel)', lw=2, color='#174c84')
ax[1].plot(s, 1+s, label='Maxwell (series)', lw=2, color='#ca6b1e')
ax[1].scatter([0], [1], color='#ca6b1e', s=15, zorder=3)
ax[1].set(xlabel=r'$s=t/\tau$', ylabel=r'$\delta/[F_0\ell^3/(3EI)]$', title='Quasistatic step-load creep', ylim=(0, 5.3))
ax[1].legend(fontsize=8, loc='upper left')
z=np.linspace(0, 8, 401)
f=np.ones_like(z)
f[1:]=z[1:]**2/(2*(np.expm1(z[1:])-z[1:]))
ax[2].semilogy(z, f, label='Diffusion limited', lw=2, color='#174c84')
ax[2].semilogy(z, np.exp(-z), label='Reaction limited', lw=2, color='#ca6b1e')
ax[2].set(xlabel=r'$z=Fa/(k_BT)$', ylabel=r'$V(F)/V(0)$', title='Ratchet: negligible removal')
ax[2].legend(fontsize=8)
for a in ax:
    a.set_facecolor('white')
    a.grid(alpha=0.15)
fig.savefig(Path('paper-71-mechanical-response.png'), dpi=100, facecolor='white', transparent=False)
plt.close(fig)
