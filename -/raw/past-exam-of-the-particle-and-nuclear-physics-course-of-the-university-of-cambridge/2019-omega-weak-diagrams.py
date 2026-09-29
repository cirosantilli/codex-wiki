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
    fig,axes=plt.subplots(2,1,figsize=(9,8))
    for ax,rare in zip(axes,[False,True]):
        A=(1.8,2.8)
        line(ax,(.5,2.8),A)
        text(ax,.2,2.8,r"$s$")
        if rare:
            B=(3.3,2.8);C=(4.4,1.2);D=(3,-.7)
            line(ax,A,B);text(ax,2.55,3.1,r"$u$")
            line(ax,B,(6.2,2.8))
            line(ax,(.5,1.2),C);line(ax,C,(6.2,2.0))
            line(ax,(.5,-1.5),(6.2,1.2))
            line(ax,A,D,"wavy",label=r"$W^-$")
            line(ax,B,C,"wavy",label=r"$W^+$")
            line(ax,D,(6.2,-.7));line(ax,D,(6.2,-1.5),backwards=True)
            labels=[(2.8,r"$d$"),(2,r"$u$"),(1.2,r"$s$"),(-.7,r"$d$"),(-1.5,r"$\bar u$")]
            for p in [A,B,C,D]:dot(ax,p)
        else:
            D=(3.3,.45)
            line(ax,A,(6.2,2.8))
            line(ax,(.5,1.2),(6.2,1.2))
            line(ax,(.5,-1.5),(6.2,-1.5))
            line(ax,A,D,"wavy",label=r"$W^-$")
            line(ax,D,(6.2,2.0));line(ax,D,(6.2,-.7),backwards=True)
            labels=[(2.8,r"$u$"),(2,r"$d$"),(1.2,r"$s$"),(-.7,r"$\bar u$"),(-1.5,r"$s$")]
            for p in [A,D]:dot(ax,p)
        text(ax,.2,1.2,r"$s$");text(ax,.2,-1.5,r"$s$")
        for y,label in labels:text(ax,6.47,y,label)
        bracket(ax,6.85,.98,3.02,r"$\Lambda^0$")
        bracket(ax,6.85,-1.72,-.48,r"$\pi^-$" if rare else r"$K^-$")
        setup(ax,xlim=(-.15,7.6),ylim=(-2,3.5))
        ax.set_title(r"$\Omega^-\to\Lambda^0\pi^-$: two W propagators, second-order weak" if rare else r"$\Omega^-\to\Lambda^0K^-$: one W propagator, first-order weak",fontsize=12,pad=12)
    fig.suptitle("Representative lowest-weak-order quark diagrams",fontsize=14)
    fig.text(.5,.018,"Time runs left to right. Only dots are vertices; line crossings are not interactions.",ha="center",fontsize=9)
    fig.tight_layout(rect=(0,.045,1,.96),h_pad=2.4);save(fig)

if __name__=="__main__":main()
