"""Original exam-solution illustration; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig,ax=plt.subplots(figsize=(9,4.1),layout="constrained",facecolor="white")
    for k in [-1,0,1]:
        x=np.linspace(-np.pi+2*k*np.pi,np.pi+2*k*np.pi,500)
        ax.plot(x,np.exp(x-2*k*np.pi),color="#17648e",lw=2.2)
    ends=np.array([-3,-1,1,3])*np.pi
    ax.scatter(ends,np.full(4,np.exp(-np.pi)),s=28,color="#17648e",zorder=6)
    ax.scatter(ends[1:],np.full(3,np.exp(np.pi)),s=42,facecolor="white",edgecolor="#17648e",lw=1.4,zorder=6)
    ax.plot([np.pi,np.pi],[np.exp(-np.pi),np.exp(np.pi)],ls=":",color=".6",lw=1)
    ax.scatter([np.pi],[np.cosh(np.pi)],s=40,marker="s",color="#b84732",zorder=7)
    ax.annotate(r"Fourier value $\cosh\pi$",(np.pi,np.cosh(np.pi)),xytext=(1.45*np.pi,14.5),arrowprops={"arrowstyle":"->","color":"#b84732"},fontsize=10)
    ax.set(xlim=(-3*np.pi-.12,3*np.pi+.12),ylim=(-1,25.8),xlabel="$x$",ylabel=r"$g_{\rm per}(x)$",title="Periodic continuation of the exponential")
    ax.set_xticks(np.arange(-3,4)*np.pi,[r"$-3\pi$",r"$-2\pi$",r"$-\pi$","0",r"$\pi$",r"$2\pi$",r"$3\pi$"])
    ax.set_yticks([np.exp(-np.pi),np.cosh(np.pi),np.exp(np.pi)],[r"$e^{-\pi}$",r"$\cosh\pi$",r"$e^\pi$"])
    ax.grid(alpha=.14)
    fig.savefig(Path("paper-1-periodic-exponential.png"),dpi=160,facecolor="white");plt.close(fig)


if __name__ == "__main__":
    main()
