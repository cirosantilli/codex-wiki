"""Compare decimal and binary place values; Python 3.14, matplotlib 3.10.7.

Run from _media to write decimal-binary-place-value.png.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

INK = '#202b38'
BLUE = '#2264a8'
ORANGE = '#b54b15'


def draw_table(ax, digits, base, bottom, left, width, color):
    weights = [base ** j for j in range(len(digits) - 1, -1, -1)]
    row_height = 0.48
    labels = ['digit', 'weight', 'contribution']
    for row, values in enumerate([digits, weights, [d*w for d, w in zip(digits, weights)]]):
        y = bottom + (2 - row) * row_height
        ax.text(left - 0.14, y + row_height / 2, labels[row], ha='right',
                va='center', fontsize=11, color=INK)
        for j, (value, digit) in enumerate(zip(values, digits)):
            x = left + j * width
            ax.add_patch(Rectangle((x, y), width, row_height,
                                  facecolor='#eef5fc' if digit else '#f5f5f5',
                                  edgecolor='white', linewidth=2))
            ax.text(x + width / 2, y + row_height / 2, str(value), ha='center',
                    va='center', fontsize=16 if row == 0 else 12,
                    color=color if digit else '#647080', weight='bold' if row == 0 else 'normal')
    return sum(d*w for d, w in zip(digits, weights))


def main():
    fig, ax = plt.subplots(figsize=(9.6, 5.8), dpi=120)
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6.4)
    ax.axis('off')
    ax.text(5, 6.1, r'One integer, two encodings: $205_{10} = 11001101_2$',
            ha='center', fontsize=18, weight='bold', color=INK)
    ax.text(1.8, 5.45, 'DECIMAL · base 10', fontsize=13, color=BLUE, weight='bold')
    dec = draw_table(ax, [2, 0, 5], 10, 3.75, 1.8, 1.05, BLUE)
    ax.text(5.3, 4.5, '200 + 0 + 5 = 205', va='center', fontsize=15, color=BLUE)
    ax.text(1.8, 3.15, 'BINARY · base 2', fontsize=13, color=ORANGE, weight='bold')
    binary = draw_table(ax, [1, 1, 0, 0, 1, 1, 0, 1], 2, 1.5, 1.8, 0.94, ORANGE)
    ax.text(5.5, 1.1, '128 + 64 + 8 + 4 + 1 = 205', ha='center', fontsize=15, color=ORANGE)
    ax.text(5, 0.45, 'Zero digits keep positions.  Each contribution = digit × weight.',
            ha='center', fontsize=12, color=INK)
    assert dec == binary == 205
    fig.subplots_adjust(left=0.025, right=0.985, top=0.985, bottom=0.035)
    fig.savefig(Path(__file__).stem + '.png', facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
