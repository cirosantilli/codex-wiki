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
    fig,axes=plt.subplots(2,2,figsize=(10.2,6.6))
    for ax,kind in zip(axes.flat,["photon","Z","neutrino","Higgs"]):
        if kind=="neutrino":
            A=(2.6,1.1);B=(2.6,-1.1)
            line(ax,(.5,1.5),A);line(ax,(.5,-1.5),B,backwards=True)
            line(ax,A,B,label=r"$\nu_e$")
            line(ax,A,(5.7,1.6),"wavy");line(ax,B,(5.7,-1.6),"wavy")
        else:
            A=(2,0);B=(4.1,0)
            line(ax,(.5,1.5),A);line(ax,(.5,-1.5),A,backwards=True)
            if kind=="Higgs":
                ax.plot([A[0],B[0]],[0,0],color="#7e5c86",lw=1.7,ls="--");text(ax,3.05,.4,r"$h^*$")
            else:line(ax,A,B,"wavy",label=r"$\gamma^*$" if kind=="photon" else r"$Z^*$")
            line(ax,B,(5.7,1.6),"wavy");line(ax,B,(5.7,-1.6),"wavy")
        for p in [A,B]:dot(ax,p)
        for x,y,l in [(.2,1.5,r"$e^-$"),(.2,-1.5,r"$e^+$"),(6.1,1.6,r"$W^-$"),(6.1,-1.6,r"$W^+$")]:text(ax,x,y,l)
        setup(ax,xlim=(-.15,6.7),ylim=(-2.15,2.15))
        ax.set_title({"photon":"s-channel photon","Z":"s-channel Z","neutrino":"t-channel electron neutrino","Higgs":"s-channel Higgs (electron Yukawa coupling)"}[kind],fontsize=11,pad=10)
    fig.suptitle(r"The four Standard Model tree diagrams for $e^+e^-\to W^+W^-$",fontsize=14)
    fig.tight_layout(rect=(0,.02,1,.95),h_pad=2,w_pad=1.3);save(fig)

if __name__=="__main__":main()
