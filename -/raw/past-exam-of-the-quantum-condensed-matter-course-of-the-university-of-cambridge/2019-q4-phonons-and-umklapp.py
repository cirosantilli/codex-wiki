"""Original thermal phonon and Fermi-surface geometry diagrams; PNG to cwd.

Tested with Python 3.14, NumPy and Matplotlib; see root pyproject.toml.
The optical mode is illustrative and requires an atomic basis. The Fermi
circles are a section of spherical Fermi surfaces, not fitted band data.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.0), facecolor="white")
    q = np.linspace(-1, 1, 1400)
    acoustic = 2/np.pi*np.sin(np.pi*abs(q)/2)
    optical = 1.15 + .10*np.cos(np.pi*q)
    ax = axes[0]
    ax.plot(q, acoustic, lw=2, color="#1768ab", label="Acoustic")
    ax.plot(q, optical, lw=2, color="#bd6426", label="Optical")
    for energy, color, label in ((.16, "#28744b", r"$k_BT_1/\hbar$"),
                                  (.37, "#8255a1", r"$k_BT_2/\hbar$")):
        q_cut = 2/np.pi*np.arcsin(np.pi*energy/2)
        ax.hlines(energy, -q_cut, q_cut, lw=1.3, ls="--", color=color)
        ax.vlines([-q_cut, q_cut], 0, energy, lw=.7, ls=":", color=color)
        ax.text(q_cut + .04, energy, label, color=color, va="center", fontsize=9)
    ax.set(xlim=(-1.04, 1.04), ylim=(0, 1.4), xlabel=r"$q/(\pi/a)$",
           ylabel=r"$\omega/(v_s\pi/a)$")
    ax.set_title("Thermally populated momenta grow with T", fontsize=10.5)
    ax.legend(frameon=False, fontsize=9, loc="upper right")

    ax = axes[1]
    angle = np.linspace(0, 2*np.pi, 500)
    for center, color, style in ((0, "#1768ab", "-"), (2, "#697781", "--")):
        xx, yy = center + .7*np.cos(angle), .7*np.sin(angle)
        ax.fill(xx, yy, color=color, alpha=.06)
        ax.plot(xx, yy, color=color, ls=style, lw=1.7)
        ax.scatter([center], [0], s=15, color=color)
    ax.axvline(1, lw=.8, ls=":", color="#9ba5ae")
    ax.annotate("", xy=(1.3, 0), xytext=(.7, 0),
                arrowprops={"arrowstyle": "<->", "color": "#bd6426", "lw": 1.6})
    ax.text(1, .12, r"$q_U=0.6\pi/a$", ha="center", fontsize=10, color="#bd6426")
    ax.text(0, -.88, r"$k_F=0.7\pi/a$", ha="center", fontsize=10)
    ax.text(2, -.88, r"Translated by $G=2\pi/a$", ha="center", fontsize=9)
    ax.text(1, .83, "Zone boundary", ha="center", fontsize=9, color="#697781")
    ax.set(xlim=(-.85, 2.85), ylim=(-1.05, 1.05), aspect="equal",
           xlabel=r"$k_x/(\pi/a)$", ylabel=r"$k_y/(\pi/a)$")
    ax.set_title("Minimum phonon for Umklapp scattering", fontsize=10.5)
    for ax in axes:
        ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout(w_pad=1.8)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=125, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
