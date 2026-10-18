"""Original analytic-model plots; Python 3.14, NumPy, Matplotlib. Output: CWD/basename.png."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
fig,axes=plt.subplots(1,2,figsize=(11,4.2),dpi=100,facecolor='white')
u=np.linspace(-3,3,1501);current=np.sign(u)*np.sqrt(np.maximum(u*u-1,0))
ax=axes[0];ax.plot(u,u,ls='--',color='#83909b',label='Normal-state line')
ax.plot(u,current,lw=2,color='#217cac',label='Ideal NIS, $T=0$')
for v in [-1,1]:ax.axvline(v,ls=':',lw=1,color='#a6aeb4')
ax.set(xlabel=r'$eV/\Delta$',ylabel=r'$eR_N I/\Delta$',title='Single-superconductor gap threshold',xlim=(-3,3),ylim=(-3,3));ax.legend(frameon=False,fontsize=10)
x=np.linspace(-4,4,2001);signed=np.sinc(x)
ax=axes[1];ax.plot(x,signed,ls='--',color='#bc672d',label='Signed coefficient')
ax.plot(x,abs(signed),lw=2,color='#217cac',label='Critical-current envelope')
ax.axhline(0,color='#a6aeb4',lw=.8)
ax.set(xlabel=r'$\Phi/\Phi_0$',ylabel='Normalized current',title='Uniform Josephson junction',xlim=(-4,4),ylim=(-.28,1.1));ax.legend(frameon=False,fontsize=10)
for ax in axes:ax.spines[['top','right']].set_visible(False)
fig.tight_layout(pad=1.6)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False,metadata={'Software':'Matplotlib'})
plt.close(fig)
