#!/usr/bin/env python3
"""Plot chained Bell measurement directions and quantum values; PNG to caller CWD."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, (ax, curve) = plt.subplots(1,2,figsize=(10.6,4.7),layout="constrained",facecolor="white")
    blue, orange = "#155d9b", "#b65b21"
    ax.set_facecolor("white")
    angles = np.linspace(0,np.pi,200)
    ax.plot(np.sin(angles),np.cos(angles),color="#d3d8df",linewidth=1)
    delta = np.pi/6
    for i in range(3):
        for offset, color, party in [(0,blue,"A"),(1,orange,"B")]:
            theta = (2*i+offset)*delta
            x,z = np.sin(theta),np.cos(theta)
            ax.annotate("",(x,z),(0,0),arrowprops={"arrowstyle":"->","color":color,"lw":2})
            ax.text(1.16*x,1.16*z,f"{party}{i+1}",ha="center",va="center",fontsize=11,color=color)
    ax.plot([0,0],[0,-1],linestyle="--",color=blue,linewidth=1)
    ax.text(0,-1.24,"Opposite A1",ha="center",fontsize=10,color=blue)
    for i in range(6):
        theta = np.linspace(i*delta,(i+1)*delta,24)
        ax.plot(.45*np.sin(theta),.45*np.cos(theta),color="#9a9fa6",linewidth=1)
    ax.text(.56,.1,r"$\delta=\pi/6$",fontsize=11)
    ax.axhline(0,color="#d9d9d9",linewidth=.6,zorder=-1)
    ax.set(xlim=(-.36,1.35),ylim=(-1.42,1.37),aspect="equal",
           title="Measurement directions for N = 3",xlabel="x component",ylabel="z component")
    ax.spines[["top","right"]].set_visible(False)
    ax.tick_params(labelsize=8)
    n = np.arange(1,21)
    value = 2*n*np.sin(np.pi/(4*n))**2
    assert np.isclose(value[0],1)
    assert np.all(value[1:]<1)
    curve.set_facecolor("white")
    curve.plot(n,value,"o-",color=blue,markersize=4,
               label=r"Quantum: $2N\sin^2(\pi/(4N))$")
    curve.axhline(1,color=orange,linestyle="--",label="Local lower bound: 1")
    curve.annotate(r"$N=2:\ 2-\sqrt{2}$",(2,value[1]),xytext=(4.7,.70),
                   arrowprops={"arrowstyle":"-","color":blue},fontsize=10,color=blue)
    curve.set(xlim=(.6,20.4),ylim=(0,1.16),xlabel="Number of settings per party, N",
              ylabel="Chained Bell expectation",title="Violation for every N ≥ 2")
    curve.set_xticks([1,2,5,10,15,20])
    curve.grid(alpha=.17)
    curve.legend(loc="upper right",fontsize=9,framealpha=1)
    fig.savefig(Path.cwd()/"paper-59-chained-bell.png",dpi=125,facecolor="white",
                transparent=False,bbox_inches="tight",pad_inches=.12)
    plt.close(fig)


if __name__ == "__main__":
    main()
