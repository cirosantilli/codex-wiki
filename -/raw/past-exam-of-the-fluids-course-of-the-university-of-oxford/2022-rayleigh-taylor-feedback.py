"""Original instability sketch; tested with Python 3.14, numpy 2.3.5, matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
fig, axes = plt.subplots(1, 2, figsize=(11, 4.3), constrained_layout=True)
ax = axes[0]
x = np.linspace(0, 2*np.pi, 500)
z = -0.22*np.cos(x)
ax.fill_between(x, z, 1, color='#d5e5f3')
ax.fill_between(x, -1, z, color='#fff0ca')
ax.plot(x, z, color='#273b53', lw=2)
ax.plot(x, z+0.065, '--', color='#7593a9', lw=0.8)
ax.plot(x, z-0.065, '--', color='#7593a9', lw=0.8)
for xpos, sign, col in [(np.pi/2, r'$-\omega_y$', '#9d3157'), (3*np.pi/2, r'$+\omega_y$', '#195c8c')]:
    ax.text(xpos, 0.12, sign, color=col, ha='center', fontsize=15)
    ax.annotate('', (xpos, -0.05), (xpos, -0.52), arrowprops={'arrowstyle':'->', 'lw':1.5, 'color':'#195c8c'})
ax.text(np.pi/2, -0.68, r'$\nabla\rho$ points upward', ha='center', fontsize=10)
ax.annotate('', (np.pi, .65), (np.pi, .26), arrowprops={'arrowstyle':'->', 'color':'#348254', 'lw':2.5})
ax.annotate('', (5.92, -.65), (5.92, -.25), arrowprops={'arrowstyle':'->', 'color':'#348254', 'lw':2.5})
ax.text(np.pi, .75, 'light crest rises', ha='center', color='#276841')
ax.text(.18, .75, r'$\rho_2>\rho_1$', color='#273b53')
ax.text(.18, -.88, r'$\rho_1$', color='#674917')
ax.text(5.82, .75, r'$\mathbf{g}\downarrow$', ha='center')
ax.set(xlim=(0, 2*np.pi), ylim=(-1, 1), xlabel='$x$', ylabel='$z$')
ax.set_xticks([])
ax.set_yticks([0])
ax.set_title('Vorticity reinforces the displacement', fontsize=12)
ax.text(.5, -.24, r'$\partial_t\gamma=-2\mathcal{A}g\,\partial_x\eta$;  $\omega_y=\partial_z u-\partial_x w$', transform=ax.transAxes, ha='center')

ax = axes[1]
s = np.logspace(-2, 2, 500)
ax.loglog(s, np.sqrt(s*np.tanh(s)), lw=2.5, color='#195c8c', label='finite-depth growth')
ax.loglog(s, s, '--', lw=1.2, color='#9d3157', label=r'shallow: $\sigma\propto k$')
ax.loglog(s, np.sqrt(s), ':', lw=1.8, color='#348254', label=r'deep: $\sigma\propto\sqrt{k}$')
ax.set(xlim=(.01, 100), ylim=(.008, 20), xlabel='$kh$', ylabel=r'$\sigma\sqrt{h/(\mathcal{A}g)}$')
ax.set_title('Sharp interface: no short-wave cutoff', fontsize=12)
ax.legend(loc='upper left', fontsize=9)
ax.grid(True, which='major', alpha=.2)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=120, facecolor='white', transparent=False, metadata={'Software':'codex-wiki original figure'})
plt.close(fig)
