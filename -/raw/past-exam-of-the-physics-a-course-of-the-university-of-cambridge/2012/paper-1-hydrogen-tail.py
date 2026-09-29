"""Original normalized hydrogen radial probability. Python 3.14; output cwd."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    u=np.linspace(0,7,1600);density=4*u*u*np.exp(-2*u)
    fig,ax=plt.subplots(figsize=(7.2,4.1),layout='constrained',facecolor='white')
    ax.plot(u,density,lw=2,color='#2166ac',label=r'$a_0p_r=4u^2e^{-2u}$')
    ax.fill_between(u,0,density,where=u>=2,color='#dd8452',alpha=.45,label=r'$P(r>2a_0)=13e^{-4}\approx0.238$')
    ax.axvline(2,color='#a44a22',ls='--',lw=1.2)
    ax.text(2.08,.37,'Classical turning radius',rotation=90,va='center',fontsize=10,color='#8b3f20')
    ax.set(xlabel=r'$u=r/a_0$',ylabel='Probability per unit dimensionless radius',xlim=(0,6),ylim=(0,.61),title='Ground-state hydrogen: a finite tail beyond the classical region')
    ax.grid(alpha=.2);ax.legend(frameon=False,loc='upper right',fontsize=9)
    fig.savefig('paper-1-hydrogen-tail.png',dpi=165,facecolor='white');plt.close(fig)

if __name__=='__main__':main()
