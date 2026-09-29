"""Draw distinguishable-scalar scattering; write the PNG to the caller's CWD."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7.2, 4.3), facecolor='white')
ax.set_facecolor('white')
v1, v2 = (0, 1), (0, -1)
for start, end in [((-2, 1.6), v1), (v1, (2, 1.6)), ((-2, -1.6), v2), (v2, (2, -1.6))]:
    ax.plot([start[0], end[0]], [start[1], end[1]], color='#222222', lw=2.1, ls=(0, (5, 3)))
ax.plot([0, 0], [-1, 1], color='#146a91', lw=2.2, ls=(0, (5, 3)))
ax.scatter([0, 0], [1, -1], s=40, color='#222222', zorder=3)
for x, y, label in [(-2.08, 1.83, r'$\phi(p)$'), (2.08, 1.83, r'$\phi(p^{\prime})$'), (-2.08, -1.9, r'$\psi(q)$'), (2.08, -1.9, r'$\psi(q^{\prime})$')]:
    ax.text(x, y, label, ha='center', va='center', fontsize=16)
ax.text(0.22, 0.1, r'$\Phi$', color='#146a91', fontsize=19)
ax.annotate('', xy=(-0.38, -0.65), xytext=(-0.38, 0.65), arrowprops={'arrowstyle': '->', 'color': '#146a91', 'lw': 1.5})
ax.text(-0.58, 0, r'$p-p^{\prime}$', ha='right', va='center', fontsize=14, color='#146a91')
ax.text(0.08, 1.27, r'$-ig$', fontsize=14, va='bottom')
ax.text(0.08, -1.27, r'$-ig$', fontsize=14, va='top')
ax.text(0, -2.35, r'$t=(p-p^{\prime})^2$', ha='center', fontsize=15)
ax.set_xlim(-2.9, 2.9)
ax.set_ylim(-2.65, 2.3)
ax.axis('off')
fig.tight_layout(pad=0.4)
fig.savefig(Path.cwd() / 'paper-44-scalar-exchange.png', dpi=150, facecolor='white', transparent=False)
plt.close(fig)
