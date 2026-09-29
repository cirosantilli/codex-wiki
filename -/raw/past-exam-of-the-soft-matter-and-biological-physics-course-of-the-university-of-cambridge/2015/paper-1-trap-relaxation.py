"""Original generic-physics solution diagram; Python3.14.4,numpy2.3.5,matplotlib3.10.7.
Run from mirrored _media directory; save basename in cwd. No biological model.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
m=.02;gamma=1.;k=1.;roots=np.roots([m,gamma,k]);rs=max(roots);rf=min(roots);time=np.linspace(0,4,900);fig,axs=plt.subplots(1,2,figsize=(11,4.6))
for v0 in [0.,15.]:
 A=(v0-rf)/(rs-rf);B=(rs-v0)/(rs-rf);x=A*np.exp(rs*time)+B*np.exp(rf*time);axs[0].plot(time,x,lw=2,label='Illustrative initial v₀ = %g'%v0)
axs[0].plot(time,np.exp(-time),'--',color='black',label='Massless response x₀ exp(−kt/γ)');axs[0].set(xlabel='Time × k/γ',ylabel='Mean position / initial position',title='ε = km/γ² = 0.02; x₀ = 1');axs[0].legend(fontsize=8);axs[0].grid(alpha=.15)
f=np.geomspace(.01,100,400);axs[1].loglog(f,1/(1+f*f),lw=2);axs[1].axvline(1,color='.5',ls=':',label='Corner fc = k/(2πγ)');axs[1].set(xlabel='Frequency / corner frequency',ylabel='Position spectrum / low-frequency plateau',title='Generic harmonic-trap calibration spectrum');axs[1].legend(fontsize=9);axs[1].grid(which='both',alpha=.15);fig.text(.5,.015,'Dimensionless mechanical illustrations only; no motor parameters or step energetics are used.',ha='center',fontsize=9);fig.tight_layout(rect=(0,.05,1,1))

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
