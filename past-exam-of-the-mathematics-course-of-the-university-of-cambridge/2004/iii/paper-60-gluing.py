"""Signed gluing map: cusp, fold tangencies and bifurcation diagrams.
Python 3.14/NumPy 2.3.5/Matplotlib 3.10.7; PNG basename in caller CWD.
Honors MPLCONFIGDIR; all panels have white opaque backgrounds.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    fig = plt.figure(figsize=(8.1, 8.0), layout='constrained')
    fig.patch.set_facecolor('white');grid = fig.add_gridspec(3, 2)
    A=.7;ax=fig.add_subplot(grid[0, :]);ax.set_facecolor('white')
    delta=np.linspace(.6, .999, 600);r=(A*delta)**(1/(1-delta));C=(1-delta)/delta*r
    ax.fill_betweenx(delta, -C, C, color='#c7e4eb', label='Three scalar fixed branches')
    ax.plot(-C, delta, color='#00679c');ax.plot(C, delta, color='#00679c')
    ax.plot(0, 1, 'o', mfc='white', mec='#222222')
    ax.set(xlim=(-.08, .08), ylim=(.6, 1.03), xlabel=r'$\mu$', ylabel=r'$\delta$', title=r'Local cusp below $\delta=1$, $A=0.7$')
    ax.legend(frameon=False, loc='lower right');ax.grid(alpha=.12)
    u=np.linspace(-6, 6, 4001);d=.8
    for j, mu in enumerate([-(1-d)/d, (1-d)/d]):
        ax=fig.add_subplot(grid[1, j]);ax.set_facecolor('white')
        value=mu+np.sign(u)*abs(u)**d/d
        ax.plot(u, value, color='#00679c', lw=2);ax.plot(u, u, '--', color='#666666', lw=1)
        fold=1 if j==0 else -1
        ax.plot(fold, fold, 'ko', ms=4)
        ax.set(xlim=(-5.5, 5.5), ylim=(-6, 6), xlabel=r'$z/r$', ylabel=r'$f(z)/r$', title=r'$\mu=-C$: fold at $+r$' if j==0 else r'$\mu=+C$: fold at $-r$')
        ax.grid(alpha=.12)
    for j, d in enumerate([1.2, .8]):
        ax=fig.add_subplot(grid[2, j]);ax.set_facecolor('white')
        u=np.linspace(-7, 7, 6001);h=(d*u-np.sign(u)*abs(u)**d)/abs(d-1)
        stable=abs(u)<1 if d>1 else abs(u)>1
        ax.plot(np.where(stable, h, np.nan), u, '-', color='#00679c', lw=2.2, label='Stable')
        ax.plot(np.where(~stable, h, np.nan), u, '--', color='#a3471b', lw=1.7, label='Unstable')
        ax.plot([1, -1], [1, -1] if d>1 else [-1, 1], 'ko', ms=4)
        ax.plot(0, 0, 'o', mfc='white', mec='#222222', ms=5)
        ax.set(xlim=(-3, 3), ylim=(-4, 4) if d>1 else (-6.2, 6.2), xlabel=r'$\mu/C$', ylabel=r'$z/r$', title=rf'$\delta={d:g}$: '+('formal large folds' if d>1 else 'local cusp branches'))
        ax.grid(alpha=.12);ax.legend(frameon=False, fontsize=8, loc='lower right')
    for ax in fig.axes:ax.spines[['top', 'right']].set_visible(False)
    fig.savefig(Path.cwd()/'paper-60-gluing.png', dpi=120, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
