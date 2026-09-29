"""Original box-model ash runout/deposit diagram; Python 3.14, root dependencies.

Outputs an opaque basename PNG to caller CWD; caller chooses MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def main():
    fig,(time_ax,dep_ax)=plt.subplots(1,2,figsize=(10.8,4.8),dpi=100,facecolor="white")
    fig.subplots_adjust(left=0.075,right=0.97,bottom=0.17,top=0.78,wspace=0.3)
    t=np.linspace(0,4.5,801)
    time_ax.plot(t,np.sqrt(np.tanh(t)),color="#1969a9",lw=2.5,label=r"Radius $R/R_\infty$")
    time_ax.plot(t,1/np.cosh(t)**4,color="#b44936",lw=2,label=r"Suspension $c/c_0$")
    time_ax.axhline(1,color="0.5",lw=1,ls="--")
    time_ax.set(xlim=(0,4.5),ylim=(0,1.08),xlabel=r"Time $t/\tau$",ylabel="Normalized value")
    time_ax.set_title("Finite limiting radius; infinite arrival time",fontsize=11,pad=14)
    time_ax.legend(loc="center right",fontsize=10,frameon=False)
    time_ax.text(1.35,0.17,"Settling removes the driving buoyancy",fontsize=9)
    r=np.linspace(0,1,501)
    dep=1-1.5*r*r+0.5*r**6
    dep_ax.plot(r,dep,color="#2d8550",lw=2.5)
    dep_ax.fill_between(r,0,dep,color="#2d8550",alpha=0.1)
    dep_ax.set(xlim=(0,1.03),ylim=(0,1.08),xlabel=r"Radius $r/R_\infty$",ylabel=r"Deposit $\Sigma(r)/\Sigma(0)$")
    dep_ax.set_title("Final deposited ash per area",fontsize=11,pad=14)
    dep_ax.text(0.11,0.29,r"$1-\frac{3}{2}(r/R_\infty)^2+\frac{1}{2}(r/R_\infty)^6$",fontsize=12)
    fig.suptitle("Axisymmetric monodisperse ash box, negligible initial vent radius",fontsize=14,y=0.95)
    for ax in (time_ax,dep_ax):
        ax.grid(alpha=0.13)
        ax.set_facecolor("white")
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
    fig.savefig(Path.cwd()/"paper-83-ash-runout.png",dpi=100,facecolor="white",transparent=False)
    plt.close(fig)


if __name__=="__main__":
    main()
