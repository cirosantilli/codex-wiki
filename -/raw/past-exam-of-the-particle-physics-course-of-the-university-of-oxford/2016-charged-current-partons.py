from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch
plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans", "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})

fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.9))
for ax, anti in zip(axes, [False, True]):
 ax.set(xlim=(-.25, 4.25), ylim=(-.65, 3.75)); ax.axis("off")
 for x0, x1, y in [(0, 2, 3), (2, 4, 3), (0, 2, 0), (2, 4, 0)]:
  ax.plot([x0,x1],[y,y], color="#234e70", lw=2)
  direction = -1 if anti and y==3 else 1
  mid=(x0+x1)/2; ax.annotate("", xy=(mid+.22*direction,y), xytext=(mid-.22*direction,y), arrowprops=dict(arrowstyle="-|>",color="#234e70",lw=1.6))
 t=np.linspace(0,1,350); ax.plot(2+.085*np.sin(2*np.pi*9*t),3*t,color="#a43a36",lw=1.8)
 ax.scatter([2,2],[0,3],s=22,color="black",zorder=4)
 lefttop,righttop,leftbottom,rightbottom=(r"$e^+$",r"$\bar\nu_e$",r"$d$",r"$u$") if anti else (r"$e^-$",r"$\nu_e$",r"$u$",r"$d$")
 for x,y,txt in [(0,3.3,lefttop),(4,3.3,righttop),(0,-.35,leftbottom),(4,-.35,rightbottom)]:ax.text(x,y,txt,ha="center",va="center",fontsize=15)
 ax.text(2.2,1.45,r"$W^+$" if anti else r"$W^-$",color="#a43a36",fontsize=14)
 ax.set_title("Positron on a valence down quark" if anti else "Electron on a valence up quark",fontsize=12)
fig.text(.5,.035,"External momenta run left to right; arrows show fermion-number flow.",ha="center",fontsize=11)
fig.subplots_adjust(left=.03,right=.98,bottom=.13,top=.85,wspace=.25)

fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=140, facecolor="white", transparent=False)
plt.close(fig)
