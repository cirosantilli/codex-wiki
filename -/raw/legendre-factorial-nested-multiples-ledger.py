"""Original contribution ledger; Python 3.14.4 / Matplotlib 3.10.7.

Run from _media; writes the matching basename.png to the working directory.
"""
from math import factorial
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def valuation(value, prime):
    count = 0
    while value % prime == 0:
        count += 1
        value //= prime
    return count


def checked_counts():
    multiples = list(range(3, 51, 3))
    rows = [[m % power == 0 for m in multiples] for power in (3, 9, 27)]
    counts = [sum(row) for row in rows]
    assert counts == [16, 5, 1]
    columns = [sum(row[i] for row in rows) for i in range(len(multiples))]
    assert columns == [valuation(m, 3) for m in multiples]
    assert [columns.count(i) for i in (1, 2, 3)] == [11, 4, 1]
    exact = factorial(50)
    assert exact % (3**22) == 0 and exact % (3**23) != 0
    for prime in (2, 3, 5, 7, 11):
        for n in range(101):
            quotient, total = n, 0
            while quotient:
                quotient //= prime
                total += quotient
            assert total == valuation(factorial(n), prime)
    return multiples, rows, counts, columns


def main():
    multiples, rows, counts, columns = checked_counts()
    colors = ['#246a9c', '#169286', '#b86428']
    plt.rcParams.update({'font.size': 12, 'figure.facecolor': 'white',
                         'savefig.facecolor': 'white'})
    fig, ax = plt.subplots(figsize=(10.8, 4.8))
    fig.subplots_adjust(left=0.025, right=0.99, top=0.81, bottom=0.13)
    fig.suptitle('Count every factor of three in 50!', fontsize=19, y=0.96)
    fig.text(0.5, 0.86, 'Each filled cell contributes one; nested multiples contribute again.',
             ha='center', fontsize=12)
    ax.set(xlim=(-4.5, 19.1), ylim=(-1.25, 4.0))
    ax.axis('off')
    for i, number in enumerate(multiples):
        ax.text(i, 3.65, str(number), ha='center', va='center')
    ax.text(-1.0, 3.65, 'factor m', ha='right', fontsize=11)
    ax.text(17.3, 3.65, 'row count', ha='center', fontsize=11)
    labels = [r'$3\mid m$', r'$9\mid m$', r'$27\mid m$']
    for row_index, (row, color, label, count) in enumerate(zip(rows, colors, labels, counts)):
        y = 2.75 - row_index
        ax.text(-1.0, y, label, ha='right', va='center', fontsize=15)
        for i, filled in enumerate(row):
            ax.add_patch(Rectangle((i - 0.35, y - 0.32), 0.7, 0.64,
                                  facecolor=color if filled else '#f1f3f4',
                                  edgecolor='white', linewidth=1))
            if filled:
                ax.text(i, y, '1', color='white', ha='center', va='center')
        ax.text(17.3, y, str(count), color=color, fontsize=18, ha='center', va='center')
    ax.plot([-3.6, 18.1], [0.12, 0.12], color='#a5afb5', lw=1)
    ax.text(-1.0, -0.43, r'$v_3(m)$', ha='right', va='center', fontsize=15)
    for i, count in enumerate(columns):
        ax.text(i, -0.43, str(count), ha='center', va='center',
                fontweight='bold' if count > 1 else 'normal', fontsize=14)
    ax.text(17.3, -0.43, '22', fontsize=20, ha='center', va='center', fontweight='bold')
    fig.text(0.5, 0.06, r'By rows: $16+5+1=22$     |     By columns: $11\cdot1+4\cdot2+1\cdot3=22$',
             ha='center', fontsize=14)
    fig.savefig(Path(__file__).with_suffix('.png').name, dpi=100, transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
