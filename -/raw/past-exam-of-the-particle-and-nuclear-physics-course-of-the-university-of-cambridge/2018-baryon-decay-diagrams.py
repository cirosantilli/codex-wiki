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
    fig,axes=plt.subplots(3,1,figsize=(8.6,10))
    for ax,emitter in zip(axes[:2],[0,1]):
        ys=[2.,.6,-1.1]
        for i,(y,label) in enumerate(zip(ys,[r"$u$",r"$d$",r"$s$"])):
            v=(2.5,y)
            if i==emitter:
                line(ax,(.7,y),v);line(ax,v,(5.9,y));dot(ax,v)
                line(ax,v,(5.9,3.1),"wavy");text(ax,6.25,3.1,r"$\gamma$")
            else:line(ax,(.7,y),(5.9,y))
            text(ax,.45,y,label);text(ax,6.2,y,label)
        bracket(ax,.12,-1.35,2.25,r"$\Sigma^0$",left=True)
        bracket(ax,6.65,-1.35,2.25,r"$\Lambda^0$")
        setup(ax,xlim=(-.7,7.5),ylim=(-1.7,3.6))
        ax.set_title("Photon emission from the up quark" if emitter==0 else "Photon emission from the down quark",fontsize=12)
    ax=axes[2];A=(2,2);B=(3.2,-.2)
    line(ax,(.7,2),A);line(ax,A,(5.9,2))
    line(ax,(.7,.6),(5.9,.6));line(ax,(.7,-1.1),(5.9,-1.1))
    line(ax,A,B,"gluon",label=r"$g^*$")
    line(ax,B,(5.9,-.2));line(ax,B,(5.9,-1.9),backwards=True)
    for y in [2,.6,-1.1]:text(ax,.45,y,r"$u$")
    for y,label in [(2,r"$u$"),(.6,r"$u$"),(-.2,r"$d$"),(-1.1,r"$u$"),(-1.9,r"$\bar d$")]:text(ax,6.2,y,label)
    bracket(ax,.12,-1.35,2.25,r"$\Delta^{++}$",left=True)
    bracket(ax,6.65,-.43,2.25,r"$p$");bracket(ax,6.65,-2.12,-.88,r"$\pi^+$")
    dot(ax,A);dot(ax,B)
    setup(ax,xlim=(-.7,7.5),ylim=(-2.55,2.7))
    ax.set_title(r"Representative strong pair creation: $\Delta^{++}\to p\pi^+$",fontsize=12)
    fig.suptitle("Constituent-quark diagrams for electromagnetic and strong baryon decays",fontsize=13)
    fig.text(.5,.015,"Only dots are vertices. Final quarks are projected onto the indicated bound states.",ha="center",fontsize=9)
    fig.tight_layout(rect=(0,.04,1,.96),h_pad=2);save(fig)

if __name__=="__main__":main()
