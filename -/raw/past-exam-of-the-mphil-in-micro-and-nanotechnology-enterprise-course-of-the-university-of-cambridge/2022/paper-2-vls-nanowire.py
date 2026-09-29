"""Original VLS, stacking and cross-section cartoons; Python 3.14/matplotlib.

The faceted section assumes a common [111] zinc-blende growth direction.
Output: PNG basename in the current working directory.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Circle,Wedge,RegularPolygon

fig,axes=plt.subplots(1,3,figsize=(10.8,4.8),layout='constrained')
fig.patch.set_facecolor('white')
for ax in axes:
    ax.set(xlim=(0,5),ylim=(0,7),aspect='equal');ax.axis('off')
ax=axes[0];ax.set_title('VLS tip growth',fontsize=12)
ax.add_patch(Rectangle((1.6,.6),1.8,3.8,facecolor='#b5d0df',edgecolor='.3'))
ax.add_patch(Wedge((2.5,4.4),1.12,0,180,facecolor='#e0b665',edgecolor='.3'))
ax.plot([1.38,3.62],[4.4,4.4],color='#b6623e',lw=2)
ax.text(2.5,4.85,'Au–Ga liquid',ha='center',fontsize=10)
ax.text(2.5,2.6,'GaAs\nsolid',ha='center',fontsize=12)
for start in [(1,6.2),(4.1,6.2)]:
    ax.annotate('',(2.5,5.6),start,arrowprops={'arrowstyle':'->','color':'.3'})
ax.text(2.5,6.5,'Ga + As supply',ha='center',fontsize=10)
ax.annotate('',(4,4.4),(4,3.1),arrowprops={'arrowstyle':'->','color':'#2d718b'})
ax.text(3.9,2.55,'Axial\ngrowth',ha='center',fontsize=9)
ax.text(2.5,.1,'Interface nucleation / step growth',ha='center',fontsize=8)
ax=axes[1];ax.set_title('Bilayer stacking alternatives',fontsize=12)
colors={'A':'#2d718b','B':'#b6623e','C':'#9274a0'}
for x,seq,label in [(1.2,'ABCABC','Zinc blende'),(3.6,'ABABAB','Wurtzite')]:
    for i,letter in enumerate(seq):
        yy=1.4+i*.65
        ax.add_patch(Circle((x,yy),.24,facecolor=colors[letter]))
        ax.text(x,yy,letter,color='white',ha='center',va='center',fontsize=9)
    ax.text(x,.65,label,ha='center',fontsize=9)
ax=axes[2];ax.set_title('Representative faceted section',fontsize=12)
ax.add_patch(RegularPolygon((2.5,3.6),6,radius=1.65,orientation=0,facecolor='#b5d0df',edgecolor='.25'))
ax.text(2.5,3.6,r'Axis $[111]$',ha='center',fontsize=12)
ax.text(2.5,1.4,r'Possible $\{110\}$ side facets',ha='center',fontsize=10)
ax.text(2.5,.55,'Other facet sets and triangular\nsections are possible.',ha='center',fontsize=9)
fig.savefig('paper-2-vls-nanowire.png',dpi=150,facecolor='white')
plt.close(fig)
