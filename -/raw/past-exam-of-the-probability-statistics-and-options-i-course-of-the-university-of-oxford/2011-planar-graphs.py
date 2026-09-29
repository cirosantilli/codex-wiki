"""Original planar embeddings for Oxford AS1 2011, question R1.

Writes 2011-planar-graphs.png in the process CWD, white background.
Tested: Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Dependencies: repository root pyproject.toml.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def draw(ax, extra):
    points={"a1":(-2,0),"a2":(2,0),"b1":(0,2),"b2":(0,0),"b3":(0,-2)}
    if extra:
        points["a3"]=(0,1)
    edges=[(a,b) for a in ["a1","a2"] for b in ["b1","b2","b3"]]
    if extra:
        edges += [("a3","b1"),("a3","b2")]
    for u,v in edges:
        x,y=points[u],points[v]
        ax.plot([x[0],y[0]],[x[1],y[1]],color="#52616b",lw=2,zorder=1)
    for name,xy in points.items():
        color="#b46321" if name[0]=="a" else "#176e9b"
        ax.scatter(*xy,s=220,color=color,edgecolor="white",linewidth=1.4,zorder=3)
        dx,dy={"a1":(-.34,0),"a2":(.34,0),"a3":(.31,0),"b1":(0,.32),"b2":(0,-.33),"b3":(0,-.33)}[name]
        ax.text(xy[0]+dx,xy[1]+dy,"$"+name[0]+"_"+name[1]+"$",ha="center",va="center",fontsize=12)
    ax.set(xlim=(-2.6,2.6),ylim=(-2.65,2.65))
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_facecolor("white")


def main():
    fig,axes=plt.subplots(1,2,figsize=(8.6,4.5),facecolor="white")
    draw(axes[0],True)
    draw(axes[1],False)
    axes[0].set_title(r"$K_{3,3}-a_3b_3$: no crossings",fontsize=13)
    axes[1].set_title(r"$K_{2,3}$: three faces",fontsize=13)
    axes[1].text(0,1,"1",ha="center",fontsize=15,color="#727d46")
    axes[1].text(0,-1,"2",ha="center",fontsize=15,color="#727d46")
    axes[1].text(1.75,1.65,"3 (exterior)",ha="center",fontsize=10,color="#727d46")
    fig.tight_layout(w_pad=3)
    fig.savefig("2011-planar-graphs.png",dpi=150,facecolor="white")
    plt.close(fig)


if __name__=="__main__":
    main()
