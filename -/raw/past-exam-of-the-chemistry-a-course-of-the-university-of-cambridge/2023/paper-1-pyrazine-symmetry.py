"""Original pyrazine pz SALCs and Hückel energies using the printed axes."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from tools.chemistry_diagram import ring, finish
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

th=np.arange(6)*np.pi/3
points=np.column_stack([np.sin(th),np.cos(th)])
vectors=np.array([[1,0,0,1,0,0],[0,1,1,0,1,1], [1,0,0,-1,0,0],
                  [0,1,-1,0,-1,1], [0,1,1,0,-1,-1], [0,1,-1,0,1,-1]],float)
vectors/=np.linalg.norm(vectors,axis=1)[:,None]
labels=[r'$N_+$: $B_{1u}$',r'$C_0$: $B_{1u}$',r'$N_-$: $B_{3g}$',
        r'$C_y$: $B_{3g}$',r'$C_x$: $B_{2g}$',r'$C_{xy}$: $A_u$']
fig=plt.figure(figsize=(9,7.4),layout='constrained')
gs=fig.add_gridspec(3,3,width_ratios=[1,1,1.8])
for k,(v,label) in enumerate(zip(vectors,labels)):
    ax=fig.add_subplot(gs[k//2,k%2]);ring(ax,points,color='0.65')
    for j,(p,c) in enumerate(zip(points,v)):
        radius=.25 if c else .055
        ax.add_patch(Circle(p,radius,facecolor='#245c9f' if c>0 else '#c56527' if c<0 else 'white',
                            edgecolor='0.3',lw=.6,zorder=3))
        ax.text(*(p*1.36),('N'+str(j+1)) if j in [0,3] else str(j+1),
                ha='center',va='center',fontsize=9)
    finish(ax,(-1.6,1.6),(-1.6,1.6));ax.set_title(label,fontsize=11,pad=1)
ax=fig.add_subplot(gs[:,2]);ax.axis('off');ax.set(xlim=(-.5,4.1),ylim=(-2.95,2.25))
ax.annotate('',(-.3,2),(-.3,-2.65),arrowprops={'arrowstyle':'->'})
ax.text(-.4,-.1,'energy',rotation=90,ha='right',va='center',fontsize=10)
levels=[(1+np.sqrt(2),r'$\alpha+(1+\sqrt{2})\beta$',r'$B_{1u}$',2),
        (np.sqrt(3),r'$\alpha+\sqrt{3}\beta$',r'$B_{3g}$',2),
        (1,r'$\alpha+\beta$',r'$B_{2g}$',2),
        (1-np.sqrt(2),r'$\alpha+(1-\sqrt{2})\beta$',r'$B_{1u}$',0),
        (-1,r'$\alpha-\beta$',r'$A_u$',0),
        (-np.sqrt(3),r'$\alpha-\sqrt{3}\beta$',r'$B_{3g}$',0)]
for lam,label,irrep,occ in levels:
    y=-lam
    ax.plot([.1,.95],[y,y],color='#245c9f',lw=2)
    for dx,start,end in ([(-.075,y-.17,y+.17),(.075,y+.17,y-.17)] if occ else []):
        ax.annotate('',(.52+dx,end),(.52+dx,start),arrowprops={'arrowstyle':'->','lw':1.1})
    ax.text(1.15,y+.12,label,va='center',fontsize=11)
    ax.text(1.15,y-.15,irrep,va='center',fontsize=10,color='0.35')
ax.set_title('Molecular orbitals\n$\\beta<0$; six $\\pi$ electrons',fontsize=12)
fig.suptitle('Pyrazine: normalized symmetry orbitals and energy levels',fontsize=13)
fig.supxlabel('Blue / orange: positive / negative upper lobe; open dot: zero coefficient.\nAxes: x right, y up, z out of the plane; N atoms at 1 and 4.',fontsize=9)
fig.savefig(Path(__file__).stem+'.png',dpi=135,facecolor='white')
plt.close(fig)
