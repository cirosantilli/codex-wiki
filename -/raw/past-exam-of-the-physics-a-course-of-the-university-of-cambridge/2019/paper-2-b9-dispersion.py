"""Original solution figure; tested with Python 3.14.

Uses NumPy and Matplotlib as declared in the root pyproject.toml.
Writes its PNG basename to the current working directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    k=np.linspace(-4.6,4.6,1000)
    fig,ax=plt.subplots(figsize=(8,4.8),layout="constrained")
    for n,color in [(1,"#0068a0"),(2,"#b55713"),(3,"#654c9e")]:
        omega=np.sqrt(k*k+n*n)
        ax.plot(k,omega,color=color,lw=2,label=f"n = {n}")
        ax.plot(0,n,"o",color=color)
    ax.plot(k,np.abs(k),ls="--",color="#777777",lw=1,label=r"$\omega=c_m|k|$")
    ax.set(xlabel=r"$ka/\pi$",ylabel=r"$\omega a/(\pi c_m)$",xlim=(-4.6,4.6),ylim=(0,5.7),
           title="Fixed-edge membrane guide: three lowest branches")
    ax.legend(loc="lower right",fontsize=10);ax.grid(alpha=.17)

    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=150,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
