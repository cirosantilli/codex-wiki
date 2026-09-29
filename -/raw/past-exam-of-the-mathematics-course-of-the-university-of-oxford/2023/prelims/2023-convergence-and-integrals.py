"""Three independent convergence examples; write the PNG into cwd."""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size':11,'savefig.facecolor':'white'})
    fig, axes = plt.subplots(1,3,figsize=(11.4,4.0),layout='constrained')
    colors=['#1565a7','#c34b20','#238354']
    x=np.linspace(0,1,2001)
    for n,color in zip([2,4,8],colors):
        axes[0].plot(x,n*np.maximum(1-np.abs(n*x-1),0),color=color,label=fr'$n={n}$')
    axes[0].set(title='Concentration: area stays 1',xlabel='$x$',ylabel='$f_n(x)$',xlim=(0,1),ylim=(0,8.5))
    x=np.linspace(-9,9,3601)
    for n,color in zip([2,4,8],colors):
        axes[1].plot(x,np.maximum(1-np.abs(x/n),0)/n,color=color,label=fr'$n={n}$')
    axes[1].set(title='Spreading: area stays 1',xlabel='$x$',ylabel='$f_n(x)$',xlim=(-9,9),ylim=(0,.54))
    x=np.linspace(0,1,2001)
    for n,color in zip([2,4,8],colors):
        axes[2].plot(x,2*n/np.sqrt(np.pi)*np.exp(-(n*x)**2),color=color,label=fr'$n={n}$')
    axes[2].set(title='Endpoint mass tends to 1',xlabel='$x$',ylabel='$g_n(x)$',xlim=(0,1),ylim=(0,9.6))
    for ax in axes:
        ax.grid(alpha=.2)
        ax.spines[['top','right']].set_visible(False)
        ax.legend(frameon=False,fontsize=10)
    fig.savefig(Path.cwd()/'2023-convergence-and-integrals.png',dpi=100,facecolor='white')
    plt.close(fig)


if __name__=='__main__':
    main()
