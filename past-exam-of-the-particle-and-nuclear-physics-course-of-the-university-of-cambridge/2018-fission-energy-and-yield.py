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
    fig,axes=plt.subplots(1,2,figsize=(10,4.1));y=np.linspace(.0001,.9999,1000)
    A,Z=236.,92.
    Q=18*A**(2/3)*(1-y**(2/3)-(1-y)**(2/3))+.72*Z*Z/A**(1/3)*(1-y**(5/3)-(1-y)**(5/3))
    ax=axes[0];ax.plot(y,Q,color="#245e87",lw=2);ax.axhline(0,color="#999999",lw=.8)
    ax.axvline(.5,color="#999999",ls=":",lw=1)
    ax.set(xlabel=r"Fragment fraction $y$",ylabel="Smooth-model energy release (MeV)",title=r"Proportional spherical fragments: $A=236$, $Z=92$",xlim=(0,1))
    ax=axes[1];f=np.exp(-.5*((y-.4)/.045)**2)+np.exp(-.5*((y-.6)/.045)**2);f/=f.max()
    ax.plot(y,f,color="#a44c38",lw=2);ax.axvline(.5,color="#999999",ls=":",lw=1)
    ax.set(xlabel=r"Fragment fraction $y$",ylabel="Schematic relative yield",title="Typical low-excitation actinide shape",xlim=(0,1),ylim=(0,1.12))
    ax.text(.5,1.04,"illustration, not measured data",ha="center",fontsize=9)
    for ax in axes:ax.grid(alpha=.13);ax.spines[["top","right"]].set_visible(False)
    fig.tight_layout(w_pad=2);save(fig)

if __name__=="__main__":main()
