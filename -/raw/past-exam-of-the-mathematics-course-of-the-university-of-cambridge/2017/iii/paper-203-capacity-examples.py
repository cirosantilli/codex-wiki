"""Original diagram. CWD PNG; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
Dependencies: unchanged repository-root pyproject.toml.
"""
import os
os.environ.setdefault('MPLCONFIGDIR', '/tmp/2017-iii-paper-203-mpl-cache')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge, Rectangle
from pathlib import Path
fig, axes = plt.subplots(1, 3, figsize=(10.8, 3.6), dpi=100, facecolor='white')
for ax in axes:
    ax.set_facecolor('white')
    ax.axhline(0, color='#333333', linewidth=1.3)
    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-0.12, 1.45)
    ax.set_aspect('equal')
    ax.set_xticks([-1, 0, 1])
    ax.set_yticks([0, 1])
    ax.tick_params(labelsize=10)
    ax.spines[['top', 'right', 'left', 'bottom']].set_visible(False)
    ax.set_xlabel('Real part', fontsize=10)
axes[0].plot([0, 0], [0, 1], linewidth=4, color='#165f9b')
axes[0].scatter([0], [1], color='#165f9b', s=25)
axes[0].set_title('Vertical slit', fontsize=13)
axes[0].text(0.5, 0.55, r'$[0,i]$', fontsize=13)
axes[0].text(0, 1.22, r'$\operatorname{hcap}=1/2$', ha='center', fontsize=13)
axes[1].add_patch(Wedge((0, 0), 1, 0, 180, facecolor='#bedaf0', edgecolor='#165f9b', linewidth=2))
axes[1].set_title('Filled half-disc', fontsize=13)
axes[1].text(0, 1.22, r'$\operatorname{hcap}=1$', ha='center', fontsize=13)
axes[2].add_patch(Rectangle((-1, 0), 2, .16, facecolor='#bedaf0', edgecolor='#165f9b', linewidth=2))
axes[2].annotate(r'$\varepsilon$', xy=(1, .08), xytext=(1.24, .6), fontsize=13, arrowprops={'arrowstyle': '->', 'color': '#165f9b'})
axes[2].set_title('Thin rectangle', fontsize=13)
axes[2].text(0, 1.2, r'$\operatorname{hcap}\leq 8\varepsilon/\pi$', ha='center', fontsize=13)
axes[2].text(0, .89, r'$\operatorname{diam}\to 2$', ha='center', fontsize=13)
fig.subplots_adjust(left=.04, right=.98, bottom=.14, top=.89, wspace=.27)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=100, facecolor='white', transparent=False)
plt.close(fig)
