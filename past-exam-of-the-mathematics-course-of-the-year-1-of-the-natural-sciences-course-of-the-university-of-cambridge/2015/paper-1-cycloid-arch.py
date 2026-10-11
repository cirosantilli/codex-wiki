"""Original exam-solution illustration; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    t=np.linspace(0,2*np.pi,700);x=t-np.sin(t);y=1-np.cos(t)
    point=np.array([np.pi/3-np.sqrt(3)/2,.5])
    fig,ax=plt.subplots(figsize=(8.8,4.1),layout="constrained",facecolor="white")
    ax.fill_between(x,0,y,color="#dceaf2",alpha=.9)
    ax.plot(x,y,color="#17648e",lw=2.5)
    ax.axhline(0,color=".5",lw=.8)
    ax.scatter([0,2*np.pi],[0,0],s=45,facecolor="white",edgecolor="#17648e",zorder=5)
    ax.scatter([np.pi],[2],s=32,color="#17648e",zorder=5)
    ax.text(np.pi,2.13,r"$(\pi a,2a)$",ha="center")
    ax.plot([np.pi,np.pi],[0,2],ls="--",color=".65",lw=.8)
    tangentx=np.linspace(point[0]-.16,point[0]+.42,80)
    ax.plot(tangentx,point[1]+np.sqrt(3)*(tangentx-point[0]),color="#b84732",lw=1.6)
    ax.scatter(*point,s=32,color="#b84732",zorder=5)
    ax.annotate(r"$t=\pi/3$, slope $\sqrt{3}$",point,xytext=(1.25,.55),arrowprops={"arrowstyle":"->","color":"#b84732"},color="#b84732")
    ax.text(3.2,.58,r"Area $=3\pi a^2$",ha="center",fontsize=12)
    ax.set(xlim=(-.25,2*np.pi+.25),ylim=(-.23,2.5),xlabel="$x/a$",ylabel="$y/a$",title="One cycloid arch")
    ax.set_xticks([0,np.pi,2*np.pi],["0",r"$\pi$",r"$2\pi$"]);ax.set_yticks([0,1,2]);ax.set_aspect("equal");ax.grid(alpha=.12)
    fig.savefig(Path("paper-1-cycloid-arch.png"),dpi=160,facecolor="white");plt.close(fig)


if __name__ == "__main__":
    main()
