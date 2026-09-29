"""Lp norms for the original three-point probability example.

Run from the desired output directory. Python/dependencies: root pyproject.toml.
Stable rescaling avoids overflowing 10**p for large p.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

p = np.geomspace(1, 512, 500)
fig, ax = plt.subplots(figsize=(9.6, 4.8), dpi=120, facecolor='white')
ax.set_facecolor('white')
for epsilon, color, label in [(0, '#176c91', 'Zero weight: (0.5, 0.5, 0)'), (0.001, '#ad3c43', 'Rare value: (0.499, 0.5, 0.001)')]:
    weights = np.array([0.5 - epsilon, 0.5, epsilon])
    values = np.array([1., 3., 10.])
    active = weights > 0
    scale = values[active].max()
    norm = scale * np.sum(weights[active, None] * (values[active, None] / scale) ** p, axis=0) ** (1 / p)
    ax.plot(p, norm, color=color, linewidth=2.6, label=label)
    ax.axhline(scale, color=color, linestyle='--', linewidth=1.2)
    ax.text(280, scale + 0.12, f'Limit = {scale:g}', color=color, fontsize=11)
ax.set_xscale('log', base=2)
ax.set(xlim=(1, 512), ylim=(1.5, 10.7), xlabel='Exponent p (logarithmic axis)', ylabel='Lp norm', title='Values 1, 3, 10: zero probability versus small positive probability')
ax.set_xticks([1, 2, 4, 8, 16, 32, 64, 128, 256, 512], labels=['1','2','4','8','16','32','64','128','256','512'])
ax.legend(loc='center right', framealpha=0.95); ax.grid(alpha=0.18)
fig.text(0.5, 0.025, 'Dashed lines are limits as p → ∞; the pointwise supremum is 10 in both cases.', ha='center', fontsize=10)
fig.subplots_adjust(left=0.085, right=0.975, top=0.89, bottom=0.16)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white')
plt.close(fig)
