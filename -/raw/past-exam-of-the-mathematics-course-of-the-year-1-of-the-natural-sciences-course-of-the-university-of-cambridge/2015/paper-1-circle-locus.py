"""Original exam-solution illustration; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    t=np.linspace(0,2*np.pi,600)
    fig,ax=plt.subplots(figsize=(6.1,5.1),layout="constrained",facecolor="white")
    ax.plot(1+2*np.cos(t),2*np.sin(t),color="#17648e",lw=2.5)
    ax.axhline(0,color="0.6",lw=.8);ax.axvline(0,color="0.6",lw=.8)
    ax.scatter([1],[0],color="#b84732",zorder=5)
    ax.annotate("Centre (1, 0)",(1,0),xytext=(1.12,.23),fontsize=10)
    ax.plot([1,1],[0,2],ls="--",color="#b84732",lw=1.3)
    ax.text(1.08,1.05,"Radius 2",color="#b84732")
    for xy,delta,label in [((-1,0),(-.32,-.34),"(−1, 0)"),((3,0),(-.47,-.34),"(3, 0)"),((0,np.sqrt(3)),(-1.25,.12),r"$(0,\sqrt{3})$"),((0,-np.sqrt(3)),(-1.43,-.31),r"$(0,-\sqrt{3})$")]:
        ax.scatter(*xy,s=23,color="#17648e",zorder=4)
        ax.text(xy[0]+delta[0],xy[1]+delta[1],label,fontsize=10)
    ax.set(xlim=(-1.7,3.7),ylim=(-2.55,2.45),xlabel="$x$",ylabel="$y$",title=r"$(x-1)^2+y^2=4$")
    ax.set_aspect("equal");ax.grid(alpha=.15)
    fig.savefig(Path("paper-1-circle-locus.png"),dpi=160,facecolor="white");plt.close(fig)


if __name__ == "__main__":
    main()
