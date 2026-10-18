from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon
plt.rcParams.update({"font.size":12,"font.family":"DejaVu Sans","figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

fig,ax=plt.subplots(figsize=(9,5.3));ax.set(xlim=(-.7,10.7),ylim=(-2.05,4.5));ax.axis("off")
def wire(xs,ys):ax.plot(xs,ys,color="#223641",lw=1.7)
def box(x0,x1,y,label):
 ax.add_patch(Rectangle((x0,y-.23),x1-x0,.46,facecolor="white",edgecolor="#223641",lw=1.6));ax.text((x0+x1)/2,y,label,ha="center",va="center",fontsize=14)
wire([0,0,.8],[1.5,3,3]);wire([.8,.8,1.3],[3,3.65,3.65]);box(1.3,3.2,3.65,r"$r_V$");wire([3.2,3.8,3.8],[3.65,3.65,3]);wire([.8,.8,1.3],[3,2.35,2.35]);box(1.3,3.2,2.35,r"$L_V$");wire([3.2,3.8,3.8,5],[2.35,2.35,3,3])
wire([5,6.5],[3,3]);box(6.5,8.3,3,r"$L_1$");wire([8.3,10,10],[3,3,1.5])
wire([0,0,1.3],[1.5,0,0]);box(1.3,3.2,0,r"$R_1$");wire([3.2,5,6.1],[0,0,0]);box(6.1,7.4,0,r"$R$");wire([7.4,8],[0,0]);box(8,9.3,0,r"$L$");wire([9.3,10,10],[0,0,1.5])
wire([5,5],[3,1.9]);wire([5,5],[1.1,0]);ax.add_patch(Circle((5,1.5),.4,facecolor="white",edgecolor="#223641",lw=1.6));ax.text(5,1.5,"A",ha="center",va="center",fontsize=15);ax.text(5.65,1.5,"Null detector",va="center",fontsize=11)
wire([0,0,4.55],[1.5,-1.5,-1.5]);wire([5.45,10,10],[-1.5,-1.5,1.5]);ax.add_patch(Circle((5,-1.5),.45,facecolor="white",edgecolor="#223641",lw=1.6));ax.text(5,-1.5,"~",ha="center",va="center",fontsize=24)
ax.scatter([0,10,5,5,.8,3.8],[1.5,1.5,3,0,3,3],s=21,color="#223641");ax.text(2.3,4.1,"Parallel variable arm",ha="center",fontsize=11);ax.text(7.8,-.58,"Series non-ideal inductor",ha="center",fontsize=11)
ax.set_title("AC bridge: equal midpoint voltages at balance",fontsize=15);fig.tight_layout()

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=140, facecolor="white", transparent=False)
plt.close(fig)
