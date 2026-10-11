"""Original exam-solution illustration; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    x=np.linspace(-1.5,1.5,700);inner=np.linspace(-1,1,400)
    fig,ax=plt.subplots(figsize=(6.7,4.5),layout="constrained",facecolor="white")
    ax.plot(x,x*x-1,color="#17648e",lw=2.2,label=r"$y=x^2-1$")
    ax.plot(x,1-x**4,color="#b84732",lw=2.2,label=r"$y=1-x^4$")
    ax.fill_between(inner,inner*inner-1,1-inner**4,color="#d5e8dc")
    ax.scatter([-1,1],[0,0],s=30,color="#27734c",zorder=6)
    ax.text(-1.4,.18,"(−1, 0)",fontsize=10);ax.text(1.04,.18,"(1, 0)",fontsize=10)
    ax.text(0,0,r"Area $=44/15$",ha="center",va="center",fontsize=12)
    ax.axhline(0,color=".65",lw=.7);ax.axvline(0,color=".65",lw=.7)
    ax.set(xlim=(-1.5,1.5),ylim=(-2,1.55),xlabel="$x$",ylabel="$y$",title="The bounded region between the two curves")
    ax.grid(alpha=.13);ax.legend(loc="lower center",fontsize=10)
    fig.savefig(Path("paper-1-parabola-quartic.png"),dpi=160,facecolor="white");plt.close(fig)


if __name__ == "__main__":
    main()
