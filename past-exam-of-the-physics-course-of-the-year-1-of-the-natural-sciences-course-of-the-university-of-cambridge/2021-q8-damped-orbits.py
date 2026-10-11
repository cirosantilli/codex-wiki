"""Original exact damped trajectories. Python 3.14.4; root pyproject.toml deps.

The overdamped example has gamma/omega=1.5, not an additional exam datum.
Run from the desired output directory; writes the PNG basename into cwd.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np


def under(t):
    omega = np.sqrt(3.95/0.10)
    gamma = 0.05/(2*0.10)
    nu = np.sqrt(omega**2-gamma**2)
    cc, ss = np.cos(nu*t), np.sin(nu*t)
    return np.exp(-gamma*t)*(cc+(gamma-omega)/nu*ss), np.exp(-gamma*t)*(cc+(gamma+omega)/nu*ss)


def main():
    fig, axes = plt.subplots(1, 2, figsize=(10.6, 5.2), layout="constrained", facecolor="white")
    ax = axes[0]
    t = np.linspace(0, 4, 2401)
    x, y = under(t)
    points = np.column_stack((x, y))
    lines = LineCollection(np.stack((points[:-1], points[1:]), axis=1), cmap="viridis", norm=plt.Normalize(0,4), linewidth=2)
    lines.set_array(t[:-1])
    ax.add_collection(lines)
    for sec, offset in [(0, (12, 8)), (1, (22, 3)), (2, (25, -8)), (3, (6, -24)), (4, (-58, -30))]:
        xx, yy = under(sec)
        ax.plot(xx, yy, "ko", ms=3.5)
        ax.annotate(f"{sec} s", (xx, yy), offset, textcoords="offset points", fontsize=8.5, arrowprops={"arrowstyle":"-", "lw":0.6})
    ax.annotate("", (0.78,1.22), (1,1), arrowprops={"arrowstyle":"->", "color":"#b46b20", "lw":1.8})
    ax.set(xlim=(-1.5,1.5), ylim=(-1.5,1.5), title="Given damping: nearly four anticlockwise turns\nInitial tangent is upper left; final radius is 0.368 of initial")
    fig.colorbar(lines, ax=ax, label="Time (s)", shrink=0.65, fraction=0.045, pad=0.02)
    ax = axes[1]
    s=np.linspace(0,18,1801)
    gamma=1.5
    alpha=np.sqrt(gamma**2-1)
    x=np.exp(-gamma*s)*(np.cosh(alpha*s)+(gamma-1)/alpha*np.sinh(alpha*s))
    y=np.exp(-gamma*s)*(np.cosh(alpha*s)+(gamma+1)/alpha*np.sinh(alpha*s))
    ax.plot(x,y,color="#205e9b",lw=2.5)
    for sec in [0.5,2,5]:
        j=np.argmin(abs(s-sec))
        ax.annotate("", (x[j+20],y[j+20]), (x[j],y[j]), arrowprops={"arrowstyle":"-|>","color":"#205e9b","lw":1.6})
    ax.plot(1,1,"ko",ms=4)
    ax.text(1.02,0.94,"Start",fontsize=9)
    ax.annotate("", (0.8,1.2), (1,1), arrowprops={"arrowstyle":"->","color":"#b46b20","lw":1.8})
    ratio=(gamma+alpha+1)/(gamma+alpha-1)
    xx=np.linspace(0,0.43,100)
    ax.plot(xx,ratio*xx,color="0.45",ls=":",lw=1.2)
    ax.text(0.06,0.62,"Late approach along\na fixed ray",fontsize=9,color="0.35")
    ax.plot(0,0,"ko",ms=4)
    ax.set(xlim=(-0.08,1.18),ylim=(-0.08,1.5),title=r"Overdamped example: $\gamma=1.5\omega$"+"\nBends toward origin without repeated revolutions")
    for ax in axes:
        ax.set(xlabel="$x/c$",ylabel="$y/c$")
        ax.set_aspect("equal")
        ax.set_facecolor("white")
        ax.axhline(0,color="0.6",lw=0.7)
        ax.axvline(0,color="0.6",lw=0.7)
        ax.grid(alpha=0.16)
        ax.spines[["top","right"]].set_visible(False)
    fig.savefig(Path(__file__).with_suffix(".png").name,dpi=150,facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
