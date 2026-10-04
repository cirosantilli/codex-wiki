"""Finite-lock sketches; Python 3.14 with root-pinned NumPy and Matplotlib.

Write the PNG basename to caller CWD, respecting MPLCONFIGDIR.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    F=1.;c0=1.;h0=1.;x0=1.;t=.6
    kF=np.sqrt(2)*F;cf=4*c0/(4+kF);uf=kF*cf
    xi_tail=uf-cf;front=uf*t
    x=np.linspace(-x0,front,500)
    xi=x/t
    c=np.where(xi<=-c0,c0,np.where(xi<=xi_tail,(4*c0-xi)/5,cf))
    h=h0*(c/c0)**2
    fig,axes=plt.subplots(1,2,figsize=(8.2,3.5),dpi=130,facecolor='white')
    ax=axes[0]
    ax.fill_between(x,0,h,color='#c7e0f1');ax.plot(x,h,color='#176dab',lw=2)
    ax.plot([front,front],[0,h[-1]],color='#176dab',lw=2)
    ax.plot([-1,0,0],[1,1,0],ls='--',color='#89949e',lw=1)
    ax.axvline(-1,color='#4b5862',lw=2);ax.axhline(0,color='#4b5862',lw=1)
    ax.annotate('Rarefaction',(-.35,.8),xytext=(-.3,1.15),fontsize=9,
                arrowprops={'arrowstyle':'->','color':'#555f68'})
    ax.text(-1.02,.17,'Wall',rotation=90,va='bottom',ha='right',fontsize=9)
    ax.set(xlim=(-1.2,1),ylim=(0,1.4),xlabel=r'$x/x_0$',ylabel=r'$h/h_0$',
           title='Before the fan reaches the wall')
    ax.text(.05,.04,r'$t<x_0/c_0$',transform=ax.transAxes,fontsize=10)
    ax=axes[1];length=4.;height=np.sqrt(x0/length);nose=length-x0
    ax.fill_between([-x0,nose],0,height,color='#c7e0f1')
    ax.plot([-x0,nose,nose],[height,height,0],color='#176dab',lw=2)
    ax.axvline(-x0,color='#4b5862',lw=2);ax.axhline(0,color='#4b5862',lw=1)
    for xx in [-.6,.4,1.4,2.4]:
        arrow=.45*(xx+x0)/length
        ax.annotate('',(xx+arrow,.22),(xx,.22),arrowprops={'arrowstyle':'->','color':'#426c8b'})
    ax.annotate('',(nose,.7),(-x0,.7),arrowprops={'arrowstyle':'<->','color':'#555f68'})
    ax.text(1.,.75,r'$\ell=x_f+x_0$',ha='center',fontsize=10)
    ax.text(1.,.38,r'$\bar h=h_0\sqrt{x_0/\ell}$',ha='center',fontsize=10)
    ax.set(xlim=(-1.3,3.4),ylim=(0,1.4),xlabel=r'$x/x_0$',ylabel=r'$h/h_0$',
           title='Late-time uniform-depth box')
    ax.text(.06,.88,r'$\ell\propto t^{4/5}$',transform=ax.transAxes,fontsize=11)
    fig.tight_layout()
    fig.savefig(Path.cwd()/'paper-83-finite-lock.png',facecolor='white',transparent=False)
    plt.close(fig)


if __name__=='__main__':main()
