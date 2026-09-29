"""Original mathematical illustration; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    fig,axes=plt.subplots(1,2,figsize=(10,4.8),layout="constrained",facecolor="white")
    for ax,seed,limit in zip(axes,[0.,5.],[3.,5.4]):
        u=np.linspace(0,limit,500)
        ax.plot(u,u,color=".45",lw=1.2,label="$v=u$")
        ax.plot(u,np.sqrt(2+u),color="#17648e",lw=2,label=r"$v=\sqrt{2+u}$")
        points=[(seed,seed)]
        current=seed
        for _ in range(7):
            following=np.sqrt(2+current)
            points.extend([(current,following),(following,following)])
            current=following
        pts=np.array(points)
        ax.plot(pts[:,0],pts[:,1],color="#b74c30",lw=1.35,marker=".",ms=3,label="Iteration steps")
        ax.scatter([2],[2],color="#27734c",s=35,zorder=6)
        ax.annotate("(2, 2)",(2,2),(2.14,1.66),fontsize=10)
        ax.set(xlim=(-.08,limit),ylim=(-.08,limit),xlabel="$u$",ylabel="$v$",title=rf"Start $y_0={seed:g}$: approach from {'below' if seed<2 else 'above'}")
        ax.set_aspect("equal")
        ax.grid(alpha=.18)
        ax.legend(loc="upper left",fontsize=8)
    fig.savefig(Path(__file__).with_suffix(".png").name,dpi=160,facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
