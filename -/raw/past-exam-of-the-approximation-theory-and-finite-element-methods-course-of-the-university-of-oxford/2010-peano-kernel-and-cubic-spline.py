"""Original plots of a Peano kernel and normalized cubic B-spline; CWD output."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    t=np.linspace(-1,1,1001)
    kernel=np.where(t<0,-(t+1)**2/8,np.where(t<=.25,-(1+2*t+3*t*t)/8,-3*(1-t)**2/8))
    s=np.linspace(-.3,4.3,1001)
    spline=sum(c*np.maximum(s-j,0)**3 for j,c in enumerate([1,-4,6,-4,1]))/6
    fig,axes=plt.subplots(1,2,figsize=(10,3.5),layout='constrained')
    axes[0].plot(t,kernel);axes[0].fill_between(t,kernel,0,alpha=.2)
    axes[0].axhline(0,color='0.5',lw=.7)
    axes[0].set(xlabel='t',ylabel='K(t)',title='Exact kernel mass: −13/96')
    axes[1].plot(s,spline)
    axes[1].scatter(range(5),[0,1/6,2/3,1/6,0],color='tab:red',zorder=3)
    axes[1].set(xlabel='x / h',ylabel='B₃(x / h)',title='Four knot intervals; nodal values sum to 1')
    for ax in axes:ax.grid(alpha=.2)
    fig.savefig(Path.cwd()/'2010-peano-kernel-and-cubic-spline.png',dpi=120,facecolor='white')
    plt.close(fig)


if __name__=='__main__':main()
