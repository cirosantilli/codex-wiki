"""Oxford A10 (2014): growing symmetric-channel vortex-sheet modes.

Writes 2014-channel-instability.png in the process CWD.
Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Dependencies: repository root pyproject.toml.
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    x=np.linspace(0,2*np.pi,800)
    fig,(ax,bx)=plt.subplots(1,2,figsize=(9,4.0),facecolor="white")
    ax.axhline(1,color="#37474f",lw=2)
    ax.axhline(-1,color="#37474f",lw=2)
    for t,color in [(0,"#7aa6bc"),(1.5,"#176b93"),(3,"#b4591c")]:
        eta=.025*np.exp(t/2)*np.cos(x-t/2)
        ax.plot(x,eta,color=color,lw=1.8,label=f"$t={t:g}$")
    ax.annotate("Upper base flow $U=1$",xy=(5.8,.65),xytext=(.4,.65),
                arrowprops={"arrowstyle":"->","color":"0.2"},va="center",fontsize=10)
    ax.text(.4,-.65,"Lower base flow at rest",fontsize=10)
    ax.set(xlim=(0,2*np.pi),ylim=(-1.15,1.15),xlabel="$x$",ylabel="$y$",
           title="Small growing waves ($k=h=U=1$)")
    ax.legend(loc="lower right",fontsize=9,frameon=False)
    kh=np.linspace(0,4,300)
    bx.plot(kh,kh/2,color="#176b93",lw=2,label="Growing branch")
    bx.plot(kh,-kh/2,color="#b4591c",lw=2,label="Decaying branch")
    bx.axhline(0,color="0.6",lw=.8)
    bx.text(.15,1.65,r"$\mathrm{Re}\,\omega=kU/2$",fontsize=11)
    bx.set(xlim=(0,4),ylim=(-2.2,2.2),xlabel="$kh$",ylabel=r"$\mathrm{Im}\,\omega\ h/U$",
           title="Complex frequencies: growth and decay")
    bx.legend(loc="lower left",fontsize=9,frameon=False)
    for axis in (ax,bx):axis.spines[["top","right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig("2014-channel-instability.png",dpi=155,facecolor="white",transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
