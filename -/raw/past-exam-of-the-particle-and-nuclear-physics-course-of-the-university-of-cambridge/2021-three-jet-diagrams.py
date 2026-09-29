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
    fig,axes=plt.subplots(2,1,figsize=(7.3,7))
    for ax,anti in zip(axes,[False,True]):
        line(ax,(.3,.9),(1.6,0));line(ax,(.3,-.9),(1.6,0),backwards=True)
        text(ax,.1,1.1,r"$e^-$");text(ax,.1,-1.1,r"$e^+$")
        line(ax,(1.6,0),(3.2,0),"wavy",label=r"$\gamma^*,Z^*$")
        upper=(4.6,.8);lower=(4.6,-.8)
        line(ax,(3.2,0),upper);line(ax,upper,(6,1.5))
        line(ax,(3.2,0),lower,backwards=True);line(ax,lower,(6,-1.5),backwards=True)
        start=lower if anti else upper;end=(6,-2.4) if anti else (6,2.4)
        line(ax,start,end,"gluon");text(ax,6.3,end[1],r"$g$")
        text(ax,6.3,1.5,r"$q$");text(ax,6.3,-1.5,r"$\bar q$")
        ax.set_title("Emission from the antiquark" if anti else "Emission from the quark",fontsize=12)
        setup(ax,ylim=(-2.8,2.9))
    fig.suptitle(r"Leading $e^+e^-\to q\bar q g$ diagrams",fontsize=14)
    fig.tight_layout(rect=(0,.02,1,.96),h_pad=1.7);save(fig)

if __name__=="__main__":main()
