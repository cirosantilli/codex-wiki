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
    c=np.array([0,.02,.04,.05,.06,.07]);gamma=np.array([72,62.3,52.4,48.5,45.2,42])
    fig,axes=plt.subplots(1,2,figsize=(10.6,4.6))
    ax=axes[0];ax.plot(c,gamma,"o-",color=BLUE,lw=1.2,label="Data and interpolation");ce=np.linspace(.07,.083,100);ax.plot(ce,42-320*(ce-.07),"--",color=ORANGE,lw=1.7,label="Local extrapolation")
    ax.axhline(40,color=GREEN,lw=1.2,ls=":");ax.plot(.055,46.85,"s",color=GREEN,ms=6);ax.plot(.07625,40,"o",mfc="white",mec=ORANGE,ms=7)
    ax.annotate(r"$\gamma(0.055)=46.85$",(.055,46.85),xytext=(.009,41.5),arrowprops={"arrowstyle":"->","color":GREY},fontsize=9)
    ax.text(.004,37.5,r"Wetting threshold: $40\,\mathrm{mN\,m^{-1}}$",color=GREEN,fontsize=9)
    ax.set(xlim=(-.002,.086),ylim=(34,76),xlabel=r"Concentration $c$ ($\mathrm{mol\,dm^{-3}}$)",ylabel=r"Surface tension $\gamma$ ($\mathrm{mN\,m^{-1}}$)",title="Interpolation and conditional wetting estimate");ax.legend(frameon=False,fontsize=9)
    ax=axes[1];x=np.log(c[1:]);ax.plot(x,gamma[1:],"o-",color=BLUE,lw=1.2);slope=(45.2-48.5)/np.log(.06/.05);xx=np.linspace(np.log(.047),np.log(.064),100)
    ax.plot(xx,48.5+slope*(xx-np.log(.05)),color=ORANGE,lw=2)
    ax.text(-3.83,44,r"Local slope $\simeq-18.1\,\mathrm{mN\,m^{-1}}$",fontsize=10,color=ORANGE)
    ax.text(-3.83,40.8,r"$\Sigma\simeq0.23\,\mathrm{nm^2}$ at room temperature",fontsize=10,color=ORANGE)
    ax.set(xlim=(-4,-2.5),ylim=(38,66),xlabel=r"$\ln[c/(1\,\mathrm{mol\,dm^{-3}})]$",ylabel=r"Surface tension ($\mathrm{mN\,m^{-1}}$)",title="Gibbs slope uses positive concentrations")
    for ax in axes:ax.grid(alpha=.18)
    fig.tight_layout(w_pad=2.2);save(fig)
if __name__=="__main__":main()
