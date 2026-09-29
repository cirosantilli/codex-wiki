"""Original mathematical illustration; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def path(moves):
    points=[(0,0)]
    for move in moves:
        x,y=points[-1]
        points.append((x+(move=="S"),y+(move=="F")))
    return np.array(points)


def main():
    fig,ax=plt.subplots(figsize=(7.6,5.5),layout="constrained",facecolor="white")
    for xx in range(4):ax.axvline(xx,color=".88",lw=.8)
    for yy in range(5):ax.axhline(yy,color=".88",lw=.8)
    ax.plot([3,3],[0,3.5],color="#2b7751",lw=4,alpha=.45)
    ax.plot([0,2.5],[4,4],color="#b64d35",lw=4,alpha=.45)
    for moves,color,label in [("SFSFFS","#17648e","Success target first, after 3 failures"),("FSSS","#2b7751","Success target first, after 1 failure"),("FFSFSF","#b64d35","Failure target first")]:
        pts=path(moves)
        ax.plot(pts[:,0],pts[:,1],color=color,lw=1.8,marker="o",ms=4,label=label)
        for start,end in zip(pts[:-1],pts[1:]):
            ax.annotate("",xy=.75*end+.25*start,xytext=.45*end+.55*start,arrowprops={"arrowstyle":"->","color":color,"lw":1.2})
    ax.text(3.15,2.5,"3 successes",rotation=90,color="#276347",fontsize=10)
    ax.text(.55,4.15,"4 failures",color="#9c412e",fontsize=10)
    ax.set(xlim=(-.15,3.6),ylim=(-.15,4.7),xlabel="Successes (forward moves)",ylabel="Failures (reverse moves)",title="Illustrative targets: 3 successes versus 4 failures")
    ax.set_xticks(range(4))
    ax.set_yticks(range(5))
    ax.set_aspect("equal")
    ax.legend(loc="upper left",bbox_to_anchor=(1.02,.98),fontsize=8)
    fig.savefig(Path(__file__).with_suffix(".png").name,dpi=160,facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
