"""Original explanatory diagram; Python 3.14, numpy and matplotlib (root pyproject)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Ellipse
plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.spines.top": False, "axes.spines.right": False})

fig,axes=plt.subplots(1,3,figsize=(11,3.6))
for ax in axes:
 ax.set(xlim=(-1.4,1.4),ylim=(-1.3,1.3),aspect='equal');ax.axis('off')
ax=axes[0];ax.add_patch(Circle((0,0),1,color='.35'));ax.add_patch(Circle((0,0),.75,color='.9'))
for xx,yy,rr in [(-.25,.22,.28),(.3,.05,.23),(-.2,-.35,.2)]:ax.add_patch(Circle((xx,yy),rr,color='white'))
ax.set_title('Possible porous projection',fontsize=11);ax.text(0,-1.23,'lighter voids / darker walls',ha='center',fontsize=9)
ax=axes[1];clip=Circle((0,0),1,facecolor='.88',edgecolor='.3');ax.add_patch(clip)
for x0 in np.arange(-1.3,1.3,.11):
 line,=ax.plot([x0,x0+1.6],[-1.1,1.1],color='.35',lw=.7);line.set_clip_path(clip)
ax.set_title('Local lattice fringes',fontsize=11);ax.text(0,-1.23,'crystallinity; orientation matters',ha='center',fontsize=9)
ax=axes[2]
for rr,col,lw in [(1.09,'.7',2),(1.03,'.15',2),(.97,'.8',2),(.90,'.25',2)]:ax.add_patch(Circle((0,0),rr,fill=False,color=col,lw=lw))
ax.set_title('Defocus-dependent edges',fontsize=11);ax.text(0,-1.23,'fringe width is not shell thickness',ha='center',fontsize=9)
fig.suptitle('Independent contrast mechanisms: a single projection does not fix 3D geometry',fontsize=12)
fig.tight_layout()
fig.savefig("paper-1-particle-interpretation.png", dpi=170, bbox_inches="tight", facecolor="white")
plt.close(fig)
