"""Rank-two root diagrams. Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Writes paper-63-rank-two-roots.png to caller CWD only; preserves MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

systems = [
    ("$A_2$: 6 roots", np.array([[1,0],[-0.5,np.sqrt(3)/2]]),
     [(1,0),(0,1),(1,1)]),
    ("$B_2$: 8 roots", np.array([[1,-1],[0,1]]),
     [(1,0),(0,1),(1,1),(1,2)]),
    ("$G_2$: 12 roots", np.array([[1,0],[-1.5,np.sqrt(3)/2]]),
     [(1,0),(0,1),(1,1),(2,1),(3,1),(3,2)]),
]
fig, axes = plt.subplots(1,3,figsize=(11.8,4.3),layout="constrained")
fig.patch.set_facecolor("white")
for ax,(title,simple,positive) in zip(axes,systems):
    roots=np.array(positive)@simple
    roots=np.concatenate([roots,-roots])
    lengths=np.einsum("ij,ij->i",roots,roots)
    limit=1.35*np.max(np.linalg.norm(roots,axis=1))
    ax.set_facecolor("white")
    ax.axhline(0,color="#d0d0d0",linewidth=0.6)
    ax.axvline(0,color="#d0d0d0",linewidth=0.6)
    for vector,length in zip(roots,lengths):
        color="#65849b" if np.isclose(length,min(lengths)) else "#ba7637"
        ax.annotate("",xy=vector,xytext=(0,0),
                    arrowprops={"arrowstyle":"->","color":color,"lw":1.6})
        ax.plot(*vector,"o",color=color,markersize=3.2)
    for i,vector in enumerate(simple):
        ax.annotate("",xy=vector,xytext=(0,0),
                    arrowprops={"arrowstyle":"->","color":"#17264c","lw":2.8})
        ax.text(*(1.16*vector),rf"$\alpha_{i+1}$",color="#17264c",
                fontsize=12,ha="center",va="center")
    ax.plot(0,0,"o",color="black",markersize=3)
    ax.set(aspect="equal",xlim=(-limit,limit),ylim=(-limit,limit),title=title)
    ax.set_xticks([]);ax.set_yticks([])
    for spine in ax.spines.values():spine.set_visible(False)
fig.suptitle("Irreducible rank-two roots; dark arrows mark ordered simple roots",fontsize=13)
fig.savefig("paper-63-rank-two-roots.png",dpi=135,facecolor="white",transparent=False)
plt.close(fig)
