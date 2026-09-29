"""Generate power-set-inclusion-cube.png in cwd.

Tested with Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Every vertex is one subset; an upward edge adds exactly one element.
"""

from itertools import combinations
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    universe=('a','b','c')
    vertices=[frozenset(c) for k in range(4) for c in combinations(universe,k)]
    positions={frozenset():(0,0),frozenset('a'):(-2,1.4),frozenset('b'):(0,1.4),frozenset('c'):(2,1.4),
               frozenset('ab'):(-2,2.8),frozenset('ac'):(0,2.8),frozenset('bc'):(2,2.8),frozenset('abc'):(0,4.2)}
    edges=[(s,t) for s in vertices for t in vertices if s<t and len(t)==len(s)+1]
    assert len(vertices)==8 and len(edges)==12
    fig,ax=plt.subplots(figsize=(7.5,5.4),dpi=120,facecolor="white")
    for s,t in edges:
        ax.plot([positions[s][0],positions[t][0]],[positions[s][1],positions[t][1]],color="#aab9c2",lw=1.4,zorder=0)
    for s,(x,y) in positions.items():
        label=r"$\varnothing$" if not s else r"$\{"+','.join(sorted(s))+r"\}$"
        ax.text(x,y,label,ha="center",va="center",fontsize=15,
                bbox={"boxstyle":"round,pad=.35","facecolor":"#e0eef6","edgecolor":"#608aa4"})
    for k,number in enumerate([1,3,3,1]):
        ax.text(3.25,1.4*k,f"Size {k}: {number} subset"+('s' if number!=1 else ''),ha="left",va="center",fontsize=11)
    ax.set(xlim=(-2.8,5.5),ylim=(-.55,4.9))
    ax.axis("off")
    fig.suptitle(r"The power set of $\{a,b,c\}$ has $2^3=8$ members",fontsize=15)
    fig.text(.5,.035,"Each element is either included or excluded. Every upward edge adds one element.\n"
             "The graph is a cube, drawn by subset size to make inclusion visible.",ha="center",fontsize=10)
    fig.tight_layout(rect=(0,.075,1,.92))
    fig.savefig(Path.cwd()/"power-set-inclusion-cube.png",facecolor="white",transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
