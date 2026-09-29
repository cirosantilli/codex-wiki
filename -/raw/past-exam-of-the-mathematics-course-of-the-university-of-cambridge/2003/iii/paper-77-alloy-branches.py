"""Alloy concentration and speed branches; Python 3.14, NumPy/Matplotlib root deps.
Writes its opaque PNG basename to caller CWD; respects caller MPLCONFIGDIR.
"""
from math import erfc, exp, sqrt, pi
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def inverse_F(z):
    if z < -20:
        return 0.0
    if z > 20:
        zz=z*z
        return 1/(1-1/(2*zz)+3/(4*zz*zz)-15/(8*zz**3))
    return 1/(sqrt(pi)*z*exp(z*z)*erfc(z))

def finite_concentration(lam,eps=.06,k=.3):
    if abs(lam)<1e-9:
        return eps/(1+k*eps)
    a=inverse_F(-lam/eps)
    return a/((1-k)+k*a-inverse_F(lam))

lam=np.linspace(-2.5,1.5,1200)
outer=np.zeros_like(lam)
negative=lam<0
r=-lam[negative]
H=np.array([sqrt(pi)*x*exp(x*x)*erfc(-x) for x in r])
outer[negative]=H/(1+H)
K=sqrt(pi)  # delta*ell=1, with m*Cs=1, below the multiplicity threshold2.
Sigma=-2*outer-K*lam
fig,axes=plt.subplots(1,2,figsize=(10.8,4.2),layout='constrained')
axes[0].plot(lam,outer,label=r'$\epsilon\to0$ outer solution',lw=2)
axes[0].plot(lam,[finite_concentration(x) for x in lam],ls='--',label=r'finite $\epsilon=0.06$',lw=1.6)
axes[0].axvline(0,color='.7',lw=.8)
axes[0].set(xlabel=r'$\lambda$',ylabel=r'$C_a/C_s$',title='Liquid interface concentration',ylim=(-.02,1.02))
axes[0].legend(fontsize=9)
axes[1].plot(Sigma,lam,lw=2,color='#285b95')
imin=np.argmin(Sigma[negative]);minSigma=Sigma[negative][imin]
mid=minSigma/2
axes[1].axvspan(minSigma,0,alpha=.13,color='#c25445',label='three distinct speeds')
axes[1].axvline(mid,color='#c25445',ls=':',lw=1.3)
axes[1].axhline(0,color='.7',lw=.8)
axes[1].set(xlabel=r'$\Sigma/(mC_s)$',ylabel=r'$\lambda$',title=r'Speed branches: $\delta\ell/(mC_s)=1$',xlim=(-1.8,3),ylim=(-2.5,1.2))
axes[1].legend(fontsize=9)
for ax in axes:
    ax.grid(alpha=.17)
fig.savefig('paper-77-alloy-branches.png',dpi=135,facecolor='white',transparent=False)
