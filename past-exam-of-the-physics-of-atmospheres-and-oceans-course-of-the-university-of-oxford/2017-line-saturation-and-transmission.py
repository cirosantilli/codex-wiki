"""Original nonexponential band transmission and normalized line saturation; Python 3.14, numpy, matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
x=np.linspace(-5,5,4001)
phi=np.exp(-x*x)/np.sqrt(np.pi)
fig,axes=plt.subplots(1,2,figsize=(10.5,4.3),constrained_layout=True,facecolor='white')
for m,col in [(1,'#1864ab'),(10,'#d9480f'),(100,'#2b8a3e')]:
 axes[0].plot(x,np.exp(-m*phi),color=col,lw=2,label=f'mS / width = {m}')
axes[0].set(xlabel='Offset from line centre / Doppler width',ylabel='Monochromatic transmission',ylim=(-.03,1.04),title='A saturated core leaves transmitting wings')
axes[0].legend(frameon=False,fontsize=9,loc='lower left')
ms=np.linspace(0,50,501)
t=np.array([np.trapezoid(np.exp(-m*phi),x)/10 for m in ms]);meanphi=np.trapezoid(phi,x)/10
axes[1].plot(ms,t,lw=2.3,color='#1864ab',label='Average of monochromatic transmissions')
axes[1].plot(ms,np.exp(-ms*meanphi),lw=2,ls='--',color='.25',label='Exponential with initial mean attenuation')
axes[1].set(xlabel='Absorber path parameter',ylabel='Mean transmission in fixed spectral band',ylim=(-.02,1.04),title='Band averaging is not a single exponential')
axes[1].legend(frameon=False,fontsize=9,loc='lower left')
for ax in axes:ax.grid(alpha=.18)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white',transparent=False)
plt.close(fig)
