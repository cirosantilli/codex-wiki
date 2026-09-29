"""Original SU(3) flavour diagrams. Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Writes only paper-41-flavour-weights.png in the working directory; respects MPLCONFIGDIR.
"""
import itertools
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def compositions(total):
    return [(u,d,total-u-d) for u in range(total+1) for d in range(total-u+1)]
def qqq_weights():return sorted(((u-d)/2,1-s) for u,d,s in compositions(3))
def connect(ax,weights):
    for (x,y),(u,v) in itertools.combinations(weights,2):
        dx,dy=abs(x-u),abs(y-v)
        if (dx==1 and dy==0) or (dx==.5 and dy==1):ax.plot([x,u],[y,v],color='#a9b7c5',lw=1.1,zorder=1)
def panel(ax,title,weights,labels,exotics=()):
    connect(ax,weights)
    if weights:ax.scatter(*zip(*weights),s=44,c='#165b89',zorder=3)
    for x,y in exotics:ax.scatter([x],[y],s=165,facecolors='none',edgecolors='#b63232',linewidths=2,zorder=4)
    for (x,y),text,dx,dy in labels:ax.annotate(text,(x,y),xytext=(dx,dy),textcoords='offset points',ha='center',fontsize=10,color='#172535')
    ax.set(title=title,xlim=(-2.0,2.0),ylim=(-2.55,2.5),xlabel=r'$I_3$',ylabel=r'$Y$')
    ax.set_xticks([-1.5,0,1.5]);ax.set_yticks([-2,-1,0,1,2]);ax.set_aspect(np.sqrt(3)/2)
    ax.axhline(0,color='#dde2e7',lw=.6,zorder=0);ax.axvline(0,color='#dde2e7',lw=.6,zorder=0)
    ax.spines[['top','right']].set_visible(False)

fig,axes=plt.subplots(2,2,figsize=(11,8),dpi=100,facecolor='white')
fig.suptitle('SU(3) flavour weights: ordinary baryons and an antidecuplet',fontsize=15,y=.975)
dec=qqq_weights()
panel(axes[0,0],r'Decuplet $\mathbf{10}$: symmetric flavour',dec,[((1.5,1),r'$\Delta^{++}$: uuu',-4,13),((0,-2),r'$\Omega^-$: sss',0,-18)])
octet=[(-.5,1),(.5,1),(-1,0),(0,0),(1,0),(-.5,-1),(.5,-1)]
panel(axes[0,1],r'Octet $\mathbf{8}$: mixed flavour',octet,[((.5,1),'p: uud',0,12),((-.5,1),'n: udd',0,12),((0,0),r'$\Sigma^0,\ \Lambda$: uds (two states)',0,-24)])
axes[0,1].scatter([0],[0],s=115,facecolors='none',edgecolors='#165b89',linewidths=1.2,zorder=4)
panel(axes[1,0],r'Singlet $\mathbf{1}$: antisymmetric flavour',[(0,0)],[((0,0),'uds: antisymmetric combination',0,15)])
anti=sorted((-x,-y) for x,y in dec)
exotic=[(0,2),(-1.5,-1),(1.5,-1)]
panel(axes[1,1],r'Pentaquark antidecuplet $\overline{\mathbf{10}}$',anti,[((0,2),r'$uudd\bar{s}$',0,12),((-1.5,-1),r'$ddss\bar{u}$',0,-19),((1.5,-1),r'$uuss\bar{d}$',0,-19)],exotic)
fig.text(.5,.025,'Weights are (isospin projection, flavour hypercharge). Red rings: the three weights absent from all qqq compositions.',ha='center',fontsize=10)
fig.subplots_adjust(left=.07,right=.97,bottom=.10,top=.89,wspace=.32,hspace=.43)
fig.savefig('paper-41-flavour-weights.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
