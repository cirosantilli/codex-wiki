"""Original solution illustration; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from the desired output directory; writes the PNG basename to cwd.
Dependencies are recorded in the repository's pyproject.toml.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
plt.rcParams.update({"font.size":11,"axes.spines.top":False,"axes.spines.right":False,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})
BLUE="#245d85";ORANGE="#b9651a";GREEN="#267c5a";GREY="#606975"
def save(fig):
    fig.savefig(Path(__file__).with_suffix(".png").name,dpi=155,bbox_inches="tight",facecolor="white")
    plt.close(fig)
def arrow(ax,a,b,color=BLUE,scale=15,lw=2):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle="-|>",mutation_scale=scale,lw=lw,color=color))

from matplotlib.patches import Rectangle

def main():
    fig,axes=plt.subplots(1,2,figsize=(9.5,4.2))
    ax=axes[0]
    for xx in [.5,2.4,5.2]:ax.add_patch(Circle((xx,0),.28,facecolor="#d2e2ed",edgecolor=BLUE,lw=1.7))
    ax.plot([.78,2.12],[0,0],color=GREY,lw=3);ax.plot([2.68,4.92],[0,0],color=GREY,lw=3)
    ax.annotate("",xy=(.5,.7),xytext=(2.4,.7),arrowprops={"arrowstyle":"<->","color":GREY});ax.text(1.45,.9,r"$\ell_1$",ha="center")
    ax.annotate("",xy=(2.4,.7),xytext=(5.2,.7),arrowprops={"arrowstyle":"<->","color":GREY});ax.text(3.8,.9,r"$\ell_2$",ha="center")
    ax.text(2.8,-.9,"Two controllable link lengths",ha="center",color=GREY)
    ax.text(2.8,-1.35,"Net external force and torque vanish",ha="center",fontsize=10)
    ax.set(xlim=(-.1,5.9),ylim=(-1.8,1.8));ax.set_aspect("equal");ax.axis("off");ax.set_title("Three-bead swimmer (schematic)")
    ax=axes[1];loop=np.array([[1,1],[2,1],[2,2],[1,2],[1,1]])
    ax.plot(loop[:,0],loop[:,1],color=BLUE,lw=2)
    for a,b in zip(loop[:-1],loop[1:]):
        mid=.5*(a+b);d=(b-a)*.14;arrow(ax,mid-d,mid+d,BLUE,lw=1.5)
    ax.plot([1,2],[.5,.5],color=ORANGE,lw=2);arrow(ax,(1.3,.5),(1.65,.5),ORANGE,lw=1.2);arrow(ax,(1.65,.4),(1.3,.4),ORANGE,lw=1.2)
    ax.text(1.5,1.5,"nonreciprocal\ncycle",ha="center",va="center",color=BLUE)
    ax.text(1.5,.15,"reciprocal: same path back",ha="center",color=ORANGE,fontsize=9)
    ax.set(xlim=(.65,2.35),ylim=(0,2.3),xlabel=r"Link length $\ell_1$",ylabel=r"Link length $\ell_2$",xticks=[],yticks=[],title="Stroke geometry in shape space")
    fig.tight_layout(w_pad=2);save(fig)
if __name__=="__main__":main()
