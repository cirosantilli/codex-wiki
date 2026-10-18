"""Causal quotients; Python 3.14, NumPy and Matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch
import numpy as np

COLORS=["#d9efdf", "#c4dff4", "#f8d4b8", "#ddd0ef"]

def regions(ax,xmin,xmax,tmin,tmax,kind):
    x=np.linspace(xmin,xmax,501);t=np.linspace(tmin,tmax,601)
    X,T=np.meshgrid(x,t)
    z=np.zeros_like(X,dtype=int)
    if kind=="time":z[:]=3
    else:
        z[T>=abs(X)]=1;z[T<=-abs(X)]=2
    ax.imshow(z,origin="lower",extent=(xmin,xmax,tmin,tmax),
              aspect="auto",cmap=ListedColormap(COLORS),vmin=0,vmax=3,
              interpolation="nearest")
    ax.axhline(0,color="#777777",lw=.7);ax.axvline(0,color="#777777",lw=.7)
    ax.plot(0,0,"ko",ms=3)
    ax.set_xlim(xmin,xmax);ax.set_ylim(tmin,tmax)


def main():
    fig,axs=plt.subplots(2,2,figsize=(11.6,9.2),dpi=100,facecolor="white")
    a,b,e,f=axs.flat
    for ax in (a,b):
        regions(ax,-3,3,-3,3,"ordinary")
        xx=np.linspace(-3,3,300)
        ax.plot(xx,abs(xx),"k",lw=1);ax.plot(xx,-abs(xx),"k",lw=1)
        ax.set_aspect("equal",adjustable="box")
    tt=np.linspace(0,3,400);xx=np.sqrt(1+tt**2)-1
    a.plot(xx,tt,color="#a41c32",lw=2.3)
    a.text(-2.6,2.5,"Accelerated charge",color="#a41c32",fontsize=10)
    a.set_title("(c) Minkowski spacetime")
    a.set_xlabel(r"$x$ (units $c^2/a$)");a.set_ylabel(r"$ct$ (units $c^2/a$)")
    beta=.6;tt=np.linspace(-3,3,100)
    b.plot(-beta*tt,tt,"--",color="#777777",lw=1)
    b.plot(tt,-beta*tt,"--",color="#777777",lw=1)
    b.text(-2.8,2.45,"Old time axis",fontsize=9)
    b.text(1.25,-1.1,"Old spatial axis",fontsize=9,rotation=-30)
    b.set_title("(d) Boosted coordinates, beta = 0.6")
    b.set_xlabel(r"$x'$ (common length unit)");b.set_ylabel(r"$ct'$ (same unit)")
    regions(e,-1,1,-2.5,5,"space")
    xx=np.linspace(-1,1,300)
    e.plot(xx,abs(xx),"k",lw=1);e.plot(xx,-abs(xx),"k",lw=1)
    for edge in (-1,1):e.axvline(edge,color="#555555",ls="--",lw=2)
    tt=np.linspace(0,5,2400);cover=np.sqrt(1+9*tt**2)/3-1/3
    wrap=(cover+1)%2-1;wrap[np.r_[False,abs(np.diff(wrap))>1]]=np.nan
    e.plot(wrap,tt,color="#a41c32",lw=2.1)
    for n in (1,2):
        treturn=np.sqrt((1+6*n)**2-1)/3
        if treturn<5:e.plot(0,treturn,"o",color="#a41c32",ms=4)
    e.text(.05,4.6,"Same position, later laps",fontsize=9,color="#a41c32")
    e.set_xticks([-1,0,1],labels=[r"$-P/2$","0",r"$P/2$"])
    e.set_title("(e) Spatial circle: vertical edges identified")
    e.set_xlabel(r"Position on the circle ($P=2$ in these units)")
    e.set_ylabel(r"$ct$ (same unit; noncompact)")
    regions(f,-2,2,-1,1,"time")
    f.axhline(-1,color="#555555",ls="--",lw=2);f.axhline(1,color="#555555",ls="--",lw=2)
    f.annotate("",xy=(0,.85),xytext=(0,-.85),arrowprops={"arrowstyle":"->","color":"#a41c32","lw":2.3})
    f.text(.12,.48,"Closed timelike curve",fontsize=10,color="#a41c32")
    f.text(-1.75,-.52,"Every event is in both\ncausal future and causal past",fontsize=10)
    f.set_yticks([-1,0,1],labels=[r"$-cP_t/2$","0",r"$cP_t/2$"])
    f.set_title("(f) Time circle: horizontal edges identified")
    f.set_xlabel(r"Noncompact $x$");f.set_ylabel(r"Periodic $ct$")
    fig.legend(handles=[Patch(facecolor=col,label=label) for col,label in zip(COLORS,["Neither","Future","Past","Both"])],
               loc="lower center",ncol=4,frameon=False,bbox_to_anchor=(.5,.012))
    fig.tight_layout(rect=(0,.06,1,1),h_pad=2,w_pad=2)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,
                facecolor="white",transparent=False,metadata={"Software":"Codex Wiki"})
    plt.close(fig)

if __name__=="__main__":main()
