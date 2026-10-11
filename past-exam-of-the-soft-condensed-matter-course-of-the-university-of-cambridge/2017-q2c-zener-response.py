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

def spring(ax,x0,x1,y,label):
    xs=np.linspace(x0,x1,13);ys=np.r_[0,np.tile([.13,-.13],5),0,0]+y
    ax.plot(xs,ys,color=BLUE,lw=1.6);ax.text((x0+x1)/2,y+.32,label,ha="center")
def main():
    fig,axes=plt.subplots(1,2,figsize=(10.1,4.2),gridspec_kw={"width_ratios":[1,1.4]})
    ax=axes[0]
    ax.plot([-.35,0,0,.4],[0,0,1,1],color=GREY,lw=1.8);spring(ax,.4,2.6,1,r"$E_0$");ax.plot([2.6,3,3,3.35],[1,1,0,0],color=GREY,lw=1.8)
    ax.plot([0,0,.35],[0,-1,-1],color=GREY,lw=1.8);spring(ax,.35,1.35,-1,r"$E_1$");ax.plot([1.35,1.65],[-1,-1],color=GREY,lw=1.8)
    ax.plot([1.65,1.65,2.3],[-1,-1.22,-1.22],color=GREY,lw=1.8);ax.plot([1.65,1.65,2.3],[-1,-.78,-.78],color=GREY,lw=1.8)
    ax.plot([2.0,2.0],[-1.16,-.84],color=BLUE,lw=2);ax.plot([2.0,3,3],[-1,-1,0],color=GREY,lw=1.8);ax.text(2,-1.65,r"$\eta$",ha="center")
    ax.text(1.5,1.85,"Equilibrium spring",ha="center",color=GREY);ax.text(1.5,-2.05,"Maxwell branch",ha="center",color=GREY)
    ax.set(xlim=(-.5,3.5),ylim=(-2.4,2.4));ax.axis("off");ax.set_title("Parallel spring and Maxwell element")
    ax=axes[1];u=np.logspace(-2,2,800);storage=1+2*u*u/(1+u*u);loss=2*u/(1+u*u)
    ax.semilogx(u,storage,color=BLUE,lw=2,label=r"Storage $E'/E_0$");ax.semilogx(u,loss,color=ORANGE,lw=2,label=r"Loss $E''/E_0$")
    ax.axhline(1,color=GREY,lw=.8,ls=":");ax.axhline(3,color=GREY,lw=.8,ls=":");ax.axvline(1,color=GREY,lw=.8,ls=":");ax.plot(1,1,"o",color=ORANGE)
    ax.set(xlabel=r"Normalized frequency $\omega\tau$",ylabel=r"Modulus / $E_0$",ylim=(0,3.4),title=r"Illustration: $E_1=2E_0$");ax.grid(alpha=.15);ax.legend(frameon=False,loc="center right",fontsize=10)
    fig.tight_layout(w_pad=2);save(fig)
if __name__=="__main__":main()
