"""Draw exact identity-testing outcomes over F_5; emit PNG in the working directory."""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

BLUE = '#156c9c'
ORANGE = '#a65b0a'
LIGHT_BLUE = '#deeff9'
LIGHT_ORANGE = '#fff0d7'
INK = '#1b2633'


def main():
    values_f = [((a + 1)**2 - a*a - 2*a - 1) % 5 for a in range(5)]
    values_g = [((a - 1)*(a - 2)) % 5 for a in range(5)]
    assert values_f == [0]*5
    assert values_g == [2, 0, 0, 2, 1]
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12})
    fig = plt.figure(figsize=(9, 5.3), dpi=120, facecolor='white')
    ax = fig.add_axes((0, 0, 1, 1), facecolor='white')
    ax.set(xlim=(0, 9), ylim=(0, 5.3))
    ax.axis('off')
    ax.text(4.5, 4.93, 'One evaluation: zero is inconclusive; nonzero is a witness',
            ha='center', va='center', fontsize=16, weight='bold', color=INK)
    ax.text(4.5, 4.47, r'Exact arithmetic in $\mathbb{F}_5$ (modulo 5)',
            ha='center', color=INK, fontsize=13)
    for a in range(5):
        ax.text(2.67 + 1.13*a, 3.95, f'a = {a}', ha='center', color=INK)
    for row, values in enumerate([values_f, values_g]):
        bottom = 2.37 - 1.42*row
        ax.text(.38, bottom + .85, 'F(a)' if row == 0 else 'G(a)',
                fontsize=17, weight='bold', color=INK)
        ax.text(.38, bottom + .42, 'identity' if row == 0 else 'nonidentity',
                fontsize=12, color=INK)
        for a, value in enumerate(values):
            left = 2.16 + 1.13*a
            false = row == 1 and value == 0
            edge = ORANGE if false else BLUE
            fill = LIGHT_ORANGE if false else LIGHT_BLUE
            ax.add_patch(Rectangle((left, bottom), 1.02, 1.23,
                                   facecolor=fill, edgecolor=edge, linewidth=1.5))
            ax.text(left + .51, bottom + .91, str(value),
                    fontsize=22, weight='bold', ha='center', color=edge)
            text = 'false\naccept' if false else ('correct\naccept' if row == 0 else 'correct\nreject')
            ax.text(left + .51, bottom + .32, text, ha='center', va='center',
                    color=INK, fontsize=11, linespacing=1.2)
    ax.text(4.5, .47, r'$F(x)=(x+1)^2-x^2-2x-1$       $G(x)=(x-1)(x-2)$',
            ha='center', fontsize=14, color=INK)
    fig.savefig(Path(__file__).stem + '.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
