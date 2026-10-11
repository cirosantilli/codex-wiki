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
    fig,axes=plt.subplots(1,2,figsize=(9.8,4.3));m=np.linspace(-1.2,1.2,800);z=np.linspace(-5,5,900);K=.5
    for r,color,label in [(-1.,BLUE,"Farther below criticality"),(-.25,ORANGE,"Closer to criticality")]:
        m0=np.sqrt(abs(r));w=np.sqrt(2*K/abs(r));f=.25*(m*m-m0*m0)**2
        axes[0].plot(m,f,color=color,lw=2,label=label);axes[1].plot(z,m0*np.tanh(z/w),color=color,lw=2,label=label)
    axes[0].set(xlabel="Composition order parameter m",ylabel="Excess bulk energy density (arb. units)",ylim=(0,.38),title="Composition contrast and barrier shrink")
    axes[1].axhline(0,color=GREY,lw=.8);axes[1].set(xlabel="Distance across interface (arb. units)",ylabel="Composition order parameter m",title="Intrinsic profile becomes wider")
    for ax in axes:ax.grid(alpha=.16)
    axes[1].legend(frameon=False,fontsize=9,loc="lower right")
    fig.tight_layout(w_pad=2);save(fig)
if __name__=="__main__":main()
