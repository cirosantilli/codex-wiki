from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False, "figure.facecolor": "white", "savefig.facecolor": "white"})
from matplotlib.patches import Rectangle,Circle
fig,axs=plt.subplots(2,1,figsize=(10,5.2),layout="constrained")
def box(ax,x,y,txt,w=.6,h=.48):
 ax.add_patch(Rectangle((x-w/2,y-h/2),w,h,facecolor="white",edgecolor="#175c9e",lw=1.6,zorder=3));ax.text(x,y,txt,ha="center",va="center",zorder=4,fontsize=13)
for ax in axs:
 ax.set(xlim=(-.3,7.5),ylim=(-.5,1.5));ax.axis("off")
 for y,label in [(1,"a"),(0,"b")]:
  ax.plot([.3,7.1],[y,y],color="0.3",lw=1.3);ax.text(0,y,label,va="center",ha="center",fontsize=13)
ax=axs[0];box(ax,1.2,0,"H");box(ax,3,.5,"G",w=.9,h=1.5);box(ax,4.8,1,"Z");box(ax,4.8,0,"H")
ax.text(6.3,.5,"= CNOT",ha="center",va="center",fontsize=14)
ax.set_title("Apply from left to right: target H, ion gate G, control Z and target H")
ax=axs[1];ax.text(.3,1.35,r"Input $|g\rangle_a$",fontsize=10);ax.text(.3,-.4,r"Input $|g\rangle_b$",fontsize=10)
box(ax,1.2,1,"H");ax.plot([3,3],[0,1],color="#175c9e",lw=1.7)
ax.add_patch(Circle((3,1),.065,facecolor="#175c9e",edgecolor="#175c9e",zorder=3));ax.add_patch(Circle((3,0),.16,facecolor="white",edgecolor="#175c9e",lw=1.6,zorder=3));ax.plot([2.84,3.16],[0,0],color="#175c9e",lw=1.4,zorder=4);ax.plot([3,3],[-.16,.16],color="#175c9e",lw=1.4,zorder=4)
ax.text(5.3,.5,r"$\frac{|gg\rangle+|ee\rangle}{\sqrt{2}}$",ha="center",va="center",fontsize=20,bbox={"facecolor":"white","edgecolor":"none"})
ax.set_title("Bell-pair preparation: control H, then the synthesized CNOT")

fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
plt.close(fig)
