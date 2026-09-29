"""Original path-dependence diagram. Python 3.14; matplotlib 3.10.7, numpy 2.3.5.

Save the white PNG to cwd, normally the mirrored _media paper directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

p=np.linspace(0,np.pi/2,500)
fig,ax=plt.subplots(figsize=(5.8,5.8),layout='constrained',facecolor='white')
x=np.linspace(0,1,500)
ax.fill_between(x,1-x,np.sqrt(1-x*x),color='#e5eef3',label=r'Area $\pi/4-1/2$')
ax.plot([1,0],[0,1],color='#d55e00',lw=2,label=r'Segment: $\int\mathbf{F}_1\cdot d\mathbf{r}=1$')
ax.plot(np.cos(p),np.sin(p),color='#0072b2',lw=2,label=r'Arc: $\int\mathbf{F}_1\cdot d\mathbf{r}=\pi/2$')
ax.annotate('',xy=(.36,.64),xytext=(.53,.47),arrowprops={'arrowstyle':'->','color':'#d55e00','lw':2})
ax.annotate('',xy=(np.cos(.85),np.sin(.85)),xytext=(np.cos(.65),np.sin(.65)),arrowprops={'arrowstyle':'->','color':'#0072b2','lw':2})
ax.scatter([1,0],[0,1],color='#333333',s=23,zorder=5)
ax.annotate('$(1,0)$',(1,0),xytext=(.84,-.11),fontsize=11)
ax.annotate('$(0,1)$',(0,1),xytext=(-.14,1.06),fontsize=11)
ax.set(xlabel='$x$',ylabel='$y$',xlim=(-.17,1.18),ylim=(-.16,1.2),title='Same endpoints, different paths in $z=0$')
ax.set_aspect('equal');ax.grid(alpha=.15)
ax.legend(loc='upper center',fontsize=9,bbox_to_anchor=(.5,-.14),frameon=False)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=160,facecolor='white')
