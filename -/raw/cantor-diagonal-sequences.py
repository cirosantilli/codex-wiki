"""Generate cantor-diagonal-sequences.png in cwd.

Tested with Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
The displayed entries are a finite window into explicitly defined infinite
binary sequences. The figure illustrates, rather than replaces, the proof.
"""

from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def entry(n, j):
    return int((3*n + 5*j + j*j) % 7 < 3)


def main():
    rows, cols = 6, 8
    bits = [[entry(n,j) for j in range(1,cols+1)] for n in range(1,rows+1)]
    opposite = [1-entry(j,j) for j in range(1,cols+1)]
    assert all(opposite[n-1] != bits[n-1][n-1] for n in range(1,rows+1))
    fig, ax = plt.subplots(figsize=(9,6.1),dpi=120,facecolor="white")
    for r, values in enumerate(bits):
        y = rows-r
        ax.text(-.85,y,rf"$a^{{({r+1})}}$",ha="center",va="center",fontsize=14)
        for c, v in enumerate(values):
            color = "#ffe1ce" if r==c else "#f4f7f9"
            ax.add_patch(Rectangle((c+.5,y-.35),1,.7,facecolor=color,edgecolor="white"))
            ax.text(c+1,y,str(v),ha="center",va="center",fontsize=16)
        ax.text(cols+1,y,"…",ha="center",va="center",fontsize=18)
    ax.text(-.85,0,r"$b$",ha="center",va="center",fontsize=16,color="#a33925")
    for c,v in enumerate(opposite):
        ax.add_patch(Rectangle((c+.5,-.35),1,.7,facecolor="#ffe1ce",edgecolor="white"))
        ax.text(c+1,0,str(v),ha="center",va="center",fontsize=16,color="#a33925")
        if c<rows:
            ax.annotate("",xy=(c+1,.45),xytext=(c+1,rows-c-.42),
                        arrowprops={"arrowstyle":"->","color":"#c26342","lw":.9,"alpha":.7})
    ax.text(cols+1,0,"…",ha="center",va="center",fontsize=18,color="#a33925")
    ax.text(-.85,-.9,"New sequence",ha="center",va="center",fontsize=11,color="#a33925")
    for c in range(cols):
        ax.text(c+1,rows+.75,str(c+1),ha="center",va="center",fontsize=11,color="#555555")
    ax.text(4.5,rows+1.35,"Coordinate j",ha="center",fontsize=12)
    ax.set(xlim=(-1.6,cols+1.6),ylim=(-1.4,rows+1.7))
    ax.axis("off")
    fig.suptitle(r"Change the diagonal: $b_j=1-a^{(j)}_j$",fontsize=17,y=.965)
    fig.text(.5,.03,"The new sequence differs from row n at coordinate n, for every n.\n"
             "Only a finite window is drawn; the argument applies to the entire infinite list.",ha="center",fontsize=10)
    fig.tight_layout(rect=(0,.065,1,.93))
    fig.savefig(Path.cwd()/"cantor-diagonal-sequences.png",facecolor="white",transparent=False)
    plt.close(fig)
    print("Displayed diagonal:", [entry(j,j) for j in range(1,7)])
    print("New sequence prefix:",opposite)


if __name__ == "__main__":
    main()
