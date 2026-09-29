#!/usr/bin/env python3
"""Plot the calculated crossed-sheet field; write the PNG basename to cwd.

Tested with Python 3.14.4, numpy 2.3.5 and matplotlib 3.10.7 (+dfsg1).
Dependencies are already listed in the repository pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    axis = np.linspace(-2.65, 2.65, 17)
    x, y = np.meshgrid(axis, axis)
    keep = (abs(y) > .13) & (abs(y-x) > .15)
    u = np.sign(y-x)/np.sqrt(2)
    v = np.sign(y)-np.sign(y-x)/np.sqrt(2)
    fig, ax = plt.subplots(figsize=(5.8, 5.5), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    ax.quiver(x[keep], y[keep], u[keep], v[keep], color="#333333",
              angles="xy", scale_units="xy", scale=5.7, width=.004)
    ax.plot([-3, 3], [0, 0], color="#c84444", lw=2)
    ax.plot([-3, 3], [-3, 3], color="#0072b2", lw=2)
    ax.text(-2.85, .12, r"$+\sigma$ on $y=0$", color="#aa3030", fontsize=11)
    ax.text(1.22, 1.82, r"$-\sigma$ on $y=x$", color="#0072b2", fontsize=11, rotation=45)
    ax.set(xlim=(-3, 3), ylim=(-3, 3), aspect="equal", xlabel=r"$x$", ylabel=r"$y$",
           title="Superposed fields of two oppositely charged sheets")
    ax.spines[["top", "right"]].set_visible(False)
    ax.text(0, -3.75, r"Arrow lengths are proportional to $|\mathbf{E}|$; sheet fields use $E_s=\sigma/(2\varepsilon_0)$.",
            ha="center", fontsize=9)
    fig.tight_layout()
    fig.savefig(Path(__file__).stem+".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
