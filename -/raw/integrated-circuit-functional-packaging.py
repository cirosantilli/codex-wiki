"""Compare functional integration and package boundaries.

Tested with Python 3.14, matplotlib 3.10.7. Run from _media; output uses
this script's basename. This is a conceptual block diagram, not a chip layout.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle


BLUE = '#235789'
ORANGE = '#bd631c'
INK = '#24313f'


def box(ax, x, y, w, h, text, edge, fill='white', fontsize=12):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                              boxstyle='round,pad=0.015,rounding_size=0.12',
                              linewidth=1.7, edgecolor=edge, facecolor=fill))
    if text:
        ax.text(x + w / 2, y + h / 2, text, ha='center', va='center',
                fontsize=fontsize, color=INK)


def arrow(ax, x1, x2, y, color):
    ax.annotate('', (x2, y), (x1, y),
                arrowprops={'arrowstyle': '-|>', 'lw': 2, 'color': color,
                            'shrinkA': 0, 'shrinkB': 0})


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11})
    fig, ax = plt.subplots(figsize=(10, 6.4), dpi=120)
    fig.patch.set_facecolor('white')
    ax.set(xlim=(0, 12), ylim=(0, 8))
    ax.axis('off')
    ax.text(6, 7.65, 'Same functions, different construction', ha='center',
            va='center', fontsize=18, weight='bold', color=INK)
    ax.text(0.55, 6.9, 'SEPARATE PACKAGES', fontsize=12, weight='bold', color=ORANGE)
    labels = ['Amplifier', 'Filter', 'Output\ndriver']
    xs = [1.65, 5.05, 8.45]
    for x, label in zip(xs, labels):
        box(ax, x - .22, 4.95, 2.35, 1.4, '', ORANGE, '#fff7ed')
        box(ax, x, 5.2, 1.9, .85, label, ORANGE, fontsize=11)
        ax.text(x + .95, 4.70, 'package', ha='center', color=ORANGE, fontsize=10)
    for x1, x2 in [(0.45, 1.65), (3.55, 5.05), (6.95, 8.45), (10.35, 11.55)]:
        arrow(ax, x1, x2, 5.62, ORANGE)
    ax.text(.48, 6.12, 'input', fontsize=10, color=INK)
    ax.text(10.95, 6.12, 'output', fontsize=10, color=INK)
    ax.text(6, 4.15, 'Connections between packages require assembly',
            ha='center', fontsize=12, color=INK)

    ax.text(.55, 3.55, 'ONE MONOLITHIC INTEGRATED CIRCUIT',
            fontsize=12, weight='bold', color=BLUE)
    box(ax, 1.2, .95, 9.6, 2.1, '', BLUE, '#f1f7fc')
    ax.add_patch(Rectangle((1.48, 1.25), 9.04, 1.5, lw=1.2,
                           edgecolor=BLUE, facecolor='white', linestyle='--'))
    for x, label in zip(xs, labels):
        box(ax, x, 1.64, 1.9, .8, label, BLUE, '#e3eff9', fontsize=11)
    for x1, x2 in [(0.45, 1.65), (3.55, 5.05), (6.95, 8.45), (10.35, 11.55)]:
        arrow(ax, x1, x2, 2.04, BLUE)
    ax.text(6, 1.38, 'one semiconductor die · internal interconnects',
            ha='center', fontsize=10, color=BLUE)
    ax.text(6, .65, 'one package', ha='center', color=BLUE, fontsize=10)
    ax.text(6, .15, 'Functional blocks only; supply and return omitted; not to scale.',
            ha='center', fontsize=10, color=INK)
    fig.subplots_adjust(left=.015, right=.985, bottom=.02, top=.99)
    fig.savefig(Path(__file__).stem + '.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
