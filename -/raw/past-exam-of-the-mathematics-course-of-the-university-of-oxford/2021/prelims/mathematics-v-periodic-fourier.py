"""Period-two function with its assigned and Fourier-midpoint jump values."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size':12,'savefig.facecolor':'white'})
    fig,ax=plt.subplots(figsize=(9.0,3.8),layout='constrained')
    for k in [-1,0,1]:
        x=np.linspace(-1+2*k,2*k,200);ax.plot(x,2*(x-2*k)+1,color='#222222',lw=2)
        x=np.linspace(2*k,1+2*k,200);ax.plot(x,1-(x-2*k),color='#222222',lw=2)
    odd=np.array([-3,-1,1,3])
    ax.scatter(odd,np.zeros(4),color='#222222',s=42,zorder=5,label='Assigned value')
    ax.scatter(odd,-np.ones(4),facecolor='white',edgecolor='#222222',s=44,zorder=5,label='Right-hand limit')
    ax.scatter(odd,-.5*np.ones(4),color='#1565a7',marker='D',s=35,zorder=5,label='Fourier sum at jump')
    ax.axhline(0,color='#888888',lw=.6)
    ax.set(xlim=(-3.15,3.15),ylim=(-1.2,1.2),xticks=range(-3,4),xlabel='$x$',ylabel='Value',title='Periodic function: Fourier sums use midpoint limits')
    ax.grid(alpha=.17);ax.spines[['top','right']].set_visible(False)
    ax.legend(ncol=3,loc='upper center',bbox_to_anchor=(.5,-.18),fontsize=10,frameon=False)
    fig.savefig(Path.cwd()/'mathematics-v-periodic-fourier.png',dpi=100,facecolor='white')
    plt.close(fig)


if __name__=='__main__':main()
