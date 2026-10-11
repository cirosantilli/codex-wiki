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
    w=np.geomspace(30,3e6,800)
    h=1/np.sqrt(1+(w/1e4)**2)
    fig,ax=plt.subplots(figsize=(7.5,4.4))
    ax.semilogx(w,h,color="#245e87",lw=2.2)
    for freq,name in [(1e3,"signal"),(1e4,"corner"),(1e5,"noise")]:
        gain=1/np.sqrt(1+(freq/1e4)**2)
        ax.plot(freq,gain,"o",color="#a04436")
        ax.vlines(freq,0,gain,ls=":",lw=1,color="#aaaaaa")
        offsets={1e3:(12,-24),1e4:(12,5),1e5:(12,16)}
        ax.annotate(f"{name}: {gain:.3f}",(freq,gain),xytext=offsets[freq],textcoords="offset points",fontsize=10)
    ax.set(xlabel=r"Angular frequency $\omega$ (rad s$^{-1}$)",ylabel=r"Voltage gain $|V_1/V_0|$",title=r"Resistor output of the ideal RL low-pass filter",ylim=(0,1.08),xlim=(30,3e6))
    ax.grid(alpha=.2,which="both");ax.spines[["top","right"]].set_visible(False)
    fig.tight_layout();save(fig)

if __name__=="__main__":main()
