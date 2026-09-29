"""Original reciprocal-cell and Fermi-circle construction, Python 3.14.

Uses numpy and matplotlib; PNG basename is written in the current directory.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle
import numpy as np

fig, axes = plt.subplots(1,2,figsize=(9,4.7),layout='constrained')
fig.patch.set_facecolor('white')
verts=[(1,0),(0,1),(-1,0),(0,-1)]
for ax in axes:
    ax.add_patch(Polygon(verts,fc='#dceeed',ec='#277b79',lw=2,zorder=2))
    ax.axhline(0,color='0.75',lw=0.8)
    ax.axvline(0,color='0.75',lw=0.8)
    ax.set_aspect('equal')
    ax.set(xlabel=r'$k_xa/\pi$',ylabel=r'$k_ya/\pi$')
    ax.spines[['top','right']].set_visible(False)
pts=[(x,y) for x in range(-3,4) for y in range(-3,4) if (x-y)%2==0]
axes[0].scatter(*zip(*pts),s=26,c='#34404f',zorder=4)
for v,label,offset in [((1,1),r'$\mathbf{b}_1$',(0.12,0)),((-1,1),r'$\mathbf{b}_2$',(-0.5,0))]:
    axes[0].annotate('',xy=v,xytext=(0,0),arrowprops={'arrowstyle':'-|>','lw':1.8,'color':'#a8562d'})
    axes[0].text(v[0]*0.7+offset[0],v[1]*0.7+offset[1],label,fontsize=12)
axes[0].set(xlim=(-2.5,2.5),ylim=(-2.5,2.5),title='Reciprocal lattice and first zone')
r=1/np.sqrt(2)
axes[1].add_patch(Circle((0,0),r,fc='#e4d9f0',ec='#7b3f8d',alpha=0.85,lw=2,zorder=3))
contacts=[(x/2,y/2) for x in [-1,1] for y in [-1,1]]
axes[1].scatter(*zip(*contacts),s=27,c='#b14a29',zorder=4)
axes[1].annotate('',xy=(r,0),xytext=(0,0),arrowprops={'arrowstyle':'<->','color':'#6e3782','lw':1.5})
axes[1].text(0.15,0.10,r'$k_Fa/\pi=1/\sqrt{2}$',fontsize=11)
axes[1].set(xlim=(-1.3,1.3),ylim=(-1.3,1.3),title='Inscribed Fermi circle')
fig.savefig('paper-2-reciprocal-zone.png',dpi=160,facecolor='white')
plt.close(fig)
