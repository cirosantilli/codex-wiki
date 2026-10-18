"""Generate the Oxford 2011 Brillouin-function sketch (Python 3.14)."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def brillouin(j, x):
    m = np.arange(-j, j+1, 1.)
    logweight = np.outer(x, m/j)
    logweight -= np.max(logweight, axis=1, keepdims=True)
    weight = np.exp(logweight)
    return (weight @ (m/j))/np.sum(weight, axis=1)


def main():
    x = np.linspace(-6,6,601)
    fig, ax = plt.subplots(figsize=(6.7,3.8), layout='constrained')
    for j, color in [(.5,'#155b8a'),(1.,'#bd542a'),(2.,'#795a98')]:
        ax.plot(x,brillouin(j,x), lw=2, color=color, label=rf'$J={j:g}$')
    for limit in [-1,1]:
        ax.axhline(limit, color='#666666',ls='--', lw=.8)
    ax.axhline(0,color='black',lw=.6)
    ax.axvline(0,color='black',lw=.6)
    ax.set(xlim=(-6,6),ylim=(-1.13,1.13), xlabel=r'$x=g\mu_BJB/(k_BT)$',
           ylabel=r'$B_J(x)=M/M_s$',title='Brillouin functions and saturation limits')
    ax.legend(frameon=True,facecolor='white',edgecolor='none',framealpha=1.,loc='upper left')
    ax.grid(alpha=.15)
    fig.savefig(Path.cwd()/'2011-brillouin-functions.png',dpi=130,
                facecolor='white',transparent=False)
    plt.close(fig)

if __name__ == '__main__':
    main()
