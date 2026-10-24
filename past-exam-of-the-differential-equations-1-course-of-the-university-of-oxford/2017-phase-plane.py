"""Original phase portrait for the solution's representative parameter k=1.

Writes to cwd; dependencies and Python version are declared in pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

k=1.0
x=np.linspace(0,3,181);y=np.linspace(0,3,181)
X,Y=np.meshgrid(x,y);U=X*(2-X)-Y;V=Y-k*X
fig,ax=plt.subplots(figsize=(8,6.2),dpi=100,facecolor='white')
ax.streamplot(x,y,U,V,color='#a6adb5',density=1.2,linewidth=0.85,arrowsize=1.0)
xp=np.linspace(0,2,301)
ax.plot(xp,xp*(2-xp),color='#1264a3',lw=2.3,label=r'$\dot x=0:\ y=x(2-x)$')
ax.plot(x,k*x,color='#bc4b21',lw=2.3,label=r'$\dot y=0:\ y=kx$')
ax.scatter([0],[0],s=95,facecolor='white',edgecolor='#202020',linewidths=2,zorder=5,clip_on=False)
ax.scatter([1],[1],s=80,marker='X',color='#202020',zorder=5)
ax.annotate('unstable node',xy=(0,0),xytext=(0.15,0.33),fontsize=10,
            arrowprops=dict(arrowstyle='->',color='#202020'))
ax.annotate('saddle (1, 1)',xy=(1,1),xytext=(1.4,1.3),fontsize=10,
            arrowprops=dict(arrowstyle='->',color='#202020'),bbox=dict(facecolor='white',edgecolor='none',alpha=.9))
ax.set(xlim=(0,3),ylim=(0,3),xlabel='x',ylabel='y',title='Nullclines and sample trajectories (k = 1)')
ax.set_aspect('equal');ax.legend(loc='upper right',framealpha=.95,fontsize=10)
ax.text(.5,-.16,'Trajectories may leave the quadrant through either axis.',transform=ax.transAxes,ha='center',fontsize=11)
ax.spines[['top','right']].set_visible(False)
fig.subplots_adjust(left=.10,right=.97,top=.91,bottom=.17)
fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white',dpi=100)
plt.close(fig)
