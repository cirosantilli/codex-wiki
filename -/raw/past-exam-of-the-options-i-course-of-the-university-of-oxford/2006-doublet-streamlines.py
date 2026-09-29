"""Python 3.12; numpy and matplotlib. Writes the same-basename PNG in CWD."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(6.4,5.2),facecolor='white')
t=np.linspace(0,2*np.pi,800)
for c in [-2,-1,-.5,.5,1,2]:
 r=abs(1/(2*c));y0=-1/(2*c)
 ax.plot(r*np.cos(t),y0+r*np.sin(t),color='#2366a8',lw=1.4)
ax.plot([-2.4,-.04],[0,0],color='#c44e28',lw=1.6)
ax.plot([.04,2.4],[0,0],color='#c44e28',lw=1.6)
ax.scatter([0],[0],s=45,facecolor='white',edgecolor='black',zorder=5)
ax.annotate('excluded origin',xy=(0,0),xytext=(.45,.25),arrowprops={'arrowstyle':'->'},fontsize=10)
ax.set(xlim=(-2.3,2.3),ylim=(-2.3,2.3),xlabel='$x$',ylabel='$y$',title='Planar doublet: constant stream function')
ax.set_aspect('equal');ax.grid(alpha=.17);fig.tight_layout()
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=150,facecolor='white')
