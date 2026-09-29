"""Original solution diagram; Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Run from the mirrored _media directory; output is a basename in cwd.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})

k=np.linspace(-1,1,700);c=1.4*k;f=.12+0*k;V=.16;lo=(c+f)/2-np.sqrt(((c-f)/2)**2+V*V);hi=(c+f)/2+np.sqrt(((c-f)/2)**2+V*V);fig,axs=plt.subplots(1,2,figsize=(8.8,3.8));axs[0].plot(k,c,'--',color='.6',lw=1,label='Unhybridized conduction band');axs[0].plot(k,f,':',color='.5',label='Localized level');axs[0].plot(k,lo,lw=2,color='royalblue');axs[0].plot(k,hi,lw=2,color='royalblue',label='Hybridized bands');axs[0].axhline(0,color='black',lw=.7);axs[0].set(xlabel='Momentum (illustrative units)',ylabel='Energy (illustrative units)',title='A narrow, heavy hybridized band');axs[0].legend(fontsize=7)
for sign,label in [(-1,'Spin up'),(1,'Spin down')]:axs[1].plot(k,k*k+sign*.24,lw=2,label=label)
axs[1].axhline(.5,color='black',ls=':',label='Common chemical potential');axs[1].set(xlabel='Momentum (illustrative units)',ylabel='Energy (illustrative units)',title='Stoner mean-field exchange splitting');axs[1].legend(fontsize=8)
for ax in axs:ax.grid(alpha=.15)
fig.tight_layout();fig.subplots_adjust(bottom=.18);fig.text(.5,.015,'Qualitative model diagrams, not measured spectra or fitted exam parameters.',ha='center',fontsize=9)

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
