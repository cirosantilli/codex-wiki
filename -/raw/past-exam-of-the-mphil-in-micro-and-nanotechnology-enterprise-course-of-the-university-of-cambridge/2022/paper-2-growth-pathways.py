"""Original nanocrystal mechanism cartoons; Python 3.14/numpy/matplotlib.

Conceptual stages, not digitized microscopy or a quantitative growth model.
Output: PNG basename in the current working directory.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, RegularPolygon
import numpy as np

BLUE, ORANGE, PURPLE = '#2d718b', '#b6623e', '#8b6a9d'
fig, axes = plt.subplots(2, 3, figsize=(11, 6.5), layout='constrained')
fig.patch.set_facecolor('white')
def setup(ax, title):
    ax.set(xlim=(0, 6), ylim=(0, 4), aspect='equal')
    ax.axis('off'); ax.set_title(title, fontsize=11)
def arrow(ax, a, b, text=None):
    ax.annotate('', b, a, arrowprops={'arrowstyle':'->', 'color':'.3', 'lw':1.5})
    if text: ax.text((a[0]+b[0])/2, (a[1]+b[1])/2+.18, text, ha='center', fontsize=8)
for ax, title in zip(axes.flat, ['Monomer addition', 'Ostwald ripening', 'Oriented attachment',
                               'One-dimensional growth', 'Two-dimensional growth', 'What the arrows represent']):
    setup(ax, title)
ax=axes[0,0]
ax.add_patch(Circle((3,2), .65, color=BLUE, alpha=.8))
for angle in np.arange(6)*np.pi/3:
    p=np.array([3,2])+1.6*np.array([np.cos(angle),np.sin(angle)])
    ax.add_patch(Circle(p,.09,color=ORANGE))
    arrow(ax,p,p*.0+np.array([3,2])+.8*np.array([np.cos(angle),np.sin(angle)]))
ax.text(3,.35,'Supersaturated solution feeds a seed',ha='center',fontsize=9)
ax=axes[0,1]
for x,r,c in [(1,.18,ORANGE),(2,.3,ORANGE),(4.8,.7,BLUE)]:
    ax.add_patch(Circle((x,2),r,color=c,alpha=.8))
arrow(ax,(2.6,2),(3.8,2),'Dissolve / redeposit')
ax.text(3,.35,'Curvature-dependent chemical potential',ha='center',fontsize=9)
ax=axes[0,2]
for x in [1,2]:
    ax.add_patch(Rectangle((x-.3,1.7),.6,.6,facecolor=BLUE,edgecolor='white'))
    for z in [.2,.4]:ax.plot([x-.3+z]*2,[1.7,2.3],color='white',lw=.7)
arrow(ax,(2.6,2),(3.8,2))
ax.add_patch(Rectangle((4,1.7),1.2,.6,facecolor=BLUE,edgecolor='white'))
ax.text(3,.35,'Aligned crystallites join and heal',ha='center',fontsize=9)
ax=axes[1,0]
centre=(.8,2.2)
ax.add_patch(RegularPolygon(centre,5,radius=.43,facecolor=BLUE,edgecolor='white'))
for angle in np.arange(5)*2*np.pi/5+np.pi/2:
    ax.plot([centre[0],centre[0]+.43*np.cos(angle)],[centre[1],centre[1]+.43*np.sin(angle)],color='white',lw=.7)
arrow(ax,(1.4,2.2),(2.4,2.2))
ax.add_patch(Rectangle((2.6,1.9),2.7,.6,facecolor=BLUE))
for yy in [2.05,2.25]:ax.plot([2.6,5.3],[yy,yy],color='white',lw=.8)
arrow(ax,(5.25,2.2),(5.85,2.2))
ax.text(3,.65,'Twinned seed + protected sides\npreferential axial addition',ha='center',fontsize=9)
ax=axes[1,1]
ax.add_patch(Rectangle((.4,2),.65,.22,facecolor=PURPLE))
ax.plot([.4,1.05],[2.11,2.11],color='white',lw=.8)
arrow(ax,(1.4,2.1),(2.3,2.1))
ax.add_patch(RegularPolygon((4,2.1),6,radius=1.15,orientation=np.pi/6,facecolor=PURPLE))
arrow(ax,(4,3.3),(4,3.8))
arrow(ax,(5.15,2.1),(5.8,2.1))
ax.text(3,.35,'Planar defect + basal-face protection\nlateral growth faster than thickening',ha='center',fontsize=9)
ax=axes[1,2]
ax.text(.2,3.3,'Growth mechanism: how material moves\n\nSymmetry breaking: which directions grow\n\nAnisotropic shape ≠ a new bulk lattice\n\nSpecific ligand and defect pathways vary',fontsize=10,va='top',linespacing=1.5)
fig.savefig('paper-2-growth-pathways.png',dpi=150,facecolor='white')
plt.close(fig)
