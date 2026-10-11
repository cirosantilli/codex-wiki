"""Original mathematical illustration; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    fig,ax=plt.subplots(figsize=(6.8,6.1),layout="constrained",facecolor="white")
    for left,right in [(-3,-.08),(.08,3)]:
        x=np.linspace(left,right,1000)
        ax.plot(x,1/x-x,color="#17648e",lw=2)
    axis=np.array([-3.,3.])
    ax.plot(axis,-axis,ls="--",color=".5",lw=1,label="$y=-x$")
    ax.axvline(0,color=".5",ls="--",lw=1,label="$x=0$")
    ax.axhline(0,color=".65",lw=.7)
    q=np.array([2**(-.25),(np.sqrt(2)-1)*2**(-.25)])
    distance=np.linalg.norm(q)
    theta=np.linspace(0,2*np.pi,500)
    ax.plot(distance*np.cos(theta),distance*np.sin(theta),color="#9a7447",ls=":",lw=1.3,label="Smallest origin-centred touching circle")
    ax.plot([0,q[0]],[0,q[1]],color="#a54130",lw=1.6)
    ax.scatter([q[0]],[q[1]],color="#a54130",s=36,zorder=5)
    ax.annotate("Closest point\n(0.84090, 0.34831)",q,(1.1,1.5),fontsize=9,arrowprops={"arrowstyle":"->","color":"#a54130"})
    ax.scatter([-1,1],[0,0],s=24,color="#17648e",zorder=5)
    ax.set(xlim=(-3,3),ylim=(-3.6,3.6),xlabel="$x$",ylabel="$y$",title=r"$x^2+xy=1$")
    ax.set_aspect("equal")
    ax.grid(alpha=.18)
    ax.legend(loc="lower left",fontsize=8)
    fig.savefig(Path(__file__).with_suffix(".png").name,dpi=160,facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
