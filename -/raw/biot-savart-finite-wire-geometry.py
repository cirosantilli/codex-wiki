"""Original finite-wire diagram. Tested with Python 3.14, matplotlib 3.10, numpy 2.3."""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def main():
    plt.rcParams.update({'font.size': 11, 'axes.titlesize': 13})
    blue, red, gray = '#176b9b', '#b33b32', '#626a73'
    fig, (ax, plot) = plt.subplots(1, 2, figsize=(10, 4.8), dpi=130,
                                  gridspec_kw={'width_ratios': [1, 1.1]}, facecolor='white')
    fig.subplots_adjust(left=.055, right=.97, bottom=.16, top=.83, wspace=.3)
    fig.suptitle('Finite straight wire: orientation and the long-wire limit', fontsize=15, y=.96)
    ax.set_title('Geometry at the midpoint', pad=10)
    ax.set_aspect('equal')
    ax.set_xlim(-.045, .12)
    ax.set_ylim(-.155, .155)
    ax.axis('off')
    a, half_length = .05, .12
    ax.plot([0, 0], [-half_length, half_length], color=blue, lw=5)
    ax.annotate('', xy=(0, .075), xytext=(0, .025),
                arrowprops={'arrowstyle': '-|>', 'lw': 2.5, 'color': red})
    ax.text(-.034, .05, r'$I=3\,\mathrm{A}$', color=red, va='center')
    ax.text(-.004, half_length+.01, r'$s_2=+0.12\,\mathrm{m}$', ha='center')
    ax.text(-.004, -half_length-.018, r'$s_1=-0.12\,\mathrm{m}$', ha='center')
    for s in (-half_length, half_length):
        ax.plot([0, a], [s, 0], '--', color=gray, lw=1.2)
    ax.plot([0, a], [0, 0], ':', color=gray)
    ax.annotate('', xy=(a, -.015), xytext=(0, -.015),
                arrowprops={'arrowstyle': '<->', 'color': gray})
    ax.text(a/2, -.032, r'$a=0.05\,\mathrm{m}$', ha='center')
    ax.annotate('', xy=(a, 0), xytext=(0, .058),
                arrowprops={'arrowstyle': '-|>', 'lw': 1.5, 'color': blue})
    ax.text(.033, .048, r'$\mathbf{R}$', color=blue)
    ax.add_patch(Circle((a, 0), .0045, edgecolor=red, facecolor='white', lw=1.7, zorder=5))
    d = .0024
    ax.plot([a-d, a+d], [-d, d], color=red, lw=1.6, zorder=6)
    ax.plot([a-d, a+d], [d, -d], color=red, lw=1.6, zorder=6)
    ax.text(a+.012, .005, 'P', va='center', fontsize=12)
    ax.text(a+.012, -.015, 'B into page', color=red, va='center')
    ax.annotate('', xy=(.09, -.105), xytext=(.06, -.105),
                arrowprops={'arrowstyle': '->', 'color': gray})
    ax.annotate('', xy=(.06, -.075), xytext=(.06, -.105),
                arrowprops={'arrowstyle': '->', 'color': gray})
    ax.text(.094, -.106, 'x', color=gray)
    ax.text(.058, -.069, 'y', color=gray)
    ratio = np.linspace(0, 8, 500)
    plot.plot(ratio, ratio/np.sqrt(1+ratio**2), color=blue, lw=2.6)
    plot.axhline(1, color=gray, ls='--', lw=1.2)
    plot.text(6.1, 1.013, 'infinite wire', color=gray, fontsize=10)
    plot.scatter([2.4], [12/13], color=red, zorder=5)
    plot.annotate(r'$L/a=2.4$'+'\n'+r'$B/B_\infty=12/13$', (2.4, 12/13),
                  xytext=(3.45, .64), arrowprops={'arrowstyle': '->', 'color': red}, color=red)
    plot.set(xlim=(0, 8), ylim=(0, 1.08), xlabel=r'Half-length / distance, $L/a$',
             ylabel=r'Midpoint field ratio, $B/B_\infty$',
             title=r'$B/B_\infty=L/\sqrt{a^2+L^2}$')
    plot.grid(alpha=.2)
    plot.spines[['top', 'right']].set_visible(False)
    fig.text(.5, .025, 'Segment contribution only; add the return path for a complete circuit.',
             ha='center', fontsize=10, color=gray)
    fig.savefig(Path.cwd() / (Path(__file__).stem+'.png'), facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
