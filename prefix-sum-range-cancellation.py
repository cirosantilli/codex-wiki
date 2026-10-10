"""A signed toy array and exact range-sum cancellation in its prefixes.

Write a white PNG to the current directory; versions are in pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

values = np.array([4, -2, 5, -1, 3, -4], dtype=int)
prefix = np.r_[0, np.cumsum(values)]
fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.8), dpi=120, facecolor='white')
for ax in axes:
    ax.set_facecolor('white')
    ax.grid(axis='y', alpha=0.17)
colors = ['#acb4ba', '#267897', '#267897', '#267897', '#acb4ba', '#acb4ba']
axes[0].bar(np.arange(1, 7), values, color=colors, width=0.68)
axes[0].axhline(0, color='#414d53', linewidth=1)
for i, a in enumerate(values, start=1):
    axes[0].text(i, a + (0.22 if a >= 0 else -0.22), f'{a:+d}', ha='center',
                 va='bottom' if a >= 0 else 'top', fontsize=12)
axes[0].set(xlim=(0.4, 6.6), ylim=(-5.8, 6.5), xticks=np.arange(1, 7),
            xlabel='Entry index i', ylabel='Input aᵢ', title='Entries 2 through 4: −2 + 5 − 1 = 2')
axes[0].text(0.5, 0.045, 'Blue entries form the requested block.', transform=axes[0].transAxes,
             ha='center', fontsize=10)
axes[1].plot(np.arange(7), prefix, 'o-', color='#657b88', linewidth=2.1)
axes[1].scatter([1, 4], prefix[[1, 4]], s=75, color='#267897', zorder=4)
axes[1].plot([1, 5.6], [4, 4], color='#267897', linestyle=':', linewidth=1)
axes[1].plot([4, 5.6], [6, 6], color='#267897', linestyle=':', linewidth=1)
axes[1].annotate('', xy=(5.6, 6), xytext=(5.6, 4),
                 arrowprops={'arrowstyle': '<->', 'color': '#267897', 'lw': 1.8})
axes[1].text(5.52, 5, 'Difference\n6 − 4 = 2', va='center', ha='right', fontsize=10, color='#176481')
axes[1].annotate('P₁ = 4', (1, 4), xytext=(0.25, 5.7),
                 arrowprops={'arrowstyle': '->', 'color': '#267897'}, fontsize=10)
axes[1].annotate('P₄ = 6', (4, 6), xytext=(3.2, 7.8),
                 arrowprops={'arrowstyle': '->', 'color': '#267897'}, fontsize=10)
axes[1].set(xlim=(-0.25, 6.3), ylim=(-0.6, 10.3), xticks=np.arange(7),
            xlabel='Prefix endpoint m', ylabel='Accumulated sum Pₘ',
            title='Subtract the shared beginning: P₄ − P₁')
fig.text(0.5, 0.025, 'P₀ = 0; prefixes retain order and need not increase when the input has negative entries.',
         ha='center', fontsize=10)
fig.subplots_adjust(left=0.065, right=0.98, top=0.9, bottom=0.17, wspace=0.29)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white')
plt.close(fig)
