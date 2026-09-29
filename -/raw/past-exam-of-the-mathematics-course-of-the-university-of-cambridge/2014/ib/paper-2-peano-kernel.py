"""Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7; cwd PNG only."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(7.2,4.4),dpi=100,facecolor='white')
a=np.linspace(0,1,201);b=np.linspace(1,2,201);c=np.linspace(2,3,201)
for t,k in [(a,2*a*a/3),(b,2-(3-b)**2/3),(c,-(3-c)**2/3)]:
    ax.plot(t,k,color='#2166ac',linewidth=2)
    ax.fill_between(t,0,k,color='#2166ac' if k.mean()>0 else '#b2182b',alpha=.15)
ax.plot(2,5/3,'o',markerfacecolor='white',markeredgecolor='#2166ac',markersize=7)
ax.plot(2,-1/3,'o',color='#2166ac',markersize=7)
ax.axhline(0,color='0.3',linewidth=.8)
ax.axvline(2,color='0.6',linewidth=.7,linestyle='--')
ax.annotate('Left limit 5/3',(2,5/3),xytext=(2.14,1.53),fontsize=10)
ax.annotate('Right limit −1/3',(2,-1/3),xytext=(.72,-.46),fontsize=10)
ax.set(xlim=(0,3),ylim=(-.6,1.9),xlabel=r'$\theta$',ylabel=r'$K(\theta)$',
       title='Peano kernel for the asymmetric second derivative')
ax.set_xticks([0,1,2,3]);ax.set_yticks([-1/3,0,2/3,5/3],['−1/3','0','2/3','5/3'])
ax.grid(alpha=.18)
fig.tight_layout(pad=1.3)
fig.savefig(Path.cwd()/'paper-2-peano-kernel.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
