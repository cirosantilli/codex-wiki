"""Draw an original RC filter schematic; emit PNG into the current directory.

Tested with Python 3.14, matplotlib 3.10.7 and NumPy 2.3.5.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

BLUE = '#146eaa'
ORANGE = '#b56c0b'
INK = '#253341'


def main():
    plt.rcParams.update({'font.size': 13, 'font.family': 'DejaVu Sans'})
    fig, ax = plt.subplots(figsize=(9.6, 4.5), dpi=110, facecolor='white')
    ax.set(xlim=(0, 8), ylim=(0, 3.9), aspect='equal')
    ax.axis('off')

    def wire(xs, ys, color=INK, style='-'):
        ax.plot(xs, ys, color=color, lw=2.2, linestyle=style, solid_capstyle='round')

    top, bottom = 2.8, 0.75
    wire([0.95, 0.95], [top, 2.23])
    wire([0.95, 0.95], [1.33, bottom])
    ax.add_patch(Circle((0.95, 1.78), 0.45, fill=False, lw=2.2, edgecolor=INK))
    ax.text(0.95, 1.99, '+', ha='center', va='center')
    ax.text(0.95, 1.57, '−', ha='center', va='center')
    ax.text(0.18, 1.78, r'$v_{\rm in}$', ha='center', va='center', color=INK)
    wire([0.95, 2.05], [top, top])
    ax.add_patch(Rectangle((2.05, top - .16), 1.0, .32, fill=False, lw=2.2, edgecolor=INK))
    ax.text(2.55, 3.22, r'$R=2.2\ {\rm k}\Omega$', ha='center')
    wire([3.05, 7.35], [top, top])
    wire([0.95, 7.35], [bottom, bottom])
    ax.annotate('', xy=(3.4, 2.43), xytext=(1.7, 2.43),
                arrowprops={'arrowstyle': '->', 'color': BLUE, 'lw': 2})
    ax.text(2.55, 2.08, r'$i=(v_{\rm in}-v_{\rm out})/R$', ha='center', color=BLUE, fontsize=12)

    wire([4.3, 4.3], [top, 1.98])
    wire([3.98, 4.62], [1.98, 1.98], BLUE)
    wire([3.98, 4.62], [1.77, 1.77], BLUE)
    wire([4.3, 4.3], [1.77, bottom])
    ax.text(4.77, 1.95, r'$C$', color=BLUE, ha='left')
    ax.text(4.77, 1.61, '47 nF', color=BLUE, ha='left', fontsize=12)

    wire([6.15, 6.15], [top, 2.12], ORANGE, '--')
    ax.add_patch(Rectangle((5.99, 1.4), .32, .72, fill=False, lw=2.0,
                           edgecolor=ORANGE, linestyle='--'))
    wire([6.15, 6.15], [1.4, bottom], ORANGE, '--')
    ax.text(6.55, 1.83, r'$R_L$', color=ORANGE, ha='left')
    ax.text(6.15, .26, 'Optional load', color=ORANGE, ha='center', fontsize=12)
    for x in (4.3, 6.15):
        ax.plot([x, x], [top, bottom], 'o', color=INK, ms=5)
    for y in (top, bottom):
        ax.plot(7.35, y, 'o', ms=7, mfc='white', mec=INK, mew=2)
    ax.annotate('', xy=(7.35, 2.6), xytext=(7.35, .96),
                arrowprops={'arrowstyle': '->', 'color': BLUE, 'lw': 1.8})
    ax.text(7.62, 1.78, r'$v_{\rm out}$', color=BLUE, ha='center', rotation=90)
    ax.text(2.35, .28, 'Common zero-voltage return', ha='center', color=INK, fontsize=12)
    ax.set_title('RC low-pass filter: read the voltage across C', fontsize=17, pad=10)
    fig.subplots_adjust(left=.035, right=.985, top=.86, bottom=.055)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
