from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-2,2,301)
y=np.linspace(-2,2,301)
X,Y=np.meshgrid(x,y)
U=(1-X**2)*Y
V=X*(1-Y**2)
fig,ax=plt.subplots(figsize=(9,8),dpi=120,facecolor='white')
ax.set_facecolor('white')
ax.streamplot(x,y,U,V,density=1.35,color='#777777',linewidth=.7,arrowsize=1.0)
for k in [-1,1]:
 ax.axvline(k,color='#896c28',ls='--',lw=1.2)
 ax.axhline(k,color='#896c28',ls='--',lw=1.2)
central=np.linspace(-1,1,151)
ax.plot(central,central,color='#356cb6',lw=1.2,label='Unstable separatrix y = x')
ax.plot(central,-central,color='#9e3f81',lw=1.2,label='Stable separatrix y = -x')
for a,b in [(.2,.6),(-.2,-.6)]:
 ax.annotate('',xy=(b,b),xytext=(a,a),arrowprops={'arrowstyle':'->','color':'#356cb6','lw':1.5})
for a,b in [(.7,.3),(-.7,-.3)]:
 ax.annotate('',xy=(b,-b),xytext=(a,-a),arrowprops={'arrowstyle':'->','color':'#9e3f81','lw':1.5})
ax.scatter([1,-1],[1,-1],color='#167b58',s=80,zorder=6,label='Stable nodes, index +1')
ax.scatter([1,-1],[-1,1],color='#cd522c',s=80,zorder=6,label='Unstable nodes, index +1')
ax.scatter([0],[0],color='black',marker='D',s=65,zorder=6,label='Saddle, index -1')
ax.set(xlim=(-2,2),ylim=(-2,2),xlabel='x',ylabel='y',title='Invariant boundaries prevent closed trajectories')
ax.set_aspect('equal')
ax.legend(loc='upper center',bbox_to_anchor=(.5,-.09),ncol=2,frameon=False,fontsize=9)
fig.subplots_adjust(bottom=.18,top=.92,left=.1,right=.95)
fig.savefig(Path.cwd()/'paper-2-phase-plane.png',facecolor='white',transparent=False)
plt.close(fig)
