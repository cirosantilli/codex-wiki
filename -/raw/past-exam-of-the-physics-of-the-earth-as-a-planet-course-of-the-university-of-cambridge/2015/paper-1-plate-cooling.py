from pathlib import Path
from math import erf
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,ax=plt.subplots(1,2,figsize=(9,3.8),layout='constrained')
z=np.linspace(0,6,350)
for age in [1,4,9]:ax[0].plot([erf(v/(2*np.sqrt(age))) for v in z],z,label=fr'$\tau/\tau_0={age}$',lw=2)
ax[0].axvline(erf(.5),ls=':',color='gray');ax[0].invert_yaxis();ax[0].set(xlabel=r'$(T-T_s)/(T_m-T_s)$',ylabel=r'depth $z/\sqrt{\kappa\tau_0}$',title='Illustrative half-space geotherms');ax[0].legend(fontsize=9);ax[0].grid(alpha=.2)
x=np.linspace(0,10,200);ax[1].plot(x,np.sqrt(x),lw=2,color='#2469a0');ax[1].plot([1,4,9],[1,2,3],'o',color='#9e4a10')
ax[1].set(xlabel=r'age $\tau/\tau_0$',ylabel=r'isotherm depth $z_*/z_*(\tau_0)$',title=r'Fixed isotherm: $z_*\propto\sqrt{\tau}$');ax[1].grid(alpha=.2)
fig.suptitle('Thermal illustration; isotherm depth is not a measured elastic thickness',fontsize=11)
fig.savefig(Path(__file__).stem+'.png',dpi=140,facecolor='white')
