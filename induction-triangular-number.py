"""Generate induction-triangular-number.png in cwd.

Tested with Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Two triangular arrays tile an n by n+1 rectangle without overlap.
"""

from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    n=5
    assert sum(range(1,n+1))==n*(n+1)//2==15
    fig,axes=plt.subplots(1,2,figsize=(9.6,4.7),dpi=120,facecolor="white")
    for ax in axes:
        ax.set_aspect("equal");ax.axis("off")
    for row in range(n):
        for col in range(row+1):
            axes[0].add_patch(Rectangle((col,row),1,1,facecolor="#b5d6ea",edgecolor="white",lw=1.5))
    for col in range(n+1):
        axes[0].add_patch(Rectangle((col,n),1,1,facecolor="#efbb91",edgecolor="white",lw=1.5))
    axes[0].set(xlim=(-.5,n+1.8),ylim=(-.4,n+1.5),title=r"Inductive step: $T_6=T_5+6=21$")
    axes[0].text(5.6,2.2,"15 old\nsquares",ha="center",fontsize=11,color="#215879")
    axes[0].text(3,6.25,"6 added squares",ha="center",fontsize=11,color="#92501f")
    blue=orange=0
    for row in range(n):
        for col in range(n+1):
            first=col<=row
            blue+=first;orange+=not first
            axes[1].add_patch(Rectangle((col,row),1,1,facecolor="#b5d6ea" if first else "#efbb91",
                                        edgecolor="white",lw=1.5))
    assert blue==orange==15
    axes[1].set(xlim=(-.6,n+1.6),ylim=(-.8,n+1.3),title=r"Two copies: $2T_5=5\cdot6=30$")
    axes[1].text(3,-.55,"6 columns",ha="center",fontsize=11)
    axes[1].text(-.35,2.5,"5 rows",ha="center",va="center",rotation=90,fontsize=11)
    fig.suptitle("One formula, two explanations: extension and rearrangement",fontsize=15)
    fig.text(.5,.035,"The pictures use n=5. Each construction works for every positive integer n.",ha="center",fontsize=10)
    fig.tight_layout(rect=(0,.075,1,.93))
    fig.savefig(Path.cwd()/"induction-triangular-number.png",facecolor="white",transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
