"""Logistic phase portrait. Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Writes only paper-2-logistic.png to the caller's CWD; honors MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    fig,axes=plt.subplots(2,1,figsize=(8,5.8),gridspec_kw={'height_ratios':[1,2.5]},constrained_layout=True,facecolor='white')
    ax=axes[0]
    ax.axhline(0,color='#666666',lw=1)
    for start,end in [(-.55,-1.05),(.25,.75),(1.85,1.35)]:
        ax.annotate('',xy=(end,0),xytext=(start,0),arrowprops={'arrowstyle':'->','lw':2,'color':'#2563a6'})
    ax.scatter([0],[0],s=80,facecolors='white',edgecolors='#222222',zorder=5)
    ax.scatter([1],[0],s=80,color='#222222',zorder=5)
    ax.text(0,.25,'0: unstable',ha='center',fontsize=10)
    ax.text(1,.25,'1: stable',ha='center',fontsize=10)
    ax.set(xlim=(-1.4,2.2),ylim=(-.2,.7),yticks=[],xlabel='State x',title=r'Logistic phase line: $\dot x=x(1-x)$')
    for side in ['top','right','left']:
        ax.spines[side].set_visible(False)
    t=np.linspace(-6,6,500)
    for x0,color in [(.15,'#2563a6'),(.5,'#ca671d'),(.85,'#3f874e')]:
        x=x0*np.exp(t)/(1-x0+x0*np.exp(t))
        axes[1].plot(t,x,lw=2,color=color,label=f'x(0) = {x0}')
        axes[1].scatter([0],[x0],color=color,s=25)
    axes[1].axhline(0,color='#666666',lw=1,ls=':')
    axes[1].axhline(1,color='#666666',lw=1,ls=':')
    axes[1].set(xlim=(-6,6),ylim=(-.05,1.05),xlabel='Time t',ylabel='State x(t)',title='Trajectories between the two equilibria')
    axes[1].legend(loc='upper left',fontsize=9)
    axes[1].grid(alpha=.2)
    for ax in axes:
        ax.set_facecolor('white')
    fig.savefig(Path.cwd()/'paper-2-logistic.png',dpi=150,facecolor='white',transparent=False)
    plt.close(fig)


if __name__=='__main__':
    main()
