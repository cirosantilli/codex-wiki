"""Original mathematical illustration; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    fig=plt.figure(figsize=(10,6.2),layout="constrained",facecolor="white")
    grid=fig.add_gridspec(2,3,height_ratios=[1.25,1])
    ax=fig.add_subplot(grid[0,:])
    x=np.linspace(0,4*np.pi,2401)
    ax.plot(x,np.exp(-x)*np.abs(np.sin(x)),color="#17648e",lw=2,label=r"$e^{-x}|\sin x|$")
    ax.plot(x,np.exp(-x),color="#b66b34",ls="--",lw=1.2,label=r"envelope $e^{-x}$")
    zeros=np.arange(5)*np.pi
    ax.scatter(zeros,np.zeros(5),s=15,color="#17648e",zorder=5)
    ax.set_xticks(zeros,["0",r"$\pi$",r"$2\pi$",r"$3\pi$",r"$4\pi$"])
    ax.set(xlim=(0,4*np.pi),ylim=(-.025,1.03),xlabel="$x$",ylabel="$y$",title="Four damped arches: full interval")
    ax.legend(loc="upper right")
    ax.grid(alpha=.18)
    for k in range(1,4):
        a=fig.add_subplot(grid[1,k-1])
        u=np.linspace(k*np.pi,(k+1)*np.pi,500)
        v=np.exp(-u)*np.abs(np.sin(u))
        a.plot(u,v,color="#17648e",lw=2)
        peak=np.pi/4+k*np.pi
        height=np.exp(-peak)/np.sqrt(2)
        a.scatter([peak],[height],color="#a54130",s=26,zorder=5)
        a.set(xlim=(k*np.pi,(k+1)*np.pi),ylim=(0,1.16*height),xlabel="$x$",ylabel="$y$",title=f"Arch {k+1}: enlarged vertical scale")
        a.set_xticks([k*np.pi,(k+.5)*np.pi,(k+1)*np.pi],[rf"${k}\pi$",rf"${2*k+1}\pi/2$",rf"${k+1}\pi$"])
        a.ticklabel_format(axis="y",style="sci",scilimits=(0,0),useMathText=True)
        a.grid(alpha=.18)
    fig.savefig(Path(__file__).with_suffix(".png").name,dpi=160,facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
