"""Original proper-divisor balances; matching opaque PNG goes to cwd."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def divisors(n):
    return [d for d in range(1,n) if n%d==0]


def main():
    cases=[6,8,12,28]
    palette=["#bfd7e4","#83b2ca","#528db0","#356687","#274b66"]
    fig,ax=plt.subplots(figsize=(11.8,5.2),dpi=100,facecolor="white")
    fig.suptitle("Compare the sum of proper divisors with the number",fontsize=16)
    for row,n in enumerate(cases):
        ds=divisors(n);total=sum(ds);left=0
        for i,d in enumerate(ds):
            ax.barh(row,d/n,left=left,color=palette[i],edgecolor="white",height=.56)
            ax.text(left+d/(2*n),row,str(d),ha="center",va="center",fontsize=11,color="#122631" if i<3 else "white")
            left+=d/n
        kind="perfect" if total==n else "deficient" if total<n else "abundant"
        ax.text(1.48,row,f"s({n}) = {total} · {kind}",va="center",fontsize=12)
        assert total=={6:6,8:7,12:16,28:28}[n]
    ax.axvline(1,color="#222",ls="--",lw=1.5)
    ax.set_yticks(range(4),[f"n = {n}" for n in cases],fontsize=12)
    ax.invert_yaxis()
    ax.set(xlim=(0,2.16),xlabel="Proper-divisor sum divided by the candidate number")
    ax.set_xticks([0,.5,1,1.5,2])
    ax.grid(axis="x",alpha=.18,zorder=0)
    ax.spines[["top","right","left"]].set_visible(False)
    fig.text(.5,.04,"Each segment is one proper divisor · Equal bar lengths can describe different divisor lists",ha="center",fontsize=11)
    fig.subplots_adjust(left=.085,right=.98,bottom=.18,top=.83)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,facecolor="white",transparent=False)
    plt.close(fig)


if __name__=="__main__":
    main()
