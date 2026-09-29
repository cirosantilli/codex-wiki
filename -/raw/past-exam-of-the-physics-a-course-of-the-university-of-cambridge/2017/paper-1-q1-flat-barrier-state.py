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
    x=np.linspace(0,3,1201);psi=np.ones_like(x)/np.sqrt(2)
    psi[x<1]=np.sin(np.pi*x[x<1]/2)/np.sqrt(2)
    psi[x>2]=np.sin(np.pi*(3-x[x>2])/2)/np.sqrt(2)
    fig,ax=plt.subplots(figsize=(7.5,3.9));ax.axvspan(1,2,color="#eef3f6")
    ax.plot(x,psi,color=BLUE,lw=2.5)
    for v in [0,1,2,3]:ax.axvline(v,color=GREY,lw=.9,ls=":" if v in [1,2] else "-")
    ax.text(1.5,.82,r"$V=E:\quad\psi''=0$",ha="center",color=BLUE)
    ax.text(.5,.12,r"$V<E$",ha="center",color=GREY);ax.text(2.5,.12,r"$V<E$",ha="center",color=GREY)
    ax.set(xlim=(-.1,3.1),ylim=(0,.95),xticks=[0,1,2,3],xticklabels=["0",r"$L$",r"$2L$",r"$3L$"],xlabel="Position",ylabel=r"Normalized amplitude $\sqrt{L}\,\psi_0$",title="Ground state: flat middle, smooth joins, no internal nodes")
    fig.tight_layout();save(fig)
if __name__=="__main__":main()
