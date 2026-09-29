"""Formal zero-boundary-speed ray; Python 3.14, existing numpy/matplotlib.

Output is a PNG basename in caller CWD. Caller MPLCONFIGDIR is honored.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
th=np.linspace(0,np.pi,801)
x=.5+.5*np.cos(th);y=.5*np.sin(th)
fig,ax=plt.subplots(figsize=(8,4.5),dpi=120,facecolor='white')
ax.set_facecolor('white')
ax.plot(x,y,color='#18567b',linewidth=2.5)
ax.axhline(0,color='#444444',linewidth=1)
ax.scatter([0,1],[0,0],facecolors='white',edgecolors='#18567b',s=65,zorder=3)
ax.annotate('Zero-speed endpoint',xy=(0,0),xytext=(-.04,.18),arrowprops={'arrowstyle':'->'},fontsize=10)
ax.annotate('Zero-speed endpoint',xy=(1,0),xytext=(.69,.18),arrowprops={'arrowstyle':'->'},fontsize=10)
ax.text(.5,.32,r'$y=\sqrt{x(1-x)}$',ha='center',fontsize=13)
ax.set(xlim=(-.15,1.15),ylim=(-.05,.63),xlabel='$x$',ylabel='$y$',title='Formal ray in a medium with c(y) = y')
ax.set_aspect('equal');ax.spines[['top','right']].set_visible(False)
fig.tight_layout();fig.savefig('paper-1-optical-ray.png',facecolor='white',transparent=False);plt.close(fig)
