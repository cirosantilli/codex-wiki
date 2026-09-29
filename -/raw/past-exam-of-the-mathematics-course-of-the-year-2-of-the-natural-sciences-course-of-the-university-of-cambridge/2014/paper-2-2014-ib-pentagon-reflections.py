"""Original five-reflection pentagon action diagram. Python 3.14, NumPy 2.3, Matplotlib 3.10.
Run in the mirrored _media directory; PNG output is relative to cwd, on white.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import numpy as np

fig,axes=plt.subplots(1,5,figsize=(11,3.7),facecolor='white')
angles=2*np.pi*np.arange(5)/5
points=np.c_[np.cos(angles),np.sin(angles)]
for j,ax in enumerate(axes):
    phi=j*np.pi/5;direction=np.array([np.cos(phi),np.sin(phi)])
    ax.plot(*np.vstack((points,points[:1])).T,color='#5e7389',lw=1.3)
    ax.plot(*np.vstack((-1.12*direction,1.12*direction)).T,color='#b24b32',ls='--',lw=1.5)
    fixed=3*j%5
    ax.scatter(*points.T,s=30,color='#284d70',zorder=4)
    ax.scatter(*points[fixed],s=65,facecolor='white',edgecolor='#b24b32',lw=2,zorder=5)
    pairs=[(k,(j-k)%5) for k in range(5) if k<(j-k)%5]
    for (p,q),color in zip(pairs,['#2779a7','#448258']):
        ax.add_patch(FancyArrowPatch(points[p],points[q],arrowstyle='<->',shrinkA=7,shrinkB=7,mutation_scale=10,lw=1.6,color=color,zorder=3))
    for k,p in enumerate(points):ax.text(*(1.19*p),str(k),ha='center',va='center',fontsize=11)
    title=r'$m$' if j==0 else (r'$Rm$' if j==1 else rf'$R^{j}m$')
    ax.set(xlim=(-1.4,1.4),ylim=(-1.4,1.4),aspect='equal',title=title)
    ax.axis('off')
fig.suptitle('Five reflection axes and their actions on pentagon vertices',fontsize=15,y=.97)
fig.text(.5,.17,r'$R$: rotation by $72^\circ$ counterclockwise; $R^jm$ sends vertex $k$ to $j-k\ (\mathrm{mod}\ 5)$.',ha='center',fontsize=11)
fig.text(.5,.06,'Red dashed line: reflection axis • outlined vertex: fixed • arrows: exchanged pairs',ha='center',fontsize=10)
fig.subplots_adjust(left=.015,right=.985,top=.79,bottom=.25,wspace=.1)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=145,facecolor='white')
plt.close(fig)
