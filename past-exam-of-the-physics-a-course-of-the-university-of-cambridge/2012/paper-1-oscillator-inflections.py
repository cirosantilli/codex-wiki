"""Original oscillator eigenfunctions. Python 3.14, numpy, matplotlib; output cwd."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def psi(n,x):
    p=np.pi**(-.25)*np.exp(-x*x/2)
    return p if n==0 else np.sqrt(2)*x*p if n==1 else (2*x*x-1)*p/np.sqrt(2)


def main():
    xx=np.linspace(-4,4,1600)
    fig,axs=plt.subplots(3,1,figsize=(8,7.2),sharex=True,layout='constrained',facecolor='white')
    for n,ax in enumerate(axs):
        ax.plot(xx,psi(n,xx),color='#2166ac',lw=1.7)
        turn=np.array([-1.,1.])*np.sqrt(2*n+1)
        nodes=[] if n==0 else [0.] if n==1 else [-1/np.sqrt(2),1/np.sqrt(2)]
        ax.scatter(turn,psi(n,turn),color='#d95f02',s=48,zorder=4,label='Turning-point inflections')
        if nodes:ax.scatter(nodes,psi(n,np.array(nodes)),color='#009e73',s=50,marker='D',zorder=4,label='Node inflections')
        for x in turn:ax.axvline(x,color='#d95f02',ls=':',alpha=.55)
        ax.axhline(0,color='#999999',lw=.7)
        ax.set(ylabel=fr'$\sqrt{{b}}\,\psi_{n}$',title=fr'$n={n}$, $E/\hbar\omega={n+.5}$',ylim=(-.68,.9))
        ax.grid(alpha=.15)
        ax.legend(frameon=True,facecolor='white',edgecolor='white',framealpha=1,fontsize=9,loc='upper right')
    axs[-1].set(xlabel=r'$\xi=x/b$',xlim=(-3.8,3.8))
    fig.savefig('paper-1-oscillator-inflections.png',dpi=155,facecolor='white')
    plt.close(fig)

if __name__=='__main__':main()
