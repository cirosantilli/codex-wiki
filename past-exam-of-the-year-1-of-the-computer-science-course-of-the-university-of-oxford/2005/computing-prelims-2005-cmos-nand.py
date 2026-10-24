"""Draw Q9(a)'s CMOS NAND. Run from the desired output directory.

Tested with Python 3.14.4 and the repository's matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12})
    fig, ax = plt.subplots(figsize=(9, 7), dpi=120, facecolor='white')
    ax.set(xlim=(0, 7.6), ylim=(-0.6, 7.0), aspect='equal')
    ax.axis('off')

    def wire(xs, ys):
        ax.plot(xs, ys, color='#243746', lw=1.8)

    def device(x, y, label, pmos=False):
        # Channel, gate, and source/drain terminals; PMOS has a gate bubble.
        wire([x, x], [y-.25, y+.25])
        wire([x-.20, x-.20], [y-.30, y+.30])
        if pmos:
            ax.add_patch(Circle((x-.31, y), .075, fc='white', ec='#243746', lw=1.6))
            wire([x-.85, x-.385], [y, y])
        else:
            wire([x-.85, x-.20], [y, y])
        ax.text(x-.93, y, label, ha='right', va='center')
        ax.text(x+.16, y, ('P' if pmos else 'N')+'_'+label, va='center', fontsize=11)

    p_x = [1.8, 3.6, 5.4]
    wire([1.8, 5.4], [6.0, 6.0])
    ax.text(3.6, 6.2, r'$V_{DD}$', ha='center', fontsize=15)
    for x, label in zip(p_x, 'ABC'):
        device(x, 4.9, label, True)
        wire([x, x], [6.0, 5.15])
        wire([x, x], [4.65, 3.8])
        ax.add_patch(Circle((x, 3.8), .035, color='#243746'))
    wire([1.8, 6.6], [3.8, 3.8])
    ax.text(6.75, 3.8, r'$Y=\overline{ABC}$', va='center', fontsize=15)
    x = 5.4
    for y, label in [(2.95, 'A'), (1.85, 'B'), (.75, 'C')]:
        device(x, y, label)
    for top, bottom in [(3.8, 3.20), (2.70, 2.10), (1.60, 1.00), (.50, .05)]:
        wire([x, x], [top, bottom])
    for width, y in [(.55, .05), (.36, -.08), (.16, -.21)]:
        wire([x-width/2, x+width/2], [y, y])
    ax.text(.1, 6.7, 'Three-input CMOS NAND', weight='bold', fontsize=17)
    ax.text(.25, 5.95, 'Parallel PMOS\npull-up network', va='top', color='#315d7a')
    ax.text(.25, 2.65, 'Series NMOS\npull-down network', va='top', color='#315d7a')
    ax.text(.25, .45, 'Each input drives one PMOS\nand one NMOS gate.', fontsize=11)
    fig.subplots_adjust(left=.035, right=.94, top=.97, bottom=.035)
    fig.savefig(Path.cwd() / 'computing-prelims-2005-cmos-nand.png', facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
