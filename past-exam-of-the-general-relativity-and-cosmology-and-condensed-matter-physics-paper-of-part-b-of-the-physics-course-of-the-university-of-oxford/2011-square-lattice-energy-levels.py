"""Generate the Oxford 2011 two/four-wave band-level sketch (Python 3.14)."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    ex = .0380998211615486*np.pi**2/.3**2
    u, w = -1., -.2
    fig, ax = plt.subplots(figsize=(7.3, 4.0), layout='constrained')
    levels = [(0,ex+u,r'$E_X+u$ (1)', '#155b8a'),
              (0,ex-u,r'$E_X-u$ (1)', '#bd542a'),
              (1,2*ex+w+2*u,r'$2E_X+w+2u$ (1)', '#155b8a'),
              (1,2*ex-w,r'$2E_X-w$ (2)', '#795a98'),
              (1,2*ex+w-2*u,r'$2E_X+w-2u$ (1)', '#bd542a')]
    for xpos, energy, label, color in levels:
        ax.plot([xpos-.17,xpos+.17], [energy,energy], color=color, lw=2.5)
        ax.text(xpos+.20, energy, label, va='center', fontsize=10, color=color)
    ax.plot([.7,.91], [ex-u,ex-u], ls=':', lw=1, color='#555555')
    ax.annotate('Band overlap', xy=(.62,(ex-u+2*ex+w+2*u)/2),
                xytext=(.35,4.4), fontsize=9,
                arrowprops={'arrowstyle':'->','color':'#555555'})
    ax.set(xlim=(-.35,2.12), ylim=(2.2,11.1), ylabel='Energy (eV)',
           title=r'$a=0.3$ nm, $u=V_{10}=-1$ eV, $w=V_{11}=-0.2$ eV')
    ax.set_xticks([0,1], [r'$X=(\pi/a,0)$',r'$M=(\pi/a,\pi/a)$'])
    ax.text(.99, .015, 'Parentheses give degeneracy per spin', transform=ax.transAxes,
            ha='right', fontsize=9)
    ax.spines[['top','right']].set_visible(False)
    ax.grid(axis='y', alpha=.15)
    fig.savefig(Path.cwd()/'2011-square-lattice-energy-levels.png', dpi=130,
                facecolor='white', transparent=False)
    plt.close(fig)

if __name__ == '__main__':
    main()
