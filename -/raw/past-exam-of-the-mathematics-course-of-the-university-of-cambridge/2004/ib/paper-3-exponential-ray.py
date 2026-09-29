"""Original ray plot; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Only write opaque PNG basename to caller CWD; preserve supplied MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

a=1.55
x=np.linspace(-a,a,1401)
y=np.log(np.cos(x)/np.cos(a))
fig,ax=plt.subplots(figsize=(7.3,4.6),constrained_layout=True)
ax.plot(x,y,lw=2,color='#176580')
ax.scatter([-a,a],[0,0],color='#176580',zorder=3)
ax.axhline(0,color='0.5',lw=1)
ax.axvline(0,color='0.65',lw=.8,ls='--')
ax.annotate(r'Height $-\log(\cos 1.55)$',xy=(0,y[len(y)//2]),xytext=(.12,3.25),arrowprops={'arrowstyle':'->'},fontsize=10)
ax.text(-1.36,.55,'Steep endpoint slopes',fontsize=9)
ax.text(-1.42,-.26,r'$(-\lambda a,0)$',fontsize=10)
ax.text(.91,-.26,r'$(\lambda a,0)$',fontsize=10)
ax.set(xlim=(-1.7,1.7),ylim=(-.38,4.2),xlabel=r'$\lambda x$',ylabel=r'$\lambda y$',title=r'Stationary light ray with $\lambda a=1.55$, close to $\pi/2$')
ax.grid(alpha=.18)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=110,facecolor='white',transparent=False)
