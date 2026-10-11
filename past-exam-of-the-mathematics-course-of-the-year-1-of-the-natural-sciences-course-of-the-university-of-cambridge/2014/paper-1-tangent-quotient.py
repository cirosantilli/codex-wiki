"""Original exam-solution illustration; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig,ax=plt.subplots(figsize=(8,4.3),layout="constrained",facecolor="white")
    poles=[-np.pi/4,3*np.pi/4]
    edges=[-np.pi,*poles,np.pi]
    for left,right in zip(edges,edges[1:]):
        x=np.linspace(left+.003,right-.003,1000)
        ax.plot(x,np.cos(x)/(np.cos(x)+np.sin(x)),color="#17648e",lw=2.2)
    for pole in poles:ax.axvline(pole,color="#b84732",ls="--",lw=1.3)
    ax.axhline(0,color=".6",lw=.8);ax.axvline(0,color=".6",lw=.8)
    ax.scatter([-np.pi/2,np.pi/2],[0,0],s=64,facecolor="white",edgecolor="#17648e",lw=1.8,zorder=6,label="Excluded: tangent undefined")
    ax.scatter([0],[1],s=25,color="#17648e",zorder=5);ax.text(.1,1.2,"(0, 1)",fontsize=10)
    ax.set(xlim=(-np.pi,np.pi),ylim=(-3.5,4.5),xlabel="$x$",ylabel="$y$",title=r"$y=1/(1+\tan x)$: period $\pi$")
    ax.set_xticks([-np.pi,-np.pi/2,-np.pi/4,0,np.pi/2,3*np.pi/4,np.pi],[r"$-\pi$",r"$-\pi/2$",r"$-\pi/4$","0",r"$\pi/2$",r"$3\pi/4$",r"$\pi$"])
    ax.grid(alpha=.12);ax.legend(loc="lower left",fontsize=9)
    fig.savefig(Path("paper-1-tangent-quotient.png"),dpi=160,facecolor="white");plt.close(fig)


if __name__ == "__main__":
    main()
