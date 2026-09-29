"""Original nearest-neighbour lattice and energy surfaces; no experimental data."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

fig=plt.figure(figsize=(12,4.9),dpi=140,facecolor='white')
ax=fig.add_subplot(121);ax.set_aspect('equal');ax.axis('off')
sq=np.sqrt(3);deltas=np.array([[0,1],[sq/2,-.5],[-sq/2,-.5]])
a1=deltas[0]-deltas[1];a2=deltas[0]-deltas[2]
cell=np.array([[0,0],a1,a1+a2,a2]);ax.add_patch(Polygon(cell,facecolor='#e6f1e7',edgecolor='#54835a',ls='--',lw=1.8,zorder=0))
A=np.array([m*a1+n*a2 for m in range(-4,5) for n in range(-4,5)])
for r in A:
    for delta in deltas:ax.plot([r[0],r[0]+delta[0]],[r[1],r[1]+delta[1]],color='#b4b9bd',lw=1,zorder=1)
B=A+deltas[0]
ax.scatter(A[:,0],A[:,1],s=65,c='#356fa3',label='A sublattice',zorder=3)
ax.scatter(B[:,0],B[:,1],s=65,c='#dc833b',label='B sublattice',zorder=3)
for j,delta in enumerate(deltas):
    ax.annotate('',delta,(0,0),arrowprops=dict(arrowstyle='->',color='#333',lw=2,shrinkA=6,shrinkB=6))
    xy=delta*.55+np.array([.18 if j!=2 else -.32,.05])
    ax.text(*xy,rf'$\delta_{j+1}$',fontsize=12,color='#222')
ax.text(-1.62,2.75,'Two sites per\nprimitive cell',fontsize=11,color='#386541')
ax.annotate('',(-.38,2.2),(-.9,2.65),arrowprops=dict(arrowstyle='->',color='#54835a'))
ax.set(xlim=(-2.3,2.3),ylim=(-1.55,3.45),title='Three hopping paths from each site')
ax.legend(loc='lower center',bbox_to_anchor=(.5,-.10),ncol=2,frameon=False,fontsize=11)
ax2=fig.add_subplot(122,projection='3d')
q=np.linspace(-.42,.42,81);X,Y=np.meshgrid(q,q);K=4*np.pi/(3*sq)
f=np.exp(1j*Y)+2*np.exp(-1j*Y/2)*np.cos(sq*(K+X)/2);E=np.abs(f)
ax2.plot_surface(X,Y,E,color='#3d82b5',alpha=.83,linewidth=0,rstride=2,cstride=2)
ax2.plot_surface(X,Y,-E,color='#dd8c49',alpha=.83,linewidth=0,rstride=2,cstride=2)
ax2.scatter([0],[0],[0],color='#222',s=22)
ax2.set(xlabel=r'$bq_x$',ylabel=r'$bq_y$',zlabel=r'$E/t$',title=r'Two bands near $\mathbf{K}_+$')
ax2.view_init(elev=24,azim=-52);ax2.set_box_aspect((1,1,1.05));ax2.tick_params(labelsize=9)
fig.suptitle('Graphene: a two-site lattice creates a conical band crossing',fontsize=16,y=.99)
fig.text(.5,.025,'Chosen model: equal nearest-neighbour hopping −t, no interactions or on-site offset. Surfaces are calculated, not measured.',ha='center',fontsize=10)
fig.subplots_adjust(left=.04,right=.96,bottom=.16,top=.84,wspace=.16)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,facecolor='white')
