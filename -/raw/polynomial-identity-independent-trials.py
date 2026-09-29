"""Enumerate all 25 ordered evaluation pairs; no random simulation."""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

BLUE = '#156c9c'
ORANGE = '#a65b0a'
LIGHT_BLUE = '#deeff9'
LIGHT_ORANGE = '#fff0d7'
INK = '#1b2633'


def main():
    outcomes = {(a, b): ((a-1)*(a-2)) % 5 == 0 and ((b-1)*(b-2)) % 5 == 0
                for a in range(5) for b in range(5)}
    assert {p for p, false in outcomes.items() if false} == {(1, 1), (1, 2), (2, 1), (2, 2)}
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12})
    fig = plt.figure(figsize=(8.2, 6), dpi=120, facecolor='white')
    ax = fig.add_axes((0, 0, 1, 1), facecolor='white')
    ax.set(xlim=(0, 8.2), ylim=(0, 6))
    ax.axis('off')
    ax.text(4.1, 5.66, 'Two independent trials: four false accepts out of 25',
            ha='center', fontsize=16, weight='bold', color=INK)
    ax.text(4.1, 5.27, r'$G(x)=(x-1)(x-2)$ in $\mathbb{F}_5$; accept only when both values are zero',
            ha='center', fontsize=12, color=INK)
    x0, y0, cell = 1.08, .95, .72
    for (a, b), false in outcomes.items():
        left, bottom = x0 + cell*a, y0 + cell*b
        ax.add_patch(Rectangle((left, bottom), cell, cell,
                               facecolor=LIGHT_ORANGE if false else LIGHT_BLUE,
                               edgecolor='white', linewidth=2))
        ax.text(left + cell/2, bottom + cell/2, f'{a},{b}',
                ha='center', va='center', color=ORANGE if false else BLUE,
                fontsize=12, weight='bold' if false else 'normal')
    for a in range(5):
        ax.text(x0 + (a+.5)*cell, y0-.25, str(a), ha='center', color=INK)
        ax.text(x0-.25, y0 + (a+.5)*cell, str(a), ha='center', va='center', color=INK)
    ax.text(x0+2.5*cell, .27, 'First choice a', ha='center', color=INK)
    ax.text(.30, y0+2.5*cell, 'Second choice b', rotation=90, ha='center', va='center', color=INK)
    ax.add_patch(Rectangle((5.02, 4.07), .28, .28, facecolor=LIGHT_ORANGE,
                           edgecolor=ORANGE))
    ax.text(5.45, 4.20, 'False acceptance', va='center', weight='bold', color=ORANGE)
    ax.text(5.02, 3.76, 'Both a and b are roots.\nFour cells, each of probability 1/25.',
            va='top', fontsize=11, linespacing=1.4, color=INK)
    ax.add_patch(Rectangle((5.02, 2.73), .28, .28, facecolor=LIGHT_BLUE,
                           edgecolor=BLUE))
    ax.text(5.45, 2.86, 'Correct rejection', va='center', weight='bold', color=BLUE)
    ax.text(5.02, 2.42, 'At least one nonzero witness.\nThe other 21 ordered pairs.',
            va='top', fontsize=11, linespacing=1.4, color=INK)
    ax.text(5.02, 1.38, r'$\mathbb{P}(\mathrm{false\ accept})$', fontsize=14, color=INK)
    ax.text(5.02, .98, r'$=\left(\frac{2}{5}\right)^2=\frac{4}{25}$', fontsize=19, color=ORANGE)
    fig.savefig(Path(__file__).stem + '.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
