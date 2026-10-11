"""Original exam-solution illustration; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def bisect(fun,left,right):
    for _ in range(70):
        mid=(left+right)/2
        if fun(left)*fun(mid)>0:left=mid
        else:right=mid
    return (left+right)/2


def main():
    fig,ax=plt.subplots(figsize=(8.7,4.6),layout="constrained",facecolor="white")
    for j,(left,right) in enumerate([(0,np.pi/2),(np.pi/2,3*np.pi/2),(3*np.pi/2,2*np.pi)]):
        x=np.linspace(left+(.002 if j else 0),right-.002,1000)
        ax.plot(x,x*np.tan(x),color="#17648e",lw=2.1,label=r"$y=x\tan x$" if j==0 else None)
    angle=np.linspace(-np.pi/2,np.pi/2,500)
    ax.plot(5*np.cos(angle),5*np.sin(angle),color="#b84732",lw=1.8,label=r"$x^2+y^2=25$, $x\geq0$")
    for pole in [np.pi/2,3*np.pi/2]:ax.axvline(pole,color=".55",ls="--",lw=.9)
    roots=[bisect(lambda v:v-5*np.cos(v),0,np.pi/2),bisect(lambda v:v+5*np.cos(v),np.pi/2,np.pi),bisect(lambda v:v+5*np.cos(v),np.pi,3*np.pi/2)]
    ax.scatter(roots,np.array(roots)*np.tan(roots),s=38,color="#27734c",zorder=6,label="Three intersections")
    ax.scatter([0,np.pi,2*np.pi],[0,0,0],s=22,color="#17648e",zorder=5)
    ax.axhline(0,color=".65",lw=.8)
    ax.set(xlim=(-.12,2*np.pi+.1),ylim=(-7,7),xlabel="$x$",ylabel="$y$",title="Tangent-product branches and circle intersections")
    ax.set_xticks([0,np.pi/2,np.pi,3*np.pi/2,2*np.pi],["0",r"$\pi/2$",r"$\pi$",r"$3\pi/2$",r"$2\pi$"])
    ax.grid(alpha=.13);ax.legend(loc="lower right",fontsize=9)
    fig.savefig(Path("paper-1-tangent-circle.png"),dpi=160,facecolor="white");plt.close(fig)


if __name__ == "__main__":
    main()
