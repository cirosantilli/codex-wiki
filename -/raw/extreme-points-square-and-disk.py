"""Original convex-set examples separating boundary from extremality."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
import numpy as np


def main():
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 5.0), dpi=120, facecolor="white")
    ax = axes[0]
    ax.add_patch(Rectangle((-1,-1), 2, 2, facecolor="#e5eff4", edgecolor="#28738f", lw=2))
    ax.plot([1,1], [-1,1], color="#a85200", lw=4, label="All maximize x")
    corners=np.array([[-1,-1],[1,-1],[1,1],[-1,1]])
    ax.scatter(*corners.T, color="#b2182b", s=55, zorder=5, label="Extreme points")
    ax.scatter(1, 0, color="#a85200", marker="D", s=55, zorder=6)
    ax.annotate(r"$(1,0)=\frac{1}{2}(1,-1)+\frac{1}{2}(1,1)$", (1,0), xytext=(-.95,.35),
                fontsize=11, arrowprops=dict(arrowstyle="->",color="#a85200"))
    ax.set_title("Square: only four corners are extreme", fontsize=13)
    ax.text(-1.33,-1.27,"The right edge maximizes x",fontsize=11,color="#a85200")
    ax = axes[1]
    ax.add_patch(Circle((0,0), 1, facecolor="#e5eff4", edgecolor="#b2182b", lw=2.5))
    theta=np.pi/3
    p=np.array([np.cos(theta),np.sin(theta)])
    tangent=np.array([-p[1],p[0]])
    t=np.linspace(-1.3,1.3,101)
    line=p+t[:,None]*tangent
    ax.plot(*line.T, color="#a85200", lw=2)
    ax.scatter(*p,color="#a85200",s=60,zorder=5)
    ax.annotate(r"$p=(1/2,\sqrt{3}/2)$",p,xytext=(-1.25,1.33),fontsize=11,
                arrowprops=dict(arrowstyle="->",color="#a85200"))
    ax.text(-1.33,-1.27,r"$p\cdot z\leq1$; equality only at $z=p$",fontsize=11)
    ax.set_title("Disk: every boundary point is extreme",fontsize=13)
    for ax in axes:
        ax.set_aspect("equal")
        ax.set(xlim=(-1.55,1.55),ylim=(-1.5,1.55),xlabel=r"$x$",ylabel=r"$y$")
        ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1])
        ax.grid(alpha=.18)
        ax.spines[["top","right"]].set_visible(False)
    fig.suptitle("Boundary points need not be extreme; extreme points need not look like corners",
                 fontsize=15,weight="bold",y=.97)
    fig.text(.5,.025,"Orange marks an optimizing supporting line; red marks the extreme points.",ha="center",fontsize=11)
    fig.subplots_adjust(left=.07,right=.98,top=.82,bottom=.24,wspace=.27)
    fig.savefig(Path(__file__).stem+".png",facecolor="white",transparent=False)
    plt.close(fig)


if __name__=="__main__":
    main()
