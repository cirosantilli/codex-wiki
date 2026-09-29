"""Original exact worldlines in Bob's frame. Python 3.14.4; root pyproject.toml deps.

Run from the desired output directory; writes the PNG basename into cwd.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, ax = plt.subplots(figsize=(6.8, 6.6), layout="constrained", facecolor="white")
    ct = np.linspace(0, 0.36, 400)
    ax.plot(np.zeros_like(ct), ct, color="0.35", lw=1.8, label="Bob: $x'=0$")
    ax.plot(ct/9, ct, color="#205e9b", lw=2.3, label="Alice: $v'=c/9$")
    ax.plot(0.2-0.6*ct, ct, color="#b46b20", lw=2.3, label="Asteroid: $v'=-3c/5$")
    xb, ctb = 1/32, 9/32
    ax.plot([0, xb], [ctb, ctb], color="#205e9b", ls=":")
    ax.plot([xb, xb], [0, ctb], color="#205e9b", ls=":")
    ax.plot([0, xb, 0], [0, ctb, 1/3], "ko", ms=5)
    ax.annotate("A", (0, 0), (-13, -17), textcoords="offset points")
    ax.annotate("B: Alice reaches asteroid\n$(x',ct')=(1/32,9/32)$ ly", (xb, ctb), (17, 10), textcoords="offset points", fontsize=9)
    ax.annotate("Asteroid reaches Bob\n$ct'=1/3$ ly", (0, 1/3), (-10, 14), textcoords="offset points", ha="right", fontsize=9)
    ax.annotate("", (-0.035, ctb), (-0.035, 0), arrowprops={"arrowstyle": "<->", "color": "0.35"})
    ax.text(-0.043, ctb/2, "$c\\Delta t'=9/32$ ly", rotation=90, ha="right", va="center", fontsize=9)
    ax.annotate("", (xb, 0.03), (0, 0.03), arrowprops={"arrowstyle": "<->", "color": "0.35"})
    ax.text(0.045, 0.035, "$\\Delta x'=1/32$ ly", va="bottom", fontsize=9)
    ax.annotate("Alice's gradient\n$d(ct')/dx'=9$", (0.017, 0.153), (0.07, 0.15), arrowprops={"arrowstyle": "->", "color": "#205e9b"}, color="#205e9b", fontsize=9)
    ax.text(0.2, -0.014, "$D/\\gamma=1/5$ ly", ha="center", fontsize=9)
    ax.set(xlim=(-0.065, 0.23), ylim=(-0.025, 0.375), xlabel="$x'$ (light years)", ylabel="$ct'$ (light years)", title="Bob's frame: Alice and the asteroid meet before Bob arrives")
    ax.legend(loc="upper right", fontsize=8.7)
    ax.grid(alpha=0.18)
    ax.set_facecolor("white")
    ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
