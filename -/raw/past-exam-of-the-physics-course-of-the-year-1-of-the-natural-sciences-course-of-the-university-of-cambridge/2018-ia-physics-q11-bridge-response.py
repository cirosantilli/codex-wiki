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

def main():
    u=np.logspace(-2.5,2.5,900);q=u-1/u
    gain=1/np.sqrt(9+q*q);phase=-180-np.degrees(np.arctan(q/3))
    fig,axes=plt.subplots(2,1,figsize=(7.6,6),sharex=True)
    ax=axes[0];ax.semilogx(u,gain,color=BLUE,lw=2);ax.plot(1,1/3,"o",color=ORANGE)
    ax.annotate(r"$H(1)=-1/3$",(1,1/3),xytext=(2.8,.29),arrowprops={"arrowstyle":"->","color":ORANGE},color=ORANGE)
    ax.set(ylabel=r"Magnitude $|V_{AC}/V_i|$",ylim=(0,.37));ax.grid(alpha=.2)
    ax.set_title(r"Equal-component bridge: $V_{AC}=V_A-V_C$",pad=12)
    ax=axes[1];ax.semilogx(u,phase,color=GREEN,lw=2);ax.plot(1,-180,"o",color=ORANGE)
    for y in [-90,-180,-270]:ax.axhline(y,color=GREY,lw=.8,ls=":")
    ax.set(xlabel=r"Normalized angular frequency $u=\omega RC$",ylabel="Unwrapped phase (degrees)",ylim=(-280,-80),yticks=[-270,-225,-180,-135,-90]);ax.grid(alpha=.2)
    for ax in axes:ax.axvline(1,color=GREY,lw=1,ls="--")
    fig.tight_layout();save(fig)
if __name__=="__main__":main()
