"""Original integral tail bounds versus even-zeta residuals; output to cwd."""
from pathlib import Path
from math import fsum, pi

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    ns=np.arange(1,101)
    fig,axes=plt.subplots(1,2,figsize=(11.6,5.1),dpi=100,facecolor="white")
    fig.suptitle("Bounds on all the terms still omitted",fontsize=17)
    for ax,s,exact,color in zip(axes,[2,4],[pi**2/6,pi**4/90],["#245f8a","#a4511d"]):
        n=ns.astype(float)
        lower=(n+1)**(1-s)/(s-1)
        upper=n**(1-s)/(s-1)
        error=np.array([exact-fsum(k**(-s) for k in range(1,j+1)) for j in ns])
        assert np.all(lower<=error) and np.all(error<=upper)
        ax.fill_between(n,lower,upper,color=color,alpha=.22,label="Integral-bound band")
        ax.loglog(n,lower,color=color,ls=":",lw=1)
        ax.loglog(n,upper,color=color,ls="--",lw=1)
        ax.loglog(n,error,color=color,lw=2,label="Exact value − partial sum")
        ax.set_title(f"Reciprocal powers s = {s}",fontsize=14,pad=12)
        ax.set(xlabel="Number of terms N",ylabel="Remaining error",xlim=(1,100))
        ax.grid(which="both",alpha=.18)
        ax.spines[["top","right"]].set_visible(False)
        ax.legend(loc="lower left",fontsize=9)
        ax.text(.07,.90,r"$1/(N+1)\leq R_N(2)\leq1/N$" if s==2 else r"$1/[3(N+1)^3]\leq R_N(4)\leq1/(3N^3)$",transform=ax.transAxes,fontsize=11)
    fig.text(.5,.035,"The full tail is larger than the first omitted term · Logarithmic scales on both axes",ha="center",fontsize=11)
    fig.subplots_adjust(left=.075,right=.98,bottom=.17,top=.82,wspace=.3)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,facecolor="white",transparent=False)
    plt.close(fig)


if __name__=="__main__":
    main()
