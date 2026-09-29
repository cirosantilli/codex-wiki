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
    fig,axes=plt.subplots(3,1,figsize=(7.2,8.2))
    for ax,minus in zip(axes[:2],[False,True]):
        line(ax,(.5,0),(2.1,0));line(ax,(2.1,0),(5.3,0))
        line(ax,(2.1,0),(3.2,1.1),"wavy",label=r"$W^-$" if minus else r"$W^+$")
        line(ax,(3.2,1.1),(5.3,1.9),backwards=not minus)
        line(ax,(3.2,1.1),(5.3,1.0),backwards=minus)
        text(ax,.2,0,r"$d$" if minus else r"$u$")
        text(ax,5.65,0,r"$u$" if minus else r"$d$")
        text(ax,5.65,1.9,r"$e^-$" if minus else r"$e^+$")
        text(ax,5.65,1.0,r"$\bar\nu_e$" if minus else r"$\nu_e$")
        ax.set_title("(b) Neutron-rich: beta-minus decay" if minus else "(a) Proton-rich: beta-plus decay",fontsize=12)
        setup(ax,ylim=(-.5,2.5))
    ax=axes[2]
    line(ax,(.5,1.2),(2.2,1.2));line(ax,(2.2,1.2),(5.3,1.2))
    line(ax,(.5,-.5),(2.2,-.5));line(ax,(2.2,-.5),(5.3,-.5))
    line(ax,(2.2,1.2),(2.2,-.5),"wavy",label=r"$W^+$")
    for x,y,l in [(.2,1.2,r"$u$"),(5.65,1.2,r"$d$"),(.2,-.5,r"$e^-$"),(5.65,-.5,r"$\nu_e$")]:text(ax,x,y,l)
    ax.set_title("(a) Alternative proton-to-neutron process: electron capture",fontsize=12)
    setup(ax,ylim=(-1.0,1.8))
    fig.suptitle("Weak charged-current quark transitions",fontsize=14)
    fig.tight_layout(rect=(0,.01,1,.96),h_pad=2.3);save(fig)

if __name__=="__main__":main()
