"""Inverse graphs and equal logarithmic areas for equal multiplicative intervals."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    parameter=np.linspace(-1.5, np.log(4.4), 701)
    ln2=np.log(2)
    t1=np.linspace(1, 2, 10001)
    t2=np.linspace(2, 4, 10001)
    assert abs(np.trapezoid(1/t1,t1)-ln2) < 1e-9
    assert abs(np.trapezoid(1/t2,t2)-ln2) < 1e-9
    assert np.isclose(np.exp(ln2),2)
    blue, orange = "#176997", "#b55d20"
    fig, axes=plt.subplots(1,2,figsize=(10.8,5.1),dpi=120)
    ax=axes[0]
    ax.plot(parameter,np.exp(parameter),color=blue,lw=2.4,label=r"$y=e^x$")
    ax.plot(np.exp(parameter),parameter,color=orange,lw=2.4,label=r"$y=\ln x$")
    ax.plot([-1.5,4.4],[-1.5,4.4],color="#94a3af",ls=":",lw=1.2,label=r"$y=x$")
    ax.axhline(0,color="#aeb8c0",lw=.8); ax.axvline(0,color="#aeb8c0",lw=.8)
    ax.scatter([ln2,2],[2,ln2],color=[blue,orange],s=40,zorder=4)
    ax.plot([ln2,2],[2,ln2],color="#687986",ls="--",lw=.9)
    ax.annotate(r"$(\ln2,2)$",(ln2,2),xytext=(-.85,2.6),fontsize=11,color=blue,
                arrowprops={"arrowstyle":"->","color":blue})
    ax.annotate(r"$(2,\ln2)$",(2,ln2),xytext=(2.2,-.65),fontsize=11,color=orange,
                arrowprops={"arrowstyle":"->","color":orange})
    ax.set(xlim=(-1.5,4.4),ylim=(-1.5,4.4),xlabel="Input x",ylabel="Output y")
    ax.set_aspect("equal")
    ax.set_title("Interchange input and output",fontsize=12)
    ax.legend(loc="upper right",frameon=False,fontsize=10)
    ax.grid(alpha=.12)
    ax=axes[1]
    t=np.linspace(.8,4.5,701)
    ax.plot(t,1/t,color="#243746",lw=2.3,label=r"$1/t$")
    ax.fill_between(t1,0,1/t1,color=blue,alpha=.27)
    ax.fill_between(t2,0,1/t2,color=orange,alpha=.27)
    for endpoint in [1,2,4]: ax.vlines(endpoint,0,1/endpoint,color="#687986",lw=.9)
    ax.text(1.49,.24,r"$\ln2$",ha="center",fontsize=14,color=blue)
    ax.text(2.95,.15,r"$\ln2$",ha="center",fontsize=14,color=orange)
    ax.annotate("Doubling t halves the height",(3.5,1/3.5),xytext=(2.05,.75),fontsize=10,
                arrowprops={"arrowstyle":"->","color":"#687986"})
    ax.set(xlim=(.8,4.5),ylim=(0,1.35),xlabel="Positive t",ylabel="Integrand 1/t")
    ax.set_xticks([1,2,3,4])
    ax.set_title("Both intervals multiply t by two",fontsize=12)
    ax.text(.5,.92,r"$\int_1^2dt/t=\int_2^4dt/t=\ln2$",transform=ax.transAxes,
            ha="center",fontsize=12)
    ax.grid(alpha=.12)
    fig.suptitle("Logarithms turn equal ratios into equal increments",fontsize=15)
    fig.subplots_adjust(left=.07,right=.97,bottom=.14,top=.80,wspace=.29)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,facecolor="white")
    plt.close(fig)


if __name__=="__main__":
    main()
