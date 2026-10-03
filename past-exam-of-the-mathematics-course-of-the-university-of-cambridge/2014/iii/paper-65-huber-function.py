"""Generate paper-65-huber-function.png in the current directory.
Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
The caller may supply MPLCONFIGDIR; the script does not replace it.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-3.5,3.5,701)
y=np.where(np.abs(x)<=1,0.5*x*x,np.abs(x)-0.5)
fig,ax=plt.subplots(figsize=(8,4),dpi=100,facecolor='white')
ax.set_facecolor('white')
ax.plot(x,y,color='#176b99',lw=2.5)
ax.axvspan(-1,1,color='#e1eef5',alpha=1,zorder=-1)
ax.axvline(-1,color='#78909c',ls='--',lw=1)
ax.axvline(1,color='#78909c',ls='--',lw=1)
ax.scatter([-1,1],[0.5,0.5],color='#176b99',s=28,zorder=3)
ax.text(0,0.93,'quadratic center',ha='center',fontsize=10)
ax.text(-2.65,2.65,'linear tail',ha='center',fontsize=10)
ax.text(2.65,2.65,'linear tail',ha='center',fontsize=10)
ax.set(xlim=(-3.5,3.5),ylim=(-0.12,3.15),xlabel='$x$',ylabel='$f(x)$',title='Huber function: quadratic center and linear tails')
ax.set_xticks([-3,-2,-1,0,1,2,3]);ax.grid(alpha=.2)
fig.tight_layout()
fig.savefig(Path.cwd()/'paper-65-huber-function.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
