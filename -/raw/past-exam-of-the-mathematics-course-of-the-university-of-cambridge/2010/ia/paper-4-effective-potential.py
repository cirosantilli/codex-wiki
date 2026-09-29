"""Draw attractive/repulsive effective potentials; tested with Python 3.14.4.

Uses the root numpy/matplotlib dependencies. Writes the PNG basename to CWD.
"""
from pathlib import Path
import os
import tempfile

os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "paper4-matplotlib"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    r = np.linspace(0.18, 6, 1200)
    fig, axes = plt.subplots(1, 2, figsize=(6.8, 3.8), dpi=150, facecolor="white")
    for ax, q in zip(axes, (1, -1)):
        ax.set_facecolor("white")
        ax.plot(r, 0.5 / r**2 - q / r, color="#286e99", linewidth=2)
        ax.axhline(0, color="#77838d", linewidth=0.8)
        ax.set(xlim=(0, 6), xlabel="$r$", ylabel="$U(r)$")
        ax.spines[["top", "right"]].set_visible(False)
        ax.set_title("Attraction: $Q=1$" if q == 1 else "Repulsion: $Q=-1$", fontsize=11)
        ax.text(0.97, 0.95, "$h=1$", ha="right", va="top", transform=ax.transAxes)
    left, right = axes
    left.set_ylim(-0.72, 2.6)
    right.set_ylim(-0.15, 3.5)
    energy = -0.3
    disc = 1 + 2 * energy
    turning = np.array([(1 - np.sqrt(disc)) / (-2 * energy),
                        (1 + np.sqrt(disc)) / (-2 * energy)])
    left.axhline(energy, color="#ac4b31", linestyle="--", linewidth=1)
    left.text(5.65, energy + 0.08, "$E=-0.3$", color="#ac4b31", ha="right", fontsize=9)
    left.scatter(turning, [energy, energy], color="#ac4b31", s=22, zorder=4)
    for rr, label in zip(turning, ("$r_{\\min}$", "$r_{\\max}$")):
        left.plot([rr, rr], [-0.68, energy], ":", color="#ac4b31", linewidth=0.9)
        left.text(rr, -0.67, label, ha="center", fontsize=9)
    left.scatter([1], [-0.5], color="#23394d", s=20, zorder=4)
    left.annotate("minimum $(1,-1/2)$", xy=(1, -0.5), xytext=(2.0, 0.6),
                  arrowprops=dict(arrowstyle="->", color="#435c75", linewidth=0.8), fontsize=9)
    right.text(2.1, 1.6, "$U(r)>0$\nstrictly decreasing", fontsize=10, color="#286e99")
    fig.tight_layout(pad=1.2, w_pad=1.5)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
