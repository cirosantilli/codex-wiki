"""Original mathematical illustration; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    fig,ax=plt.subplots(figsize=(6.2,5.7),layout="constrained",facecolor="white")
    s=np.linspace(0,6,601)
    r0=1.5
    ax.fill_between(s,s,6,color="#bcded1",alpha=.85,label="No interruption: $t>s$")
    use=s>=r0
    ax.fill_between(s[use],0,s[use]-r0,color="#f3d5a7",alpha=.9,label=r"$r>r_0$: $s>t+r_0$")
    ax.plot(s,s,color="#2c7356",lw=1.6)
    ax.plot(s[use],s[use]-r0,color="#a56829",lw=1.6)
    ax.text(1.1,4.8,"No interruption\nnegative sentinel",color="#275d48",fontsize=11)
    ax.text(4.25,1.05,r"$r>r_0$",color="#8a5520",fontsize=13)
    ax.text(2.65,2.1,r"$0<r<r_0$",rotation=45,color=".35",fontsize=10)
    ax.annotate(r"$r_0$",(r0,0),(r0,-.48),ha="center",fontsize=11)
    ax.set(xlim=(0,6),ylim=(0,6),xlabel="$s$ (minutes)",ylabel="$t$ (minutes)",title="Regions for two independent waiting times")
    ax.set_aspect("equal")
    ax.grid(alpha=.18)
    ax.legend(loc="upper left",bbox_to_anchor=(0,-.16),fontsize=9)
    fig.savefig(Path(__file__).with_suffix(".png").name,dpi=160,facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
