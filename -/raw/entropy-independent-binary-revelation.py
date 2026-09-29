"""Plot an independent reveal-or-hide model in the current directory.

Tested with Python 3.14, Matplotlib 3.10.7 and NumPy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    p = 0.25
    h = -p * np.log2(p) - (1 - p) * np.log2(1 - p)
    assert np.isclose(h, 2 - 0.75 * np.log2(3))
    r = np.linspace(0, 1, 201)
    remaining = (1 - r) * h
    revealed = r * h
    assert np.allclose(remaining + revealed, h)

    plt.rcParams.update({'font.size': 12, 'axes.spines.top': False,
                         'axes.spines.right': False})
    fig = plt.figure(figsize=(10, 7), layout='constrained', facecolor='white')
    grid = fig.add_gridspec(2, 1, height_ratios=[1, 1.5])
    diagram = fig.add_subplot(grid[0])
    diagram.set(xlim=(0, 1), ylim=(0, 1))
    diagram.axis('off')
    box = {'boxstyle': 'round,pad=0.55', 'facecolor': '#f4f7fa',
           'edgecolor': '#526e8c'}
    diagram.text(0.17, 0.5, 'Binary state X\nP(X = 1) = 1/4\nH(X) = 0.811278 bits',
                 ha='center', va='center', bbox=box)
    diagram.text(0.76, 0.77, 'Reveal with probability r\nY = X: state known\nRemaining entropy = 0',
                 ha='center', va='center', bbox={**box, 'edgecolor': '#db802e'})
    diagram.text(0.76, 0.22, 'Hide with probability 1 − r\nY = ⊥: prior unchanged\nRemaining entropy = H(X)',
                 ha='center', va='center', bbox={**box, 'edgecolor': '#2862a5'})
    for endpoint in [(0.54, 0.77), (0.54, 0.22)]:
        diagram.annotate('', xy=endpoint, xytext=(0.34, 0.5),
                         arrowprops={'arrowstyle': '->', 'lw': 1.8, 'color': '#526e8c'})
    diagram.text(0.46, 0.95, 'Reveal decision independent of X',
                 ha='center', va='center', fontsize=11)

    ax = fig.add_subplot(grid[1])
    ax.plot(r, remaining, color='#2862a5', lw=2.5,
            label=r'Remaining: $H(X\mid Y)=(1-r)H(X)$')
    ax.plot(r, revealed, color='#db802e', lw=2.5,
            label=r'Revealed: $I(X;Y)=rH(X)$')
    ax.axhline(h, color='#526e8c', ls='--', lw=1.7,
               label=r'Original: $H(X)=h_2(1/4)$')
    ax.scatter([0.5], [h / 2], color='#26866f', s=55, zorder=5)
    ax.annotate('r = 1/2: each is 0.405639 bits', xy=(0.5, h / 2),
                xytext=(0.34, 0.14),
                arrowprops={'arrowstyle': '->', 'color': '#26866f'},
                bbox={'facecolor': 'white', 'edgecolor': '#d2d9df', 'pad': 5})
    ax.set(xlim=(0, 1), ylim=(0, 0.9), xlabel='Reveal probability r',
           ylabel='Bits per original state')
    ax.set_xticks(np.linspace(0, 1, 5))
    ax.grid(alpha=0.18)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), fontsize=11,
              frameon=False)
    fig.suptitle('Independent revelation splits the original uncertainty', fontsize=15)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=120,
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
