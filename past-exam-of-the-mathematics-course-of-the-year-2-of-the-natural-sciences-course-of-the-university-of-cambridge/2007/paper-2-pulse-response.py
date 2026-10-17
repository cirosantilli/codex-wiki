"""Calculate finite-pulse responses of f'-f=S; write PNG to cwd."""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def response(t,n):
    a,b=1-1/(2*n),1+1/(2*n)
    out=np.zeros_like(t)
    active=(t>=a)&(t<=b)
    out[active]=n*np.expm1(t[active]-a)
    after=t>b
    out[after]=2*n*np.sinh(1/(2*n))*np.exp(t[after]-1)
    return out


def main():
    plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.facecolor':'white'})
    fig,axes=plt.subplots(2,1,figsize=(8.5,5.8),sharex=True,layout='constrained',
                          gridspec_kw={'height_ratios':[2,1]})
    t=np.linspace(0,2.6,2001)
    for n,color in [(1,'#1764ab'),(4,'#b14928')]:
        axes[0].plot(t,response(t,n),color=color,lw=2,label=f'n={n}')
        a,b=1-1/(2*n),1+1/(2*n)
        axes[1].plot([0,a,a,b,b,2.6],[0,0,n,n,0,0],color=color,lw=2,label=f'n={n}')
    axes[0].plot(t,np.where(t>=1,np.exp(t-1),0),'--',color='#555555',lw=1.2,label='impulse limit')
    axes[0].set(ylabel='$f(t)$',title="Finite pulse input to f' − f = S")
    axes[0].legend(loc='upper left')
    axes[1].set(ylabel='$S_n(t)$',xlabel='$t$',ylim=(-.2,4.5),xlim=(0,2.6))
    for ax in axes:
        ax.axhline(0,color='#777777',lw=.7)
        ax.grid(alpha=.18)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white')
    plt.close(fig)


if __name__=='__main__':
    main()
