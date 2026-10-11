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
    fig,axes=plt.subplots(1,2,figsize=(10.7,4.6),gridspec_kw={"width_ratios":[1,1.2]})
    ax=axes[0];ax.add_patch(Circle((0,0),.42,facecolor="#c5d4df",edgecolor=BLUE,lw=1.8));ax.add_patch(Circle((0,0),1.35,fill=False,edgecolor=ORANGE,lw=1.7,ls="--"))
    for t in np.linspace(0,2*np.pi,8,endpoint=False):
        p=np.array([np.cos(t),np.sin(t)]);arrow(ax,1.24*p,.75*p,BLUE,lw=1.7)
    arrow(ax,(0,0),(.42,0),GREY,scale=10,lw=1);ax.text(.19,.1,r"$b$",ha="center")
    t=np.deg2rad(24);p=1.35*np.array([np.cos(t),np.sin(t)]);arrow(ax,p,p*1.3,ORANGE,lw=1.6);ax.text(1.68,.78,"outward normal",ha="center",fontsize=9,color=ORANGE)
    ax.plot([0,-1.35],[0,0],color=ORANGE,lw=1);ax.text(-.76,.1,r"$r$",ha="center",color=ORANGE)
    ax.text(0,-1.72,r"Side flux: $2\pi rL\,g_r$",ha="center");ax.text(0,-2.04,"End-cap flux = 0",ha="center",fontsize=10)
    ax.set(xlim=(-1.9,2.1),ylim=(-2.2,1.85));ax.set_aspect("equal");ax.axis("off");ax.set_title("Infinite rod: transverse section",pad=12)
    ax=axes[1];s=np.linspace(0,7,700);v=(1+s*s)**(-.25)
    ax.plot(s,v,color=BLUE,lw=2,label=r"$[1+(R/a)^2]^{-1/4}$")
    z=np.linspace(1.2,7,200);ax.plot(z,z**(-.5),color=ORANGE,ls="--",label=r"Far limit $(R/a)^{-1/2}$")
    ax.axhline(1,color=GREEN,lw=1,ls=":");ax.text(3.5,1.025,r"Near limit: $\sqrt{2G\lambda}$",ha="center",color=GREEN,fontsize=10)
    ax.set(xlim=(0,7),ylim=(0,1.12),xlabel=r"Orbital radius $R/a$",ylabel=r"Speed $v/\sqrt{GM/a}$",title="Finite line rod: circular speed");ax.grid(alpha=.18);ax.legend(frameon=False,loc="lower left",fontsize=10)
    fig.tight_layout(w_pad=2);save(fig)
if __name__=="__main__":main()
