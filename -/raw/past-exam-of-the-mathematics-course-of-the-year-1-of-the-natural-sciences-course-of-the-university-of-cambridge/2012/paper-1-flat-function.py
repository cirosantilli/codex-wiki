"""Original mathematical illustration; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    fig,axes=plt.subplots(1,2,figsize=(10,4.2),layout="constrained",facecolor="white")
    x=np.linspace(-4,4,2001)
    f=np.zeros_like(x)
    df=np.zeros_like(x)
    mask=x!=0
    f[mask]=np.exp(-1/x[mask]**2)
    df[mask]=2*f[mask]/x[mask]**3
    for ax,values,title in zip(axes,[f,df],[r"$f(x)$: even",r"$f'(x)$: odd"]):
        ax.plot(x,values,color="#17648e",lw=2)
        ax.scatter([0],[0],color="#a54130",s=26,zorder=5)
        ax.axhline(0,color=".5",lw=.8)
        ax.axvline(0,color=".5",lw=.8)
        ax.set(xlim=(-4,4),xlabel="$x$",title=title)
        ax.grid(alpha=.18)
    axes[0].axhline(1,color="#a56c37",ls="--",lw=1,label=r"asymptote $y=1$")
    axes[0].set(ylim=(-.06,1.08),ylabel="$f(x)$")
    axes[0].legend(loc="lower right")
    axes[1].set(ylim=(-.92,.92),ylabel="$f'(x)$")
    fig.suptitle(r"$f(x)=e^{-1/x^2}$ for $x\ne0$, with $f(0)=0$")
    fig.savefig(Path(__file__).with_suffix(".png").name,dpi=160,facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
