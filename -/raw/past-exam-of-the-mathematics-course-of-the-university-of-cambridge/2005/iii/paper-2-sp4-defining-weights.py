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

roots=[(2,0),(-2,0),(0,2),(0,-2),(1,1),(1,-1),(-1,1),(-1,-1)]
def panel(ax,weights,title,highest=None):
    ax.set_aspect("equal")
    ax.axhline(0,lw=.8,color="#9faeb8");ax.axvline(0,lw=.8,color="#9faeb8")
    ax.set(xlim=(-2.55,2.55),ylim=(-2.55,2.55),xticks=range(-2,3),yticks=range(-2,3),
           xlabel=r"$L_1$ coefficient",ylabel=r"$L_2$ coefficient",title=title)
    ax.grid(alpha=.15)
    for (x,y),multiplicity in weights.items():
        color="#ae3f35" if highest==(x,y) else "#256c96"
        ax.scatter([x],[y],s=48*multiplicity,color=color,zorder=3)
        ax.annotate(str(multiplicity),(x,y),xytext=(7,8),textcoords="offset points",
                    color=color,fontsize=12)

fig,ax=plt.subplots(figsize=(4.9,4.9))
panel(ax,{(1, 0): 1, (-1, 0): 1, (0, 1): 1, (0, -1): 1},'$V$: dimension 4')
fig.text(.5,.01,"Numbers at points are weight multiplicities.",ha="center",fontsize=10)
finish(fig)
