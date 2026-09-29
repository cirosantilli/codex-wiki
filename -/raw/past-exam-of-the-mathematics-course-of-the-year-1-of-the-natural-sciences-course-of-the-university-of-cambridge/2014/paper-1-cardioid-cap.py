"""Original exam-solution illustration; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    ph=np.linspace(-np.pi,np.pi,900);rr=1+np.cos(ph)
    beta=np.pi/3;p=np.linspace(-beta,beta,450)
    outer=1+np.cos(p);inner=1.5*np.ones_like(p)
    fig,ax=plt.subplots(figsize=(6.4,5.2),layout="constrained",facecolor="white")
    ax.plot(rr*np.cos(ph),rr*np.sin(ph),color="#17648e",lw=2,label=r"$r=1+\cos\phi$")
    ax.plot(1.5*np.cos(ph),1.5*np.sin(ph),color="#b84732",lw=1.8,label=r"$r=3/2$")
    ax.fill(np.r_[outer*np.cos(p),(inner*np.cos(p))[::-1]],np.r_[outer*np.sin(p),(inner*np.sin(p))[::-1]],color="#b9d9c6",alpha=.9,label="$D$")
    ax.text(1.7,0,"$D$",fontsize=14,ha="center")
    for sign in [-1,1]:
        xy=(.75,sign*3*np.sqrt(3)/4)
        ax.scatter(*xy,s=26,color="#17648e",zorder=5)
        ax.plot([0,xy[0]],[0,xy[1]],ls="--",color=".6",lw=.8)
        ax.text(.12,sign*.63,r"$\phi=\pi/3$" if sign>0 else r"$\phi=-\pi/3$",fontsize=9)
    ax.axhline(0,color=".7",lw=.8);ax.axvline(0,color=".7",lw=.8)
    ax.set(xlim=(-1.7,2.25),ylim=(-1.8,1.8),xlabel="$x$",ylabel="$y$",title="A cap between the cardioid and circle")
    ax.set_aspect("equal");ax.grid(alpha=.12);ax.legend(loc="upper left",fontsize=9)
    fig.savefig(Path("paper-1-cardioid-cap.png"),dpi=160,facecolor="white");plt.close(fig)


if __name__ == "__main__":
    main()
