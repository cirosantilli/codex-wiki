"""Original functional Barkhausen schematic; Python 3.14, matplotlib 3.10.7.
Run from the desired output directory; emits only this script's basename.png.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Ellipse

BLUE = '#245d8c'
ORANGE = '#a45d17'


def main():
    fig, ax = plt.subplots(figsize=(12, 7.6), dpi=110)
    fig.patch.set_facecolor('white')
    ax.set(xlim=(0, 12), ylim=(0, 7.6))
    ax.axis('off')
    ax.text(.3, 7.3, 'Barkhausen measurement: drive, specimen, readout', fontsize=19, weight='bold')
    ax.text(.3, 6.94, 'Functional schematic • control additions are orange and dashed', fontsize=12, color='#444444')

    def box(x, y, w, h, text, color=BLUE, dashed=False):
        p = FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.07',
                           facecolor='white', edgecolor=color, linewidth=1.6,
                           linestyle='--' if dashed else '-')
        ax.add_patch(p)
        ax.text(x+w/2, y+h/2, text, ha='center', va='center', fontsize=12, color=color)

    def arrow(points, color=BLUE, dashed=False):
        xs, ys = zip(*points)
        ax.plot(xs[:-1], ys[:-1], color=color, lw=1.6, ls='--' if dashed else '-')
        ax.annotate('', xy=points[-1], xytext=points[-2],
                    arrowprops=dict(arrowstyle='->', lw=1.6, color=color,
                                    linestyle='--' if dashed else '-'))

    box(.4, 5.35, 1.75, 1.02, 'Triangle\ngenerator')
    box(2.8, 5.35, 1.7, 1.02, 'Drive\namplifier')
    arrow([(2.22, 5.87), (2.73, 5.87)])
    arrow([(4.57, 5.87), (5.25, 5.87)])
    ax.plot([.7, .98, 1.26, 1.54, 1.82], [5.03, 5.25, 5.03, 5.25, 5.03], color=BLUE, lw=1.6)
    ax.text(.5, 4.65, 'Slow field sweep;\nmonitor drive current', fontsize=11, color=BLUE)

    ax.add_patch(Rectangle((5.3, 4.9), 6.2, 1.65, facecolor='#f1f6fa', edgecolor=BLUE, lw=1.5))
    for x in [5.5, 5.85, 6.2, 6.55, 6.9, 7.25, 7.6, 7.95, 8.3, 8.65, 9, 9.35, 9.7, 10.05, 10.4, 10.75, 11.1, 11.35]:
        ax.plot([x, x], [6.42, 6.55], color=BLUE, lw=1)
        ax.plot([x, x], [4.9, 5.03], color=BLUE, lw=1)
    ax.text(8.4, 6.68, 'Long drive solenoid', ha='center', fontsize=12, color=BLUE)
    ax.add_patch(Rectangle((5.8, 5.52), 3.65, .36, facecolor='#858f98', edgecolor='#40484f'))
    for x in [7.25, 7.34, 7.43, 7.52, 7.61]:
        ax.add_patch(Ellipse((x, 5.7), .15, .86, facecolor='none', edgecolor='#19364d', lw=1.4))
    ax.text(6.4, 5.14, 'Stationary ferromagnet', fontsize=10.5, ha='center')
    ax.text(7.46, 6.24, 'Pickup coil', fontsize=10.5, ha='center')
    for x in [10.17, 10.26, 10.35, 10.44, 10.53]:
        ax.add_patch(Ellipse((x, 5.7), .15, .86, facecolor='none', edgecolor=ORANGE, lw=1.3, linestyle='--'))
    ax.text(10.35, 5.12, 'Empty coil', color=ORANGE, fontsize=10.5, ha='center')
    arrow([(9.3, 6.18), (10.9, 6.18)])
    ax.text(10.1, 6.31, r'$H_{\rm applied}(t)$', fontsize=12, ha='center', color=BLUE)
    ax.text(8.4, 4.62, 'Specimen and coils fixed in position', ha='center', fontsize=11)

    arrow([(7.43, 5.25), (7.43, 4.22), (1.0, 4.22), (1.0, 3.05)])
    ax.text(4.0, 4.3, 'Material + direct drive pickup', ha='center', fontsize=11, color=BLUE)
    arrow([(10.35, 5.25), (10.35, 3.72), (1.95, 3.72), (1.95, 3.05)], ORANGE, True)
    ax.text(6.2, 3.8, 'Matched empty coil: direct drive pickup', ha='center', fontsize=11, color=ORANGE)

    box(.5, 1.95, 2.0, 1.0, 'Difference\n(optional control)', ORANGE, True)
    ax.text(.92, 3.12, '+', fontsize=15, color=BLUE)
    ax.text(1.87, 3.12, '−', fontsize=15, color=ORANGE)
    box(3.2, 1.95, 1.7, 1.0, 'Low-noise\namplifier')
    box(5.6, 1.95, 1.7, 1.0, 'Low-pass\nfilter')
    box(8.05, 1.95, 2.4, 1.0, 'Digitizer\nvoltage vs time')
    for a, b in [(2.57, 3.13), (4.97, 5.53), (7.37, 7.98)]:
        arrow([(a, 2.45), (b, 2.45)])
    ax.text(.45, 1.2, r'Pickup: $e=-d\lambda/dt$     →     gain and filtering     →     recorded $v_{\rm out}(t)$', fontsize=14)
    ax.text(.45, .68, 'Checks: drive off • specimen removed • repeat both ramp directions • vary sweep rate', fontsize=12)
    ax.text(.45, .25, 'No measured trace shown. Coil geometry is schematic; the empty coil links no specimen.', fontsize=11, color='#444444')
    fig.subplots_adjust(left=.02, right=.99, bottom=.02, top=.99)
    fig.savefig(Path(__file__).stem+'.png', facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
