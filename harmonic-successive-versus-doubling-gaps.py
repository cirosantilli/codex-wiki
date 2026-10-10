"""Harmonic-sum gaps: shrinking local steps versus persistent long-lag drift.

Run in desired output directory. Versions/dependencies: root pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

maximum = 8192
terms = 1.0 / np.arange(1, 2 * maximum + 1)
harmonic = np.concatenate(([0.], np.cumsum(terms)))
n = np.unique(np.geomspace(1, maximum, 500).astype(int))
local = 1.0 / (n + 1)
long_gap = harmonic[2 * n] - harmonic[n]
fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.6), dpi=120, facecolor='white')
ax = axes[0]
ax.loglog(n, local, color='#176c91', linewidth=2.5, label='Successive: Hₙ₊₁ − Hₙ')
ax.loglog(n, long_gap, color='#ad3c43', linewidth=2.5, label='Doubling: H₂ₙ − Hₙ')
ax.axhline(0.5, color='#a8773e', linestyle='--', linewidth=1.1, label='Exact lower bound 1/2')
ax.set(xlim=(1, maximum), ylim=(8e-5, 1.2), xlabel='Index n (log scale)', ylabel='Gap size (log scale)', title='Small latest steps do not control all pairs')
ax.legend(loc='lower left', fontsize=9, framealpha=0.95); ax.grid(alpha=0.17, which='major')
ax = axes[1]
k = np.arange(1, 81)
ax.plot(k, harmonic[k], color='#777f86', linewidth=2)
ax.fill_between(k, harmonic[k], 0, where=(k >= 20) & (k <= 40), color='#f2d6d8', alpha=0.7)
ax.scatter([20, 40], harmonic[[20, 40]], color='#ad3c43', s=55, zorder=4)
ax.vlines([20, 40], [0, 0], harmonic[[20, 40]], color='#ad3c43', linestyle=':', linewidth=1.2)
ax.annotate('', xy=(46, harmonic[40]), xytext=(46, harmonic[20]), arrowprops=dict(arrowstyle='<->', color='#ad3c43', linewidth=1.6))
ax.text(49, (harmonic[20] + harmonic[40]) / 2, 'H₄₀ − H₂₀\n≈ 0.681 > 1/2', va='center', color='#ad3c43', fontsize=10)
ax.set(xlim=(0, 80), ylim=(0, 5.8), xlabel='Index k', ylabel='Harmonic sum Hₖ', title='A growing lag accumulates many small terms')
ax.grid(alpha=0.16)
fig.text(0.5, 0.025, 'Computed harmonic sums; H₂ₙ − Hₙ ≥ 1/2 holds for every n ≥ 1 by an exact block bound.', ha='center', fontsize=10)
fig.subplots_adjust(left=0.07, right=0.98, top=0.88, bottom=0.16, wspace=0.26)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white')
plt.close(fig)
