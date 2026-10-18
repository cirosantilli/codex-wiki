"""Original finite-size phonon population plot; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

L=180e-9;a=.409e-9;theta=215.;hbar=1.054571817e-34;kB=1.380649e-23
N=4*(L/a)**3;qD=(6*np.pi**2*4/a**3)**(1/3);v=kB*theta/(hbar*qD);T1=2*np.pi*hbar*v/(L*kB)
# Integer periodic-box wavevectors, with all signs and three polarizations.
nmax=80;vindex=np.arange(nmax+1);i,j,k=np.meshgrid(vindex,vindex,vindex,indexing='ij');s=i*i+j*j+k*k
weights=np.where(i==0,1,2)*np.where(j==0,1,2)*np.where(k==0,1,2)
mask=(s>0)&(s<=nmax*nmax);deg=np.bincount(s[mask],weights=weights[mask],minlength=nmax*nmax+1)*3
shells=np.flatnonzero(deg);energies=T1*np.sqrt(shells);T=np.geomspace(.02,2,220)
discrete=np.array([np.sum(deg[shells]/np.expm1(np.minimum(energies/t,700))) for t in T]);bulk=18*1.202056903159594*N*(T/theta)**3
fig,ax=plt.subplots(figsize=(9,5.3),layout='constrained',facecolor='white')
ax.loglog(T,bulk,lw=2.3,color='#2563eb',label='Bulk Debye continuum: proportional to T³')
ax.loglog(T,discrete,lw=2.3,color='#c2410c',label='Illustrative discrete periodic cube')
ax.axvline(T1,color='#64748b',ls='--',lw=1.2,label=f'First periodic-box quantum: {T1:.3f} K')
ax.set(xlabel='Temperature (K)',ylabel='Expected thermal phonon number',title='180 nm silver cube: finite size suppresses the lowest excitations',ylim=(1e-10,2e4))
ax.text(.027,2e2,'Three equal acoustic speeds;\nrigid translation excluded.\nBoundary conditions set the actual spectrum.',fontsize=10,color='#334155')
ax.grid(alpha=.18,which='both');ax.legend(loc='lower right',fontsize=9)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=140,facecolor='white')
