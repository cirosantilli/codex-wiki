"""Original exam-solution illustration; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    x=np.linspace(-1.7,1.7,850);X,Y=np.meshgrid(x,x);f=X*Y*(X*X+Y*Y-1)
    fig,ax=plt.subplots(figsize=(7.2,6.8),layout="constrained",facecolor="white")
    neg=ax.contour(X,Y,f,levels=[-1,-.25,-.1,-.05],colors="#17648e",linewidths=1)
    pos=ax.contour(X,Y,f,levels=[.05,.1,.25,1],colors="#8b427d",linewidths=1)
    ax.clabel(neg,inline=True,fmt="%g",fontsize=8);ax.clabel(pos,inline=True,fmt="%g",fontsize=8)
    ph=np.linspace(0,2*np.pi,500)
    ax.plot(np.cos(ph),np.sin(ph),color=".35",lw=1.6,label="Zero level: circle and axes")
    ax.axhline(0,color=".35",lw=1.6);ax.axvline(0,color=".35",lw=1.6)
    ax.scatter([0,1,-1,0,0],[0,0,0,1,-1],s=48,marker="x",lw=1.8,color="#b84732",zorder=7,label="Five saddles: $f=0$")
    ax.scatter([.5,-.5],[.5,-.5],s=34,color="#27734c",zorder=7,label="Minima: $f=-1/8$")
    ax.scatter([.5,-.5],[-.5,.5],s=36,marker="^",color="#8b427d",zorder=7,label="Maxima: $f=1/8$")
    ax.set(xlim=(-1.7,1.7),ylim=(-1.7,1.7),xlabel="$x$",ylabel="$y$",title=r"$f(x,y)=xy(x^2+y^2-1)$")
    ax.set_aspect("equal");ax.grid(alpha=.1)
    ax.legend(loc="upper center",bbox_to_anchor=(.5,-.12),ncol=2,fontsize=9)
    fig.savefig(Path("paper-1-quartic-contours.png"),dpi=160,facecolor="white");plt.close(fig)


if __name__ == "__main__":
    main()
