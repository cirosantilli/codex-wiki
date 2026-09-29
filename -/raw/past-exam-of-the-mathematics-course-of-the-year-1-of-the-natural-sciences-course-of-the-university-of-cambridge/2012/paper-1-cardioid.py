"""Original mathematical illustration; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    fig,ax=plt.subplots(figsize=(6.4,5.4),layout="constrained",facecolor="white")
    theta=np.linspace(0,2*np.pi,1401)
    r=1+np.cos(theta)
    x,y=r*np.cos(theta),r*np.sin(theta)
    ax.fill(x,y,color="#d4eaf0",alpha=.8)
    ax.plot(x,y,color="#17648e",lw=2)
    ax.axhline(0,color=".5",lw=.8)
    ax.axvline(0,color=".5",lw=.8)
    ax.scatter([0,0,0,2],[0,1,-1,0],color="#17648e",s=24,zorder=4)
    ax.annotate("cusp",(0,0),(-.4,-.35),arrowprops={"arrowstyle":"->","color":".3"})
    ax.annotate("(2, 0)",(2,0),(1.55,-.28))
    ax.annotate("(0, 1)",(0,1),(-.5,1.12))
    ax.annotate("(0, −1)",(0,-1),(-.55,-1.23))
    ax.scatter([.75],[3*np.sqrt(3)/4],color="#ac4630",s=42,zorder=5)
    ax.annotate(r"$M=(3/4,3\sqrt{3}/4)$",(.75,3*np.sqrt(3)/4),(.76,1.5),fontsize=10,arrowprops={"arrowstyle":"->","color":"#ac4630"})
    ax.set(xlim=(-.68,2.28),ylim=(-1.55,1.75),xlabel="$x$",ylabel="$y$",title=r"Cardioid $r=1+\cos\theta$")
    ax.set_aspect("equal")
    ax.grid(alpha=.18)
    fig.savefig(Path(__file__).with_suffix(".png").name,dpi=160,facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
