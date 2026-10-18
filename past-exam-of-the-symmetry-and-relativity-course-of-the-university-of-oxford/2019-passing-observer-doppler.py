"""Passing-observer frequency; Python 3.14, NumPy and Matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    z=np.linspace(-10,10,1401)
    fig,ax=plt.subplots(figsize=(7.8,4.9),dpi=100,facecolor="white")
    for beta,color in zip((.1,.6,.95),("#1263a0","#27806a","#b44728")):
        gamma=1/np.sqrt(1-beta**2)
        ratio=gamma*(1-beta**2*z/np.sqrt(1+beta**2*z**2))
        ax.plot(z,ratio,color=color,lw=2.1,label=fr"$v/c={beta:g}$")
        ax.plot(0,gamma,"ko",ms=3)
    g=1/np.sqrt(1-.95**2)
    for value,label in [(g*(1+.95),"Early approach limit"),(g*(1-.95),"Late recession limit")]:
        ax.axhline(value,color="#888888",ls=":",lw=1)
        ax.text(-9.7,value+.08,label,fontsize=9,color="#666666")
    ax.axhline(1,color="#777777",lw=.7);ax.axvline(0,color="#777777",ls="--",lw=.9)
    ax.set(xlabel=r"Source-frame reception time $ct/L$",ylabel=r"Measured frequency $f_{\rm in}/f_0$",
           xlim=(-10,10),ylim=(0,6.7),title="A moving receiver passing a stationary source")
    ax.legend(loc="upper right");ax.grid(alpha=.2)
    fig.tight_layout(pad=1.6)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,
                facecolor="white",transparent=False,metadata={"Software":"Codex Wiki"})
    plt.close(fig)

if __name__=="__main__":main()
