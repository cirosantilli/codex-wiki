"""Original solution illustration; output the matching PNG into the cwd."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patches
plt.rcParams.update({"font.size":12,"figure.facecolor":"white"})

fig,ax=plt.subplots(figsize=(10.4,5),layout="constrained")
def wire(xs,ys):ax.plot(xs,ys,color="#30343a",lw=1.6)
def resistor(x,y,width,label):
    ax.add_patch(patches.Rectangle((x,y-.13),width,.26,facecolor="white",edgecolor="#30343a",lw=1.6));ax.text(x+width/2,y+.22,label,ha="center")
def ground(x,y):
    for dy,w in [(0,.22),(-.09,.15),(-.18,.07)]:wire([x-w,x+w],[y+dy,y+dy])
ax.add_patch(patches.Polygon([[4.8,-.3],[4.8,2.5],[7,1.1]],facecolor="#e6eff3",edgecolor="#30343a",lw=1.8))
ax.text(5.02,1.72,"−",fontsize=18,ha="center");ax.text(5.02,.37,"+",fontsize=16,ha="center")
wire([.2,1],[2.8,2.8]);resistor(1,2.8,1.2,r"$R$");wire([2.2,3.9,3.9,4.8],[2.8,2.8,1.75,1.75])
wire([.2,1],[1.75,1.75]);resistor(1,1.75,1.2,r"$R/2$");wire([2.2,4.8],[1.75,1.75]);ax.scatter([3.9],[1.75],s=20,color="#30343a")
ax.text(.05,2.8,r"$V_a$",ha="right",va="center");ax.text(.05,1.75,r"$V_b$",ha="right",va="center")
wire([4.8,4.2,4.2],[.4,.4,-.45]);ground(4.2,-.45)
wire([7,8.5],[1.1,1.1]);ax.text(8.65,1.1,r"$V_{\mathrm{out}}$",va="center")
wire([7.7,7.7,6.1],[1.1,4,4]);resistor(4.8,4,1.3,r"$R_f=2R$");wire([4.8,3.9,3.9],[4,4,1.75]);ax.scatter([7.7],[1.1],s=20,color="#30343a")
ax.text(5.8,-1.05,r"$V_{\mathrm{out}}=-2(V_a+2V_b)$",ha="center",fontsize=15)
ax.set(xlim=(-.6,10),ylim=(-1.5,4.6));ax.set_aspect("equal");ax.axis("off")

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
