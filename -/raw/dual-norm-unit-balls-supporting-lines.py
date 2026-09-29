"""Draw three unit balls and exact support points; output matching PNG in CWD."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np


def main():
    theta = np.linspace(0, 2*np.pi, 721)
    boundaries = [np.array([[1,0],[0,1],[-1,0],[0,-1]]), np.column_stack([np.cos(theta),np.sin(theta)]), np.array([[1,1],[-1,1],[-1,-1],[1,-1]])]
    a = np.array([2.,-1.])
    points = [np.array([1.,0.]), a/np.sqrt(5), np.array([1.,-1.])]
    bounds = [2.,np.sqrt(5),3.]
    labels = [r"$\|x\|_1\leq1$",r"$\|x\|_2\leq1$",r"$\|x\|_\infty\leq1$"]
    values = [r"$\|p\|_*=2$",r"$\|p\|_*=\sqrt{5}$",r"$\|p\|_*=3$"]
    fig, axes = plt.subplots(1,3,figsize=(12.3,4.6),dpi=120)
    fig.patch.set_facecolor("white")
    for ax,boundary,point,bound,label,value in zip(axes,boundaries,points,bounds,labels,values):
        assert np.isclose(a @ point,bound)
        ax.add_patch(Polygon(boundary,closed=True,facecolor="#dcebf2",edgecolor="#28738f",lw=2))
        t = np.linspace(-1.4,1.4,100)
        ax.plot(t,2*t-bound,color="#bf6529",lw=2,label="supporting line")
        ax.scatter(*point,color="#bf6529",s=55,zorder=5)
        ax.axhline(0,color="#aaaaaa",lw=.6)
        ax.axvline(0,color="#aaaaaa",lw=.6)
        ax.grid(color="#e5e5e5",lw=.5)
        ax.set(xlim=(-1.38,1.38),ylim=(-1.38,1.38),xlabel=r"$x_1$",ylabel=r"$x_2$")
        ax.set_aspect("equal")
        ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1])
        ax.set_title(label+"\n"+value,fontsize=15,pad=14)
        ax.spines[["top","right"]].set_visible(False)
    fig.suptitle(r"The same functional $p(x)=2x_1-x_2$, three input unit balls",fontsize=18,weight="bold")
    fig.text(.5,.035,r"Orange line: $2x_1-x_2=\|p\|_*$.  Its marked contact point attains the maximum.",ha="center",fontsize=12)
    fig.subplots_adjust(left=.055,right=.975,top=.73,bottom=.17,wspace=.28)
    fig.savefig(Path(__file__).stem+".png",facecolor="white",transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
