"""Original mathematical illustration; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def position(t):
    return ((4*np.pi-t)*np.sin(t),(4*np.pi-t)*np.cos(t))


def main():
    fig,ax=plt.subplots(figsize=(6.8,6.7),layout="constrained",facecolor="white")
    t=np.linspace(0,4*np.pi,2001)
    x,y=position(t)
    ax.plot(x,y,color="#17648e",lw=2)
    for start in [1.,3.5,5.7,7.7,9.7,11.5]:
        ax.annotate("",xy=position(start+.15),xytext=position(start),arrowprops={"arrowstyle":"->","color":"#b34b30","lw":1.8})
    ax.scatter([0,7*np.pi/2,0,0,0],[4*np.pi,0,-3*np.pi,2*np.pi,0],color="#17648e",s=24,zorder=5)
    ax.annotate(r"start $(0,4\pi)$",(0,4*np.pi),(1,12.8),fontsize=10)
    ax.annotate(r"$P=(7\pi/2,0)$",(7*np.pi/2,0),(6.2,2),fontsize=10,arrowprops={"arrowstyle":"->","color":".4"})
    ax.annotate(r"$(0,-3\pi)$",(0,-3*np.pi),(1,-10.4),fontsize=10)
    ax.annotate(r"$(0,2\pi)$",(0,2*np.pi),(-5.6,6.8),fontsize=10)
    ax.annotate("end",(0,0),(-3.2,-2.8),fontsize=10,arrowprops={"arrowstyle":"->","color":".4"})
    ax.axhline(0,color=".6",lw=.7)
    ax.axvline(0,color=".6",lw=.7)
    ax.set(xlim=(-11,13.5),ylim=(-11.5,14),xlabel="$x$",ylabel="$y$",title="Two clockwise inward turns")
    ax.set_aspect("equal")
    ax.grid(alpha=.18)
    fig.savefig(Path(__file__).with_suffix(".png").name,dpi=160,facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
