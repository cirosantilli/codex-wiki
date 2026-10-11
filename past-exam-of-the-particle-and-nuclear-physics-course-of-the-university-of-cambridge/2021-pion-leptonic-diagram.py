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
    fig,ax=plt.subplots(figsize=(7.2,3.8))
    line(ax,(.5,1.1),(2.2,0));line(ax,(.5,-1.1),(2.2,0),backwards=True)
    line(ax,(2.2,0),(4.2,0),"wavy",label=r"$W^{-*}$")
    line(ax,(4.2,0),(6.1,1.1));line(ax,(4.2,0),(6.1,-1.1),backwards=True)
    for x,y,l in [(.2,1.1,r"$d$"),(.2,-1.1,r"$\bar u$"),(6.45,1.1,r"$\ell^-$"),(6.45,-1.1,r"$\bar\nu_\ell$")]:text(ax,x,y,l)
    text(ax,.8,0,r"$\pi^-$")
    setup(ax,ylim=(-1.8,1.8));ax.set_title(r"$d\bar u\to W^{-*}\to\ell^-\bar\nu_\ell$,  $\ell=e,\mu$",fontsize=14,pad=15)
    fig.tight_layout();save(fig)

if __name__=="__main__":main()
