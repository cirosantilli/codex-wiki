"""Original linking geometry; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; writes its own basename PNG into the current directory.
The torus is shown in a meridional section, not as an axial flux tube.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon
import numpy as np

BLUE = '#186aaf'
ORANGE = '#c25a17'
GRAY = '#e6e8eb'


def arrow(ax, start, end, color):
    ax.annotate('', xy=end, xytext=start,
                arrowprops={'arrowstyle': '-|>', 'color': color, 'lw': 2,
                            'mutation_scale': 16})


def main():
    plt.rcParams.update({'font.size': 12, 'axes.titlesize': 14})
    fig, axes = plt.subplots(1, 2, figsize=(12, 6.2), facecolor='white')
    for ax in axes:
        ax.set_aspect('equal')
        ax.axis('off')
    ax = axes[0]
    ax.set_title('Ideal infinite flux tube: transverse section', pad=20)
    ax.add_patch(Circle((0, 0), .92, facecolor=GRAY, edgecolor='#59616b', lw=2))
    ax.add_patch(Circle((0, 0), .55, facecolor='#cbdce9', edgecolor=BLUE, lw=1.5))
    ax.text(0, 0, r'$\otimes\ \Phi$', ha='center', va='center', fontsize=19, color=BLUE)
    t = np.linspace(0, 1, 250)
    x = -3 + 6*t
    y = 1.7*np.sin(np.pi*t)
    ax.plot(x, y, color=BLUE, lw=3)
    ax.plot(x, -y, color=ORANGE, lw=3)
    arrow(ax, (-.3, 1.67), (.3, 1.67), BLUE)
    arrow(ax, (-.3, -1.67), (.3, -1.67), ORANGE)
    ax.scatter([-3, 3], [0, 0], c='#222222', s=34, zorder=5)
    ax.text(-3, -.35, '$S$', ha='center')
    ax.text(3, -.35, '$D$', ha='center')
    ax.text(-1.9, 1.65, r'$\gamma_1$', color=BLUE, fontsize=15)
    ax.text(-1.9, -1.9, r'$\gamma_2$', color=ORANGE, fontsize=15)
    ax.annotate('excluded region', xy=(.72, -.5), xytext=(.2, -2.55), ha='center',
                arrowprops={'arrowstyle': '-', 'color': '#59616b'})
    ax.text(0, 2.45, r'$\mathbf{B}=0$ along both paths', ha='center')
    ax.text(0, -3.25, r'$C=\gamma_1-\gamma_2$ links the flux once', ha='center')
    ax.set(xlim=(-3.6, 3.6), ylim=(-3.65, 3.1))

    ax = axes[1]
    ax.set_title('Excluded solid torus: meridional section', pad=20)
    ax.add_patch(Polygon([(0, -2.35), (3.1, -2.35), (3.1, 2.35), (0, 2.35)],
                         facecolor='#f2f6fa', edgecolor='none', zorder=0))
    for cx, symbol in [(-1.45, r'$\odot$'), (1.45, r'$\otimes$')]:
        ax.add_patch(Circle((cx, 0), .75, facecolor=GRAY, edgecolor='#59616b', lw=2))
        ax.add_patch(Circle((cx, 0), .43, facecolor='#cbdce9', edgecolor=BLUE, lw=1.5))
        ax.text(cx, 0, symbol, ha='center', va='center', color=BLUE, fontsize=25)
    ax.plot([0, 0], [-2.35, 2.35], color=BLUE, lw=3)
    ax.plot([0, 3.1, 3.1, 0], [-2.35, -2.35, 2.35, 2.35], color=ORANGE, lw=3)
    arrow(ax, (0, -.6), (0, .2), BLUE)
    arrow(ax, (3.1, -.6), (3.1, .2), ORANGE)
    ax.scatter([0, 0], [-2.35, 2.35], c='#222222', s=34, zorder=5)
    ax.text(-.15, -2.65, '$S$', ha='right')
    ax.text(-.15, 2.5, '$D$', ha='right')
    ax.text(-.15, 1.0, 'through\nhole', color=BLUE, ha='right')
    ax.text(3.28, .8, 'outside', color=ORANGE, rotation=90, va='center')
    ax.annotate('one spanning surface\ncrosses this core', xy=(1.6, .3),
                xytext=(1.7, 1.35), ha='center', fontsize=11,
                arrowprops={'arrowstyle': '->', 'color': '#59616b'})
    ax.text(.7, -3.25, 'Core field circulates around the torus;\nit is not an axial field in the central hole.', ha='center', fontsize=11)
    ax.set(xlim=(-2.7, 3.8), ylim=(-3.65, 3.1))
    fig.suptitle('Aharonov–Bohm geometry: a closed loop remembers inaccessible flux', fontsize=16, y=.98)
    fig.subplots_adjust(left=.025, right=.975, bottom=.04, top=.86, wspace=.16)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=100,
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
