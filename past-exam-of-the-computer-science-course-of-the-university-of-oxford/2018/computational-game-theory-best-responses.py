"""Best-response correspondences for the solved two-action zero-sum game.

Run from the desired output directory; uses the root pyproject.toml environment.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7, 5.2), dpi=100, facecolor='white')
p, q = 5 / 8, 3 / 8
# Player 1 chooses p=1 below the horizontal threshold and p=0 above it.
ax.plot([1, 1, 0, 0], [0, q, q, 1], color='#1264a3', lw=3,
        label='Player 1: best responses p to q', zorder=2)
# Player 2 chooses q=0 to the left of its vertical threshold and q=1 right of it.
ax.plot([0, p, p, 1], [0, 0, 1, 1], color='#c04b19', lw=3,
        linestyle='--', label='Player 2: best responses q to p', zorder=3)
ax.scatter([p], [q], color='#202020', s=55, zorder=5)
ax.annotate('Unique equilibrium\n(p, q) = (5/8, 3/8)', xy=(p, q),
            xytext=(0.18, 0.60), fontsize=11,
            arrowprops={'arrowstyle': '->', 'color': '#202020'},
            bbox={'facecolor': 'white', 'edgecolor': '#dddddd', 'pad': 5},
            zorder=6)
ax.set(xlim=(-0.045, 1.045), ylim=(-0.045, 1.045),
       xlabel="Player 1's probability p of Head",
       ylabel="Player 2's probability q of Head",
       title='Best-response correspondences (X = 1, Y = 3)')
ax.set_xticks([0, p, 1], ['0', '5/8', '1'])
ax.set_yticks([0, q, 1], ['0', '3/8', '1'])
ax.grid(alpha=0.22)
ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.31), frameon=False, fontsize=10)
fig.subplots_adjust(left=0.12, right=0.96, top=0.90, bottom=0.28)
fig.savefig(Path(__file__).with_suffix('.png').name, facecolor='white', dpi=100)
plt.close(fig)
