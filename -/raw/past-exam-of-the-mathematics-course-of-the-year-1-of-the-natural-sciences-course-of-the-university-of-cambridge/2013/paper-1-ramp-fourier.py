"""Original exam-solution illustration; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig,ax=plt.subplots(figsize=(7.5,4.3),layout="constrained",facecolor="white")
    ax.plot([-np.pi,0],[0,np.pi],color="#17648e",lw=2.5)
    ax.plot([0,np.pi],[0,0],color="#17648e",lw=2.5)
    ax.scatter([-np.pi,0,0,np.pi],[0,0,np.pi,0],s=47,facecolor="white",edgecolor="#17648e",lw=1.6,zorder=6)
    ax.plot([0,0],[0,np.pi],color=".6",ls=":",lw=1)
    ax.scatter([0],[np.pi/2],s=43,marker="D",color="#b84732",zorder=7)
    ax.annotate(r"Fourier value $\pi/2$",(0,np.pi/2),xytext=(.75,2.08),arrowprops={"arrowstyle":"->","color":"#b84732"},fontsize=10)
    ax.text(-2.45,1.25,r"$x+\pi$",color="#17648e",fontsize=12)
    ax.text(1.5,.14,"0",color="#17648e",fontsize=11)
    ax.set(xlim=(-np.pi-.2,np.pi+.2),ylim=(-.3,np.pi+.4),xlabel="$x$",ylabel="$f(x)$",title="One period of the ramp-and-zero function")
    ax.set_xticks([-np.pi,0,np.pi],[r"$-\pi$","0",r"$\pi$"])
    ax.set_yticks([0,np.pi/2,np.pi],["0",r"$\pi/2$",r"$\pi$"]);ax.grid(alpha=.13)
    fig.savefig(Path("paper-1-ramp-fourier.png"),dpi=160,facecolor="white");plt.close(fig)


if __name__ == "__main__":
    main()
