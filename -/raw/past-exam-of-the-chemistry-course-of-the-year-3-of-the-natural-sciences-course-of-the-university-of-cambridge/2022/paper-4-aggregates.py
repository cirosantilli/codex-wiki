"""Original explanatory diagram; tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})

fig,axes=plt.subplots(1,3,figsize=(11,3.8),layout='constrained')
cube=np.array([[i,j,k] for i in [0,1] for j in [0,1] for k in [0,1]])
xy=np.column_stack([cube[:,0]+.45*cube[:,2],cube[:,1]+.35*cube[:,2]])
ax=axes[0]
for i in range(8):
    for j in range(i):
        if np.abs(cube[i]-cube[j]).sum()==1:ax.plot(*xy[[i,j]].T,color='.45',zorder=0)
for i,p in enumerate(xy):
    li=cube[i].sum()%2==0
    ax.scatter(*p,s=600,color='#b9d5ed' if li else '#f7d5a2',edgecolors='white')
    ax.text(*p,'Li' if li else 'Me/X',ha='center',va='center',fontsize=9)
ax.set(xlim=(-.4,1.85),ylim=(-.4,1.8),title='Alternating cubane vertices')
ax.axis('off');ax.set_aspect('equal')
for ax,n,title in zip(axes[1:],[2,3],['D: two equivalent lithium-6 nuclei','A: three equivalent lithium-6 nuclei']):
    weights=np.array([1])
    for _ in range(n):weights=np.convolve(weights,[1,1,1])
    positions=np.arange(len(weights))-n
    ax.vlines(positions,0,weights,color='#2166ac',lw=2.5)
    for x,w in zip(positions,weights):ax.text(x,w+.13,str(w),ha='center',fontsize=9)
    ax.set(xlabel='Carbon frequency offset / coupling',ylabel='Relative intensity',title=title,ylim=(0,weights.max()*1.24))
    ax.set_xticks(positions)
fig.suptitle('Ideal aggregate connectivity and proton-decoupled carbon multiplets')

fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=155,facecolor='white')
plt.close(fig)
