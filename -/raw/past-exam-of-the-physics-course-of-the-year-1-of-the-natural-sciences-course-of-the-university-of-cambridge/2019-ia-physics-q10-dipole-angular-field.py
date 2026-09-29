"""Original solution figure for the 2019 Natural Sciences IA Physics paper.

Writes its PNG basename to cwd. Dependencies: numpy and matplotlib, already
specified in the repository pyproject.toml. Tested with Python 3.14.4,
NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle
import numpy as np


def save(fig):
    fig.savefig(Path(__file__).with_suffix(".png").name,dpi=145,facecolor="white")
    plt.close(fig)


def arrow(ax,a,b,colour="#333333",**kwargs):
    ax.annotate("",xy=b,xytext=a,arrowprops={"arrowstyle":"-|>","lw":1.6,"color":colour,**kwargs})


def main():
    theta=np.linspace(0,2*np.pi,900)
    fig,ax=plt.subplots(figsize=(7.5,3.9))
    ax.plot(theta,np.sqrt(1+3*np.cos(theta)**2),color="#245e87",lw=2)
    ax.set_xticks([0,np.pi/2,np.pi,3*np.pi/2,2*np.pi],["0",r"$\pi/2$",r"$\pi$",r"$3\pi/2$",r"$2\pi$"])
    ax.set_yticks([1,1.5,2]);ax.set(xlim=(0,2*np.pi),ylim=(.9,2.12),xlabel=r"Angle $\theta$ from the dipole moment",ylabel=r"$4\pi\epsilon_0r^3|\mathbf{E}|/p$",title="Dipole field magnitude at fixed large radius")
    ax.text(np.pi,2.04,"axial maximum",ha="center",fontsize=10)
    ax.text(np.pi/2,1.08,"equatorial minimum",ha="center",fontsize=10)
    ax.grid(alpha=.18);ax.spines[["top","right"]].set_visible(False)
    fig.tight_layout();save(fig)

if __name__=="__main__":main()
