"""Original oscillator absorption graph; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Write only Path.cwd()/Path(__file__).with_suffix('.png').name.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
    g=.2
    x=np.linspace(0,2.2,1600)
    y=g*g*x*x/((1-x*x)**2+g*g*x*x)
    x1=(np.sqrt(4+g*g)-g)/2
    x2=(np.sqrt(4+g*g)+g)/2
    fig,ax=plt.subplots(figsize=(7.4,4.6),dpi=120,facecolor='white')
    ax.set_facecolor('white')
    ax.plot(x,y,color='#246797',lw=2.2)
    ax.hlines(.5,0,x2+.16,color='#6f7d86',ls='--',lw=1)
    ax.vlines([x1,x2],0,.5,color='#bd6c2e',ls='--',lw=1)
    ax.scatter([x1,x2],[.5,.5],s=38,color='#bd6c2e',zorder=4)
    ax.scatter([1],[1],s=38,color='#246797',zorder=4)
    ax.annotate(r'$\omega_0$',(1,1),xytext=(16,8),textcoords='offset points',fontsize=13)
    ax.annotate(r'$\omega_1$',(x1,0),xytext=(-4,-11),textcoords='offset points',
                ha='right',va='top',fontsize=13,color='#9d4f1a')
    ax.annotate(r'$\omega_2$',(x2,0),xytext=(4,-11),textcoords='offset points',
                ha='left',va='top',fontsize=13,color='#9d4f1a')
    ax.annotate('',xy=(x2,.68),xytext=(x1,.68),
                arrowprops={'arrowstyle':'<->','color':'#9d4f1a','lw':1.3})
    ax.annotate(r'$\Delta\omega=\gamma$',((x1+x2)/2,.68),xytext=(50,15),
                textcoords='offset points',fontsize=12,color='#9d4f1a')
    ax.set(xlim=(0,2.2),ylim=(0,1.12),xticks=[0,.5,1.5,2],yticks=[0,.5,1])
    ax.set_xlabel(r'Angular frequency $\omega/\omega_0$',labelpad=28)
    ax.set_ylabel(r'Average power $\overline{P}/\overline{P}_{\max}$')
    ax.set_title(r'Absorbed power: $\gamma/\omega_0=0.2$',pad=12)
    ax.spines[['top','right']].set_visible(False)
    ax.grid(axis='y',alpha=.14)
    fig.subplots_adjust(left=.13,right=.97,bottom=.23,top=.87)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,
                facecolor='white',transparent=False,
                metadata={'Software':'codex-wiki oscillator power graph'})
    plt.close(fig)


if __name__=='__main__':
    main()
