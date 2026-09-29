"""Asymptotic CDM spectrum sketch; opaque PNG to cwd only.
Python 3.14 / NumPy 2.3.5 / Matplotlib 3.10.7. The interpolant is
schematic, not a fitted cosmology or a nonlinear power spectrum.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    q=np.logspace(-3,3,1200)
    transfer=np.log1p(q)/q/np.sqrt(1+q*q)
    power=q*transfer**2/4  # D(z=1)^2, taking D(0)=1 in the matter approximation.
    plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.facecolor':'white'})
    fig,ax=plt.subplots(figsize=(10,4.2),dpi=100)
    ax.loglog(q,power,color='#0077a8',lw=2,label=r'$P_{\delta_c}(k,z=1)$, schematic normalization')
    lo=q[q<.15];hi=q[q>30]
    ax.loglog(lo,lo/4,'--',color='0.45',label=r'large-scale slope $k$')
    ax.loglog(hi,np.log(hi)**2/(4*hi**3),':',color='#b84922',lw=2,label=r'small-scale $k^{-3}\ln^2(k/k_{\rm eq})$')
    ax.axvline(1,color='0.4',ls='--',lw=1)
    ax.set_xlim(1e-3,1e3);ax.set_xlabel(r'$k/k_{\rm eq}$, where $k_{\rm eq}=\mathcal{H}_{\rm eq}$')
    ax.set_ylabel('Dimensional power (arbitrary units)')
    ax.set_title('Scale-invariant seed: equality turnover in the linear CDM power spectrum')
    ax.grid(alpha=.18);ax.legend(loc='lower left',fontsize=10)
    fig.text(.5,.025,'Illustrative interpolant T(q)=ln(1+q)/(q sqrt(1+q²)); asymptotes are the mathematical result.\nSubhorizon or comoving-density spectrum; ideal linear matter + radiation, without baryon or dark-energy effects.',ha='center',fontsize=9)
    fig.tight_layout(rect=[0,.085,1,1])
    fig.savefig(Path.cwd()/'paper-49-matter-spectrum.png',dpi=100,facecolor='white',transparent=False)
    plt.close(fig)

if __name__=='__main__':main()
