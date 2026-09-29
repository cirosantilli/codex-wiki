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
    fig,ax=plt.subplots(figsize=(8,4.2))
    left=np.linspace(-2*np.pi,0,600);right=np.linspace(0,2*np.pi,300)
    ax.plot(left,4*np.cos(left)**2,color="#245e87",lw=2,label="incident + reflected standing wave")
    ax.plot(right,np.full_like(right,4),color="#2c7a5c",lw=2,label="zero-wavenumber transmitted limit")
    ax.axvline(0,color="#777777",ls=":",lw=1)
    ax.axhline(0,color="#999999",lw=.7)
    ax.set_xticks([-2*np.pi,-3*np.pi/2,-np.pi,-np.pi/2,0,np.pi,2*np.pi],[r"$-2\pi$",r"$-3\pi/2$",r"$-\pi$",r"$-\pi/2$","0",r"$\pi$",r"$2\pi$"])
    ax.set(xlim=(-2*np.pi,2*np.pi),ylim=(-.12,4.6),xlabel=r"Position $k_1x$",ylabel=r"Density $|\psi|^2/|A|^2$",title=r"Positive-step threshold: $E\to V_0^+$")
    ax.set_yticks([0,2,4]);ax.legend(loc="lower right",fontsize=9,framealpha=.95)
    ax.text(.35,4.2,"finite density; transmitted current tends to zero",fontsize=9,color="#2c7a5c")
    ax.grid(alpha=.14);ax.spines[["top","right"]].set_visible(False)
    fig.tight_layout();save(fig)

if __name__=="__main__":main()
