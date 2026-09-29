"""Original exam-solution illustration; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    x=np.linspace(.006,np.pi-.006,1000)
    fig,ax=plt.subplots(figsize=(6.6,4.1),layout="constrained",facecolor="white")
    ax.plot(x,np.log(np.sin(x)),color="#17648e",lw=2.5)
    ax.axhline(0,color="0.6",lw=.8)
    ax.axvline(0,color="#b84732",ls="--",lw=1.4)
    ax.axvline(np.pi,color="#b84732",ls="--",lw=1.4)
    ax.scatter([np.pi/2],[0],s=30,color="#b84732",zorder=5)
    ax.annotate(r"Maximum $(\pi/2,0)$",(np.pi/2,0),xytext=(np.pi/2,.35),ha="center")
    ax.set(xlim=(-.12,np.pi+.12),ylim=(-4.3,.65),xlabel="$x$",ylabel="$y$",title=r"$y=\ln(\sin x)$, $0<x<\pi$")
    ax.set_xticks([0,np.pi/2,np.pi],["0",r"$\pi/2$",r"$\pi$"])
    ax.grid(alpha=.15)
    fig.savefig(Path("paper-1-log-sine.png"),dpi=160,facecolor="white");plt.close(fig)


if __name__ == "__main__":
    main()
