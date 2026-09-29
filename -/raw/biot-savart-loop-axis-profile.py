"""Original loop field diagram. Tested with Python 3.14, matplotlib 3.10, numpy 2.3."""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
import numpy as np


def main():
    plt.rcParams.update({'font.size': 11, 'axes.titlesize': 13})
    blue, red, gray = '#176b9b', '#b33b32', '#626a73'
    fig, (ax, plot) = plt.subplots(1, 2, figsize=(10, 4.8), dpi=130,
                                  gridspec_kw={'width_ratios': [1, 1.35]}, facecolor='white')
    fig.subplots_adjust(left=.065, right=.97, bottom=.19, top=.81, wspace=.33)
    fig.suptitle('Circular current loop: field direction on both sides of the center', fontsize=15, y=.96)
    ax.set_title('View from +z toward the loop', pad=13)
    ax.set_aspect('equal')
    ax.set_xlim(-1.45, 1.45)
    ax.set_ylim(-1.4, 1.4)
    ax.axis('off')
    phi = np.linspace(0, 2*np.pi, 360)
    ax.plot(np.cos(phi), np.sin(phi), color=blue, lw=4)
    for t in (.25, 2.35, 4.45):
        ax.add_patch(FancyArrowPatch((np.cos(t), np.sin(t)),
                                    (np.cos(t+.33), np.sin(t+.33)),
                                    connectionstyle='arc3,rad=.12', arrowstyle='-|>',
                                    mutation_scale=19, color=red, lw=2.7, zorder=3))
    ax.text(1.06, .57, r'$I=2\,\mathrm{A}$', color=red, ha='center')
    ax.add_patch(Circle((0, 0), .12, facecolor='white', edgecolor=blue, lw=2))
    ax.plot(0, 0, 'o', color=blue, ms=4)
    ax.text(0, .27, 'B toward viewer (+z)', color=blue, ha='center')
    ax.annotate('', xy=(-.72, -.69), xytext=(0, 0),
                arrowprops={'arrowstyle': '->', 'color': gray, 'lw': 1.4})
    ax.text(-.65, -.38, r'$R=0.04\,\mathrm{m}$', rotation=43, ha='center', color=gray)
    ax.text(0, -1.28, 'Counterclockwise conventional current', ha='center', fontsize=10, color=red)
    z = np.linspace(-3, 3, 601)
    plot.plot(z, (1+z*z)**(-1.5), color=blue, lw=2.6)
    plot.axvline(0, color=gray, ls=':', lw=1)
    plot.scatter([-.75, .75], [.512, .512], color=red, zorder=5)
    plot.hlines(.512, -.75, .75, color=red, ls=':', lw=1)
    plot.annotate(r'$B/B(0)=0.512$'+'\n'+r'at $z/R=\pm0.75$', (.75, .512),
                  xytext=(1.15, .76), arrowprops={'arrowstyle': '->', 'color': red},
                  color=red, fontsize=10)
    for start in (-2.55, -1.55, .95, 1.95):
        plot.annotate('', xy=(start+.43, .13), xytext=(start, .13),
                      arrowprops={'arrowstyle': '-|>', 'lw': 2, 'color': blue})
    plot.text(-1.92, .2, 'B points to +z', ha='center', fontsize=10, color=blue)
    plot.text(1.65, .2, 'B points to +z', ha='center', fontsize=10, color=blue)
    plot.set(xlim=(-3, 3), ylim=(0, 1.08), xlabel=r'Axial position, $z/R$',
             ylabel=r'Axial field ratio, $B_z/B(0)$',
             title=r'$B_z/B(0)=(1+z^2/R^2)^{-3/2}$')
    plot.grid(alpha=.2)
    plot.spines[['top', 'right']].set_visible(False)
    plot.annotate('+z', xy=(1.02, -.09), xycoords='axes fraction', ha='left', color=gray, fontsize=10)
    fig.text(.5, .045, r'One turn: $B(0)=31.42\,\mu\mathrm{T}$; $B(\pm0.03\,\mathrm{m})=16.08\,\mu\mathrm{T}$.',
             ha='center', fontsize=11, color=gray)
    fig.savefig(Path.cwd() / (Path(__file__).stem+'.png'), facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
