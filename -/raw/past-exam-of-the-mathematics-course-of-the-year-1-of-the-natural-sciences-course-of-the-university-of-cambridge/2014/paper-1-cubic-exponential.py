"""Original exam-solution illustration; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    x=np.linspace(-1.4,2.5,1100);r=(2/3)**(1/3)
    fig,ax=plt.subplots(figsize=(7,4.2),layout="constrained",facecolor="white")
    ax.plot(x,np.exp(-x**3),color="#17648e",lw=2.5)
    ax.axhline(0,color="#b84732",ls="--",lw=1);ax.axvline(0,color=".7",lw=.8)
    ax.scatter([0,r],[1,np.exp(-2/3)],s=30,color="#b84732",zorder=5)
    ax.annotate("Stationary inflection (0, 1)",(0,1),xytext=(-.33,2.15),arrowprops={"arrowstyle":"->","color":"#b84732"},fontsize=10)
    ax.annotate("Second inflection",(r,np.exp(-2/3)),xytext=(1.1,1.12),arrowprops={"arrowstyle":"->","color":"#b84732"},fontsize=9)
    ax.text(1.5,.18,"Approaches zero",fontsize=9,color="#b84732")
    ax.set(xlim=(-1.4,2.5),ylim=(-.15,5.5),xlabel="$x$",ylabel="$y$",title=r"$y=e^{-x^3}$")
    ax.grid(alpha=.14)
    fig.savefig(Path("paper-1-cubic-exponential.png"),dpi=160,facecolor="white");plt.close(fig)


if __name__ == "__main__":
    main()
