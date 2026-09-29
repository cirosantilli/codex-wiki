"""Original 2019 Particle and Nuclear Physics solution figure.

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


def dot(ax,p):
    ax.plot(*p,"o",color="#333333",ms=4)


def bracket(ax,x,y0,y1,label):
    ax.plot([x-.12,x,x,x-.12],[y0,y0,y1,y1],color="#6e7580",lw=1.3)
    text(ax,x+.35,(y0+y1)/2,label)


def main():
    fig,axes=plt.subplots(2,1,figsize=(8.2,7.1))
    for ax,initial in zip(axes,["d","s"]):
        A=(2,1.0);B=(3.4,2.1)
        line(ax,(.5,1),A);line(ax,A,(6,1))
        line(ax,(.5,-.7),(6,-.7));line(ax,(.5,-1.5),(6,-1.5))
        line(ax,A,B,"wavy",label=r"$W^-$")
        line(ax,B,(6,3));line(ax,B,(6,2.1),backwards=True)
        for x,y,l in [(.2,1,'$'+initial+'$'),(.2,-.7,r"$u$"),(.2,-1.5,r"$d$"),(6.3,1,r"$u$"),(6.3,-.7,r"$u$"),(6.3,-1.5,r"$d$"),(6.3,3,r"$e^-$"),(6.3,2.1,r"$\bar\nu_e$")]:text(ax,x,y,l)
        bracket(ax,6.65,-1.75,1.25,r"$p$")
        dot(ax,A);dot(ax,B)
        setup(ax,xlim=(-.2,7.4),ylim=(-2.1,3.5))
        ax.set_title(r"$n\to pe^-\bar\nu_e$: $d\to u$, coupling $V_{ud}\simeq\cos\theta_C$" if initial=="d" else r"$\Lambda^0\to pe^-\bar\nu_e$: $s\to u$, coupling $V_{us}\simeq\sin\theta_C$",fontsize=12,pad=13)
    fig.suptitle("The spectator u and d quarks are unchanged",fontsize=14)
    fig.tight_layout(rect=(0,.01,1,.95),h_pad=2.3);save(fig)

if __name__=="__main__":main()
