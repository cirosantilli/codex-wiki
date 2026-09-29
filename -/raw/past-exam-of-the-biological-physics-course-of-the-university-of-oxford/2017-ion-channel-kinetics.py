"""Original two-state relaxation and illustrative channel currents; Python 3.14, numpy, matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
fig,axs=plt.subplots(1,3,figsize=(12,3.7),constrained_layout=True,facecolor='white')
t=np.linspace(0,5,601)
axs[0].plot(t,.5*(-np.expm1(-t)),lw=2.1,color='#1864ab',label=r'A: $\tau=1$ ms')
axs[0].plot(t,.5*(-np.expm1(-10*t)),lw=2.1,color='#d9480f',label=r'B: $\tau=0.1$ ms')
axs[0].axhline(.5,color='.5',ls=':',lw=1)
axs[0].set(xlabel='Time after step (ms)',ylabel='Open probability',title='Same limit, different relaxation',ylim=(0,.54));axs[0].legend(frameon=False,fontsize=9)
u=np.linspace(0,20,1001)
m=-np.expm1(-u/.3);h=np.exp(-u/1.5);i=-m**3*h;i=i/abs(i.min())
axs[1].plot(u,i,color='#1864ab',lw=2.2);axs[1].axhline(0,color='.6',lw=1)
axs[1].set(xlabel='Time after maintained step (ms)',ylabel='Normalized inward current',title='Fast activation plus inactivation',ylim=(-1.1,.08))
n=-np.expm1(-u/3)
axs[2].plot(u,n**4,color='#d9480f',lw=2.2)
axs[2].set(xlabel='Time after maintained step (ms)',ylabel='Normalized outward current',title='Delayed sustained activation',ylim=(-.04,1.1))
for ax in axs:ax.grid(alpha=.15)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white',transparent=False)
plt.close(fig)
