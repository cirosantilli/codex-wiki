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
    fig,axes=plt.subplots(2,1,figsize=(7.2,4.6))
    for ax,flip in zip(axes,[False,True]):
        left,right=(r"$\bar\nu_\mu$",r"$\mu^-$") if flip else (r"$\mu^-$",r"$\bar\nu_\mu$")
        for x,direction,name in [(1.4,-1,left),(4.5,1,right)]:
            text(ax,x,.95,name)
            for y,colour in [(.5,"#333333"),(.0,"#b84b34")]:
                ax.annotate("",xy=(x+direction*.7,y),xytext=(x-direction*.25,y),arrowprops={"arrowstyle":"-|>","lw":2,"color":colour})
            text(ax,x,-.48,r"$h=+\frac{1}{2}$")
        text(ax,2.9,.5,"momentum",color="#333333")
        text(ax,2.9,0,"spin",color="#b84b34")
        setup(ax,xlim=(0,6),ylim=(-.9,1.4))
    fig.suptitle("Back-to-back momenta, opposite spins, equal positive helicities",fontsize=12)
    fig.tight_layout(rect=(0,.01,1,.94),h_pad=1.2);save(fig)

if __name__=="__main__":main()
