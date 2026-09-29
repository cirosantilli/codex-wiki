"""Original root-avoidance diagram. Python 3.14, numpy==2.3.5,
matplotlib==3.10.7, matching root pins. Output: same-basename CWD PNG.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def selected_height(xi):
    return np.where(np.abs(xi)>=1,0.,3.)

def main():
    fig,ax=plt.subplots(figsize=(7.6,4),dpi=100,facecolor="white")
    x=np.linspace(-3.4,3.4,1201)
    for root in [x,-x]:
        ax.fill_between(x,root-1,root+1,color="#808080",alpha=.10)
        ax.plot(x,root,color="#888888",lw=1.1)
    ax.axhline(0,color="#555555",lw=.6,ls=":")
    ax.axhline(3,color="#555555",lw=.6,ls=":")
    ax.plot([-3.4,-1],[0,0],color="#1667a8",lw=3,label="selected height")
    ax.plot([-1,1],[3,3],color="#1667a8",lw=3)
    ax.plot([1,3.4],[0,0],color="#1667a8",lw=3)
    for edge in [-1,1]:
        ax.plot([edge,edge],[0,3],color="#1667a8",ls=":",lw=1)
        ax.plot([edge],[0],"o",color="#1667a8",ms=5)
        ax.plot([edge],[3],"o",mfc="white",mec="#1667a8",ms=5)
    ax.text(-.75,3.25,r"$h=3$",color="#1667a8",fontsize=11)
    ax.text(-2.35,.25,r"$h=0$",color="#1667a8",fontsize=11)
    ax.text(2.15,.25,r"$h=0$",color="#1667a8",fontsize=11)
    ax.text(2.3,2.7,r"$\operatorname{Im}z=\xi_1$",fontsize=10,color="#666666")
    ax.text(-3.2,2.45,r"$\operatorname{Im}z=-\xi_1$",fontsize=10,color="#666666")
    ax.set(xlim=(-3.4,3.4),ylim=(-2,4),
           xlabel=r"real transverse frequency $\xi_1$",
           ylabel=r"imaginary height in $z$")
    ax.set_title(r"$P(\xi_1,z)=\xi_1^2+z^2$: heights avoid both roots",fontsize=11)
    ax.text(.04,.04,"Grey bands: distance less than 1 from a root height.\n"
            "Dotted jumps are not additional integration segments.",
            transform=ax.transAxes,fontsize=8.5,
            bbox=dict(facecolor="white",edgecolor="none",alpha=.95))
    ax.grid(alpha=.13);fig.tight_layout()
    output=Path.cwd()/(Path(__file__).stem+".png")
    fig.savefig(output,dpi=100,facecolor="white",transparent=False)
    plt.close(fig);print(output)

if __name__=="__main__":
    main()
