"""An original hook graph and beta-set diagram; output basename in the cwd."""
import os
import tempfile
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "codex-wiki-matplotlib"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def main():
    shape = (4, 2, 1)
    conjugate = [sum(row >= j for row in shape) for j in range(1, 5)]
    fig, axes = plt.subplots(1, 2, figsize=(9, 4), dpi=100)
    fig.patch.set_facecolor("white")
    ax = axes[0]
    for i, row in enumerate(shape):
        for j in range(row):
            marked = (i == 0 and j >= 1) or (j == 1 and i >= 0)
            ax.add_patch(Rectangle((j, -i-1), 1, 1, facecolor="#f7d68d" if marked else "white", edgecolor="#333333", linewidth=1.5))
            hook = row-(j+1)+conjugate[j]-(i+1)+1
            ax.text(j+.5, -i-.5, str(hook), fontsize=19, ha="center", va="center")
    ax.text(2, -3.65, r"$H_\lambda=6\cdot4\cdot2\cdot1\cdot3\cdot1\cdot1=144$", ha="center", fontsize=11)
    ax.text(2, -4.05, r"$\dim S^{(4,2,1)}=7!/144=35$", ha="center", fontsize=12)
    ax.set(xlim=(-.2,4.2),ylim=(-4.3,.3),xticks=[],yticks=[])
    ax.set_aspect("equal")
    ax.set_title("Hook lengths; hook at (1,2) shaded", fontsize=11, pad=6)
    ax.axis("off")
    ax = axes[1]
    beta = (6, 3, 1)
    ax.axhline(0, color="#555555", linewidth=1)
    for q in range(7):
        ax.plot(q, 0, "o", markersize=9, markerfacecolor="#245d88" if q in beta else "white", markeredgecolor="#245d88" if q in beta else "#666666", zorder=3)
        ax.text(q, -.25, str(q), ha="center", fontsize=11)
    for q in [0, 2, 4, 5]:
        height=.3+.2*(6-q)
        ax.annotate("",xy=(q,height),xytext=(6,height),arrowprops={"arrowstyle":"<->","color":"#a9640b","lw":1.2})
        ax.text((q+6)/2,height+.07,str(6-q),ha="center",fontsize=11,color="#8c5209")
    ax.text(3,-.75,r"$\beta=\{6,3,1\}$: filled nodes",ha="center",fontsize=12)
    ax.text(3,-1.05,"First-row hooks: distances to lower holes",ha="center",fontsize=10)
    ax.text(3,-1.55,r"$H_\lambda=\dfrac{6!\,3!\,1!}{(6-3)(6-1)(3-1)}=144$",ha="center",fontsize=12)
    ax.set(xlim=(-.4,6.4),ylim=(-1.9,1.7),xticks=[],yticks=[])
    ax.set_title("Beta numbers encode the same hooks",fontsize=11,pad=6)
    ax.axis("off")
    fig.suptitle(r"Hook graph and beta set for $\lambda=(4,2,1)$",fontsize=15,y=.96)
    fig.subplots_adjust(left=.035,right=.965,top=.82,bottom=.04,wspace=.18)
    fig.savefig("paper-5-hook-graph.png",dpi=100,facecolor="white",transparent=False)
    plt.close(fig)

if __name__ == "__main__":main()
