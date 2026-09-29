"""Original exam-solution illustration; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    t=np.linspace(0,2*np.pi,600);angle=.7
    point=2*np.array([np.cos(angle),np.sin(angle)])
    tangent=np.array([-np.sin(angle),np.cos(angle)])
    fig,ax=plt.subplots(figsize=(6.1,5),layout="constrained",facecolor="white")
    ax.plot(2*np.cos(t),2*np.sin(t),color="#17648e",lw=2.5)
    ax.axhline(0,color=".6",lw=.8);ax.axvline(0,color=".6",lw=.8)
    ax.plot([0,point[0]],[0,point[1]],ls="--",color=".5",lw=1)
    ax.scatter(*point,color="#b84732",zorder=6)
    ax.annotate("",point+1.05*tangent,point,arrowprops={"arrowstyle":"-|>","lw":2,"color":"#b84732"})
    ax.text(point[0]+.14,point[1]-.16,r"$z=2e^{i\theta}$",fontsize=11)
    ax.text(point[0]-.85,point[1]+.72,r"$\dot z=2\dot\theta\,ie^{i\theta}$",color="#b84732",fontsize=11)
    arc=np.linspace(0,angle,80);ax.plot(.65*np.cos(arc),.65*np.sin(arc),color=".45",lw=1)
    ax.text(.77,.22,r"$\theta$")
    ax.text(-2.45,-2.5,r"Anticlockwise: $\dot\theta>0$; tangent arrow is perpendicular to the radius.",fontsize=9)
    ax.set(xlim=(-2.6,2.8),ylim=(-2.65,2.65),xlabel=r"$\operatorname{Re}z$",ylabel=r"$\operatorname{Im}z$",title=r"$|z|=2$")
    ax.set_xticks([-2,0,2]);ax.set_yticks([-2,0,2]);ax.set_aspect("equal");ax.grid(alpha=.15)
    fig.savefig(Path("paper-1-complex-motion.png"),dpi=160,facecolor="white");plt.close(fig)


if __name__ == "__main__":
    main()
