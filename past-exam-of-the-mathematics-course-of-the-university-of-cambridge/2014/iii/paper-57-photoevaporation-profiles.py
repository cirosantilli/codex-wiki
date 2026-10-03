"""Generate the Paper 57 sketches; tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from the desired output directory. Respect the caller's MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
    x=np.geomspace(.03,1e3,1200)
    wind=np.where(x<1,1,x**-.5)
    sigma=np.zeros_like(x);outer=x>=1
    sigma[outer]=1-(1+.5*np.log(x[outer]))/np.sqrt(x[outer])
    plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
    fig,axes=plt.subplots(1,2,figsize=(10,4.4),dpi=100,facecolor='white')
    for eta,color in [(1,'#155d8b'),(1.5,'#b55b16')]:
        axes[0].semilogx(x,eta-wind,color=color,lw=2.2,label=rf'$\dot M_d/\dot M_w={eta:g}$')
        axes[0].axhline(eta,color=color,ls=':',lw=1)
    axes[0].set_title('Inward accretion flux')
    axes[0].set_ylabel(r'$F_{\rm acc}/\dot M_w$')
    axes[0].set_ylim(-.04,1.68)
    axes[0].legend(loc='upper left',frameon=False)
    axes[0].text(.055,.13,r'Flat inside $r_g$',fontsize=10)
    axes[1].semilogx(x,sigma,color='#155d8b',lw=2.2)
    axes[1].axhline(1,color='#6c6c6c',ls=':',lw=1)
    axes[1].set_title(r'Surface density: $\dot M_d=\dot M_w$')
    axes[1].set_ylabel(r'$3\pi\nu\Sigma/\dot M_w$')
    axes[1].set_ylim(-.04,1.08)
    axes[1].text(.055,.14,'Empty inner disk',fontsize=10)
    axes[1].text(.055,.55,'Zero slope at the wind edge',fontsize=9)
    for ax in axes:
        ax.axvline(1,color='#777777',ls='--',lw=1)
        ax.set_xlabel(r'Radius $r/r_g$ (logarithmic scale)')
        ax.set_xlim(.03,1e3)
        ax.grid(axis='y',alpha=.18)
    fig.subplots_adjust(left=.075,right=.985,bottom=.16,top=.87,wspace=.25)
    fig.savefig(Path.cwd()/'paper-57-photoevaporation-profiles.png',dpi=100,facecolor='white',transparent=False)
    plt.close(fig)

if __name__=='__main__':main()
