"""Original even-zeta partial sums; write opaque basename PNG to cwd."""
from pathlib import Path
from math import fsum, pi

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    ns = np.arange(1,31)
    fig, axes = plt.subplots(1,2,figsize=(11.6,5.1),dpi=100,facecolor="white")
    fig.suptitle("Convergence to exact even zeta values",fontsize=17)
    for ax,s,exact,color in zip(axes,[2,4],[pi**2/6,pi**4/90],["#245f8a","#a4511d"]):
        sums = np.array([fsum(k**(-s) for k in range(1,n+1)) for n in ns])
        assert np.all(np.diff(sums)>0) and np.all(sums<exact)
        ax.plot(ns,sums,"o-",color=color,markersize=3,lw=2,label="Computed partial sum")
        ax.axhline(exact,color="#444",ls="--",label="Exact infinite sum")
        ax.annotate(f"N = 10: {sums[9]:.9f}", (10,sums[9]),xytext=(13,1.3 if s==2 else 1.027),arrowprops={"arrowstyle":"->","color":color},fontsize=10,color=color)
        ax.set_title(r"$\zeta(2)=\pi^2/6$" if s==2 else r"$\zeta(4)=\pi^4/90$",fontsize=15,pad=12)
        ax.set(xlabel="Number of terms N",ylabel="Partial sum",xlim=(.5,31),ylim=((.96,1.68) if s==2 else (.99,1.09)))
        ax.grid(alpha=.22)
        ax.spines[["top","right"]].set_visible(False)
        ax.legend(loc="lower right",fontsize=10)
        ax.text(.05,.20,f"Exact sum ≈ {exact:.9f}",transform=ax.transAxes,fontsize=11)
    fig.text(.5,.035,"Different vertical scales · Positive omitted terms keep every finite sum below its limit",ha="center",fontsize=11)
    fig.subplots_adjust(left=.075,right=.98,bottom=.17,top=.82,wspace=.3)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,facecolor="white",transparent=False)
    plt.close(fig)


if __name__=="__main__":
    main()
