"""Original fixed-chord isoperimetric arc construction; output to cwd."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

half_chord,theta=1.0,1.05
radius=half_chord/np.sin(theta)
center=-radius*np.cos(theta)
x=np.linspace(-half_chord,half_chord,700)
y=np.sqrt(radius*radius-x*x)+center
fig,axes=plt.subplots(1,2,figsize=(9.2,4.5),layout="constrained")
for ax in axes:
    ax.axhline(0,color="#6d5d51",lw=1.4)
    ax.plot(x,y,color="#28739e",lw=2.6)
    ax.fill_between(x,0,y,color="#a1c9df",alpha=0.6)
    ax.scatter([-1,1],[0,0],color="#333333",s=24,zorder=4)
    ax.set_aspect("equal");ax.set_xlabel("Distance along the wall")
    ax.grid(alpha=0.14)
axes[0].plot([0,-1],[center,0],ls="--",color="#777777",lw=1)
axes[0].plot([0,1],[center,0],ls="--",color="#777777",lw=1)
axes[0].scatter([0],[center],color="#777777",s=20)
axes[0].annotate("R",(0.5,center/2),(0.7,center/2-0.2),arrowprops={"arrowstyle":"->"},fontsize=12)
axes[0].annotate("Fence length 2l",(0,y[len(y)//2]),(-0.85,0.88),arrowprops={"arrowstyle":"->"},fontsize=10)
axes[0].text(0,-0.16,"Wall chord 2a",ha="center",fontsize=11)
axes[0].set(xlim=(-1.4,1.4),ylim=(center-0.35,1.1),ylabel="Distance from the wall",title="The maximizing fence is a minor arc")
# The complementary arc runs from the left attachment around the bottom to right.
t=np.linspace(np.pi/2+theta,5*np.pi/2-theta,900)
xx=radius*np.cos(t);yy=center+radius*np.sin(t)
axes[1].plot(xx,yy,color="#777777",lw=2)
axes[1].fill_between(xx,yy,0,color="#d1d1d1",alpha=0.3)
# Use a circle clipped below the wall to fill the major segment without a
# nonmonotone-x fill artefact along its overhanging sides.
from matplotlib.patches import Circle,Rectangle
axes[1].collections[-1].remove()
patch=Circle((0,center),radius,color="#dedede",zorder=-1)
clip=Rectangle((-2,-4),4,4,transform=axes[1].transData)
patch.set_clip_path(clip)
axes[1].add_patch(patch)
axes[1].text(0,center-0.28,"Fixed major arc\nand fixed added area",ha="center",va="center",fontsize=10,color="#555555")
axes[1].text(0,0.18,"Fenced area",ha="center",fontsize=10)
axes[1].set(xlim=(-1.4,1.4),ylim=(center-radius-0.15,0.85),title="Complete to a fixed-perimeter curve")
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
plt.close(fig)
