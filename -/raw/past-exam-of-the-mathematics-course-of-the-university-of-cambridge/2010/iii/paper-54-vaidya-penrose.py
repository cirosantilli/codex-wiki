"""Schematic double-null Penrose diagram. Python 3.14, numpy 2.3.5,
matplotlib 3.10.7. Write an opaque PNG basename to caller CWD.
MPLCONFIGDIR is owned by the caller and is not changed here.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def point(p, q):
    return ((q-p)/2, (q+p)/2)


def main():
    fig, ax = plt.subplots(figsize=(9, 6), facecolor="white")
    vertices=[point(-1,0),point(-1,1),point(0,1),point(1,0)]
    ax.add_patch(Polygon(vertices,closed=True,facecolor="#f3f7fb",edgecolor="none"))
    # p labels outgoing null rays, q labels ingoing null rays; both increase
    # to the future. The spacelike singularity is schematic p+q=1.
    q0, q1 = .30, .56
    band=[point(-1,q0),point(-1,q1),point(1-q1,q1),point(1-q0,q0)]
    ax.add_patch(Polygon(band,closed=True,facecolor="#deedce",edgecolor="none"))
    for qa in (q0,q1):
        p=np.linspace(-1,1-qa,160); x,y=point(p,qa+0*p)
        ax.plot(x,y,color="#498c3f",lw=1.3)
    # Past boundary of the ingoing chart. It is not a regular axis.
    x,y=point(np.linspace(-1,1,200),0);ax.plot(x,y,color="#606975",ls=":",lw=1.3)
    p=-np.ones(200);q=np.linspace(0,1,200);x,y=point(p,q)
    ax.plot(x,y,color="black",lw=1.8)
    p=np.linspace(-1,0,200);x,y=point(p,np.ones(200));ax.plot(x,y,color="black",lw=1.8)
    xx=np.linspace(-.5,.5,221); yy=.5+.009*np.sin(np.linspace(0,38*np.pi,len(xx)))
    ax.plot(xx,yy,color="black",lw=1.7)
    # Event horizon p=0; apparent horizon p>0 before final stationarity.
    q=np.linspace(0,1,400);x,y=point(0*q,q);ax.plot(x,y,color="#b3292d",lw=3)
    h=np.clip((q-q0)/(q1-q0),0,1);papp=.18*(1-3*h*h+2*h*h*h)
    x,y=point(papp,q);ax.plot(x,y,color="#2268ac",lw=2,ls="--")
    for pp,qa,qb in [(-.30,.60,1),(.20,.62,.80)]:
        x0,y0=point(pp,qa);x1,y1=point(pp,qb)
        ax.annotate("",(x1,y1),(x0,y0),arrowprops={"arrowstyle":"->","lw":1.7,"color":"#7356a7"})
    xa,ya=point(-.65,.43);xb,yb=point(-.18,.43)
    ax.annotate("",(xb,yb),(xa,ya),arrowprops={"arrowstyle":"->","lw":1.8,"color":"#376b30"})
    ax.text(.04,.565,"Future spacelike singularity  r = 0",ha="center",fontsize=12)
    ax.text(.90,.24,r"$\mathscr{I}^{+}$",fontsize=23)
    ax.text(.77,-.31,r"$\mathscr{I}^{-}$",fontsize=23)
    ax.text(1.03,0,r"$i^{0}$",fontsize=15)
    ax.text(.53,.51,r"$i^{+}$",fontsize=15)
    ax.annotate("Event horizon",point(0,.79),(.06,.36),fontsize=11,color="#a12427",
                arrowprops={"arrowstyle":"-","color":"#a12427"})
    ax.annotate("Apparent horizon\n(finally coincident)",point(.18,.17),(-.45,-.13),fontsize=10,color="#2268ac",
                arrowprops={"arrowstyle":"-","color":"#2268ac"})
    ax.text(.36,.04,"Accretion",fontsize=11,color="#376b30",rotation=-45)
    ax.text(.58,-.13,r"Initially $m=M_0$",fontsize=11,rotation=-45)
    ax.text(.67,.39,r"Finally $m=M_1$",fontsize=11,rotation=-45)
    ax.text(-.30,.23,"Black-hole interior",fontsize=11)
    ax.text(.49,-.48,"Future",fontsize=10)
    ax.annotate("",(.49,-.37),(.49,-.45),arrowprops={"arrowstyle":"->","color":"black"})
    ax.set_title("Accretion onto a pre-existing black hole",fontsize=15,pad=18)
    ax.text(.24,-.59,"Schematic: ingoing and outgoing null directions have slopes −1 and +1.\nOne exterior and the future interior; no regular centre is depicted.",
            ha="center",va="top",fontsize=10)
    ax.set_xlim(-.61,1.16);ax.set_ylim(-.68,.63);ax.set_aspect("equal");ax.axis("off")
    fig.savefig(Path(__file__).with_suffix(".png").name,dpi=140,facecolor="white",transparent=False,bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
