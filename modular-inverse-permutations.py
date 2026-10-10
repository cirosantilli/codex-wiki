"""Plot exact reversible and many-to-one modular multiplication maps."""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def main():
    x17 = np.arange(17)
    y17 = 5 * x17 % 17
    x15 = np.arange(15)
    y15 = 5 * x15 % 15
    assert set(y17.tolist()) == set(x17.tolist())
    assert set(y15.tolist()) == {0, 5, 10}
    assert np.array_equal(7 * y17 % 17, x17)
    assert set(x15[y15 == 10].tolist()) == {2, 5, 8, 11, 14}
    plt.rcParams.update({'font.size': 12})
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.6), layout='constrained', facecolor='white')
    for ax, n, xs, ys, color in [(axes[0], 17, x17, y17, '#2563a6'),
                               (axes[1], 15, x15, y15, '#b76816')]:
        ax.scatter(xs, ys, s=65, color=color, zorder=3)
        ax.set(xlabel='Input residue x', ylabel=f'Output residue 5x mod {n}',
               xlim=(-.6, n - .4), ylim=(-.7, n - .3),
               xticks=np.arange(0, n, 2), yticks=np.arange(0, n, 2))
        ax.grid(alpha=.2)
    axes[0].set_title('Modulo 17: every output appears once\nInverse multiplication is by 7')
    axes[0].scatter([7], [1], s=210, facecolor='none', edgecolor='#146747', linewidth=2, zorder=4)
    axes[0].annotate('5 × 7 = 1 mod 17', (7, 1), xytext=(6, 5), fontsize=10,
                     arrowprops={'arrowstyle': '->', 'color': '#146747'})
    axes[1].set_title('Modulo 15: only three outputs\nFive different inputs per output')
    axes[1].set_yticks([0, 5, 10, 14])
    fig.suptitle('A modular inverse exists exactly when multiplier and modulus are coprime', fontsize=14)
    fig.savefig(Path.cwd() / 'modular-inverse-permutations.png', dpi=120, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
