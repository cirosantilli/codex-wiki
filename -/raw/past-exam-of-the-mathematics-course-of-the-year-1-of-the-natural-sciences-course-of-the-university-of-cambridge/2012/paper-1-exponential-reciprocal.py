"""Original mathematical illustration; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    fig,ax=plt.subplots(figsize=(8,4.5),layout="constrained",facecolor="white")
    for left,right in [(-6,-.025),(.025,6)]:
        x=np.linspace(left,right,1400)
        ax.plot(x,1/np.expm1(x),color="#17648e",lw=2)
    ax.axvline(0,color=".35",ls="--",lw=1)
    ax.axhline(0,color=".35",ls="--",lw=1)
    ax.axhline(-1,color="#a34a30",ls="--",lw=1,label=r"$y=-1$")
    ax.text(5.8,.23,r"$y=0$",ha="right",fontsize=10)
    ax.text(.13,3.5,r"$x=0$",fontsize=10)
    ax.set(xlim=(-6,6),ylim=(-5,4),xlabel="$x$",ylabel="$y$",title=r"$y=1/(e^x-1)$")
    ax.grid(alpha=.18)
    ax.legend(loc="lower right")
    fig.savefig(Path(__file__).with_suffix(".png").name,dpi=160,facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
