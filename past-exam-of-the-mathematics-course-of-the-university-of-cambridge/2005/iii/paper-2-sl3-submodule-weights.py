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

fig,axes=plt.subplots(1,2,figsize=(11.2,6.4),gridspec_kw={"width_ratios":[1.6,1]})
ax,dual=axes
setup(ax)
for i in range(3):
    for j in range(3):
        if i!=j:
            put(ax,L[i]-2*L[j],rf"$T_{{{i+1};{j+1}{j+1}}}$",highest=(i==0 and j==2))
    others=[j for j in range(3) if j!=i]
    put(ax,2*L[i],rf"$T_{{{i+1};{others[0]+1}{others[1]+1}}}$")
for j in range(3):
    put(ax,-L[j],rf"$K_{{{j+1},1}}$"+"\n"+rf"$K_{{{j+1},2}}$")
setup(dual,compact=True)
for j in range(3):
    put(dual,-L[j],rf"$-L_{j+1}: Q_{j+1}$",highest=(j==2))
ax.set_title(r"$\ker C=\Gamma_{1,2}$ (dimension 15)")
dual.set_title(r"$\iota(V^*)=\Gamma_{0,1}$ (dimension 3)")
fig.text(.5,.025,"Basis vectors at each point; red marks a highest-weight vector.",
         ha="center",fontsize=10)
finish(fig)
