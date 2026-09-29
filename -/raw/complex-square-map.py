"""Plot z -> z**2 globally and its local rotation/scaling at 1+i.

Run from _media; tested with Python 3.14.4, NumPy 2.3.5 and
Matplotlib 3.10.7. The opaque PNG is saved in the current directory.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def draw_complex(ax, points, **kwargs):
    ax.plot(points.real, points.imag, **kwargs)


def arrow(ax, endpoint, color, label, offset):
    ax.annotate("", xy=(endpoint.real, endpoint.imag), xytext=(0, 0),
                arrowprops={"arrowstyle": "->", "lw": 2.3, "color": color})
    ax.annotate(label, xy=(endpoint.real, endpoint.imag), xytext=offset,
                textcoords="offset points", color=color, fontsize=11)


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    blue, orange, purple = "#2366a8", "#b95d16", "#844ba0"
    fig, axes = plt.subplots(2, 2, figsize=(9.6, 7.8), dpi=120,
                             constrained_layout=True)
    fig.patch.set_facecolor("white")
    fig.suptitle(r"The complex square: global bending, local rotation and scaling",
                 fontsize=15)
    source, target, local_source, local_target = axes.flat

    t = np.linspace(-1.5, 1.5, 601)
    for level in np.linspace(-1.5, 1.5, 7):
        vertical = level + 1j*t
        horizontal = t + 1j*level
        for curve, color in ((vertical, blue), (horizontal, orange)):
            draw_complex(source, curve, color=color, lw=1.2, alpha=.8)
            draw_complex(target, curve**2, color=color, lw=1.2, alpha=.8)
    source.set(title=r"Input grid in the $z$ plane", xlim=(-1.7, 1.7),
               ylim=(-1.7, 1.7), xlabel=r"Re $z$", ylabel=r"Im $z$")
    target.set(title=r"Exact image $w=z^2$", xlim=(-4.9, 4.9),
               ylim=(-4.9, 4.9), xlabel=r"Re $w$", ylabel=r"Im $w$")
    for ax, point, text_label in ((source, 1+1j, r"$z_0=1+i$"),
                                 (target, 2j, r"$w_0=2i$")):
        ax.scatter([point.real], [point.imag], color=purple, s=42, zorder=6)
        ax.annotate(text_label, (point.real, point.imag), xytext=(7, 8),
                    textcoords="offset points", color=purple,
                    bbox={"facecolor": "white", "edgecolor": "none", "alpha": .9})
        ax.scatter([0], [0], color="black", s=22, zorder=6)
    target.annotate("critical point: derivative = 0", (0, 0), xytext=(-4.5, -3.8),
                    fontsize=10, arrowprops={"arrowstyle": "->", "color": "#444444"},
                    bbox={"facecolor": "white", "edgecolor": "none", "alpha": .9})

    theta = np.linspace(0, 2*np.pi, 601)
    h = .1*np.exp(1j*theta)
    linear = 2*(1+1j)*h
    exact = linear+h**2
    draw_complex(local_source, h, color=purple, lw=2)
    draw_complex(local_target, exact, color=purple, lw=2, label="exact displacement")
    draw_complex(local_target, linear, color="black", lw=1.4, ls="--",
                 label=r"linear prediction $(2+2i)h$")
    arrow(local_source, .1+0j, blue, r"$h=0.1$", (5, -5))
    arrow(local_source, .1j, orange, r"$h=0.1i$", (5, 2))
    arrow(local_target, .2+.2j, blue, r"$0.2+0.2i$", (0, 10))
    arrow(local_target, -.2+.2j, orange, r"$-0.2+0.2i$", (-42, 10))
    local_source.set(title=r"Small increments around $z_0=1+i$",
                     xlim=(-.17, .17), ylim=(-.17, .17),
                     xlabel=r"Re $h$", ylabel=r"Im $h$")
    local_source.text(0, -.15, r"$|h|=0.1$", ha="center", fontsize=11)
    local_target.set(title=r"Rotation $45^\circ$; scale $2\sqrt{2}$",
                     xlim=(-.44, .44), ylim=(-.44, .44),
                     xlabel=r"Re $(f(z_0+h)-f(z_0))$",
                     ylabel=r"Im $(f(z_0+h)-f(z_0))$")
    local_target.legend(loc="lower center", fontsize=9, framealpha=1)
    for ax in axes.flat:
        ax.set_facecolor("white")
        ax.set_aspect("equal", adjustable="box")
        ax.axhline(0, color="#999999", lw=.7, zorder=0)
        ax.axvline(0, color="#999999", lw=.7, zorder=0)
        ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path.cwd() / "complex-square-map.png", facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
