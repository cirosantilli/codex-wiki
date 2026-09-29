"""Original tunnel section; Python 3.14, NumPy and Matplotlib from root pyproject.

The illustrative dimensions satisfy both inequalities. PNG output is in cwd.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def main():
    L, H, D = 1.3, 1.0, 0.65
    x = np.linspace(-L, L, 600)
    floor = H*(x/L)**2
    fig, ax = plt.subplots(figsize=(6.8, 4.3), layout="constrained")
    fig.set_facecolor("white")
    ax.fill_between(x, floor, H, color="#e1edf1", label="projected material")
    ax.plot(x, floor, color="#176b9b", lw=2)
    ax.plot([-L, L], [H, H], color="#176b9b", lw=2)
    ax.add_patch(Circle((0, D/2), D/2, facecolor="white", edgecolor="#b83c32", lw=2,
                        label="tunnel section"))
    ax.scatter([0], [D/2], color="#b83c32", s=20)
    ax.axhline(0, color="0.5", lw=0.8)
    ax.axvline(0, color="0.5", lw=0.8)
    ax.annotate("$z=Hx^2/L^2$", (0.95, H*(0.95/L)**2), xytext=(0.85, 0.23),
                arrowprops={"arrowstyle": "->", "lw": 0.8})
    ax.annotate("$(0,D/2)$", (0, D/2), xytext=(25, 0), textcoords="offset points",
                arrowprops={"arrowstyle": "->", "lw": 0.8})
    ax.set(xlim=(-1.45, 1.45), ylim=(-0.09, 1.2), aspect="equal", xlabel="$x$", ylabel="$z$",
           title="Cross-section viewed along the tunnel axis")
    ax.set_xticks([-L, 0, L], ["$-L$", "0", "$L$"])
    ax.set_yticks([0, D, H], ["0", "$D$", "$H$"])
    ax.legend(loc="upper center", ncol=2, fontsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
