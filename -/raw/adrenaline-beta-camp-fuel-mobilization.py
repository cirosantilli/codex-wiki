"""Original qualitative diagram; Python 3.14, matplotlib 3.10.7.

Run from the desired output directory. No measurements or molecular structures.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def main():
    fig, ax = plt.subplots(figsize=(10, 6.7), dpi=120)
    fig.patch.set_facecolor('white')
    ax.set(xlim=(0, 10), ylim=(0, 6.7))
    ax.axis('off')
    blue, orange, ink = '#236b8e', '#b45c21', '#18313d'

    def box(x, y, text, width=2.35, height=.57, color=blue):
        ax.add_patch(FancyBboxPatch((x-width/2, y-height/2), width, height,
                                   boxstyle='round,pad=0.07', facecolor='#f4f8fa',
                                   edgecolor=color, linewidth=1.5))
        ax.text(x, y, text, ha='center', va='center', fontsize=12, color=ink)

    def arrow(start, end, dashed=False):
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle='-|>',
                                    mutation_scale=16, linewidth=1.7,
                                    linestyle='--' if dashed else '-',
                                    color=orange if dashed else blue))

    ax.text(5, 6.38, 'Adrenaline: reception and fuel mobilization',
            ha='center', fontsize=18, weight='bold', color=ink)
    box(3.2, 5.75, 'Adrenaline outside cell')
    box(3.2, 4.85, 'β-adrenergic receptor')
    ax.plot([.7, 8.9], [4.85, 4.85], color='#b7cbd3', lw=6, zorder=0)
    ax.text(8.9, 5.10, 'Cell membrane', ha='right', color=ink, fontsize=11)
    box(3.2, 3.95, 'Stimulatory G protein')
    box(3.2, 3.05, 'Adenylyl cyclase → cAMP', width=3.0)
    box(3.2, 2.15, 'Protein kinase A')
    box(3.2, 1.25, 'Phosphorylase kinase')
    for y in [5.75, 4.85, 3.95, 3.05, 2.15]:
        arrow((3.2, y-.36), (3.2, y-.54))
    box(7.2, 1.25, 'Glycogen phosphorylase', width=2.9)
    arrow((4.47, 1.25), (5.65, 1.25))
    box(7.2, .42, 'Glycogenolysis', color=orange)
    arrow((7.2, .91), (7.2, .76))
    box(7.2, 2.9, 'Lipolysis in responsive\nadipocytes', width=2.9, height=.85,
        color=orange)
    arrow((4.80, 3.05), (5.65, 2.90), dashed=True)
    ax.text(7.2, 3.56, 'Separate downstream branch', ha='center', fontsize=11,
            color=orange)
    ax.text(.65, .43, 'Arrows: selected causal influences\nDashed: intermediate steps omitted\nQualitative schematic; no measured rates',
            fontsize=10, va='center', color=ink)
    fig.subplots_adjust(left=.02, right=.98, bottom=.02, top=.98)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
