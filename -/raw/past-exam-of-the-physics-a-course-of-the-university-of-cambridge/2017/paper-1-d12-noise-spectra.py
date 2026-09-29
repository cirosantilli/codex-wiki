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
    f=np.logspace(-2.5,6.4,1500)
    measured_f=np.array([.01,.1,1,10,100,1000,10000,100000,1000000.])
    measured_p=np.array([1e-4,1e-5,1e-6,1e-6,1e-6,5e-7,1e-8,1e-10,1e-15])
    fig,axes=plt.subplots(1,2,figsize=(11,4.8))
    ax=axes[0]
    for fc,color in [(100,ORANGE),(1000,BLUE)]:
        ax.loglog(f,1/(f*f+fc*fc),color=color,lw=2,label=fr"$f_c={fc}\,\mathrm{{Hz}}$")
        ax.plot(fc,1/(2*fc*fc),"o",color=color)
    ax.set(xlim=(.1,1e6),ylim=(1e-13,1e-3),xlabel="Frequency (Hz)",ylabel="Ideal PSD (arbitrary normalization)",title="Two Lorentzians with a common numerator");ax.legend(frameon=False,fontsize=10)
    ax.text(.4,2e-5,"flat plateaux",fontsize=10,color=GREY);ax.text(4e3,2e-10,r"high-frequency slope $-2$",rotation=-30,fontsize=10,color=GREY)
    ax=axes[1];ax.loglog(f,1e-6/(1+(f/1e3)**2),color=BLUE,lw=1.8,label=r"Ideal curve: $f_c=1\,\mathrm{kHz}$")
    ax.loglog(measured_f,measured_p,"o",ms=5.5,color="#222222",label="Measured values")
    ax.loglog([1,1e4],[1e-6,1e-6],color=GREEN,ls=":",lw=1.4)
    z=np.array([1e3,1e6]);ax.loglog(z,1/z**2,color=ORANGE,ls="--",lw=1.1)
    ax.axvline(1e3,color=GREY,lw=.9,ls=":")
    ax.annotate("half plateau",(1e3,5e-7),xytext=(2e3,3e-5),arrowprops={"arrowstyle":"->","color":GREY},fontsize=9)
    ax.annotate("low-frequency\nexcess",(.01,1e-4),xytext=(.02,2e-7),arrowprops={"arrowstyle":"->","color":GREY},fontsize=9)
    ax.annotate("extra suppression",(1e6,1e-15),xytext=(2e2,3e-14),arrowprops={"arrowstyle":"->","color":GREY},fontsize=9)
    ax.set(xlim=(.004,2.5e6),ylim=(2e-16,1e-3),xlabel="Frequency (Hz)",ylabel=r"Measured PSD ($\mathrm{V^2\,Hz^{-1}}$)",title="Data and graphical corner estimate");ax.legend(frameon=False,loc="lower left",fontsize=9)
    for ax in axes:ax.grid(alpha=.18)
    fig.tight_layout(w_pad=2.2);save(fig)
if __name__=="__main__":main()
