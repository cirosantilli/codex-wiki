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
    A=np.linspace(4,250,900)
    Z=A/(2+(.71/(2*23.3))*A**(2/3))
    volume=np.full_like(A,-15.7);surface=17.2/A**(1/3)
    coulomb=.71*Z**2/A**(4/3);asymmetry=23.3*(1-2*Z/A)**2
    total=volume+surface+coulomb+asymmetry
    fig,ax=plt.subplots(figsize=(8.7,5.1))
    for term,label,colour in [(volume,"Volume", "#28659a"),(surface,"Surface", "#c46c26"),(coulomb,"Coulomb", "#c13e47"),(asymmetry,"Asymmetry", "#7654a8")]:ax.plot(A,term,label=label,lw=2,color=colour)
    ax.plot(A,total,label="Sum (pairing omitted)",color="#222222",lw=2.4)
    ax.axhline(0,color="#bbbbbb",lw=.8)
    ax.axhline(-8,color="#888888",ls=":",lw=1)
    ax.text(173,-7.1,"Typical signed value: about -8 MeV",fontsize=9,ha="center")
    ax.set_xlabel(r"Mass number $A$")
    ax.set_ylabel(r"Paper's signed contribution $E_{\rm bind}/A$ (MeV)")
    ax.set_title("Semi-empirical contributions on a smooth stated stability path",fontsize=12)
    ax.set_xlim(0,250);ax.set_ylim(-18,12);ax.set_yticks([-16,-8,0,4,8,12])
    ax.legend(loc="upper right",fontsize=9,ncol=2,framealpha=.95)
    ax.grid(alpha=.18);ax.spines[["top","right"]].set_visible(False)
    fig.text(.5,.015,r"$Z_*(A)=A/[2+(a_3/2a_4)A^{2/3}]$; conventional positive binding has the opposite sign.",ha="center",fontsize=9)
    fig.tight_layout(rect=(0,.05,1,1));save(fig)

if __name__=="__main__":main()
