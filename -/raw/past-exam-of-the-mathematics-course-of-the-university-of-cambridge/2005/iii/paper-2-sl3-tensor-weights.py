"""Draw original weight diagrams; write same-basename opaque PNG to caller CWD."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 11})
def finish(fig):
    fig.set_facecolor("white")
    fig.tight_layout()
    fig.savefig(Path.cwd()/(Path(__file__).stem+".png"), dpi=130,
                facecolor="white", transparent=False)
    plt.close(fig)

L=np.array([[1.0,0.0],[-0.5,np.sqrt(3)/2],[-0.5,-np.sqrt(3)/2]])
def setup(ax, compact=False):
    for j,l in enumerate(L):
        ax.annotate("", .82*l, (0,0), arrowprops={"arrowstyle":"->","lw":.8,"color":"#aeb8c1"})
        ax.text(*(.95*l), rf"$L_{j+1}$", fontsize=9, color="#75818b", ha="center")
    ax.scatter([0],[0],marker="+",color="#aeb8c1",s=24)
    ax.set_aspect("equal")
    ax.set(xticks=[],yticks=[],xlim=(-1.55,1.55) if compact else (-3.15,2.75),
           ylim=(-1.5,1.6) if compact else (-3.15,3.2))
    for spine in ax.spines.values():spine.set_visible(False)
def put(ax,pt,label,highest=False,dy=9):
    ax.scatter([pt[0]],[pt[1]],s=42,color="#ae3f35" if highest else "#256c96",zorder=3)
    ax.annotate(label,pt,xytext=(0,dy),textcoords="offset points",
                ha="center",va="bottom",fontsize=10,color="#ae3f35" if highest else "#243847")

from collections import defaultdict
groups=defaultdict(list)
for i in range(3):
    for j in range(3):
        for k in range(j,3):
            weight=L[i]-L[j]-L[k]
            key=tuple(np.round(weight,8))
            groups[key].append((i+1,j+1,k+1))
fig,ax=plt.subplots(figsize=(7.0,6.8))
setup(ax)
for pt,basis in groups.items():
    label="\n".join(rf"$T_{{{i};{j}{k}}}$" for i,j,k in basis)
    put(ax,pt,label,highest=basis==[(1,3,3)])
ax.set_title(r"$W=V\otimes\mathrm{Sym}^2(V^*)$: 18 basis vectors")
ax.text(.5,-.02,"Tensors sharing a point form its complete weight-space basis.",
        transform=ax.transAxes,ha="center",fontsize=10)
finish(fig)
