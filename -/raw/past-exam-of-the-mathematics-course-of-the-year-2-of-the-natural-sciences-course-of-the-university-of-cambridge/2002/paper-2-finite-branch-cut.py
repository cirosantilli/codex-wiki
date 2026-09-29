"""Finite-cut square root and contour orientation; Python 3.14, matplotlib 3.10."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np


def main():
    plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
    fig, ax = plt.subplots(figsize=(8.5, 4.0), dpi=120, layout='constrained')
    ax.axhline(0, color='0.8', lw=.8)
    ax.axvline(0, color='0.88', lw=.8)
    ax.add_patch(Ellipse((0, 0), 3.02, 1.40, fill=False, ls='--', lw=1.3, color='0.6'))
    blue, brown = '#176d9c', '#ad562b'
    eps = .17
    ax.plot([-1, 1], [0, 0], color=brown, lw=4, solid_capstyle='round', label='Branch cut')
    ax.scatter([-1, 1], [0, 0], color=brown, s=36, zorder=5)
    for y in [-eps, eps]:
        ax.plot([-1, 1], [y, y], color=blue, lw=1.8)
    for x, lo, hi in [(1, -np.pi/2, np.pi/2), (-1, np.pi/2, 3*np.pi/2)]:
        t = np.linspace(lo, hi, 100)
        ax.plot(x + eps*np.cos(t), eps*np.sin(t), color=blue, lw=1.8)
    for x in [-.55, .55]:
        ax.annotate('', xy=(x-.13, eps), xytext=(x+.13, eps), arrowprops={'arrowstyle': '-|>', 'color': blue, 'lw': 1.8})
        ax.annotate('', xy=(x+.13, -eps), xytext=(x-.13, -eps), arrowprops={'arrowstyle': '-|>', 'color': blue, 'lw': 1.8})
    ax.text(0, .34, r'$f(x+i0)=+i\sqrt{1-x^2}$', ha='center', color=blue, fontsize=13)
    ax.text(0, -.43, r'$f(x-i0)=-i\sqrt{1-x^2}$', ha='center', color=blue, fontsize=13)
    ax.text(-1, -.085, r'$-1$', ha='center', va='top', color=brown, bbox={'facecolor':'white','edgecolor':'none','pad':.2})
    ax.text(1, -.085, r'$1$', ha='center', va='top', color=brown, bbox={'facecolor':'white','edgecolor':'none','pad':.2})
    ax.text(1.35, .48, r'$C$', color='0.45', fontsize=13)
    ax.annotate(r'Endpoint arcs: $O(\sqrt{\varepsilon})$', xy=(1.17, 0), xytext=(.9, -.68), ha='center', color='0.35', arrowprops={'arrowstyle':'->','color':'0.5'}, fontsize=10)
    ax.text(1.57, .035, r'$\operatorname{Re}\zeta$', ha='right', color='0.4')
    ax.set(xlim=(-1.65, 1.65), ylim=(-.82, .85), xticks=[], yticks=[], title=r'Finite cut; branch normalized by $f(z)\sim z$ at infinity')
    ax.set_aspect('equal')
    for spine in ax.spines.values():
        spine.set_visible(False)
    fig.savefig(Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
