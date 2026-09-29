"""Analytic density, half-box probability and current for Oxford 2014 A11.

Write PNG to CWD; run from the matching _media topic directory.
Tested: Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7 (root pyproject.toml).
"""
from pathlib import Path
import os
os.environ.setdefault("MPLCONFIGDIR", "/tmp/codex-wiki-matplotlib")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig = plt.figure(figsize=(8.5,4.3), layout="constrained")
    grid = fig.add_gridspec(2,2)
    density_ax = fig.add_subplot(grid[:,0])
    prob_ax = fig.add_subplot(grid[0,1])
    current_ax = fig.add_subplot(grid[1,1])
    y = np.linspace(0,1,601)
    for tau,color,label in [(0,"#1d679d",r"$\tau=0$"),(np.pi/2,"#777777",r"$\tau=\pi/2$"),(np.pi,"#bd5228",r"$\tau=\pi$")]:
        density = np.sin(np.pi*y)**2+np.sin(2*np.pi*y)**2+2*np.sin(np.pi*y)*np.sin(2*np.pi*y)*np.cos(tau)
        density_ax.plot(y,density,color=color,lw=2,label=label)
    density_ax.axvline(.5,color="#444444",ls="--",lw=.8)
    density_ax.set(xlabel=r"$x/a$",ylabel=r"$a|\Psi|^2$",xlim=(0,1),ylim=(0,3.5),title="Density moves between the two halves")
    density_ax.legend(frameon=False,fontsize=9)
    tau = np.linspace(0,2*np.pi,601)
    prob_ax.plot(tau,.5+4/(3*np.pi)*np.cos(tau),color="#1d679d",lw=2)
    prob_ax.axhline(.5,color="#777777",lw=.7,ls="--")
    prob_ax.set(xlim=(0,2*np.pi),ylim=(0,1),ylabel=r"$P(0<x<a/2)$",title="Transfer probability and current")
    current_ax.plot(tau,np.sin(tau),color="#bd5228",lw=2)
    current_ax.axhline(0,color="#777777",lw=.7)
    current_ax.set(xlim=(0,2*np.pi),ylim=(-1.15,1.15),ylabel=r"$ma^2 j(a/2,t)/(2\pi\hbar)$",xlabel=r"$\tau=(E_2-E_1)t/\hbar$")
    for ax in [prob_ax,current_ax]:
        ax.set_xticks([0,np.pi/2,np.pi,3*np.pi/2,2*np.pi],[r"$0$",r"$\pi/2$",r"$\pi$",r"$3\pi/2$",r"$2\pi$"])
    prob_ax.tick_params(labelbottom=False)
    for ax in [density_ax,prob_ax,current_ax]:
        ax.grid(alpha=.15)
        ax.spines[["top","right"]].set_visible(False)
        ax.set_facecolor("white")
    fig.suptitle("Two box modes: interference drives probability flow",fontsize=13)
    out=Path.cwd()/Path(__file__).with_suffix('.png').name
    fig.savefig(out,dpi=120,facecolor="white")
    plt.close(fig)
    print(out)


if __name__ == '__main__':
    main()
