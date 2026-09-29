"""Original exam-solution illustration; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    t=np.linspace(0,2*np.pi,600);aa=np.sqrt(3);bb=np.sqrt(1.5)
    fig,ax=plt.subplots(figsize=(6.6,4.8),layout="constrained",facecolor="white")
    ax.plot(1+aa*np.cos(t),bb*np.sin(t),color="#17648e",lw=2.5)
    ax.axhline(0,color=".6",lw=.8);ax.axvline(0,color=".6",lw=.8)
    ax.plot([1,1+aa],[0,0],ls="--",color="#b84732",lw=1.8)
    ax.plot([1,1],[0,bb],ls="--",color="#b84732",lw=1.5)
    ax.scatter([1],[0],color="#b84732",zorder=5)
    ax.text(1.08,-.26,"Centre (1, 0)",fontsize=10)
    ax.text(1.75,.1,r"$\sqrt{3}$",color="#b84732")
    ax.text(1.06,.64,r"$\sqrt{3/2}$",color="#b84732")
    ax.scatter([0,0],[1,-1],s=22,color="#17648e",zorder=5)
    ax.text(-.63,1.06,"(0, 1)",fontsize=10);ax.text(-.73,-1.15,"(0, −1)",fontsize=10)
    ax.set(xlim=(-1.15,3.1),ylim=(-1.65,1.65),xlabel="$x$",ylabel="$y$",title=r"$(x-1)^2+2y^2=3$")
    ax.set_aspect("equal");ax.grid(alpha=.14)
    fig.savefig(Path("paper-1-ellipse.png"),dpi=160,facecolor="white");plt.close(fig)


if __name__ == "__main__":
    main()
