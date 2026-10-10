"""Illustrate all-pair tail control, not a test based on finite observations.

Run in desired output directory. Versions/dependencies: root pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

n = np.arange(1, 15)
q = 1.0 - 2.0 ** (-n)
a = (-1.0) ** n
fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.6), dpi=120, facecolor='white')
for ax, values in zip(axes, [q, a]):
    ax.set_facecolor('white')
    ax.plot(n, values, color='#a0a9af', linestyle=':', linewidth=1.3)
    ax.scatter(n[n < 4], values[n < 4], color='#bc803d', s=45, zorder=4, label='Initial terms')
    ax.scatter(n[n >= 4], values[n >= 4], color='#176c91', s=45, zorder=4, label='Terms n ≥ 4')
    ax.axvline(3.5, color='#77848c', linestyle='--', linewidth=1)
    ax.set(xlabel='Index n', xlim=(0.5, 14.5))
    ax.set_xticks([1, 4, 7, 10, 14]); ax.grid(alpha=0.16)
axes[0].axhspan(15 / 16, 1, color='#bde0d0', alpha=0.6)
axes[0].axhline(1, color='#47856a', linestyle='--', linewidth=1)
axes[0].annotate('Whole tail fits in [15/16, 1)\nDiameter = 1/16 < 0.1', xy=(7.5, 0.97), xytext=(4.4, 0.73), arrowprops=dict(arrowstyle='->', color='#365e50'), fontsize=10, color='#365e50')
axes[0].set(ylim=(0.43, 1.07), ylabel='qₙ', title='Cauchy: qₙ = 1 − 2⁻ⁿ')
axes[1].axhline(1, color='#ad3c43', linestyle='--', linewidth=1)
axes[1].axhline(-1, color='#ad3c43', linestyle='--', linewidth=1)
axes[1].text(5, 0.13, 'Arbitrarily late pairs\nremain separated by 2', fontsize=11, ha='left', color='#ad3c43', bbox=dict(facecolor='white', edgecolor='none', alpha=0.95))
axes[1].set(ylim=(-1.4, 1.4), ylabel='aₙ', title='Not Cauchy: aₙ = (−1)ⁿ')
fig.text(0.5, 0.025, 'Finite illustrations; the formulas establish the claims for every later index.', ha='center', fontsize=10)
fig.subplots_adjust(left=0.07, right=0.98, top=0.88, bottom=0.16, wspace=0.24)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white')
plt.close(fig)
