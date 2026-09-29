"""Original uniform birthday curves; opaque matching PNG is written to cwd."""
from pathlib import Path
from math import prod,exp

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def any_pair(n,m):
    return 1.0 if n>m else 1-prod((m-j)/m for j in range(n))


def main():
    m=365;ns=np.arange(1,81)
    exact=np.array([any_pair(int(n),m) for n in ns])
    specified=1-((m-1)/m)**(ns-1)
    lower=np.array([1-exp(-n*(n-1)/(2*m)) for n in ns])
    assert any_pair(22,m)<.5<any_pair(23,m)
    assert np.all(lower<=exact+1e-14) and np.all(specified<=exact+1e-14)
    fig,ax=plt.subplots(figsize=(10.8,5.4),dpi=100,facecolor="white")
    fig.suptitle("Which birthday match are we asking for?",fontsize=17)
    ax.plot(ns,exact,color="#245f8a",lw=2.5,label="Any equal-label pair")
    ax.plot(ns,lower,color="#6c8291",lw=1.5,ls="--",label="Exponential lower bound")
    ax.plot(ns,specified,color="#b26922",lw=2.3,label="A match with one designated member")
    ax.axhline(.5,color="#555",ls=":",lw=1)
    ax.scatter([23],[exact[22]],color="#245f8a",s=45,zorder=5)
    ax.annotate("23 people: 50.73%",(23,exact[22]),xytext=(33,.57),arrowprops={"arrowstyle":"->","color":"#245f8a"},fontsize=12,color="#245f8a")
    ax.scatter([23],[specified[22]],color="#b26922",s=45,zorder=5)
    ax.annotate("23 people: 5.86%",(23,specified[22]),xytext=(31,.25),arrowprops={"arrowstyle":"->","color":"#b26922"},fontsize=12,color="#b26922")
    ax.set(xlim=(1,80),ylim=(0,1.035),xlabel="Total group size n",ylabel="Probability")
    ax.grid(alpha=.18)
    ax.spines[["top","right"]].set_visible(False)
    ax.legend(loc="upper left",fontsize=10,framealpha=.96)
    fig.text(.5,.035,"Independent uniform 365-label model · The designated member is included in total size n",ha="center",fontsize=11)
    fig.subplots_adjust(left=.085,right=.975,bottom=.17,top=.84)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,facecolor="white",transparent=False)
    plt.close(fig)


if __name__=="__main__":
    main()
