"""Original all-pairs and designated-member example; matching PNG to cwd."""
from pathlib import Path
from itertools import combinations

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    labels=[1,2,1,4,4,5];names=list("ABCDEF")
    angles=np.pi/2-np.arange(6)*2*np.pi/6
    positions=np.column_stack([np.cos(angles),np.sin(angles)])
    all_pairs=list(combinations(range(6),2));star=[(i,5) for i in range(5)]
    assert len(all_pairs)==15 and len(star)==5
    assert [(i,j) for i,j in all_pairs if labels[i]==labels[j]]==[(0,2),(3,4)]
    assert all(labels[i]!=labels[j] for i,j in star)
    fig,axes=plt.subplots(1,2,figsize=(12,5.3),dpi=100,facecolor="white")
    fig.suptitle("All possible pairs versus one designated member",fontsize=17)
    for ax,pairs,designated in zip(axes,[all_pairs,star],[False,True]):
        for i,j in pairs:
            matched=labels[i]==labels[j]
            points=positions[[i,j]]
            ax.plot(points[:,0],points[:,1],color="#c8534b" if matched else "#bccbd5",lw=3 if matched else 1.2,zorder=1)
        for i,(x,y) in enumerate(positions):
            color="#f4d2ca" if labels[i]==1 else "#f5e0c3" if labels[i]==4 else "#dcebf2"
            if designated and i==5:color="#c8e6d6"
            ax.scatter([x],[y],s=900,color=color,edgecolor="#30647d",lw=2.5 if designated and i==5 else 1.2,zorder=3)
            ax.text(x,y,names[i],ha="center",va="center",fontsize=12,weight="bold",zorder=4)
            offset=(0,30) if i==0 else (0,-30) if i==3 else (42,0) if i in [1,2] else (-42,0)
            ax.annotate(f"label {labels[i]}",(x,y),xytext=offset,textcoords="offset points",ha="center",va="center",fontsize=11)
        ax.set_aspect("equal")
        ax.set(xlim=(-1.65,1.65),ylim=(-1.65,1.65))
        ax.axis("off")
        ax.set_title("15 pairs · 2 equal-label pairs" if not designated else "5 pairs with F · 0 matches",fontsize=13,pad=3)
    fig.text(.5,.04,"Chosen labels (1, 2, 1, 4, 4, 5) · Edges represent comparisons · Synthetic configuration",ha="center",fontsize=11)
    fig.subplots_adjust(left=.04,right=.96,bottom=.14,top=.80,wspace=.12)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,facecolor="white",transparent=False)
    plt.close(fig)


if __name__=="__main__":
    main()
