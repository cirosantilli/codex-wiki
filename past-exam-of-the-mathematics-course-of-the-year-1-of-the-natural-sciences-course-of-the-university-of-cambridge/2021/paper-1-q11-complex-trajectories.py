"""Original complex trajectories. Python 3.14.4; root pyproject.toml deps.

Run from the desired output directory; writes the PNG basename into cwd.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def arrow(ax, points, j, color):
    a, b = points[j], points[j+65]
    ax.annotate("", (b.real,b.imag), (a.real,a.imag), arrowprops={"arrowstyle":"-|>","color":color,"lw":1.7})


def main():
    t=np.linspace(.5,2,1001)
    z=t+1j/t; u=z*z; v=u*u
    fig,axes=plt.subplots(1,3,figsize=(12,4.7),layout="constrained",facecolor="white")
    ax=axes[0]
    for points,color,label in [(z,"#205e9b","$z$"),(z.conjugate(),"#b16b20","$z^*$")]:
        ax.plot(points.real,points.imag,color=color,lw=2,label=label)
        arrow(ax,points,400,color)
        ax.plot([points[0].real,points[-1].real],[points[0].imag,points[-1].imag],"o",color=color,ms=4)
    for xy,label,offset in [((.5,2),"$(1/2,2)$",(4,9)),((2,.5),"$(2,1/2)$",(-5,10)),((.5,-2),"$(1/2,-2)$",(4,-17)),((2,-.5),"$(2,-1/2)$",(-5,-17))]:
        ax.annotate(label,xy,offset,textcoords="offset points",fontsize=9)
    ax.set(xlim=(-.1,2.65),ylim=(-2.6,2.6),title="Reciprocal-coordinate hyperbolas")
    ax.legend(loc="upper right")
    ax=axes[1]
    ax.plot(u.real,u.imag,color="#205e9b",lw=2)
    arrow(ax,u,350,"#205e9b")
    ax.plot([-15/4,0,15/4],[2,2,2],"o",color="#205e9b",ms=4)
    ax.annotate("$(-15/4,2)$",(-15/4,2),(0,10),textcoords="offset points",ha="center",fontsize=9)
    ax.annotate("$(15/4,2)$",(15/4,2),(0,10),textcoords="offset points",ha="center",fontsize=9)
    ax.annotate("$(0,2)$\n$t=1$",(0,2),(4,-32),textcoords="offset points",fontsize=9)
    ax.set(xlim=(-5.2,5.2),ylim=(-.3,3.3),title="$u=z^2$: horizontal segment")
    ax=axes[2]
    ax.plot(v.real,v.imag,color="#205e9b",lw=2)
    for j in [120,500,820]:arrow(ax,v,j,"#205e9b")
    for xy,label,offset,ha in [((161/16,-15),"$(161/16,-15)$",(-5,-17),"right"),((161/16,15),"$(161/16,15)$",(-5,10),"right"),((0,-8),"$(0,-8)$",(5,-9),"left"),((0,8),"$(0,8)$",(5,4),"left"),((-4,0),"$(-4,0)$",(5,-16),"left")]:
        ax.plot(*xy,"o",color="#205e9b",ms=4)
        ax.annotate(label,xy,offset,textcoords="offset points",fontsize=8.8,ha=ha)
    ax.set(xlim=(-6,13),ylim=(-19,19),title=r"$v=z^4$: $X=Y^2/16-4$")
    for ax in axes:
        ax.axhline(0,color="0.5",lw=.8)
        ax.axvline(0,color="0.5",lw=.8)
        ax.set(xlabel="Real part",ylabel="Imaginary part")
        ax.set_facecolor("white")
        ax.spines[["top","right"]].set_visible(False)
        ax.grid(alpha=.15)
    fig.savefig(Path(__file__).with_suffix(".png").name,dpi=150,facecolor="white")
    plt.close(fig)


if __name__=="__main__":
    main()
