"""Original explanatory diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import os
import numpy as np
os.environ.setdefault("MPLCONFIGDIR", "/tmp/cambridge-nano2-matplotlib")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, RegularPolygon, FancyArrowPatch, Wedge
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "savefig.facecolor": "white"})

fig, axs=plt.subplots(2,3,figsize=(10,5.4),layout="constrained")
examples=[("Perfect local network",[6,6,6,6]),("Bond rotation (Stone–Wales)",[5,7,7,5]),("Reconstructed monovacancy",[5,9]),("Reconstructed divacancy",[5,8,5]),("Curvature / junction",[5,6,7])]
for ax,(title,ns) in zip(axs.flat,examples):
    for i,n in enumerate(ns):
        x=i*1.2
        ax.add_patch(RegularPolygon((x,0),n,radius=.65,orientation=np.pi/n,fill=False,ec="#246c99",lw=1.8))
        ax.text(x,0,str(n),ha="center",va="center")
    ax.set(title=title,xlim=(-.9,max(2.1,len(ns)*1.2-.3)),ylim=(-1,1),aspect="equal")
    ax.axis("off");ax.set_title(title,fontsize=10)
ax=axs.flat[-1]
for y in [.2,.5,.8]:
    ax.plot([0,2.7],[y,y],color="#246c99");ax.plot([0,2.7],[-y,-y],color="#246c99")
ax.plot([1.35,1.35],[.2,.5],color="#b23a37",lw=3)
ax.plot([1.9,2.15],[.8,.5],color="#b23a37",lw=3)
ax.annotate("Interwall bridges",xy=(1.95,.65),xytext=(.2,1.1),arrowprops=dict(arrowstyle="->"),fontsize=9)
ax.annotate("Broken outer wall",xy=(2.5,-.8),xytext=(.1,-1.35),arrowprops=dict(arrowstyle="->"),fontsize=9)
ax.plot([2.4,2.7],[-.8,-.8],color="white",lw=4)
ax.set(xlim=(-.2,3),ylim=(-1.6,1.5),aspect="equal");ax.axis("off");ax.set_title("Additional multiwall imperfections",fontsize=10)
fig.suptitle("Ring inventory and wall defects: schematic, not relaxed atomic coordinates",fontsize=12)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=145)
