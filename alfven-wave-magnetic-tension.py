"""Draw a linear shear Alfvén displacement; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from _media; the output is this generator's basename with extension .png.
The geometry is original and illustrative, not measured experimental data.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

BLUE = '#176c9c'
RED = '#b33e38'
GREEN = '#268365'
plt.rcParams.update({'font.size': 11, 'font.family': 'DejaVu Sans'})
fig = plt.figure(figsize=(9.6, 5.4), facecolor='white')
ax = fig.add_axes((0.08, 0.29, 0.87, 0.55))
z = np.linspace(0, 2 * np.pi, 600)
xi = 0.40 * np.sin(z)
for offset in [-0.9, 0, 0.9]:
    ax.plot(z, np.full_like(z, offset), '--', color='#bec8ce', lw=1)
    ax.plot(z, offset + xi, color=BLUE, lw=2.3)
    for zz in [0.55, 3.65, 5.65]:
        ax.annotate('', xy=(zz + 0.19, offset + 0.40 * np.sin(zz + 0.19)),
                    xytext=(zz, offset + 0.40 * np.sin(zz)),
                    arrowprops={'arrowstyle': '->', 'color': BLUE, 'lw': 2})
crest = np.pi / 2
ax.annotate('', xy=(crest, 0.4), xytext=(crest, 0),
            arrowprops={'arrowstyle': '->', 'color': GREEN, 'lw': 2.4})
ax.text(crest - 0.14, 0.17, r'$\xi_x$', ha='right', color=GREEN)
ax.annotate('', xy=(crest + 0.22, -0.12), xytext=(crest + 0.22, 0.4),
            arrowprops={'arrowstyle': '->', 'color': RED, 'lw': 2.4})
ax.text(crest + 0.36, 0.14, 'restoring force', color=RED)
zz = 3.3
ax.annotate('', xy=(zz + 0.65, 0.40 * np.sin(zz) + 0.65 * 0.4 * np.cos(zz)),
            xytext=(zz, 0.40 * np.sin(zz)),
            arrowprops={'arrowstyle': '->', 'color': BLUE, 'lw': 2.4})
ax.text(3.30, -0.65, r'$b_x = B_0\,\partial_z\xi_x$', color=BLUE)
ax.annotate('', xy=(6.05, 1.48), xytext=(4.30, 1.48),
            arrowprops={'arrowstyle': '->', 'color': '#333333', 'lw': 1.8})
ax.text(5.15, 1.58, r'background $B_0$ and propagation axis $z$', ha='center')
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.5, 1.9)
ax.set_xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
              ['0', r'$\lambda_\parallel/4$', r'$\lambda_\parallel/2$',
               r'$3\lambda_\parallel/4$', r'$\lambda_\parallel$'])
ax.set_yticks([])
ax.set_xlabel('Position along the background field')
ax.set_ylabel('Transverse position $x$')
ax.spines[['top', 'right', 'left']].set_visible(False)
fig.suptitle('A sideways bend produces a restoring magnetic tension', y=0.97, fontsize=15)
fig.text(0.5, 0.115,
         r'$\rho\,\partial_t^2\xi_x = (B_0^2/\mu_0)\,\partial_z^2\xi_x$',
         ha='center', fontsize=14)
fig.text(0.5, 0.045, 'Dashed: straight equilibrium lines.  Blue: displaced lines.  Bend exaggerated; linear theory assumes small slope.',
         ha='center', fontsize=10, color='#444444')
fig.savefig(Path(__file__).with_suffix('.png').name, dpi=120, facecolor='white')
plt.close(fig)
