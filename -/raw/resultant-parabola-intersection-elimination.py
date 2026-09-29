"""Original elimination/projection example; write PNG to the current directory."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size':12,'figure.facecolor':'white','axes.facecolor':'white'})
    fig,(ax,bx)=plt.subplots(1,2,figsize=(10.6,4.9),layout='constrained')
    x=np.linspace(-1.7,1.7,600)
    ax.plot(x,x*x,color='#1979a2',lw=2.5,label=r'$F=0:\ y=x^2$')
    ax.plot(x,2-x*x,color='#c47825',lw=2.5,label=r'$G=0:\ y=2-x^2$')
    ax.scatter([-1,1],[1,1],s=70,color='#7053a0',zorder=5)
    for xx in [-1,1]:
        ax.plot([xx,xx],[-.50,1],color='#7053a0',ls='--',lw=1.5)
        ax.scatter([xx],[-.50],marker='v',color='#7053a0',s=40)
        ax.annotate(f'({xx}, 1)',(xx,1),xytext=(14,15),textcoords='offset points',fontsize=11)
    ax.axhline(-.50,color='#6e7b84',lw=1)
    ax.text(-1.6,-.78,'Keep each intersection\'s x-coordinate',fontsize=10,color='#7053a0')
    ax.set(xlim=(-1.7,1.7),ylim=(-1.05,3.05),xlabel=r'$x$',ylabel=r'$y$',
           title='Two equations must vanish at the same point')
    ax.legend(loc='upper center',fontsize=10);ax.grid(alpha=.15)
    bx.plot(x,2*x*x-2,color='#7053a0',lw=2.6,
            label=r'$R(x)=\mathrm{Res}_y(F,G)=2(x^2-1)$')
    bx.axhline(0,color='#6e7b84',lw=1)
    bx.scatter([-1,1],[0,0],s=70,color='#7053a0',zorder=5)
    bx.text(-1.5,3.0,r'$x=-1,1$',fontsize=15,color='#7053a0')
    bx.text(-1.5,2.35,r'Back-substitute: $y=x^2=1$',fontsize=12)
    bx.annotate('A root gives an x-coordinate,\nnot a full solution pair.',(-1,0),
                xytext=(-1.5,-2.95),fontsize=11,
                arrowprops={'arrowstyle':'->','color':'#7053a0'})
    bx.set(xlim=(-1.7,1.7),ylim=(-3.45,4.2),xlabel=r'$x$',ylabel=r'Resultant $R(x)$',
           title='Eliminating y leaves one polynomial equation')
    bx.legend(loc='upper center',fontsize=10);bx.grid(alpha=.15)
    fig.savefig(Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white')
    plt.close(fig)


if __name__=='__main__':main()
