"""Original spacetime plot; Python 3.14, repository plotting packages."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    a=1.2
    first=np.linspace(0,a,250); middle=np.linspace(a,3*a,500); last=np.linspace(3*a,4*a,250)
    times=[np.sinh(first),2*np.sinh(a)-np.sinh(2*a-middle),
           4*np.sinh(a)-np.sinh(4*a-last)]
    positions=[np.cosh(first),2*np.cosh(a)-np.cosh(2*a-middle),np.cosh(4*a-last)]
    finish=4*np.sinh(a); emission=2*np.sinh(a); far=2*np.cosh(a)-1
    receive=2*(np.exp(a)-1)
    fig,ax=plt.subplots(figsize=(5.6,7.0),facecolor="white")
    ax.set_facecolor("white")
    ax.plot([1,1],[0,finish],color="#606060",lw=2,label="Planet")
    for i,(x,t) in enumerate(zip(positions,times)):
        ax.plot(x,t,color="#2563a5",lw=2.3,label="Mission" if i==0 else None)
    ax.plot([far,1],[emission,receive],color="#c4791e",ls="--",lw=1.8,label="Light signal")
    ax.scatter([1,far,1,1],[0,emission,receive,finish],color="black",s=27,zorder=5)
    ax.annotate("Emission",(far,emission),xytext=(far+0.08,emission),fontsize=10)
    ax.annotate("Reception",(1,receive),xytext=(0.2,receive-0.35),fontsize=10,
                arrowprops={"arrowstyle":"-","color":"black"})
    ax.text(1.08,finish+0.08,"Reunion",fontsize=10)
    ax.annotate("",xy=(0.7,finish),xytext=(0.7,receive),
                arrowprops={"arrowstyle":"<->","color":"#99504c","lw":1.4})
    ax.text(0.64,(finish+receive)/2,"Wait",ha="right",va="center",color="#99504c",fontsize=10)
    ax.set(xlabel=r"$\omega x/c$",ylabel=r"$\omega t$",title=r"Round trip at $\omega T=1.2$",
           xlim=(0.05,3.8),ylim=(-0.12,finish+0.55))
    ax.set_aspect("equal")
    ax.legend(loc="lower right",fontsize=9)
    ax.spines[["right","top"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(Path.cwd()/"2014-accelerated-journey.png",dpi=140,facecolor="white")
    plt.close(fig)
if __name__ == "__main__": main()
