"""Render an original value-function sensitivity example to CWD, without empirical data."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size': 12, 'axes.spines.top': False, 'axes.spines.right': False})
    fig, (ax, right) = plt.subplots(1, 2, figsize=(12, 5.8), layout='constrained', facecolor='white')
    c = np.linspace(0, 5, 350)
    ax.plot(c, 2*c*c/3, c='#2375b9', lw=2.5, label=r'Optimal cost $V(c)=2c^2/3$')
    ax.plot(c, 6+4*(c-3), c='#d85b26', ls='--', lw=2, label=r'Tangent $6+4(c-3)$')
    ax.scatter([3], [6], c='#162f46', s=60, zorder=5)
    ax.annotate(r'$V(3)=6$; slope $\lambda_*(3)=4$', (3, 6), xytext=(0.3, 12), arrowprops={'arrowstyle': '->'}, fontsize=11)
    ax.set(xlim=(0, 5), ylim=(-1, 18), xlabel=r'Required total $c$', ylabel='Minimum cost', title='The multiplier is a derivative')
    ax.legend(loc='upper left', fontsize=10)
    delta = np.linspace(0, 1, 350)
    linear = 4*delta
    exact = linear+2*delta*delta/3
    right.fill_between(delta, linear, exact, color='#efc8a8', label=r'Correction $2\delta^2/3$')
    right.plot(delta, exact, c='#2375b9', lw=2.5, label='Exact cost increase')
    right.plot(delta, linear, c='#d85b26', ls='--', lw=2, label=r'First order: $4\delta$')
    right.scatter([.1], [4*.1+2*.1**2/3], c='#162f46', s=45, zorder=5)
    right.annotate(r'$\delta=0.1$'+'\nExact: 0.406667\nFirst order: 0.4', (.1, 4*.1+2*.1**2/3), xytext=(.12, 2.5), arrowprops={'arrowstyle': '->'}, fontsize=10)
    right.set(xlim=(0, 1), ylim=(0, 5.4), xlabel=r'Increase $\delta$ from $c=3$', ylabel='Increase in minimum cost', title='Finite changes include curvature')
    right.legend(loc='upper left', fontsize=10)
    fig.suptitle('Marginal cost predicts a small change, with an explicit correction', fontsize=16)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=110, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
