"""Original damped oscillator reflection and lossless polariton dispersion."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
fig,axes=plt.subplots(1,2,figsize=(11,4.2),layout='constrained',facecolor='white')
TO=45.;LO=50.;eps=8.3;E=np.linspace(25,110,1500);gamma=.5
per=eps*(LO*LO-E*E-1j*gamma*E)/(TO*TO-E*E-1j*gamma*E);n=np.sqrt(per);R=abs((n-1)/(n+1))**2
ax=axes[0];ax.axvspan(TO,LO,color='#dfe9f1',label='negative ε without damping');ax.plot(E,R,color='#355a9b',lw=2)
for x,label in [(TO,'TO'),(LO,'LO')]:ax.axvline(x,color='#777',lw=.7,ls=':');ax.text(x,.98,label,ha='center',va='top',fontsize=9)
ax.set(xlabel='photon energy (meV)',ylabel='normal-incidence reflectivity',ylim=(0,1.05),title='A  Oscillator model, damping energy 0.5 meV');ax.legend(frameon=False,fontsize=9,loc='upper right')
ax=axes[1];q=np.linspace(0,4,1000);hbarc=197.3269804 # meV µm; q units 10^4 cm^-1 = 1 µm^-1
u=(hbarc*q)**2/eps;disc=np.sqrt((LO*LO+u)**2-4*u*TO*TO);upper=np.sqrt((LO*LO+u+disc)/2)
# Product of roots avoids cancellation at large wavevector.
lower=np.sqrt(np.divide(u*TO*TO,upper*upper))
ax.axhspan(TO,LO,color='#e7eff9',alpha=.7);ax.plot(q,lower,color='#355a9b',lw=2,label='lower transverse polariton');ax.plot(q,upper,color='#269572',lw=2,label='upper transverse polariton')
ax.axhline(LO,color='#bd7820',ls='--',label='longitudinal optical mode');ax.axhline(TO,color='#777',lw=.7,ls=':')
ax.set(xlabel='wavevector (10⁴ cm⁻¹)',ylabel='excitation energy (meV)',ylim=(0,95),title='B  LO is distinct from the upper polariton');ax.legend(frameon=False,fontsize=9,loc='lower right')
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white')
