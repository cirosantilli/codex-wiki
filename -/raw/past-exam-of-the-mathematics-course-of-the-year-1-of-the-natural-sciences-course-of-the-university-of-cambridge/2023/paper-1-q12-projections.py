"""Generate the PNG in cwd. Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7;
dependencies are declared in the repository pyproject.toml.
"""
from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR', '/tmp/nst-2023-ia-paper-1-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig,axes=plt.subplots(1,3,figsize=(10.6,3.8),layout='constrained',facecolor='white')
axes[0].fill([-1,1,0,-1],[0,0,1,0],facecolor='#d9eaf5',edgecolor='#17679a',linewidth=1.8)
axes[0].set(xlabel='$x/L$',ylabel='$y/D$',title='Onto the $(x,y)$ plane',xlim=(-1.15,1.15),ylim=(-0.08,1.12))
z=np.linspace(0,1,300)
w=np.sqrt(1-z/2)
axes[1].fill_betweenx(z,-w,w,color='#d9eaf5')
axes[1].plot(-w,z,color='#17679a',linewidth=1.8)
axes[1].plot(w,z,color='#17679a',linewidth=1.8)
axes[1].plot([-1,1],[0,0],color='#17679a',linewidth=1.8)
axes[1].plot([-1/np.sqrt(2),1/np.sqrt(2)],[1,1],color='#17679a',linewidth=1.8)
axes[1].set(xlabel='$x/L$',ylabel='$z/H$',title='Onto the $(x,z)$ plane',xlim=(-1.15,1.15),ylim=(-0.08,1.12))
axes[1].annotate(r'top width $\sqrt{2}L$',(0,1),(0,0.72),ha='center',fontsize=9,arrowprops={'arrowstyle':'->'})
axes[2].fill([0,1,0,0],[0,0,1,0],facecolor='#d9eaf5',edgecolor='#17679a',linewidth=1.8)
axes[2].set(xlabel='$y/D$',ylabel='$z/H$',title='Onto the $(y,z)$ plane',xlim=(-0.08,1.12),ylim=(-0.08,1.12))
for ax in axes:
    ax.set_aspect('equal')
    ax.grid(alpha=0.2)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white')
plt.close(fig)
