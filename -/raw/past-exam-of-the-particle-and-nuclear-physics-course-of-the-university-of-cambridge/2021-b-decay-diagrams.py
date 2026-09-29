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
    fig,axes=plt.subplots(2,1,figsize=(7.3,6.4))
    for ax,charm in zip(axes,[True,False]):
        line(ax,(.5,1.0),(2.0,1.0));line(ax,(2.0,1.0),(5.5,1.0))
        line(ax,(.5,0),(5.5,0),backwards=True)
        line(ax,(2,1),(3.1,2.0),"wavy",label=r"$W^-$")
        line(ax,(3.1,2),(5.5,2.9));line(ax,(3.1,2),(5.5,1.95),backwards=True)
        for x,y,l in [(.2,1,r"$b$"),(.2,0,r"$\bar d$"),(5.85,1,r"$c$" if charm else r"$u$"),(5.85,0,r"$\bar d$"),(5.85,2.9,r"$d$"),(5.85,1.95,r"$\bar u$")]:text(ax,x,y,l)
        ax.set_title(r"$\bar B_d^0\to D^+\pi^-$: $V_{cb}V_{ud}^*$" if charm else r"$\bar B_d^0\to\pi^+\pi^-$: $V_{ub}V_{ud}^*$",fontsize=12)
        setup(ax,ylim=(-.5,3.5))
    fig.suptitle("External-W spectator decay diagrams",fontsize=14)
    fig.tight_layout(rect=(0,.01,1,.95),h_pad=1.9);save(fig)

if __name__=="__main__":main()
