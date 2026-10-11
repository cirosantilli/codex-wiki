"""Original exam-solution illustration; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    x=np.linspace(-2*np.pi,2*np.pi,900);y=np.linspace(-3,3,550)
    X,Y=np.meshgrid(x,y);g=1-np.cos(X)+Y*Y/2
    fig,ax=plt.subplots(figsize=(9,4.7),layout="constrained",facecolor="white")
    contours=ax.contour(X,Y,g,levels=[.25,.75,1.25,3,4.5,6],colors="#17648e",linewidths=1.2)
    ax.clabel(contours,inline=True,fmt="%g",fontsize=9)
    ax.plot(x,2*np.cos(x/2),color="#b84732",lw=2,label="$g=2$: saddle level")
    ax.plot(x,-2*np.cos(x/2),color="#b84732",lw=2)
    ax.scatter([0],[0],s=40,color="#27734c",zorder=5,label="Minimum: $g=0$")
    ax.scatter([-np.pi,np.pi],[0,0],marker="x",s=65,lw=2,color="#b84732",zorder=6,label="Saddles: $g=2$")
    ax.set(xlim=(-2*np.pi,2*np.pi),ylim=(-3,3),xlabel="$x$",ylabel="$y$",title=r"$g(x,y)=1-\cos x+y^2/2$")
    ax.set_xticks([-2*np.pi,-np.pi,0,np.pi,2*np.pi],[r"$-2\pi$",r"$-\pi$","0",r"$\pi$",r"$2\pi$"])
    ax.grid(alpha=.15);ax.legend(loc="upper center",fontsize=9,ncol=3,bbox_to_anchor=(.5,-.16))
    fig.savefig(Path("paper-1-cosine-contours.png"),dpi=160,facecolor="white");plt.close(fig)


if __name__ == "__main__":
    main()
