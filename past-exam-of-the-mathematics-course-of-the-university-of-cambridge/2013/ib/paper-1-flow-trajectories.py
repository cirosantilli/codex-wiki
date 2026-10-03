"""Write an opaque 1000x500 PNG basename to caller's current directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(10, 5), dpi=100, facecolor='white')
x=np.linspace(-3,3,100);y=np.linspace(-3,3,100);X,Y=np.meshgrid(x,y)
axes[0].streamplot(x,y,X,-Y,density=1.05,color='#3274a1',linewidth=.9,arrowsize=1.)
axes[0].axhline(0,color='#313131',lw=.8);axes[0].axvline(0,color='#313131',lw=.8)
axes[0].set(xlim=(-3,3),ylim=(-3,3),xlabel='x',ylabel='y',title='Streamlines at t = 0: xy = constant')
axes[0].set_aspect('equal')
past=np.linspace(.38,1,200);future=np.linspace(1,12,500)
curve=lambda z:np.log(z)-1+2/z
axes[1].plot(past,curve(past),'--',color='#929292',label='before t = 0')
axes[1].plot(future,curve(future),color='#c24a32',lw=2,label='after t = 0')
axes[1].scatter([1,2],[1,np.log(2)],color='#313131',s=22,zorder=4)
axes[1].annotate('(1, 1)',(1,1),xytext=(12,18),textcoords='offset points')
axes[1].annotate('minimum (2, log 2)',(2,np.log(2)),xytext=(18,-26),textcoords='offset points')
for z in [1.5,5,9]:
 axes[1].annotate('',xy=(z+.35,curve(z+.35)),xytext=(z,curve(z)),arrowprops={'arrowstyle':'->','color':'#c24a32','lw':1.5})
axes[1].set(xlim=(0,12.2),ylim=(.25,3.5),xlabel='x',ylabel='y',title='Material path: y = log x - 1 + 2/x')
axes[1].grid(alpha=.22);axes[1].legend(loc='upper right',frameon=False)
fig.tight_layout(pad=1.6)
fig.savefig(Path('paper-1-flow-trajectories.png'),dpi=100,facecolor='white',transparent=False)
plt.close(fig)
