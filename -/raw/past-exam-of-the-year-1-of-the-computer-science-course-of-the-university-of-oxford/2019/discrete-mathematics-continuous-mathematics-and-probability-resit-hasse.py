"""Original Hasse diagram; Python 3.14.4, Matplotlib 3.10.7.

The PNG is written to the current working directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 13})
    fig, ax = plt.subplots(figsize=(6.4, 4.3), dpi=160, facecolor='white')
    ax.set_facecolor('white')
    positions = {2: (-1.2, 0), 3: (0, 0), 5: (1.2, 0),
                 1: (-0.75, 1.55), 4: (0.75, 1.55)}
    for lower in (2, 3, 5):
        for upper in (1, 4):
            x0, y0 = positions[lower]
            x1, y1 = positions[upper]
            ax.plot([x0, x1], [y0, y1], color='#526779', lw=1.8, zorder=1)
    for value, (x, y) in positions.items():
        ax.scatter([x], [y], s=580, facecolor='white', edgecolor='#172c3d', lw=1.8, zorder=3)
        ax.text(x, y, str(value), ha='center', va='center', color='#172c3d', zorder=4)
    ax.text(0, 1.96, 'Nonprimes: upper antichain', ha='center', color='#172c3d')
    ax.text(0, -0.43, 'Primes: lower antichain', ha='center', color='#172c3d')
    ax.set_title('Five-element order: six cover relations', pad=16)
    ax.set_xlim(-1.8, 1.8)
    ax.set_ylim(-0.65, 2.15)
    ax.set_aspect('equal')
    ax.axis('off')
    fig.tight_layout(pad=1.3)
    output = Path(Path(__file__).stem + '.png')
    temporary = output.with_suffix('.png.tmp')
    fig.savefig(temporary, format='png', dpi=160, facecolor='white', transparent=False,
                metadata={'Software': 'Matplotlib; original mathematical diagram'})
    temporary.replace(output)
    plt.close(fig)


if __name__ == '__main__':
    main()
