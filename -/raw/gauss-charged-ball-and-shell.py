"""Normalized Gauss-law fields and enclosed charges of two ideal distributions."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    inside = np.linspace(0, 1, 301)
    outside = np.linspace(1, 3, 501)
    assert np.isclose((.5**3)/(.5**2), .5)
    assert np.isclose(1/2**2, .25)
    assert np.allclose(outside**2 * (1/outside**2), 1)
    blue, orange = "#176997", "#b55d20"
    fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.8), dpi=120)
    for ax in axes:
        ax.axvline(1, color="#a3afb9", ls=":", lw=1)
        ax.set(xlim=(0, 3), ylim=(-.08, 1.2), xlabel="Radius r / R")
        ax.grid(alpha=.15)
    ax = axes[0]
    ax.plot(inside, inside, color=blue, lw=2.5, label="Uniform volume charge")
    ax.plot(outside, 1/outside**2, color=blue, lw=3)
    ax.plot(inside, np.zeros_like(inside), color=orange, lw=2, ls="--",
            label="Uniform thin-shell charge")
    ax.plot(outside, 1/outside**2, color=orange, lw=2, ls="--")
    ax.scatter([1, 1], [0, 1], facecolor="white", edgecolor=orange, s=65, lw=1.5, zorder=4)
    ax.scatter([.5, 2], [.5, .25], color=blue, s=33, zorder=5)
    ax.text(.08, 1.12, "At r = R/2:\nball field = $E_R/2$\nshell field = 0", fontsize=9, va="top")
    ax.annotate("Same exterior field", (1.75, 1/1.75**2), xytext=(1.52, .62),
                fontsize=10, arrowprops={"arrowstyle": "->", "color": "#60727f"})
    ax.set_ylabel(r"Radial field $E/E_R$")
    ax.set_title("Field: enclosed charge / surface area", fontsize=12)
    ax.legend(loc="upper right", fontsize=9, frameon=False)
    ax = axes[1]
    ax.plot(inside, inside**3, color=blue, lw=2.5, label="Volume fraction (r/R)³")
    ax.plot(outside, np.ones_like(outside), color=blue, lw=3)
    ax.plot(inside, np.zeros_like(inside), color=orange, lw=2, ls="--", label="Shell: 0 inside, 1 outside")
    ax.plot(outside, np.ones_like(outside), color=orange, lw=2, ls="--")
    ax.scatter([1, 1], [0, 1], facecolor="white", edgecolor=orange, s=65, lw=1.5, zorder=4)
    ax.scatter([.5], [.125], color=blue, s=33, zorder=5)
    ax.annotate("r = R/2 encloses Q/8\nfor volume charge", (.5, .125), xytext=(1.15, .45),
                fontsize=10, arrowprops={"arrowstyle": "->", "color": blue})
    ax.set_ylabel("Enclosed charge / total charge Q")
    ax.set_title("Different interior sources; same total Q", fontsize=12)
    ax.legend(loc="upper right", fontsize=9, frameon=False)
    fig.suptitle("Gauss' law distinguishes where the same charge is distributed", fontsize=14)
    fig.text(.5, .025, r"$E_R=Q/(4\pi\varepsilon_0R^2)$; hollow shell endpoints show one-sided limits at the ideal charged sheet",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=.065, right=.97, bottom=.18, top=.80, wspace=.25)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
