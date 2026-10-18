from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 11, 'axes.titlesize': 13, 'axes.labelsize': 12})
fig, (ax, bx) = plt.subplots(1, 2, figsize=(10.6, 4.4), dpi=120, facecolor='white')
q = np.linspace(0, 7, 700)
ax.plot(q, q/(1+q*q), color='#2268a3', lw=2.5, label=r'$S=q/(1+q^2)$')
ax.plot([0, 0.62], [0, 0.62], color='0.5', ls='--', lw=1.2, label='Small-rate tangent')
ax.plot(1, 0.5, 'o', color='#b83434', ms=6)
ax.annotate('Maximum (1, 1/2)', xy=(1, 0.5), xytext=(2.05, 0.56), arrowprops={'arrowstyle': '->', 'color': '0.3'}, fontsize=10)
ax.annotate(r'$S\sim 1/q$', xy=(5.7, 5.7/(1+5.7**2)), xytext=(4.4, 0.32), arrowprops={'arrowstyle': '->', 'color': '0.3'})
ax.set(xlim=(0, 7), ylim=(0, 0.65), xlabel=r'$q=\dot\gamma\sqrt{\alpha(2\tau-\alpha)}$', ylabel=r'$S=T_{xy}\sqrt{\alpha(2\tau-\alpha)}/\mu$', title='Homogeneous steady shear')
ax.legend(loc='lower left', fontsize=9, frameon=False)
K = np.linspace(0, 2.3, 700)
r = np.sqrt(np.maximum(1-4*K*K, 0))
im = 0.5*np.sqrt(np.maximum(4*K*K-1, 0))
bx.plot(K, (-1+r)/2, lw=2.2, color='#2268a3', label=r'$\mathrm{Re}(\tau\sigma_+)$')
bx.plot(K, (-1-r)/2, lw=2.2, color='#b83434', label=r'$\mathrm{Re}(\tau\sigma_-)$')
bx.plot(K, im, lw=1.8, ls='--', color='#26764e', label=r'$\pm\mathrm{Im}(\tau\sigma)$')
bx.plot(K, -im, lw=1.8, ls='--', color='#26764e')
bx.axvline(0.5, color='0.6', lw=1, ls=':')
bx.text(0.54, 1.7, 'Damped oscillation', fontsize=10)
bx.set(xlim=(0, 2.3), ylim=(-2.4, 2.4), xlabel=r'$K=|k|\sqrt{\tau\nu}$', ylabel='Dimensionless temporal exponent', title='Linear temporal branches')
bx.legend(loc='lower left', fontsize=9, frameon=False)
for a in (ax, bx):
    a.set_facecolor('white')
    a.spines[['top', 'right']].set_visible(False)
    a.grid(alpha=0.18)
fig.tight_layout()
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False)
