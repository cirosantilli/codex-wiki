"""Original characteristic and entropy-solution sketches; output PNG to CWD."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    tstar=np.log(2.)
    fig,axes=plt.subplots(1,3,figsize=(12,3.7),layout='constrained')
    for t in [0,.3,.6]:
        height=2*np.exp(-t);left=1-height
        axes[0].plot([-1.8,left,0,1],[height,height,0,0],label=f't = {t:g}')
    axes[0].plot([-1.8,0,0,1],[1,1,0,0],ls='--',color='black',label='t = log(2)')
    axes[0].set(title='Decay and steepening',xlabel='x',ylabel='u',xlim=(-1.8,.8),ylim=(-.06,2.1))
    axes[0].legend(fontsize=8)
    ts=np.linspace(0,tstar,151)
    for initial in np.linspace(-1.7,.6,24):
        u0=2 if initial<=-1 else -2*initial if initial<=0 else 0
        xs=initial+u0*(1-np.exp(-ts))
        axes[1].plot(xs,ts,lw=.9,color=plt.cm.viridis((initial+1.7)/2.3))
    axes[1].scatter([0],[tstar],color='black',zorder=3)
    axes[1].set(title='Characteristics meet at first shock',xlabel='x',ylabel='t',xlim=(-1.4,.6),ylim=(0,tstar*1.04))
    for t in [tstar,1.,1.5]:
        s=.5-np.exp(-t);height=2*np.exp(-t)
        axes[2].plot([-1.8,s,s,1],[height,height,0,0],label=f't = {t:.3g}')
    axes[2].set(title='Entropy shock moves right',xlabel='x',ylabel='u',xlim=(-.5,.7),ylim=(-.04,1.06))
    axes[2].legend(fontsize=8)
    for ax in axes:ax.grid(alpha=.2)
    fig.savefig(Path.cwd()/'2011-damped-burgers-shock.png',dpi=120,facecolor='white')
    plt.close(fig)


if __name__=='__main__':main()
