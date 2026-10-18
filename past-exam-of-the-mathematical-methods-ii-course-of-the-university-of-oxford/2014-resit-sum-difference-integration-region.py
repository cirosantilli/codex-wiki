from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","savefig.transparent":False})

from matplotlib.patches import Rectangle
fig,(ax,bx)=plt.subplots(1,2,figsize=(9.7,4.6),layout="constrained")
ax.fill([0,3.2,3.2,0],[0,0,3.2,3.2],color="#e2eff6");ax.plot([0,3.2],[0,0],color="#b45636",lw=2.5);ax.plot([0,0],[0,3.2],color="#4c7397",lw=2.5)
ax.annotate("Positive quadrant\ncontinues to infinity",xy=(2.7,2.7),xytext=(.3,2.2),arrowprops={"arrowstyle":"->"},fontsize=11)
ax.text(1.5,.17,"y = 0 → v = 1",color="#b45636",ha="center",fontsize=11);ax.text(.1,1.35,"x = 0\n→ v = −1",color="#4c7397",fontsize=11)
ax.set(xlabel="x",ylabel="y",xlim=(-.15,3.3),ylim=(-.15,3.3),title="Original positive quadrant");ax.set_aspect("equal")
bx.add_patch(Rectangle((0,-1),4,2,facecolor="#e2eff6",edgecolor="none"));bx.plot([0,4],[1,1],color="#b45636",lw=2.5);bx.plot([0,4],[-1,-1],color="#4c7397",lw=2.5);bx.plot([0,0],[-1,1],ls=":",color="#555555",lw=2)
bx.annotate("continues",xy=(4.15,0),xytext=(2.4,0),arrowprops={"arrowstyle":"->"},ha="center")
bx.text(.2,-1.33,"u = 0 collapses to the original origin",fontsize=10)
bx.set(xlabel="u = x + y",ylabel="v = (x − y)/(x + y)",xlim=(-.2,4.3),ylim=(-1.5,1.5),title="Unbounded half-strip: u > 0, −1 ≤ v ≤ 1");bx.set_yticks([-1,0,1]);bx.grid(alpha=.1)
fig.suptitle("Sum and normalized difference; area element dx dy = (u/2) du dv",fontsize=14)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120)
plt.close(fig)
