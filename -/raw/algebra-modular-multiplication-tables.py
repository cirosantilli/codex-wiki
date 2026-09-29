"""Show exact finite multiplication tables and nontrivial zero products."""

from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import Rectangle
import numpy as np


def main():
    tables = {n: np.arange(n)[:, None] * np.arange(n)[None, :] % n for n in (5, 6)}
    assert all(set(tables[5][a].tolist()) == set(range(5)) for a in range(1, 5))
    assert tables[6][2, 3] == tables[6][3, 2] == 0
    assert set(tables[6][2].tolist()) == {0, 2, 4}
    assert [a for a in range(8) if a * a % 8 == 1] == [1, 3, 5, 7]
    plt.rcParams.update({'font.size': 12})
    colors = ['#eff2f5', '#dde8f2', '#9ac5e5', '#f3c277', '#bfafd4', '#a7c49b']
    fig, axes = plt.subplots(1, 2, figsize=(11, 6.2), layout='constrained', facecolor='white')
    for ax, n in zip(axes, (5, 6)):
        ax.imshow(tables[n], cmap=ListedColormap(colors), vmin=-.5, vmax=5.5)
        for a in range(n):
            for b in range(n):
                ax.text(b, a, str(tables[n][a, b]), ha='center', va='center', fontsize=15)
                if a and b and tables[n][a, b] == 0:
                    ax.add_patch(Rectangle((b - .47, a - .47), .94, .94, fill=False,
                                           edgecolor='#9b1c1c', linewidth=2))
        ax.set(xticks=range(n), yticks=range(n), xlabel='Second factor b', ylabel='First factor a')
        ax.set_xticks(np.arange(-.5, n), minor=True)
        ax.set_yticks(np.arange(-.5, n), minor=True)
        ax.grid(which='minor', color='white', linewidth=2)
        ax.tick_params(which='minor', length=0)
    axes[0].set_title('Modulo 5: a field\nEach nonzero row permutes residues', fontsize=12, pad=12)
    axes[1].set_title('Modulo 6: a ring with zero divisors\nRed boxes: nonzero factors multiply to zero', fontsize=12, pad=12)
    fig.suptitle('The allowed arithmetic determines which algebraic arguments work', fontsize=14)
    fig.savefig(Path.cwd() / 'algebra-modular-multiplication-tables.png', dpi=120, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
