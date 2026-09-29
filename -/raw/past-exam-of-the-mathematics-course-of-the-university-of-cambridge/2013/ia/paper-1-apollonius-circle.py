"""Write paper-1-apollonius-circle.png to the current working directory.
Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Respects externally supplied MPLCONFIGDIR and uses an opaque background.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
fig,ax=plt.subplots(figsize=(6.4,4.4),dpi=100,facecolor='white')
ax.set_facecolor('white');t=np.linspace(0,2*np.pi,721)
ax.plot(9/8*np.cos(t),3/8+9/8*np.sin(t),color='#176b99',lw=2.2,label='$|z+3i|=3|z|$')
ax.axhline(0,color='#777777',lw=.8);ax.axvline(0,color='#777777',lw=.8)
ax.scatter([0],[3/8],color='#aa5035',s=30,zorder=4)
ax.annotate('Center $3i/8$',(0,3/8),(.25,.57),fontsize=10,arrowprops={'arrowstyle':'-','color':'#aa5035'})
for y,label,xtext in [(1.5,'$3i/2$',.16),(-.75,'$-3i/4$',.16)]:
 ax.scatter([0],[y],color='#176b99',s=25,zorder=4);ax.text(xtext,y+.04,label,fontsize=11)
ax.plot([0,9/8],[3/8,3/8],ls='--',color='#aa5035',lw=1)
ax.text(.58,.24,'$9/8$',color='#874029',fontsize=10)
ax.set(xlim=(-1.6,1.8),ylim=(-1.1,1.9),xlabel='$\\operatorname{Re} z$',ylabel='$\\operatorname{Im} z$',title='Circle with center $3i/8$ and radius $9/8$')
ax.set_aspect('equal',adjustable='box');ax.grid(alpha=.18);ax.legend(loc='upper left',frameon=False,fontsize=10)
fig.tight_layout();fig.savefig(Path.cwd()/'paper-1-apollonius-circle.png',dpi=100,facecolor='white',transparent=False);plt.close(fig)
