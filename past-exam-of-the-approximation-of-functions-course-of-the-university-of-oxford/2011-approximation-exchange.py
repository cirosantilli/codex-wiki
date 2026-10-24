"""Original explanatory plots; write the PNG to the working directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    x=np.linspace(-1,1,1001)
    a=np.sinh(1.)
    b=(np.cosh(1.)+a-a*np.log(a))/2
    err=(np.cosh(1.)-a+a*np.log(a))/2
    fig,axes=plt.subplots(1,3,figsize=(13,3.8),layout='constrained')
    axes[0].plot(x,np.exp(x),label=r'$e^x$')
    axes[0].plot(x,a*x+b,label='Best affine approximation')
    axes[0].set_title('Uniformly best line')
    axes[0].legend(fontsize=8)
    axes[1].plot(x,np.exp(x)-a*x-b,color='tab:purple')
    axes[1].axhline(err,color='0.5',ls='--')
    axes[1].axhline(-err,color='0.5',ls='--')
    nodes=np.array([-1,np.log(a),1])
    axes[1].scatter(nodes,np.exp(nodes)-a*nodes-b,color='tab:red',zorder=3)
    axes[1].set_title('Three alternating extreme errors')
    axes[1].set_ylabel('Approximation error')
    xp=np.array([-1,0,.2,.4,.6,1]);yp=np.array([-2,1,-1,1,-1,-1])
    axes[2].plot(xp,yp,label='Old error (piecewise linear)')
    q=3/64-25/32*x*(x-.4)
    axes[2].plot(x,np.interp(x,xp,yp)-q,label='Error after printed exchange',ls='--')
    ref=np.array([0,.2,.4,.6])
    axes[2].scatter(ref,[1,-1,1,-1],s=26,color='black',zorder=3,label='Old reference points')
    axes[2].scatter([-1],[-2],color='tab:red',zorder=4)
    axes[2].annotate(r'$\eta$',(-1,-2),xytext=(-.85,-1.85))
    axes[2].set_title('Exterior exchange can decrease height')
    axes[2].legend(fontsize=7,loc='lower right')
    for ax in axes:
        ax.set_xlabel('x');ax.grid(alpha=.2)
    fig.savefig(Path.cwd()/'2011-approximation-exchange.png',dpi=120,facecolor='white')
    plt.close(fig)


if __name__=='__main__':
    main()
