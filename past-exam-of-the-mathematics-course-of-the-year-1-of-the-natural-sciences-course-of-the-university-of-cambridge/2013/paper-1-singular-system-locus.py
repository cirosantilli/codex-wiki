"""Original exam-solution illustration; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    ph=np.linspace(0,2*np.pi,600)
    fig,ax=plt.subplots(figsize=(6,5.5),layout="constrained",facecolor="white")
    for r in [1,2,3]:
        ax.plot(r*np.cos(ph),r*np.sin(ph),color="#17648e",lw=1.8)
        ax.text(.72*r+.05,.7*r+.03,"$r="+str(r)+"$",fontsize=10,color="#17648e",bbox={"facecolor":"white","edgecolor":"none","pad":1})
    ax.axhline(0,color="#b84732",lw=1.8,label="Both axes")
    ax.axvline(0,color="#b84732",lw=1.8)
    ax.scatter([0],[0],s=24,color="#b84732",zorder=6)
    ax.set(xlim=(-3.4,3.4),ylim=(-3.4,3.4),xlabel="$a$",ylabel="$b$",title="Singular-system parameter locus")
    ax.text(-3.1,-3.1,"Further circles have radii 4, 5, …",fontsize=9)
    ax.set_aspect("equal");ax.grid(alpha=.13)
    fig.savefig(Path("paper-1-singular-system-locus.png"),dpi=160,facecolor="white");plt.close(fig)


if __name__ == "__main__":
    main()
