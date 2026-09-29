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

from matplotlib.patches import Polygon, Rectangle

def main():
    fig,ax=plt.subplots(figsize=(10,4.8))
    ax.add_patch(Rectangle((0,-.45),1,.9,facecolor="#eee7dc",edgecolor=GREY,lw=1.5));ax.text(.5,0,"heated\nsource",ha="center",va="center",fontsize=10)
    for xx in [1.8,2.65]:
        ax.plot([xx,xx],[-.75,-.12],color=GREY,lw=3);ax.plot([xx,xx],[.12,.75],color=GREY,lw=3)
    ax.text(2.2,-1.05,"collimation",ha="center",color=GREY)
    ax.plot([1,3.3],[0,0],color=GREY,lw=1.8);arrow(ax,(1.05,0),(1.6,0),GREY,lw=1.4)
    ax.add_patch(Rectangle((3.3,-1.1),2.1,2.2,facecolor="#eef3f6",edgecolor=BLUE,lw=1,ls=":"))
    ax.text(4.35,1.36,"inhomogeneous magnetic field",ha="center",fontsize=10,color=BLUE)
    ax.text(4.35,-1.45,r"$G=\partial B_z/\partial z>0$",ha="center",color=BLUE)
    xx=np.linspace(3.3,8,400);base=np.where(xx<=5.4,.11*(xx-3.3)**2,.11*2.1**2+.22*2.1*(xx-5.4))
    for sign,color in [(1,ORANGE),(-1,GREEN)]:
        ax.plot(xx,sign*base,color=color,lw=2);ax.plot(8,sign*base[-1],"o",ms=8,color=color)
    ax.plot([8,8],[-2,2],color=GREY,lw=3);ax.text(8,2.17,"screen",ha="center")
    ax.text(6.65,1.9,r"$\mu_z\simeq+\mu_B$",ha="center",color=ORANGE)
    ax.text(6.65,-1.97,r"$\mu_z\simeq-\mu_B$",ha="center",color=GREEN)
    arrow(ax,(.05,1.2),(.05,1.9),GREY);ax.text(.15,1.85,r"$+z$",va="center")
    ax.text(4.1,2.13,r"Neutral atoms: $F_z\simeq\mu_zG$",ha="center",fontsize=12)
    ax.set(xlim=(-.3,8.6),ylim=(-2.35,2.65));ax.axis("off");ax.set_title("An ideal electronic two-channel Stern–Gerlach measurement",pad=12)
    fig.tight_layout();save(fig)
if __name__=="__main__":main()
