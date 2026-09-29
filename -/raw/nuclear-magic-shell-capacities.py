"""Draw state capacities for a chosen spherical nuclear level scheme.

Python 3.14, matplotlib 3.10.7. Run from _media with MPLBACKEND=Agg.
Orbital grouping is illustrative, not a computed energy spectrum or a universal
ordering. Integers preceding orbital letters count radial levels from one.
"""
from pathlib import Path
import matplotlib.pyplot as plt

# (radial index, orbital letter, twice j); all states count ONE species.
GROUPS = [
    [(1, 's', 1)],
    [(1, 'p', 3), (1, 'p', 1)],
    [(1, 'd', 5), (2, 's', 1), (1, 'd', 3)],
    [(1, 'f', 7)],
    [(2, 'p', 3), (1, 'f', 5), (2, 'p', 1), (1, 'g', 9)],
    [(1, 'g', 7), (2, 'd', 5), (2, 'd', 3), (3, 's', 1), (1, 'h', 11)],
    [(1, 'h', 9), (2, 'f', 7), (2, 'f', 5), (3, 'p', 3), (3, 'p', 1), (1, 'i', 13)],
]


def main():
    plt.rcParams.update({'font.size': 12, 'font.family': 'DejaVu Sans'})
    fig, ax = plt.subplots(figsize=(11.6, 6.9), dpi=100, facecolor='white')
    fig.subplots_adjust(left=0.025, right=0.985, top=0.84, bottom=0.14)
    ax.set(xlim=(0, 12), ylim=(-0.65, 6.7))
    ax.axis('off')
    ax.text(0.1, 6.55, 'Levels in the group  (capacity below each level)', weight='bold')
    ax.text(8.95, 6.55, 'Added', ha='center', weight='bold')
    ax.text(10.7, 6.55, 'Filled total', ha='center', weight='bold')
    total = 0
    for row, group in enumerate(GROUPS):
        y = 5.9 - row
        color = '#156c9a' if row % 2 == 0 else '#276e51'
        ax.axhspan(y - 0.43, y + 0.43, color='#f2f5f8', zorder=0)
        for k, (n, letter, twice_j) in enumerate(group):
            x = 0.73 + 1.34 * k
            ax.text(x, y + 0.10, rf'${n}{letter}_{{{twice_j}/2}}$', ha='center', fontsize=15, color=color)
            ax.text(x, y - 0.24, str(twice_j + 1), ha='center', fontsize=12)
            if k + 1 < len(group):
                ax.text(x + 0.67, y - 0.24, '+', ha='center', color='#737d88')
        added = sum(twice_j + 1 for _, _, twice_j in group)
        total += added
        ax.text(8.95, y - 0.02, f'+{added}', ha='center', fontsize=15)
        ax.annotate('', xy=(10.05, y - 0.02), xytext=(9.45, y - 0.02),
                    arrowprops={'arrowstyle': '->', 'color': '#737d88'})
        ax.text(10.7, y - 0.02, str(total), ha='center', va='center', color=color,
                fontsize=20, weight='bold', bbox={'boxstyle': 'round,pad=0.2', 'fc': 'white', 'ec': color})
    fig.suptitle('From orbital capacities to traditional magic numbers', y=0.97, fontsize=18)
    fig.text(0.5, 0.895, r'One species: each $nlj$ level holds $2j+1$ neutrons OR $2j+1$ protons', ha='center', fontsize=14)
    fig.text(0.5, 0.065, 'Chosen grouping; rows are not an energy axis. Level ordering and physical gaps depend on the nucleus.', ha='center', fontsize=11)
    fig.text(0.5, 0.025, 'Capacities follow from state counting; strong spin–orbit coupling helps explain why the groups change.', ha='center', fontsize=11, color='#505967')
    fig.savefig(Path(__file__).stem + '.png', facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
