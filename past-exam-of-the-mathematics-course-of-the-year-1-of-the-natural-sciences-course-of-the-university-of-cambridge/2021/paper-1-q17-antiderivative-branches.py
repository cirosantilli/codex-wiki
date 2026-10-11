"""Original real antiderivative branch plots. Python 3.14.4; root pyproject.toml deps.

Run from the desired output directory; writes the PNG basename into cwd.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig,axes=plt.subplots(1,2,figsize=(10,4.6),layout="constrained",facecolor="white")
    ax=axes[0]
    x=np.linspace(.025,6,1000)
    ax.plot(x,np.log(x),color="#205e9b",lw=2)
    ax.plot(-x,np.log(x),color="#205e9b",lw=2)
    ax.axvline(0,color="0.4",ls="--",lw=1)
    ax.plot([-1,1],[0,0],"o",color="#205e9b",ms=4)
    ax.text(2,.3,"$G(x)=\\ln|x|$",fontsize=11)
    ax.text(.25,-3.25,"$G\\to-\\infty$ at $0^\\pm$",fontsize=9)
    ax.set(ylim=(-3.8,2.3),title="Antiderivative of $1/x$\nEven; logarithmic singularity at zero")
    ax=axes[1]
    x=np.linspace(1.0001,6,1000)
    y=np.arccosh(x)
    ax.axvspan(-1,1,color="0.92",zorder=-1)
    ax.plot(x,y,color="#205e9b",lw=2)
    ax.plot(-x,-y,color="#205e9b",lw=2)
    ax.plot([-1,1],[0,0],"o",mfc="white",mec="#205e9b",ms=6)
    ax.text(2,1,"$R(x)=\\operatorname{arcosh}x$",fontsize=10)
    ax.text(-5.8,-1.2,"$R(x)=-\\operatorname{arcosh}(-x)$",fontsize=10)
    ax.annotate("Finite limit 0;\nvertical tangent",(1,0),(1.5,-1.1),fontsize=9,arrowprops={"arrowstyle":"->","lw":.8})
    ax.text(0,2.1,"Excluded\ndomain",ha="center",fontsize=9,color="0.4")
    ax.set(ylim=(-3,3),title=r"Antiderivative of $1/\sqrt{x^2-1}$"+"\nOdd branches with independent additive constants")
    for ax in axes:
        ax.set(xlim=(-6,6),xlabel="$x$",ylabel="Antiderivative (constants set to zero)")
        ax.axhline(0,color="0.5",lw=.8)
        ax.set_facecolor("white")
        ax.spines[["top","right"]].set_visible(False)
        ax.grid(alpha=.16)
    fig.savefig(Path(__file__).with_suffix(".png").name,dpi=150,facecolor="white")
    plt.close(fig)


if __name__=="__main__":
    main()
