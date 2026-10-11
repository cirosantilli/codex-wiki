"""Original exam-solution illustration; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    a,b=1.2,.8;X=(a*b*b)**(1/3);Y=(a*a*b)**(1/3)
    xmax,ymax=2.8,2.6
    fig,ax=plt.subplots(figsize=(6.5,5.5),layout="constrained",facecolor="white")
    ax.fill([0,xmax,xmax,a,a,0],[0,0,b,b,ymax,ymax],color="#e3eff5")
    ax.fill([a,xmax,xmax,a],[b,b,ymax,ymax],color=".91")
    ax.plot([0,0],[0,ymax],color=".2",lw=2);ax.plot([0,xmax],[0,0],color=".2",lw=2)
    ax.plot([a,a,xmax],[ymax,b,b],color=".2",lw=2)
    ax.plot([0,a+X],[b+Y,0],color="#b84732",lw=3)
    ax.scatter([0,a+X],[b+Y,0],s=34,color="#b84732",zorder=6)
    ax.scatter([a],[b],s=40,color="#27734c",zorder=7)
    ax.annotate(r"Corner $(a,b)$",(a,b),xytext=(1.65,1.5),arrowprops={"arrowstyle":"->","color":"#27734c"},color="#27734c",fontsize=10)
    ax.text(-.08,b+Y+.15,r"$(0,b+Y)$",fontsize=10)
    ax.text(a+X,-.2,r"$(a+X,0)$",ha="center",fontsize=10)
    ax.annotate("",(.02,ymax-.25),(a-.02,ymax-.25),arrowprops={"arrowstyle":"<->","color":".4"})
    ax.text(a/2,ymax-.2,"$a$",ha="center")
    ax.annotate("",(xmax-.2,.02),(xmax-.2,b-.02),arrowprops={"arrowstyle":"<->","color":".4"})
    ax.text(xmax-.12,b/2,"$b$",va="center")
    ax.text(.42,.8,"Ladder",rotation=-41,color="#b84732")
    ax.set(xlim=(-.24,xmax+.12),ylim=(-.28,ymax+.12),title="The critical ladder position")
    ax.set_aspect("equal");ax.axis("off")
    fig.savefig(Path("paper-1-ladder-corner.png"),dpi=160,facecolor="white");plt.close(fig)


if __name__ == "__main__":
    main()
