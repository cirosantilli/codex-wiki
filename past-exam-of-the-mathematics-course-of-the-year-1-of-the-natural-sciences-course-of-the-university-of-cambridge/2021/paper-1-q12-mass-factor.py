"""Original dimensionless mass factor. Python 3.14.4; root pyproject.toml deps.

Run from the desired output directory; writes the PNG basename into cwd.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def f(q):
    # expm1 avoids subtracting nearly equal constants in the exponential.
    return 1+q*np.expm1(-1/q)


def main():
    fig,axes=plt.subplots(1,2,figsize=(9.8,4.3),layout="constrained",facecolor="white")
    q=np.linspace(.001,8,2001)
    ax=axes[0]
    ax.plot(q,f(q),color="#205e9b",lw=2,label="$f(q)$")
    a=np.linspace(0,.8,200)
    ax.plot(a,1-a,color="#b16b20",ls="--",label="Initial tangent $1-q$")
    a=np.linspace(1.2,8,400)
    ax.plot(a,1/(2*a),color="#39805c",ls=":",lw=2,label="Late approximation $1/(2q)$")
    ax.plot(0,1,"o",mfc="white",mec="#205e9b")
    ax.text(.25,1,"$f(0^+)=1$",va="bottom",fontsize=9)
    ax.set(xlim=(0,8),ylim=(-.03,1.1),xlabel="$q=r_0/R$",ylabel="$f(q)$",title="Positive, decreasing and convex")
    ax.legend(loc="upper right",fontsize=8.5)
    ax=axes[1]
    a=np.linspace(.01,30,1500)
    ax.plot(a,2*a*f(a),color="#205e9b",lw=2,label="$2qf(q)$")
    ax.axhline(1,color="0.4",ls=":")
    ax.text(15,.94,"Approaches 1 from below",fontsize=9)
    ax.set(xlim=(0,30),ylim=(0,1.08),xlabel="$q=r_0/R$",ylabel="$2qf(q)$",title=r"Large-$q$ limit: $f(q)\sim1/(2q)$")
    for ax in axes:
        ax.set_facecolor("white")
        ax.grid(alpha=.18)
        ax.spines[["top","right"]].set_visible(False)
    fig.savefig(Path(__file__).with_suffix(".png").name,dpi=150,facecolor="white")
    plt.close(fig)


if __name__=="__main__":
    main()
