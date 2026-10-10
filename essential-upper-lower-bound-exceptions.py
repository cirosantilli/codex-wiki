"""Two singleton changes alter pointwise bounds but not Lebesgue essential bounds.

Run from the desired output directory. Python/dependencies: root pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(9.6, 4.8), dpi=120, facecolor='white')
ax.set_facecolor('white')
ax.axhspan(0, 1, color='#d8ede5', alpha=0.65, label='Essential bounds: 0 and 1')
# Break the line at the two excluded values rather than interpolating jumps.
for lo, hi in [(0, 0.25), (0.25, 0.75), (0.75, 1)]:
    x = np.linspace(lo, hi, 250)
    ax.plot(x, x, color='#176c91', linewidth=2.6)
ax.scatter([0.25, 0.75], [0.25, 0.75], s=85, facecolors='white', edgecolors='#176c91', linewidths=2, zorder=5)
ax.scatter([0.25, 0.75], [-3, 4], s=80, color='#ad3c43', zorder=5)
for y, label, x in [(-3, 'Pointwise infimum = −3', 0.3), (4, 'Pointwise supremum = 4', 0.15)]:
    ax.axhline(y, color='#ad3c43', linestyle='--', linewidth=1.1)
    ax.text(x, y + 0.15, label, color='#ad3c43', fontsize=11)
ax.text(0.04, 0.6, 'Essential supremum = 1\nEssential infimum = 0', fontsize=11, va='center', bbox=dict(facecolor='white', edgecolor='none', alpha=0.9))
ax.set(xlim=(-0.02, 1.02), ylim=(-3.5, 4.6), xlabel='Input x', ylabel='g(x)', title='Changing two inputs: pointwise bounds versus essential bounds')
ax.set_xticks([0, 0.25, 0.5, 0.75, 1]); ax.grid(alpha=0.15)
fig.text(0.5, 0.025, 'Lebesgue measure on [0, 1] • filled points are included; hollow points are excluded', ha='center', fontsize=10)
fig.subplots_adjust(left=0.085, right=0.975, top=0.89, bottom=0.16)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white')
plt.close(fig)
