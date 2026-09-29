"""Original candidate table and divisor ratios; matching PNG output to cwd."""
from pathlib import Path
from math import isqrt

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def sigma(n):
    return sum(d+(n//d if d*d!=n else 0) for d in range(1,isqrt(n)+1) if n%d==0)


def main():
    exponents=[2,3,5,7,11,13]
    ms=[2**p-1 for p in exponents]
    candidates=[2**(p-1)*m for p,m in zip(exponents,ms)]
    totals=[sigma(n)-n for n in candidates]
    assert candidates==[6,28,496,8128,2096128,33550336]
    assert totals[4]==2325392 and all(t==n for i,(t,n) in enumerate(zip(totals,candidates)) if i!=4)
    fig=plt.figure(figsize=(12.8,5.6),dpi=100,facecolor="white")
    fig.suptitle(r"Euclid construction: $N=2^{p-1}(2^p-1)$",fontsize=17)
    top=fig.add_axes([.05,.54,.9,.30]);top.axis("off")
    rows=[[str(p),str(m) if p!=11 else "2047 = 23 × 89",f"{n:,}","prime" if p!=11 else "composite"] for p,m,n in zip(exponents,ms,candidates)]
    table=top.table(cellText=rows,colLabels=["Exponent p","Mersenne factor 2ᵖ − 1","Candidate N","Factor test"],cellLoc="center",loc="center",colWidths=[.14,.31,.28,.19])
    table.auto_set_font_size(False);table.set_fontsize(11);table.scale(1,1.35)
    for (r,c),cell in table.get_celld().items():
        cell.set_edgecolor("#d4dde3")
        if r==0:cell.set_facecolor("#dce7ee")
        elif r==5:cell.set_facecolor("#f9dcc6")
        else:cell.set_facecolor("#f3f7fa")
    ax=fig.add_axes([.1,.15,.83,.30])
    ratios=[t/n for t,n in zip(totals,candidates)]
    ax.bar(range(len(exponents)),ratios,color=["#397ba1" if p!=11 else "#c46b27" for p in exponents],width=.6)
    ax.axhline(1,color="#222",ls="--",lw=1.2)
    ax.set_xticks(range(len(exponents)),[f"p = {p}" for p in exponents],fontsize=11)
    ax.set(ylim=(0,1.3),ylabel="s(N) / N")
    ax.text(4,ratios[4]+.045,f"{ratios[4]:.6f} > 1",ha="center",fontsize=11,color="#8c4616")
    ax.spines[["top","right"]].set_visible(False)
    ax.grid(axis="y",alpha=.18)
    fig.text(.5,.045,"All six exponents are prime · The factor test fails at p = 11, and its candidate is abundant",ha="center",fontsize=11)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,facecolor="white",transparent=False)
    plt.close(fig)


if __name__=="__main__":
    main()
