"""Finite order interpolation by lattice operations; write PNG to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

nodes=np.array([-2.,-.5,.8,2.]);values=np.array([-1.5,-.2,1.8,3.])
grid=np.linspace(-2.6,2.6,1500)
rows=[]
for i in range(len(nodes)):
    pairs=[]
    for j in range(len(nodes)):
        slope=(values[j]-values[i])/(nodes[j]-nodes[i])if i!=j else 1.
        pairs.append(slope*(grid-nodes[i])+values[i])
    rows.append(np.min(pairs,axis=0))
fig,ax=plt.subplots(figsize=(8.5,5),dpi=120,facecolor='white')
ax.set_facecolor('white')
for i,row in enumerate(rows):ax.plot(grid,row,lw=1.5,alpha=.8,label=rf'$u_{i+1}=\min_j h_{{{i+1}j}}$')
ax.plot(grid,np.max(rows,axis=0),color='#202020',lw=2.8,ls='--',label=r'$h=\max_i u_i$')
ax.scatter(nodes,values,color='black',s=36,zorder=8,label='Prescribed values')
ax.set(xlim=(-2.6,2.6),ylim=(-3,4.5),xlabel='Input',ylabel='Output',title='Finite interpolation by pointwise minimum and maximum')
ax.grid(alpha=.18);ax.legend(loc='upper left',fontsize=10)
fig.tight_layout();fig.savefig(Path.cwd()/'paper-4-interpolation.png',facecolor='white');plt.close(fig)
