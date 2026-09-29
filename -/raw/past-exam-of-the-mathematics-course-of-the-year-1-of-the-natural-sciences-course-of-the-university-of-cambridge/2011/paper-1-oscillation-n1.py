"""Original mathematical illustration; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def phase_segments():
    # Sampling the tangent phase resolves each oscillation without connecting poles.
    positive=np.unique(np.r_[np.linspace(.00001,10,4001),np.arange(10,800,.07)])
    negative=-positive[::-1]
    return [(np.arctan(positive)-np.pi,positive),
            (np.arctan(negative),negative),
            (np.arctan(positive),positive),
            (np.arctan(negative)+np.pi,negative)]


def draw_curves(ax,n):
    a=np.pi/2
    for x,phase in phase_segments():
        values=((x-a)/x)**n*np.sin(phase)
        ax.plot(x,values,color="#17648e",lw=.8)


def main():
    a=np.pi/2
    n=1
    fig,ax=plt.subplots(figsize=(9,4.9),layout="constrained",facecolor="white")
    draw_curves(ax,n)
    for pole in [-a,a]:
        ax.axvline(pole,color=".55",ls="--",lw=.8)
    if n==2:ax.axvline(0,color=".55",ls="--",lw=.8)
    ax.axhline(0,color=".6",lw=.7)
    ax.scatter([-a,0,a],[0,0,0],s=31,color="#ad4731",zorder=7,label="Assigned value zero")
    if n==1:
        ax.scatter([0],[-a],s=49,facecolor="white",edgecolor="#17648e",lw=1.5,zorder=8,label=r"Missing limit value $-\pi/2$")
    ax.set_xticks([-np.pi,-a,0,a,np.pi],[r"$-\pi$",r"$-\pi/2$","0",r"$\pi/2$",r"$\pi$"])
    ax.set(xlim=(-np.pi,np.pi),ylim=(-3, 3),xlabel="$x$",ylabel=rf"$f_{n}(x)$",title='Linear suppression: $f_1(x)$')
    ax.grid(alpha=.16)
    ax.legend(loc="lower left",fontsize=8)
    if n>0:
        zoom=ax.inset_axes([.65,.64,.31,.3])
        draw_curves(zoom,n)
        xx=np.linspace(a-.2,a+.2,700)
        envelope=np.abs((xx-a)/xx)**n
        zoom.plot(xx,envelope,color="#bc8a54",ls="--",lw=.9)
        zoom.plot(xx,-envelope,color="#bc8a54",ls="--",lw=.9)
        zoom.scatter([a],[0],color="#ad4731",s=14,zorder=8)
        zoom.axvline(a,color=".6",lw=.7)
        zoom.set(xlim=(a-.18,a+.18),ylim=(-0.145, 0.145),title=r"Near $\pi/2$: shrinking envelope")
        zoom.set_xticks([a],[r"$\pi/2$"])
        zoom.tick_params(labelsize=7)
        zoom.title.set_fontsize(8)
    fig.savefig(Path(__file__).with_suffix(".png").name,dpi=160,facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
