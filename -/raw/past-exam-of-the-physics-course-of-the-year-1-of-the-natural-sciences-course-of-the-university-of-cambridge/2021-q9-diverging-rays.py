"""Original diverging-lens ray construction. Python 3.14.4; root pyproject.toml deps.

Run from the desired output directory; writes the PNG basename into cwd.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    fig,ax=plt.subplots(figsize=(9.3,4.9),layout="constrained",facecolor="white")
    ax.axhline(0,color="0.45",lw=1)
    ax.plot([0,0],[-3.3,5.4],color="#506882",lw=2)
    for y,sign in [(5.4,-1),(-3.3,1)]:
        ax.annotate("",(0,y+sign*0.55),(-0.3,y),arrowprops={"arrowstyle":"->","color":"#506882","lw":1.6})
        ax.annotate("",(0,y+sign*0.55),(0.3,y),arrowprops={"arrowstyle":"->","color":"#506882","lw":1.6})
    ax.annotate("",(-8,2),(-8,0),arrowprops={"arrowstyle":"-|>","color":"#28794c","lw":2.6})
    ax.text(-8.2,2.45,"Object: 2 cm",ha="center",color="#28794c")
    ax.annotate("",(-4,1),(-4,0),arrowprops={"arrowstyle":"-|>","color":"#28794c","lw":2.3,"ls":"--"})
    ax.text(-4.1,-0.65,"Virtual image\n1 cm, upright",ha="center",color="#28794c",fontsize=10)
    ax.plot([-8,0,10],[2,2,4.5],color="#205e9b",lw=2,label="Parallel ray and refracted ray")
    ax.plot([-8,0],[0,2],color="#205e9b",ls="--",lw=1.4)
    ax.plot([-8,0,10],[2,0,-2.5],color="#b46b20",lw=2,label="Central ray")
    ax.plot([-4,0],[1,0],color="#b46b20",ls="--",lw=1.4)
    for start,end,color in [((-5.5,2),(-4.5,2),"#205e9b"),((4,3),(5,3.25),"#205e9b"),((4,-1),(5,-1.25),"#b46b20")]:
        ax.annotate("",end,start,arrowprops={"arrowstyle":"-|>","lw":1.5,"color":color})
    for x,label in [(-8,"Near focus"),(8,"Far focus")]:
        ax.plot(x,0,"ko",ms=4)
        ax.text(x,-0.35,label,ha="center",fontsize=9)
    ax.text(0.4,5.1,"Diverging lens: $f=-8$ cm",color="#506882",fontsize=10)
    ax.plot(-4,1,"ko",ms=3.5)
    ax.set(xlim=(-12,12),ylim=(-3.8,5.8),xlabel="$x$ (cm)",ylabel="Height (cm)",title="Backward extensions meet at (−4, 1) cm")
    ax.legend(loc="lower left",fontsize=8.5)
    ax.set_facecolor("white")
    ax.spines[["top","right"]].set_visible(False)
    fig.savefig(Path(__file__).with_suffix(".png").name,dpi=150,facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
