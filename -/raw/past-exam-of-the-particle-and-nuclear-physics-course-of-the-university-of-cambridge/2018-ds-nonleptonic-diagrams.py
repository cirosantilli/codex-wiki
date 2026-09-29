"""Original 2018 Particle and Nuclear Physics solution figure.

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


def dot(ax,p):ax.plot(*p,"o",color="#333333",ms=4)


def bracket(ax,x,y0,y1,label,left=False):
    d=-.12 if not left else .12
    ax.plot([x+d,x,x,x+d],[y0,y0,y1,y1],color="#6e7580",lw=1.3)
    text(ax,x+(-.4 if left else .4),(y0+y1)/2,label)


def main():
    fig,axes=plt.subplots(3,1,figsize=(8.7,9.6))
    for ax,kind in zip(axes,["Kpi","KK","phipi"]):
        A=(2,1);B=(3.2,2.6)
        line(ax,(.6,1),A);line(ax,A,(5.9,1))
        line(ax,A,B,"wavy",label=r"$W^+$")
        line(ax,B,(5.9,3.2))
        if kind=="phipi":
            line(ax,B,(5.9,2.3),backwards=True)
            line(ax,(.6,-.5),(5.9,.1),backwards=True)
            labels=[(3.2,r"$u$"),(2.3,r"$\bar d$"),(1,r"$s$"),(.1,r"$\bar s$")]
            top,bottom=r"$\pi^+$",r"$\phi$"
        else:
            line(ax,B,(5.9,.1),backwards=True)
            line(ax,(.6,-.5),(5.9,2.3),backwards=True)
            labels=[(3.2,r"$u$"),(2.3,r"$\bar s$"),(1,r"$d$" if kind=="Kpi" else r"$s$"),(.1,r"$\bar d$")]
            top,bottom=r"$K^+$",r"$\pi^0$" if kind=="Kpi" else r"$\bar K^0$"
        text(ax,.28,1,r"$c$");text(ax,.28,-.5,r"$\bar s$")
        for y,label in labels:text(ax,6.2,y,label)
        bracket(ax,6.65,2.06,3.45,top);bracket(ax,6.65,-.14,1.25,bottom)
        dot(ax,A);dot(ax,B)
        titles={"Kpi":r"$D_s^+\to K^+\pi^0$: $|V_{cd}V_{ud}|$, use $-d\bar d/\sqrt{2}$", "KK":r"$D_s^+\to K^+\bar K^0$: $|V_{cs}V_{ud}|$", "phipi":r"$D_s^+\to\phi\pi^+$: $|V_{cs}V_{ud}|$"}
        ax.set_title(titles[kind],fontsize=12,pad=12)
        setup(ax,xlim=(-.2,7.5),ylim=(-1,3.9))
    fig.suptitle("Representative spectator tree diagrams; the antiquark spectator is unchanged",fontsize=13)
    fig.text(.5,.012,"Only dots denote vertices; unmarked crossings do not join lines.",ha="center",fontsize=9)
    fig.tight_layout(rect=(0,.035,1,.96),h_pad=2.3);save(fig)

if __name__=="__main__":main()
