"""Unseeded undepleted sum-frequency growth; write PNG to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    z = np.linspace(0, 4, 900)
    intensity = np.sin(np.pi * z / 2) ** 2
    fig, ax = plt.subplots(figsize=(6, 3.4), dpi=150, facecolor="white")
    ax.plot(z, intensity, lw=2, color="#165d9b")
    ax.axvline(1, color="#9b5a16", ls="--", lw=1)
    ax.scatter([0, 1, 2, 4], [0, 1, 0, 0], s=20, color="#165d9b", zorder=4)
    ax.annotate("First maximum", (1, 1), xytext=(1.45, 1.06),
                arrowprops={"arrowstyle": "->", "lw": .8}, fontsize=9)
    ax.annotate("First return to zero", (2, 0), xytext=(2.3, .22),
                arrowprops={"arrowstyle": "->", "lw": .8}, fontsize=9)
    ax.set(xlim=(0, 4.08), ylim=(-.035, 1.16),
           xlabel=r"Distance $z/\ell_c$, with $\ell_c=\pi/|\Delta k|$",
           ylabel=r"Generated intensity $I_3/I_{3,\mathrm{peak}}$",
           title="Phase mismatch prevents monotonic growth")
    ax.set_xticks([0, 1, 2, 3, 4])
    ax.grid(alpha=.2)
    fig.text(.5, .025, r"$A_3(0)=0$; $L=4\ell_c$; lossless crystal and constant pumps",
             ha="center", fontsize=9)
    fig.subplots_adjust(left=.12, right=.97, bottom=.23, top=.86)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
