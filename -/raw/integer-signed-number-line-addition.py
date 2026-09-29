"""Draw signed integer addition; Python 3.14, matplotlib 3.10.7.

Run from _media to write integer-signed-number-line-addition.png.
"""
from pathlib import Path

import matplotlib.pyplot as plt

BLUE = '#2264a8'
ORANGE = '#b54b15'
INK = '#202b38'


def main():
    fig, ax = plt.subplots(figsize=(9.6, 4.4), dpi=120)
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    ax.set_xlim(-6.4, 6.4)
    ax.set_ylim(-1.05, 2.45)
    ax.axis('off')
    ax.axvspan(-6.25, -0.02, ymin=0.19, ymax=0.34, color='#f3f6fb')
    ax.axvspan(0.02, 6.25, ymin=0.19, ymax=0.34, color='#fff4eb')
    ax.annotate('', xy=(6.2, 0), xytext=(-6.2, 0),
                arrowprops=dict(arrowstyle='<->', lw=1.6, color=INK))
    for n in range(-6, 7):
        ax.plot([n, n], [-0.065, 0.065], color=INK, lw=1.2)
        ax.text(n, -0.22, str(n), ha='center', va='top', fontsize=12, color=INK)
    ax.text(-3.3, -0.73, 'negative integers', ha='center', fontsize=12, color=INK)
    ax.text(0, -0.73, 'zero', ha='center', fontsize=12, color=INK)
    ax.text(3.3, -0.73, 'positive integers', ha='center', fontsize=12, color=INK)
    for start, end, y, color, label in [
        (-3, 2, 1.5, BLUE, '1. Add +5: move five units right'),
        (2, -2, 0.7, ORANGE, '2. Add −4: move four units left'),
    ]:
        ax.plot([start, start], [0.12, y], ':', color=color, lw=1.3)
        ax.plot([end, end], [0.12, y], ':', color=color, lw=1.3)
        ax.annotate('', xy=(end, y), xytext=(start, y),
                    arrowprops=dict(arrowstyle='-|>', mutation_scale=18, lw=2.5, color=color))
        ax.text((start + end) / 2, y + 0.15, label, ha='center', fontsize=12, color=color)
    for n, color in [(-3, BLUE), (2, BLUE), (-2, ORANGE)]:
        ax.scatter(n, 0, s=65, color=color, zorder=4, edgecolors='white', linewidths=1)
    ax.text(0, 2.23, 'Signed integers: positions and changes', ha='center',
            fontsize=17, weight='bold', color=INK)
    ax.text(0, 1.95, '−3 + 5 = 2       then       2 + (−4) = −2',
            ha='center', fontsize=14, color=INK)
    fig.subplots_adjust(left=0.025, right=0.975, bottom=0.06, top=0.96)
    fig.savefig(Path(__file__).stem + '.png', facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
