"""Original heat-pulse profiles; Python 3.14, NumPy and Matplotlib.

Run in the mirrored _media paper directory; writes the PNG to cwd.
"""
from pathlib import Path
from math import erf
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1,2,figsize=(9.6,3.6),facecolor='white',sharey=True)
x=np.linspace(-7,7,1601)
erf_array=np.vectorize(erf)
colors=['#1e293b','#be123c','#2563eb','#15803d']
for t,color in zip([0,.2,1,4],colors):
    g=np.exp(-x*x/(1+4*t))/np.sqrt(np.pi*(1+4*t))
    pulse=.5*((x>-1)&(x<1)) if t==0 else .25*(erf_array((x+1)/(2*np.sqrt(t)))-erf_array((x-1)/(2*np.sqrt(t))))
    for ax,y in zip(axes,[g,pulse]):
        ax.plot(x,y,color=color,label=f'$t={t:g}$',lw=1.8)
for ax,title in zip(axes,['Gaussian initial data','Interval initial data']):
    ax.set(title=title,xlabel='$x$',xlim=(-7,7),ylim=(0,.64))
    ax.grid(alpha=.18)
    ax.spines[['top','right']].set_visible(False)
axes[0].set_ylabel(r'Temperature $\theta(x,t)$')
axes[1].legend(frameon=False,loc='upper right',fontsize=9)
fig.suptitle(r'Unit-integral pulses: $\theta_t=\theta_{xx}$',fontsize=12)
fig.tight_layout()
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=155,facecolor='white')
plt.close(fig)
