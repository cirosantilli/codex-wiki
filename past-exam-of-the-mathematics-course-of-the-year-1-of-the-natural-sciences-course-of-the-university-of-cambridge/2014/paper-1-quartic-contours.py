"""Original exam-solution illustration; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    x=np.linspace(-5.3,5.3,801);X,Y=np.meshgrid(x,x);g=X**4+Y**4-36*X*Y
    fig,ax=plt.subplots(figsize=(7,6),layout="constrained",facecolor="white")
    neg=ax.contour(X,Y,g,levels=[-150,-100,-30],colors="#28744d",linewidths=1.2)
    pos=ax.contour(X,Y,g,levels=[30,150,400],colors="#17648e",linewidths=1.15)
    ax.clabel(neg,inline=True,fmt="%g",fontsize=8);ax.clabel(pos,inline=True,fmt="%g",fontsize=8)
    ph=np.linspace(0,np.pi/2,1200);cs=np.cos(ph);sn=np.sin(ph)
    radius=np.sqrt(np.maximum(36*cs*sn/(cs**4+sn**4),0))
    for sign in [-1,1]:ax.plot(sign*radius*cs,sign*radius*sn,color="#b84732",lw=2,label="$g=0$" if sign==1 else None)
    ax.scatter([3,-3],[3,-3],s=34,color="#28744d",zorder=6,label="Global minima: $g=-162$")
    ax.scatter([0],[0],s=60,marker="x",lw=2,color="#b84732",zorder=7,label="Saddle: $g=0$")
    ax.text(3.15,3.15,"(3, 3)",fontsize=9);ax.text(-4.3,-3.38,"(−3, −3)",fontsize=9)
    ax.axhline(0,color=".75",lw=.6);ax.axvline(0,color=".75",lw=.6)
    ax.set(xlim=(-5.3,5.3),ylim=(-5.3,5.3),xlabel="$x$",ylabel="$y$",title=r"$g(x,y)=x^4+y^4-36xy$")
    ax.set_aspect("equal");ax.grid(alpha=.1);ax.legend(loc="upper left",fontsize=8)
    fig.savefig(Path("paper-1-quartic-contours.png"),dpi=160,facecolor="white");plt.close(fig)


if __name__ == "__main__":
    main()
