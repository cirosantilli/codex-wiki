"""Draw an original chosen type-I band profile and injection/readout schematic.

Tested with Python 3.14, matplotlib 3.10.7 and NumPy 2.3.5.
Run from the output directory; no material parameters or historical data are used.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle
import numpy as np


def main():
    plt.rcParams.update({'font.size': 11, 'axes.spines.top': False,
                         'axes.spines.right': False, 'figure.facecolor': 'white'})
    fig = plt.figure(figsize=(9.4, 7.2), layout='constrained')
    gs = fig.add_gridspec(2, 1, height_ratios=[1.8, 1])
    ax = fig.add_subplot(gs[0])
    ax.axvspan(-1, 1, color='#f0f7e6')
    x = [-3, -1, -1, 1, 1, 3]
    ax.plot(x, [1.6, 1.6, 1, 1, 1.6, 1.6], color='#215a9a', lw=2.7)
    ax.plot(x, [-.4, -.4, 0, 0, -.4, -.4], color='#ac3c31', lw=2.7)
    for pos in [-1, 1]:
        ax.axvline(pos, color='.55', ls=':', lw=1)
    ax.text(-2, 2.03, 'B: n-type injector', ha='center')
    ax.text(0, 2.03, 'A: active layer', ha='center')
    ax.text(2, 2.03, 'B: p-type injector', ha='center')
    ax.annotate('electrons', xy=(-.15, 1.15), xytext=(-2, 1.8),
                arrowprops={'arrowstyle': '->', 'color': '#215a9a', 'lw': 1.8},
                color='#215a9a', ha='center')
    ax.annotate('holes', xy=(.15, -.14), xytext=(2, -.75),
                arrowprops={'arrowstyle': '->', 'color': '#ac3c31', 'lw': 1.8},
                color='#ac3c31', ha='center')
    for xpos, low, high, label in [(-1.28, 1, 1.6, r'$\Delta E_c=0.6$'),
                                   (1.3, -.4, 0, r'$\Delta E_v=0.4$')]:
        ax.annotate('', xy=(xpos, low), xytext=(xpos, high),
                    arrowprops={'arrowstyle': '<->', 'color': '.2'})
        ax.text(xpos + (-.12 if xpos < 0 else .12), (low + high) / 2, label,
                ha='right' if xpos < 0 else 'left', va='center', fontsize=10)
    ax.annotate('', xy=(0, .12), xytext=(0, .87),
                arrowprops={'arrowstyle': '->', 'lw': 2, 'color': '#8139a1'})
    ax.text(.13, .48, 'recombination\n→ light', color='#8139a1', va='center')
    ax.text(2.5, 1.68, r'$E_c$', color='#215a9a')
    ax.text(-2.7, -.3, r'$E_v$', color='#ac3c31')
    ax.set(xlim=(-3.1, 3.1), ylim=(-.95, 2.25), ylabel='Electron energy (chosen units)',
           xlabel='Position across layers', xticks=[-1, 1], xticklabels=[r'$-a$', r'$a$'])
    ax.set_title('A chosen type-I double heterostructure', weight='bold', pad=12)

    bx = fig.add_subplot(gs[1])
    bx.set(xlim=(0, 10), ylim=(0, 3.4))
    bx.axis('off')
    bx.add_patch(Rectangle((2.4, 1.12), 4.3, 1.4, facecolor='#e6eef8', edgecolor='.25'))
    bx.add_patch(Rectangle((2.4, 1.7), 4.3, .25, facecolor='#9cba64', edgecolor='none'))
    bx.text(4.55, 2.2, 'semiconductor layers', ha='center')
    bx.text(4.55, 1.37, 'active layer + optical mode', ha='center', fontsize=10)
    bx.annotate('electrical injection', xy=(4.55, 2.55), xytext=(4.55, 3.08),
                ha='center', arrowprops={'arrowstyle': '->', 'lw': 2})
    bx.add_patch(FancyArrowPatch((6.8, 1.82), (8.0, 1.82), arrowstyle='->',
                                mutation_scale=17, color='#8139a1', lw=2.5))
    bx.add_patch(Rectangle((8.15, 1.25), 1.25, 1.15, facecolor='white', edgecolor='.3'))
    bx.text(8.77, 1.82, 'optical\nreadout', ha='center', va='center')
    bx.text(4.8, .64, 'Band offsets confine carriers; index contrast guides light.', ha='center')
    bx.text(4.8, .1, 'Conceptual schematic • flat bands omit electrostatic bending',
            ha='center', color='.35', fontsize=10)
    fig.savefig(Path(__file__).stem + '.png', dpi=120, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
