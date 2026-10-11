"""Original mathematical illustration; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    fig,ax=plt.subplots(figsize=(7.6,4.4),layout="constrained",facecolor="white")
    x=np.linspace(-np.pi/4,np.pi/4,601)
    ax.plot(x,np.sin(x+np.pi/4),color="#17648e",lw=2)
    ax.scatter([-np.pi/4,0,np.pi/4],[0,1/np.sqrt(2),1],color="#a84a30",s=28,zorder=5)
    ax.annotate(r"$(-\pi/4,0)$",(-np.pi/4,0),(-.71,.13),fontsize=10)
    ax.annotate(r"$(0,1/\sqrt{2})$",(0,1/np.sqrt(2)),(-.13,.4),fontsize=10,arrowprops={"arrowstyle":"->","color":".4"})
    ax.annotate(r"$(\pi/4,1)$",(np.pi/4,1),(.34,1.11),fontsize=10)
    ax.set_xticks([-np.pi/4,0,np.pi/4],[r"$-\pi/4$","0",r"$\pi/4$"])
    ax.axhline(0,color=".5",lw=.8)
    ax.set(xlim=(-np.pi/4-.05,np.pi/4+.05),ylim=(-.07,1.25),xlabel="$x$",ylabel="$y$",title=r"$y=\sin(x+\pi/4)$")
    ax.grid(alpha=.18)
    fig.savefig(Path(__file__).with_suffix(".png").name,dpi=160,facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
