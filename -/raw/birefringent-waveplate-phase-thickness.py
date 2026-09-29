"""Plot stipulated waveplate retardance and original electric-field traces.

Run from _media; tested with Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig = plt.figure(figsize=(10, 6.4), layout="constrained")
    grid = fig.add_gridspec(2, 4, height_ratios=(1.5, 1))
    ax = fig.add_subplot(grid[0, :])
    thickness = np.linspace(0, 33, 500)  # micrometres
    delta = 2 * np.pi * .0100 * thickness / .600
    ax.plot(thickness, delta / np.pi, color="#1765a5", lw=2.5)
    for d, y, label in [(15, .5, "Quarter-wave: 15 µm"),
                         (30, 1, "Half-wave: 30 µm")]:
        ax.plot(d, y, "o", color="#b74d0b")
        ax.plot([0, d, d], [y, y, 0], ls="--", color="#8b949d", lw=1)
        ax.annotate(label, (d, y), xytext=(-12, 18),
                    textcoords="offset points", ha="right", fontsize=11)
    ax.set(xlim=(0, 33), ylim=(0, 1.2), xlabel="Thickness d (µm)",
           ylabel=r"Retardance $\delta/\pi$", yticks=[0, .25, .5, .75, 1])
    ax.grid(alpha=.18)
    ax.set_title(r"$\delta=2\pi\Delta n\,d/\lambda_0$; stipulated $\Delta n=0.0100$, $\lambda_0=600$ nm", pad=12)
    t = np.linspace(0, 2 * np.pi, 600)
    for i, (d, label) in enumerate([(0, "Linear"), (7.5, "Elliptical"),
                                  (15, "Circular"), (30, "Linear, rotated")]):
        a = fig.add_subplot(grid[1, i])
        retardance = 2 * np.pi * .0100 * d / .600
        ef, es = np.cos(t), np.cos(t + retardance)
        a.plot(ef, es, color="#1765a5", lw=2.1)
        a.scatter([ef[0]], [es[0]], color="#b74d0b", s=20, zorder=3)
        a.axhline(0, color="#d7dde2", lw=.8)
        a.axvline(0, color="#d7dde2", lw=.8)
        a.set(xlim=(-1.22, 1.22), ylim=(-1.22, 1.22), aspect="equal",
              xticks=[-1, 0, 1], yticks=[-1, 0, 1], xlabel=r"$E_f/A$",
              ylabel=r"$E_s/A$" if i == 0 else "")
        a.set_title(f"{label}\nd = {d:g} µm", fontsize=11)
    fig.suptitle("One overlapping beam: thickness changes relative phase", fontsize=15)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=130,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
