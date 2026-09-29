"""Original PCR strand schematic. Tested with Python 3.14 / matplotlib 3.10.7.
Run from _media; saves a matching opaque white PNG in the current directory.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

OLD = '#55565b'
NEW = '#22835c'
FWD = '#1769aa'
REV = '#b33c76'


def strand(ax, left, right, y, direction, color, labels=True, lw=2.7):
    start, end = (left, right) if direction == 1 else (right, left)
    ax.add_patch(FancyArrowPatch((start, y), (end, y), arrowstyle='-|>',
                                mutation_scale=12, lw=lw, color=color))
    if labels:
        ax.text(left - .13, y, "5′" if direction == 1 else "3′",
                ha='right', va='center', fontsize=11, color=color)
        ax.text(right + .13, y, "3′" if direction == 1 else "5′",
                ha='left', va='center', fontsize=11, color=color)


def setup(ax, title):
    ax.set_xlim(-.9, 11)
    ax.set_ylim(-.1, 3.6)
    ax.axis('off')
    ax.set_title(title, fontsize=13, loc='left', fontweight='bold', pad=8)
    for x in (2, 8):
        ax.plot([x, x], [.45, 3], '--', color='#d0d3d5', lw=1, zorder=0)


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11})
    fig, axes = plt.subplots(2, 3, figsize=(11, 7.9), dpi=120, facecolor='white')
    fig.subplots_adjust(left=.065, right=.96, top=.87, bottom=.12, wspace=.36, hspace=.62)
    fig.suptitle('Opposed primers select a bounded DNA interval', fontsize=17, y=.97)
    fig.text(.5, .917, 'Arrows mark 5′ → 3′ strand direction; dashed lines mark the eventual outer boundaries.', ha='center', fontsize=11)
    for ax, title in zip(axes[0], ['1  Separate strands', '2  Bind opposed primers', '3  Extend paired 3′ ends']):
        setup(ax, title)
        strand(ax, 0, 10, 2.6, 1, OLD)
        strand(ax, 0, 10, .85, -1, OLD)
    axes[0, 0].text(5, 1.7, 'Heat separates pairing\nBackbones remain intact', ha='center', va='center', fontsize=10)
    strand(axes[0, 1], 7, 8, 2.22, -1, REV)
    strand(axes[0, 1], 2, 3, 1.23, 1, FWD)
    # Once extended, a primer's former 3′ end is an internal position.
    strand(axes[0, 2], 7, 8, 2.22, -1, REV, labels=False)
    strand(axes[0, 2], 2, 3, 1.23, 1, FWD, labels=False)
    for x, y, label, color in [(8.15, 2.22, "5′", REV), (-.45, 2.22, "3′", NEW),
                                (1.55, 1.23, "5′", FWD), (10.45, 1.23, "3′", NEW)]:
        axes[0, 2].text(x, y, label, color=color, ha='center', va='center')
    axes[0, 1].text(5, 1.72, 'Extendible 3′ ends\nface into the interval', ha='center', va='center', fontsize=10)
    strand(axes[0, 2], 0, 7, 2.22, -1, NEW, labels=False)
    strand(axes[0, 2], 3, 10, 1.23, 1, NEW, labels=False)
    axes[0, 2].text(5, .23, 'First copies can extend beyond\nthe opposite primer site.', ha='center', fontsize=10)
    titles = ['Cycle 1: one bounded end', 'Cycle 2: first bounded strand', 'Cycle 3: bounded duplex']
    for ax, title in zip(axes[1], titles):
        setup(ax, title)
    strand(axes[1, 0], 0, 10, 2.6, 1, OLD)
    strand(axes[1, 0], 0, 7, 2.12, -1, NEW, labels=False)
    strand(axes[1, 0], 7, 8, 2.12, -1, REV, labels=False)
    axes[1, 0].text(-.45, 2.12, '3′', color=NEW, ha='center', va='center')
    axes[1, 0].text(8.45, 2.12, '5′', color=REV, ha='center', va='center')
    axes[1, 0].text(5, .7, 'Selected reverse-primer copy\nretains a long left flank.', ha='center', fontsize=10)
    strand(axes[1, 1], 0, 8, 2.12, -1, OLD)
    strand(axes[1, 1], 2, 3, 2.6, 1, FWD, labels=False)
    axes[1, 1].text(1.55, 2.6, '5′', color=FWD, ha='center', va='center')
    axes[1, 1].text(8.45, 2.6, '3′', color=NEW, ha='center', va='center')
    strand(axes[1, 1], 3, 8, 2.6, 1, NEW, labels=False)
    axes[1, 1].text(5, .7, 'Forward-primer copy stops\nat this template’s right end.', ha='center', fontsize=10)
    strand(axes[1, 2], 2, 8, 2.6, 1, OLD)
    strand(axes[1, 2], 2, 7, 2.12, -1, NEW, labels=False)
    strand(axes[1, 2], 7, 8, 2.12, -1, REV, labels=False)
    axes[1, 2].text(1.55, 2.12, '3′', color=NEW, ha='center', va='center')
    axes[1, 2].text(8.45, 2.12, '5′', color=REV, ha='center', va='center')
    axes[1, 2].text(5, .7, 'Both strands span only\nthe primer-defined interval.', ha='center', fontsize=10)
    fig.text(.5, .065, 'Gray: template in the displayed step   Green: new extension   Blue: forward primer   Pink: reverse primer', ha='center', fontsize=10)
    fig.text(.5, .025, 'Bottom row follows one lineage only; it omits other products. Original schematic, not an observed experiment.', ha='center', fontsize=10)
    fig.savefig(Path(__file__).stem + '.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
