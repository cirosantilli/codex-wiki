#!/usr/bin/env python3
"""Draw SU(3) weights; numbers count states and red outlines mark highest weights.

The PNG is written under this script's basename in the caller's current directory.
"""
from collections import Counter
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def weights(p, q):
    """Integer coordinates (2H1, 2sqrt(3)H2), via interlacing GL(3) patterns."""
    out = Counter()
    total = p + 2*q
    for a in range(q, p+q+1):
        for b in range(q+1):
            for c in range(b, a+1):
                n1, n2, n3 = c, a+b-c, total-a-b
                out[n1-n2, n1+n2-2*n3] += 1
    assert sum(out.values()) == (p+1)*(q+1)*(p+q+2)//2
    return out


def convolution(first, second):
    out = Counter()
    for (x,y), a in first.items():
        for (u,v), b in second.items():
            out[x+u,y+v] += a*b
    return out


def hull(points):
    points = sorted(set(points))
    def cross(o,a,b):
        return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    halves = []
    for sequence in [points, points[::-1]]:
        half = []
        for p in sequence:
            while len(half) >= 2 and cross(half[-2],half[-1],p) <= 0:
                half.pop()
            half.append(p)
        halves += half[:-1]
    return halves


def draw(ax, weight_counts, title, highest=None, quarks=False):
    coordinate = lambda t: (t[0]/2, t[1]/(2*np.sqrt(3)))
    boundary = hull(weight_counts)
    if len(boundary) > 1:
        xy = np.array([coordinate(t) for t in boundary+[boundary[0]]])
        ax.plot(xy[:,0],xy[:,1],color="#bad0e2",linewidth=1.3,zorder=0)
    labels = {(1,1):"u",(-1,1):"d",(0,-2):"s"}
    for weight, count in sorted(weight_counts.items()):
        x,y = coordinate(weight)
        edge = "#ab3144" if weight == highest else "#1f5684"
        ax.scatter(x,y,s=220,facecolors="white",edgecolors=edge,linewidths=1.5,zorder=3)
        ax.text(x,y,str(count),ha="center",va="center",fontsize=9,color=edge,zorder=4)
        if quarks:
            ax.annotate(labels[weight],(x,y),xytext=(11,6),textcoords="offset points",fontsize=11)
    ax.axhline(0,color="#dddddd",linewidth=0.6,zorder=-1)
    ax.axvline(0,color="#dddddd",linewidth=0.6,zorder=-1)
    ax.set(title=title,xlabel=r"$H_1$",ylabel=r"$H_2$",aspect="equal")
    ax.set_xlim(-1.85,1.85)
    ax.set_ylim(-1.95,1.85)
    ax.tick_params(labelsize=8)
    ax.spines[["top","right"]].set_visible(False)


def main():
    tri, octet = weights(1,0), weights(1,1)
    mode = "triplet-octet"
    if mode == "diagrams":
        labels = [("Singlet: (0,0)",0,0),("Triplet: (1,0)",1,0),
                  ("Antitriplet: (0,1)",0,1),("Octet: (1,1)",1,1),
                  ("15: (2,1)",2,1),("27: (2,2)",2,2)]
        panels = [(weights(p,q),name,(p,p+2*q),(p,q)==(1,0)) for name,p,q in labels]
        shape, size = (2,3),(10.5,7.1)
        title = "SU(3) weight diagrams: numbers are multiplicities"
    elif mode == "cube":
        total = convolution(convolution(tri,tri),tri)
        double_octet = Counter({w:2*m for w,m in octet.items()})
        assert total == weights(3,0)+double_octet+weights(0,0)
        panels = [(total,r"$3\otimes3\otimes3$",(3,3),False),
                  (weights(3,0),r"$10$ : (3,0)",(3,3),False),
                  (double_octet,r"$8\oplus8$",(1,3),False),
                  (weights(0,0),r"$1$",(0,0),False)]
        shape, size = (2,2),(8.1,7.4)
        title = r"$3\otimes3\otimes3=10\oplus8\oplus8\oplus1$"
    else:
        total = convolution(tri,octet)
        assert total == weights(2,1)+weights(0,2)+tri
        panels = [(total,r"$3\otimes8$",(2,4),False),
                  (weights(2,1),r"$15$ : (2,1)",(2,4),False),
                  (weights(0,2),r"$\overline{6}$ : (0,2)",(0,4),False),
                  (tri,r"$3$ : (1,0)",(1,1),True)]
        shape, size = (2,2),(8.1,7.4)
        title = r"$3\otimes8=15\oplus\overline{6}\oplus3$"
    fig, axes = plt.subplots(*shape,figsize=size,layout="constrained",facecolor="white")
    for ax,(counts,name,highest,quarks) in zip(axes.flat,panels):
        ax.set_facecolor("white")
        draw(ax,counts,name,highest,quarks)
    fig.suptitle(title,fontsize=14)
    fig.savefig(Path.cwd()/(Path(__file__).stem+".png"),dpi=120,
                facecolor="white",transparent=False,bbox_inches="tight",pad_inches=0.12)
    plt.close(fig)


if __name__ == "__main__":
    main()
