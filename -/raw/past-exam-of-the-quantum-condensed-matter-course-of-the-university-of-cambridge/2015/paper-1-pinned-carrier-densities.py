"""Original solution diagram; Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Run from the mirrored _media directory; output is a basename in cwd.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})

# Normalized Fermi-Dirac F_{1/2}: quadrature after x=s²; no scipy dependency.
nodes,weights=np.polynomial.legendre.leggauss(200)
def F(eta):
 if eta>25:return 4/(3*np.sqrt(np.pi))*eta**1.5*(1+np.pi**2/(8*eta**2)+7*np.pi**4/(640*eta**4))
 upper=np.sqrt(max(eta,0)+42);s=.5*upper*(nodes+1);return 4/np.sqrt(np.pi)*.5*upper*np.sum(weights*s*s*np.exp(-np.logaddexp(0,s*s-eta)))
f0=F(0);t=np.linspace(.015,3,550);n=f0*t**1.5;p=t**1.5*np.array([F(-1/x) for x in t]);ratio=f0*np.array([F(-1/x)*np.exp(1/x) for x in t]);u=np.linspace(.005,2.5,500);positive=3*np.sqrt(np.pi)/4*u**1.5*np.array([F(1/x) for x in u]);fig,axs=plt.subplots(1,3,figsize=(12.8,4));axs[0].plot(t,n,label='Electrons n',lw=2);axs[0].plot(t,p,label='Holes p',lw=2);axs[0].set(xlabel='kBT/Eg',ylabel='Density / [2(mEg/2πℏ²)³ᐟ²]',title='μ pinned to the conduction edge');axs[0].legend(fontsize=8);axs[1].plot(t,ratio,lw=2);axs[1].axhline(f0,color='.4',ls=':',label='Low-T limit f₀');axs[1].axhline(f0*f0,color='.6',ls='--',label='High-T limit f₀²');axs[1].set(xlabel='kBT/Eg',ylabel='np / classical mass-action prediction',title='Pauli statistics reduce the product',ylim=(.56,.79));axs[1].legend(fontsize=8);axs[2].plot(np.r_[0,u],np.r_[1,positive],lw=2);z=np.linspace(0,.35,100);axs[2].plot(z,1+np.pi*np.pi*z*z/8,'--',color='.5',label='Low-T quadratic rise');axs[2].set(xlabel='kBT/μ',ylabel='n(T)/n(0)',title='Fixed positive μ');axs[2].legend(fontsize=8)
for ax in axs:ax.grid(alpha=.15)
fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
