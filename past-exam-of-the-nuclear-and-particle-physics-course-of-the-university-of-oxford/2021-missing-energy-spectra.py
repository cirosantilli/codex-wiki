"""Original normalized schematic spectra, with explicit spin approximations.
Python 3.14, numpy 2.3.5, matplotlib 3.10.7.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 12, 'figure.facecolor':'white', 'savefig.facecolor':'white'})
z = np.linspace(0,1,5001)
dz=z[1]-z[0]
g=5/3-3*z*z+4*z**3/3
weights=g.copy(); weights[[0,-1]]*=.5
summed=np.convolve(weights,weights)*dz
y=1-np.arange(summed.size)*dz/2
order=np.argsort(y)
y=y[order]; tau=2*summed[order]
tau/=np.trapezoid(tau,y)
x=np.linspace(0,1,2001)
beta=np.sqrt(1-4*80.379**2/200**2)
ww=np.maximum(0,2/beta-4*np.abs(x-.5)/beta**2)
fig, ax=plt.subplots(figsize=(9,4.8), layout='constrained')
ax.plot(y,tau,lw=2.5,color='#275c96',label=r'$\tau^+\tau^-$: high boost, unpolarized independent decays')
ax.plot(x,ww,lw=2.5,color='#b45a20',label=r'$W^+W^-$: $\sqrt{s}=200$ GeV, independent isotropic decays')
ax.axvline(.65,color='#275c96',ls=':',lw=1.2)
ax.text(.66,.35,r'$\langle y\rangle_\tau=0.65$',color='#275c96')
ax.annotate(r'$W$ threshold limit: $\delta(y-1/2)$',xy=(.5,3.35),xytext=(.08,4.1),arrowprops={'arrowstyle':'->','color':'#78421f'},color='#78421f',fontsize=11)
ax.set(xlim=(0,1),ylim=(0,4.5),xlabel=r'Missing-energy fraction $y=E_{\rm miss}/\sqrt{s}$',ylabel='Normalized density',title='Shape comparison; no detector cuts or radiative effects')
ax.grid(alpha=.18)
ax.legend(loc='upper left',fontsize=9.5,bbox_to_anchor=(0,-.19))
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=115,facecolor='white')
plt.close(fig)
