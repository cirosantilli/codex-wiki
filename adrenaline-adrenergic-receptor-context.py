"""Original qualitative human-adipocyte receptor context, not assay data.

Python 3.14 and matplotlib 3.10.7; writes its matching PNG to CWD.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def main():
    fig, ax = plt.subplots(figsize=(10, 5.7), dpi=120)
    fig.patch.set_facecolor('white')
    ax.set(xlim=(0, 10), ylim=(0, 5.7))
    ax.axis('off')
    blue, orange, green, ink = '#236b8e', '#b45c21', '#367a55', '#18313d'

    def box(x, y, text, color=blue, width=2.5, height=.62):
        ax.add_patch(FancyBboxPatch((x-width/2, y-height/2), width, height,
                                   boxstyle='round,pad=0.07', facecolor='#f6f9fa',
                                   edgecolor=color, linewidth=1.6))
        ax.text(x, y, text, ha='center', va='center', fontsize=12, color=ink)

    def arrow(a, b, color=blue):
        ax.add_patch(FancyArrowPatch(a, b, arrowstyle='-|>', mutation_scale=17,
                                    color=color, linewidth=1.8))

    ax.text(5, 5.33, 'One messenger, distinct receptor responses',
            ha='center', fontsize=18, weight='bold', color=ink)
    box(5, 4.65, 'Adrenaline')
    for x, text, color in [(1.7, 'β receptor', blue),
                            (5, 'α₂ receptor', orange),
                            (8.3, 'α₁ receptor', green)]:
        box(x, 3.6, text, color)
        arrow((5, 4.26), (x, 4.0), color)
    box(3.4, 2.35, 'Adenylyl cyclase', width=3.4)
    arrow((1.7, 3.21), (2.4, 2.75))
    ax.text(1.32, 2.73, 'promotes', color=blue, fontsize=11)
    # T-ended inhibition line: alpha-2 opposes the cyclase branch.
    ax.plot([5, 4.42], [3.21, 2.76], color=orange, lw=1.8)
    ax.plot([4.27, 4.57], [2.93, 2.59], color=orange, lw=2.3)
    ax.text(5.04, 2.77, 'opposes', color=orange, fontsize=11)
    box(3.4, 1.35, 'cAMP → lipolysis tendency', width=3.4)
    arrow((3.4, 1.95), (3.4, 1.75))
    box(8.3, 2.15, 'Separate phospholipid\nlabeling readout', green,
        width=2.7, height=.9)
    arrow((8.3, 3.21), (8.3, 2.69), green)
    ax.text(8.3, 1.25, 'Different measured branch', ha='center', fontsize=11,
            color=green)
    ax.text(5, .39, 'Human fat-cell assay context • qualitative directions only\nReceptor balance and available cellular machinery determine the net response',
            ha='center', fontsize=11, color=ink)
    fig.subplots_adjust(left=.02, right=.98, bottom=.02, top=.98)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
