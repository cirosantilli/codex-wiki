"""Original tree diagrams for e+ e- -> W+ W-; write PNG to cwd."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def line(ax, start, end, *, arrow=False, reverse=False, dashed=False):
    ax.plot(*zip(start, end), color="#20354a", lw=1.8,
            ls="--" if dashed else "-")
    if arrow:
        start, end = np.asarray(start), np.asarray(end)
        a, b = start + 0.42 * (end - start), start + 0.62 * (end - start)
        if reverse:
            a, b = b, a
        ax.annotate("", xy=b, xytext=a,
                    arrowprops={"arrowstyle": "-|>", "color": "#20354a",
                                "lw": 1.4, "mutation_scale": 12})


def wave(ax, start, end, *, cycles=6):
    start, end = np.asarray(start), np.asarray(end)
    delta = end - start
    normal = np.array([-delta[1], delta[0]]) / np.linalg.norm(delta)
    t = np.linspace(0, 1, 350)
    points = start[:, None] + delta[:, None] * t
    points += normal[:, None] * 0.014 * np.sin(2 * np.pi * cycles * t)
    ax.plot(*points, color="#8a3b18", lw=1.5)


def labels(ax):
    for x, y, text in [(0.03, 0.93, r"$e^-$"),
                       (0.03, 0.07, r"$e^+$"),
                       (0.97, 0.93, r"$W^-$"),
                       (0.97, 0.07, r"$W^+$")]:
        ax.text(x, y, text, ha="center", va="center", fontsize=15)
    ax.set(xlim=(-0.04, 1.04), ylim=(-0.06, 1.08), aspect="equal")
    ax.axis("off")


def schannel(ax, name, title, *, scalar=False):
    left, right = (0.34, 0.5), (0.66, 0.5)
    line(ax, (0.08, 0.84), left, arrow=True)
    line(ax, (0.08, 0.16), left, arrow=True, reverse=True)
    wave(ax, right, (0.92, 0.84))
    wave(ax, right, (0.92, 0.16))
    if scalar:
        line(ax, left, right, dashed=True)
    else:
        wave(ax, left, right, cycles=5)
    ax.text(0.5, 0.59, name, ha="center", fontsize=16)
    ax.plot(*zip(left, right), "o", color="#20354a", ms=4)
    labels(ax)
    ax.set_title(title, fontsize=13, pad=6)


def tchannel(ax):
    top, bottom = (0.5, 0.77), (0.5, 0.23)
    line(ax, (0.08, 0.84), top, arrow=True)
    line(ax, (0.08, 0.16), bottom, arrow=True, reverse=True)
    line(ax, top, bottom, arrow=True)
    wave(ax, top, (0.92, 0.84))
    wave(ax, bottom, (0.92, 0.16))
    ax.text(0.56, 0.5, r"$\nu_e$", ha="left", va="center", fontsize=16)
    ax.plot(*zip(top, bottom), "o", color="#20354a", ms=4)
    labels(ax)
    ax.set_title("t-channel electron neutrino", fontsize=13, pad=6)


def main():
    fig, axes = plt.subplots(2, 2, figsize=(9, 7), dpi=120,
                             facecolor="white")
    schannel(axes[0, 0], r"$\gamma$", "s-channel photon")
    schannel(axes[0, 1], r"$Z$", "s-channel Z boson")
    tchannel(axes[1, 0])
    schannel(axes[1, 1], r"$h$", "s-channel Higgs boson", scalar=True)
    fig.suptitle(r"$e^-e^+\;\longrightarrow\;W^-W^+$ at tree level",
                 fontsize=17, y=0.98)
    fig.text(0.5, 0.018, "Fermion arrows show fermion flow; all incoming particles are on the left.",
             ha="center", fontsize=10, color="#3a4652")
    fig.subplots_adjust(left=0.04, right=0.96, bottom=0.07, top=0.89,
                        wspace=0.08, hspace=0.26)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
