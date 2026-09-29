"""Generate the PNG in cwd. Tested with Python 3.14.4, NumPy 2.3.5,
Matplotlib 3.10.7; dependencies are declared in the repository pyproject.toml.
"""
from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR','/tmp/nst-2022-ia-paper-1-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

N=6-2*np.exp(-2)
x=np.linspace(-2,2,1001)
f=(1+np.exp(-np.abs(x)))/N
edge=(1+np.exp(-2))/N
fig,ax=plt.subplots(figsize=(7,3.8),layout='constrained',facecolor='white')
ax.plot(x,f,color='#17679a',linewidth=2)
ax.plot([-3,-2],[0,0],color='#17679a',linewidth=2)
ax.plot([2,3],[0,0],color='#17679a',linewidth=2)
for side in [-2,2]:
    ax.plot(side,edge,'o',markerfacecolor='white',markeredgecolor='#17679a',zorder=5)
    ax.plot(side,0,'o',color='#17679a',markersize=4,zorder=5)
    ax.plot([side,side],[0,edge],':',color='gray',linewidth=1)
ax.plot(0,2/N,'o',color='#b3472d',markersize=4)
ax.set(xlim=(-3,3),ylim=(-0.02,0.41),xlabel='$x$',ylabel='$f(x)$',title=r'Question 16: $f(x)=(1+e^{-|x|})/N$ on $(-2,2)$',
       xticks=[-3,-2,-1,0,1,2,3],yticks=[0,edge,2/N],yticklabels=['0',r'$(1+e^{-2})/N$',r'$2/N$'])
ax.grid(alpha=0.18)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white')
plt.close(fig)
