"""Original 2021 Particle and Nuclear Physics solution figure.

Writes the PNG basename to the current working directory. Dependencies are
numpy and matplotlib, declared in the repository pyproject.toml.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def line(ax, a, b, kind="fermion", backwards=False, label=None):
    a, b = np.array(a, dtype=float), np.array(b, dtype=float)
    d = b - a
    n = np.array([-d[1], d[0]]) / np.linalg.norm(d)
    if kind in ("wavy", "gluon"):
        t = np.linspace(0, 1, 300)
        phase = 16 * np.pi * t
        curve = a[:, None] + d[:, None] * t + 0.045 * n[:, None] * np.sin(phase)
        if kind == "gluon":
            curve += 0.045 * (d / np.linalg.norm(d))[:, None] * (np.cos(phase)-1) * np.sin(np.pi*t)
        ax.plot(*curve, color="#27618c", lw=1.6)
    else:
        ax.plot([a[0], b[0]], [a[1], b[1]], color="#333333", lw=1.5)
        if kind == "fermion":
            if backwards:
                a, b = b, a
            ax.annotate("", xy=a+0.61*(b-a), xytext=a+0.43*(b-a),
                        arrowprops={"arrowstyle":"-|>","color":"#333333","lw":1.3})
    if label:
        pos=(a+b)/2+0.17*n
        ax.text(*pos, label, fontsize=12, ha="center", va="center", color="#174564")


def text(ax, x, y, label, **kwargs):
    ax.text(x, y, label, ha="center", va="center", fontsize=12, **kwargs)


def setup(ax, xlim=(-.3,7), ylim=(-2.1,3.9)):
    ax.set_xlim(*xlim);ax.set_ylim(*ylim);ax.axis("off")


def save(fig):
    fig.savefig(Path(__file__).with_suffix(".png").name,dpi=145,facecolor="white")
    plt.close(fig)


def main():
    fig,ax=plt.subplots(figsize=(10.2,3.8))
    ax.annotate("",xy=(1.1,0),xytext=(0,0),arrowprops={"arrowstyle":"->","lw":2})
    text(ax,.45,.38,r"protons")
    ax.add_patch(Rectangle((1.1,-.3),.18,.6,color="#7a6860"));text(ax,1.2,-.65,"target")
    ax.add_patch(Rectangle((1.65,-.32),.8,.64,fill=False,edgecolor="#2a6d85",lw=1.5));text(ax,2.05,.63,"horn")
    ax.annotate("",xy=(3.65,0),xytext=(1.3,0),arrowprops={"arrowstyle":"->","lw":1.7,"color":"#2a6d85"})
    text(ax,3,.32,r"select $\pi^-$")
    ax.annotate("",xy=(2.9,1.05),xytext=(2.5,.05),arrowprops={"arrowstyle":"->","color":"#999999"})
    text(ax,3.6,1.15,r"reject $\pi^+$ and off-momentum parents")
    ax.add_patch(Rectangle((3.9,-.38),3.2,.76,facecolor="#edf3f6",edgecolor="#6e8a99"));text(ax,5.5,.7,"evacuated decay tunnel")
    text(ax,5.4,0,r"$\pi^-\to\mu^-+\bar\nu_\mu$")
    ax.annotate("",xy=(10.3,0),xytext=(7.15,0),arrowprops={"arrowstyle":"->","lw":2,"color":"#2b7c46"})
    text(ax,9.4,.45,r"forward $\bar\nu_\mu$ beam",color="#2b7c46")
    ax.annotate("",xy=(8.3,-1.1),xytext=(7.2,-.05),arrowprops={"arrowstyle":"->","lw":1.8,"connectionstyle":"arc3,rad=.25"})
    ax.add_patch(Rectangle((7.7,-1.65),1.7,.45,facecolor="#b7b7b7",edgecolor="#555555"));text(ax,8.55,-1.43,"charged dump")
    ax.text(5.8,-1.0,"sweep residual charged particles",fontsize=10,ha="center")
    setup(ax,xlim=(-.15,10.8),ylim=(-1.9,1.65));ax.set_title("Focus the charged parents; let their neutrinos continue straight",fontsize=13,pad=10)
    fig.tight_layout();save(fig)

if __name__=="__main__":main()
