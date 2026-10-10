"""Original ideal TE10 field diagram; Python 3.14, numpy 2.3.5, matplotlib 3.10.7.

Run from _media; the output basename matches this script. All dimensions are
stipulated, not measurements or a commercial waveguide specification.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def main():
    a, b = 30.0, 12.0  # millimetres
    plt.rcParams.update({'font.size': 11, 'axes.spines.top': False,
                         'axes.spines.right': False, 'figure.facecolor': 'white'})
    fig, (ax, profile) = plt.subplots(1, 2, figsize=(10.8, 4.7),
                                    gridspec_kw={'width_ratios': [1.65, 1]})
    fig.subplots_adjust(left=0.065, right=0.975, bottom=0.19, top=0.78, wspace=0.32)
    fig.suptitle(r'$\mathrm{TE}_{10}$: one electric-field half-wave across the broad dimension',
                 fontsize=15, y=0.97)
    fig.text(0.5, 0.865, r'Chosen vacuum guide: $a=30$ mm, $b=12$ mm; '
             r'$f=1.25f_c\approx6.246$ GHz; ideal conducting walls', ha='center')
    ax.add_patch(Rectangle((0, 0), a, b, fill=False, linewidth=5, edgecolor='#505963'))
    x = np.linspace(2, 28, 13)
    for y in (2.1, 6, 9.9):
        amp = 3.2 * np.sin(np.pi * x / a)
        ax.quiver(x, y - amp / 2, np.zeros_like(x), amp, angles='xy',
                  scale_units='xy', scale=1, width=0.006, color='#1670b6')
    ax.plot([0, a], [b / 2, b / 2], 'o', color='#c45131', markersize=6)
    ax.annotate('', (a, -2), (0, -2), arrowprops={'arrowstyle': '<->', 'color': '#505963'})
    ax.text(a / 2, -3.7, r'$a=30$ mm', ha='center')
    ax.annotate('', (-2, b), (-2, 0), arrowprops={'arrowstyle': '<->', 'color': '#505963'})
    ax.text(-4.0, b / 2, r'$b=12$ mm', ha='center', va='center', rotation=90)
    ax.text(a / 2, b + 1.4, r'$E_y\propto\sin(\pi x/a)$, independent of $y$', ha='center')
    ax.text(0, -6.1, r'$x\rightarrow$     $y\uparrow$     $\odot\ +z$ out of page', fontsize=11)
    ax.text(a / 2, b / 2 + 0.8, r'$E_y$ strongest at $x=a/2$', ha='center', fontsize=10,
            bbox={'facecolor': 'white', 'edgecolor': 'none', 'alpha': 0.9})
    ax.set(xlim=(-5.5, 32), ylim=(-7, 15), aspect='equal')
    ax.axis('off')
    xx = np.linspace(0, a, 501)
    ee = np.sin(np.pi * xx / a)
    profile.plot(xx, ee, color='#1670b6', linewidth=2.7)
    profile.fill_between(xx, ee, color='#1670b6', alpha=0.1)
    profile.plot([0, a], [0, 0], 'o', color='#c45131', clip_on=False)
    profile.axvline(a / 2, color='#b4bcc4', linestyle=':', linewidth=1)
    profile.set(xlim=(0, a), ylim=(0, 1.1), xticks=[0, 15, 30], yticks=[0, .5, 1],
                xlabel=r'$x$ across broad dimension (mm)', ylabel=r'$E_y/E_0$ at a positive-phase plane')
    profile.set_title('Electric profile at every height', fontsize=12, pad=10)
    profile.grid(alpha=0.18)
    fig.text(0.5, 0.045, 'Zero tangential E at the side walls; normal E is allowed at the top and bottom walls.',
             ha='center', fontsize=10, color='#3e4952')
    fig.savefig(Path(__file__).stem + '.png', dpi=130, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
