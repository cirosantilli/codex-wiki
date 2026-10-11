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
    fig,axes=plt.subplots(1,2,figsize=(9.5,4.1))
    x=np.linspace(-4,4,1001);ax=axes[0];ax.plot(x,np.exp(-np.abs(x)),color=BLUE,lw=2)
    ax.axvline(0,color=GREY,lw=.8,ls=":");ax.set(xlabel=r"Position $\kappa x$",ylabel=r"Amplitude $\psi/\sqrt{\kappa}$",ylim=(0,1.1),title="One bound state, with a cusp")
    eta=np.linspace(0,5,600);ax=axes[1];ax.plot(eta,eta**2/(1+eta**2),color=ORANGE,lw=2,label="Reflection R");ax.plot(eta,1/(1+eta**2),color=GREEN,lw=2,label="Transmission T")
    ax.plot(1,.5,"o",color=GREY);ax.axvline(1,color=GREY,lw=.8,ls=":");ax.set(xlabel=r"Attraction $\eta=mV_0/(\hbar^2 k)$",ylabel="Probability",ylim=(0,1.1),xlim=(0,5),title="Scattering at fixed positive energy");ax.legend(frameon=False)
    for ax in axes:ax.grid(alpha=.15)
    fig.tight_layout(w_pad=2);save(fig)
if __name__=="__main__":main()
