"""Calculate the signed Dirichlet kernels and their response; output to cwd."""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def kernel(x, xi):
    return -np.sinh(np.minimum(x, xi))*np.sinh(1-np.maximum(x, xi))/np.sinh(1)


def response(x):
    return .5*(x*np.exp(x)-np.e*np.sinh(x)/np.sinh(1))


def main():
    plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4), layout='constrained')
    x=np.linspace(0, 1, 801)
    for xi,color in [(.25,'#1764ab'),(.5,'#b14928'),(.75,'#664799')]:
        axes[0].plot(x,kernel(x,xi),color=color,lw=2,label=rf'$\xi={xi:g}$')
        axes[0].scatter([xi],[kernel(xi,xi)],s=20,color=color,zorder=4)
    axes[0].set(title='Negative kernel; positive derivative jump',xlabel='$x$',ylabel=r'$G(x,\xi)$')
    axes[0].legend(loc='lower right')
    axes[1].plot(x,response(x),color='#1764ab',lw=2.5)
    axes[1].set(title=r'Forced solution: $u^{\prime\prime}-u=e^x$',xlabel='$x$',ylabel='$u(x)$')
    for ax in axes:
        ax.axhline(0,color='#777777',lw=.7)
        ax.set_xlim(0,1)
        ax.grid(alpha=.18)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white')
    plt.close(fig)


if __name__=='__main__':
    main()
