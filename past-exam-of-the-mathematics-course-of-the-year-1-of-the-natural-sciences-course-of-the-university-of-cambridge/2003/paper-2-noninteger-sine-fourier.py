"""Illustrate a noninteger sine's periodic extension and Fourier partial sums."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def main():
    plt.rcParams.update({'font.size':11, 'figure.facecolor':'white', 'axes.facecolor':'white'})
    a=0.5
    x=np.linspace(-1.23*np.pi,1.23*np.pi,3500)
    wrapped=(x+np.pi)%(2*np.pi)-np.pi
    target=np.sin(a*wrapped)
    target[np.abs(np.abs(x)-np.pi)<0.012]=np.nan
    fig,ax=plt.subplots(figsize=(7.7,4.5),dpi=120,layout='constrained')
    ax.plot(x,target,color='#333333',lw=2.3,label='Periodic extension')
    for number,color in [(5,'#bc682a'),(40,'#227ca6')]:
        n=np.arange(1,number+1)[:,None]
        bn=2*(-1.0)**(n+1)*n*np.sin(np.pi*a)/(np.pi*(n*n-a*a))
        partial=np.sum(bn*np.sin(n*x),axis=0)
        ax.plot(x,partial,color=color,lw=1.3,label=f'{number} sine modes')
    for boundary in [-np.pi,np.pi]:
        ax.axvline(boundary,color='0.65',ls='--',lw=.9)
        ax.scatter([boundary],[0],color='black',s=27,zorder=6)
    ax.axhline(0,color='0.6',lw=.8)
    ax.set(xticks=[-np.pi,0,np.pi],xticklabels=[r'$-\pi$','0',r'$\pi$'],xlabel='x',ylabel='Function / partial sum',ylim=(-1.32,1.32),xlim=(x[0],x[-1]),title=r'$\sin(x/2)$ on one period, then repeated')
    ax.legend(loc='upper center',fontsize=10,ncol=3)
    ax.grid(alpha=.16)
    fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
    plt.close(fig)

if __name__=='__main__':main()
