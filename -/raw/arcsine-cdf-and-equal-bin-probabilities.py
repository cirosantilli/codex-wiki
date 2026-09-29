"""Original arcsine CDF and integrated finite-bin masses; output PNG to cwd."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def cdf(x):return 2*np.arcsin(np.sqrt(x))/np.pi


def main():
    plt.rcParams.update({'font.size':12,'figure.facecolor':'white','axes.facecolor':'white'})
    fig,(ax,bx)=plt.subplots(1,2,figsize=(10.8,4.9),layout='constrained')
    x=np.linspace(0,1,1001)
    ax.plot(x,cdf(x),color='#74549b',lw=2.7,label='Arcsine')
    ax.plot(x,x,color='#2d8c96',ls='--',lw=2,label='Uniform')
    for u,v in [(.25,1/3),(.75,2/3)]:
        ax.plot([u,u],[0,v],color='#7c6b8e',ls=':',lw=1.3)
        ax.plot([0,u],[v,v],color='#7c6b8e',ls=':',lw=1.3)
        ax.scatter([u],[v],color='#74549b',s=40,zorder=5)
    ax.text(.12,.84,r'$F(3/4)-F(1/4)=1/3$',fontsize=14)
    ax.text(.12,.75,'Middle half of the interval',fontsize=10)
    ax.set(xlim=(0,1),ylim=(0,1),xlabel='x',ylabel=r'Cumulative probability $P(X\leq x)$',
           title='The CDF stays finite and continuous')
    ax.grid(alpha=.17);ax.legend(loc='lower right',fontsize=11)
    edges=np.linspace(0,1,11);mass=np.diff(cdf(edges));centers=(edges[:-1]+edges[1:])/2
    bx.bar(centers-.019,mass,width=.036,color='#8a6bad',label='Arcsine: integrated bins')
    bx.bar(centers+.019,np.full(10,.1),width=.036,color='#4b9da5',label='Uniform: 0.1 in every bin')
    bx.set_xticks(centers,[f'{j/10:.1f}–{(j+1)/10:.1f}' for j in range(10)],rotation=50,ha='right',fontsize=8)
    bx.text(.18,.232,'Each bin has width 0.1',fontsize=11)
    bx.set(xlim=(-.01,1.01),ylim=(0,.27),xlabel='Value interval',ylabel='Probability in the bin',
           title='Equal widths do not mean equal probability')
    bx.grid(axis='y',alpha=.17);bx.legend(loc='upper center',bbox_to_anchor=(.5,.82),fontsize=9)
    fig.savefig(Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white')
    plt.close(fig)


if __name__=='__main__':main()
