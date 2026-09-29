"""Original subthreshold step-scattering diagram; matching PNG output in CWD."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

k,kap=1.5,1.
r=(k-1j*kap)/(k+1j*kap)
c=2*k/(k+1j*kap)
xn,xp=np.linspace(-7,0,1200),np.linspace(0,4,600)
yn=np.exp(1j*k*xn)+r*np.exp(-1j*k*xn)
yp=c*np.exp(-kap*xp)
fig,axes=plt.subplots(2,1,figsize=(8,5.2),sharex=True,layout='constrained')
ax=axes[0]
ax.plot([-7,0,0,4],[0,0,k*k+kap*kap,k*k+kap*kap],color='.2',lw=2,label='potential')
ax.axhline(k*k,color='#b24c29',ls='--',label='incident energy')
ax.set(ylabel=r'Energy, $\hbar^2/(2m)=1$',ylim=(-.4,4),title='Complete reflection with a nonzero evanescent tail')
ax.legend(loc='lower left')
ax=axes[1]
ax.plot(xn,yn.real,color='#1769aa',label=r'$\mathrm{Re}\,\psi(x)$ at a fixed time')
ax.plot(xp,yp.real,color='#1769aa')
ax.plot(xp,np.abs(c)*np.exp(-kap*xp),':',color='#168347',label='amplitude envelope in barrier')
ax.plot(xp,-np.abs(c)*np.exp(-kap*xp),':',color='#168347')
ax.annotate('',(-6.6,-1.8),(-6.6+2*np.pi/k,-1.8),arrowprops={'arrowstyle':'<->'})
ax.text(-5.7,-1.6,r'$\lambda=2\pi/k$',fontsize=10)
ax.annotate('',(0,-1.1),(1/kap,-1.1),arrowprops={'arrowstyle':'<->'})
ax.text(.05,-.9,r'$1/\kappa$',fontsize=10)
ax.set(xlabel='Position x (arbitrary length units)',ylabel='Wave-function amplitude',ylim=(-2.2,2.2),xlim=(-7,4))
ax.legend(loc='upper right',fontsize=9)
for ax in axes:
    ax.axvline(0,color='.6',lw=.6)
    ax.grid(alpha=.15)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white')
plt.close(fig)
