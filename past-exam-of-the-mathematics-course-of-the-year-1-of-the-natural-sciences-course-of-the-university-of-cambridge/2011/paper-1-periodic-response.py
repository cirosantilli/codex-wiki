"""Original mathematical illustration; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    fig,ax=plt.subplots(figsize=(8.5,4.4),layout="constrained",facecolor="white")
    x=np.linspace(0,2*np.pi,801)
    y=2*np.sin(x-np.pi/3)
    ax.plot(x,y,color="#17648e",lw=2)
    ax.scatter([5*np.pi/6,11*np.pi/6],[2,-2],color="#b14b32",s=35,zorder=5)
    ax.scatter([np.pi/3,4*np.pi/3],[0,0],color="#17648e",s=22,zorder=5)
    ax.annotate(r"maximum $(5\pi/6,2)$",(5*np.pi/6,2),(2.1,2.43),fontsize=10)
    ax.annotate(r"minimum $(11\pi/6,-2)$",(11*np.pi/6,-2),(3.7,-2.58),fontsize=10)
    ax.axhline(0,color=".5",lw=.8)
    ax.set_xticks([0,np.pi/3,np.pi,4*np.pi/3,2*np.pi],["0",r"$\pi/3$",r"$\pi$",r"$4\pi/3$",r"$2\pi$"])
    ax.set(xlim=(0,2*np.pi),ylim=(-2.8,2.75),xlabel="$x$",ylabel="$y(x)$",title=r"$y=2\sin(x-\pi/3)$")
    ax.grid(alpha=.18)
    fig.savefig(Path(__file__).with_suffix(".png").name,dpi=160,facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
