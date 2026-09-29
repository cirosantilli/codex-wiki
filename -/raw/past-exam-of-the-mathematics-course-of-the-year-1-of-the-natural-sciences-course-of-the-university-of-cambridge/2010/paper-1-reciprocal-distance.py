"""Original mathematical illustration; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    fig,ax=plt.subplots(figsize=(8,4.7),layout="constrained",facecolor="white")
    for left,right in [(-4,2.98),(3.02,10)]:
        x=np.linspace(left,right,1000)
        ax.plot(x,2/np.abs(x-3),color="#17648e",lw=2)
    ax.axvline(3,color="#ab5133",ls="--",lw=1,label="$x=3$")
    ax.axhline(0,color=".4",ls="--",lw=1,label="$y=0$")
    ax.scatter([0],[2/3],color="#17648e",s=28,zorder=5)
    ax.annotate(r"$(0,2/3)$",(0,2/3),(-2.7,1.8),fontsize=10,arrowprops={"arrowstyle":"->","color":".4"})
    ax.set(xlim=(-4,10),ylim=(-.15,6.3),xlabel="$x$",ylabel="$y$",title=r"$y=2/|x-3|$")
    ax.grid(alpha=.18)
    ax.legend(loc="upper right")
    fig.savefig(Path(__file__).with_suffix(".png").name,dpi=160,facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
