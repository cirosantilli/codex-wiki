"""Python 3.14; NumPy and Matplotlib in ../pyproject.toml. Output in CWD."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig,axs=plt.subplots(1,2,figsize=(8,3.8),facecolor="white")
ax=axs[0]
for j in range(-1,2):
 ax.plot([-1,1],[j,j],color=".55",lw=1)
 ax.plot([j,j],[-1,1],color=".55",lw=1)
for i in [-1,0]:
 for j in [-1,0]:ax.plot([i,i+1],[j,j+1],color=".6",lw=1)
ax.fill([0,1,1],[0,0,1],color="C0",alpha=.15)
ax.scatter([0,1,1],[0,0,1],s=22,color="C0")
ax.text(.03,.08,"1");ax.text(.86,.08,"2");ax.text(.86,.84,"3")
ax.set(title="Same positive diagonal in every square")
ax=axs[1]
ax.plot([-1,1],[0,0],color="C0",lw=2)
ax.plot([0,0],[-1,1],color="C0",lw=2)
ax.plot([-1,1],[-1,1],color=".7",ls="--",lw=1)
ax.scatter([0,-1,1,0,0],[0,0,0,-1,1],s=130,facecolor="white",edgecolor="C0",zorder=4)
for x,y,s in [(0,0,"4"),(-1,0,"-1"),(1,0,"-1"),(0,-1,"-1"),(0,1,"-1")]:
 ax.text(x,y,s,ha="center",va="center",zorder=5,fontsize=9)
ax.text(.72,.86,"0",color=".4");ax.text(-.93,-.83,"0",color=".4")
ax.set(title="Assembled couplings at the central node")
for ax in axs:
 ax.set_aspect("equal");ax.set_xlim(-1.25,1.25);ax.set_ylim(-1.25,1.25);ax.axis("off")
fig.tight_layout();fig.savefig("2009-triangle-stencil.png",dpi=150,facecolor="white")
