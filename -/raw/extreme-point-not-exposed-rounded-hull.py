"""Original rounded convex hull with an extreme but nonexposed contact point."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np


def main():
    P=np.array([2.,0.])
    T=np.array([.5,np.sqrt(3)/2])
    bottom=np.array([.5,-np.sqrt(3)/2])
    theta=np.linspace(np.pi/3,5*np.pi/3,601)
    arc=np.column_stack([np.cos(theta),np.sin(theta)])
    boundary=np.vstack([arc,P])
    assert np.isclose(T@P,1) and np.isclose(T@T,1)
    fig,ax=plt.subplots(figsize=(8.4,5.2),dpi=120,facecolor="white")
    ax.add_patch(Polygon(boundary,closed=True,facecolor="#e5eff4",edgecolor="#28738f",lw=2))
    x=np.linspace(-1.35,2.5,401)
    ax.plot(x,(1-T[0]*x)/T[1],color="#a85200",lw=2,label=r"Only support at T: $T\cdot z=1$")
    ax.plot([T[0],P[0]],[T[1],P[1]],color="#a85200",lw=4)
    ax.scatter(*T,color="#b2182b",s=70,zorder=5)
    ax.scatter(*P,color="#222222",s=55,zorder=5)
    ax.annotate(r"$T=(1/2,\sqrt{3}/2)$"+"\nExtreme, not exposed",T,xytext=(-1.2,1.30),
                fontsize=12,arrowprops=dict(arrowstyle="->",color="#b2182b"),
                bbox=dict(facecolor="white",edgecolor="none",alpha=.92,pad=2))
    ax.annotate(r"$P=(2,0)$",P,xytext=(1.6,-.38),fontsize=12)
    p=np.array([np.cos(2*np.pi/3),np.sin(2*np.pi/3)])
    tangent=np.array([-p[1],p[0]])
    t=np.linspace(-.6,.6,31)
    line=p+t[:,None]*tangent
    ax.plot(*line.T,color="#6b7780",ls="--",lw=1.2)
    ax.scatter(*p,color="#6b7780",s=40,zorder=5)
    ax.annotate("This arc point is exposed",p,xytext=(-1.28,-.1),fontsize=10.5,
                arrowprops=dict(arrowstyle="->",color="#6b7780"))
    ax.set(xlim=(-1.35,2.5),ylim=(-1.25,1.75),xlabel=r"$x$",ylabel=r"$y$")
    ax.set_aspect("equal");ax.grid(alpha=.18)
    ax.spines[["top","right"]].set_visible(False)
    ax.legend(loc="lower left",fontsize=10.5,frameon=False)
    fig.suptitle("Extremality does not guarantee a unique linear optimum",fontsize=16,weight="bold",y=.96)
    fig.text(.5,.025,"Hull of the unit disk and P. The sole supporting line at T contains the entire segment TP.",
             ha="center",fontsize=11)
    fig.subplots_adjust(left=.08,right=.96,top=.84,bottom=.15)
    fig.savefig(Path(__file__).stem+".png",facecolor="white",transparent=False)
    plt.close(fig)


if __name__=="__main__":
    main()
