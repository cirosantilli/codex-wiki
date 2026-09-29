"""Proposed apparatus and calculated controls; no historical data. Python 3.14."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle


def main():
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig = plt.figure(figsize=(10, 6.2), facecolor="white", layout="constrained")
    grid = fig.add_gridspec(2, 2, height_ratios=(3.3, 1), width_ratios=(1.15, 1))
    ax = fig.add_subplot(grid[0, 0])
    ax.set(xlim=(0, 10), ylim=(0, 10))
    ax.axis("off")
    ax.set_title("Proposed modern readout", loc="left", weight="bold")
    ax.add_patch(Rectangle((0.15, 3.65), 1.8, 1.1, facecolor="0.95", edgecolor="0.4"))
    ax.text(1.05, 4.2, "Stable\nsource", ha="center", va="center")
    ax.plot([2, 8], [4.2, 4.2], color="#166da0", lw=2)
    ax.plot([4.5, 4.5], [1.7, 8], color="#166da0", lw=2)
    ax.plot([4, 5], [3.7, 4.7], color="0.25", lw=5)
    ax.text(3.6, 3.2, "Beam splitter", ha="right")
    ax.plot([3.8, 5.2], [8, 8], lw=4, color="0.3")
    ax.text(4.5, 8.45, "Fixed reference mirror", ha="center")
    ax.plot([8, 8], [3.5, 4.9], lw=4, color="#b04e00")
    ax.text(7.7, 5.55, "Moving mirror\n+ calibrated drive", ha="center")
    ax.annotate("", xy=(9.2, 4.2), xytext=(8.2, 4.2),
                arrowprops={"arrowstyle": "->", "color": "#b04e00", "lw": 2})
    ax.add_patch(Rectangle((3.6, 0.7), 1.8, 1.0, facecolor="0.95", edgecolor="0.4"))
    ax.text(4.5, 1.2, "Photodiode", ha="center", va="center")
    ax.text(6.6, 1.1, "→ record cycles\n   and fractional phase", va="center")
    ax.annotate("", xy=(4.5, 2.1), xytext=(4.5, 3.2), arrowprops={"arrowstyle": "->", "color": "#166da0"})
    ax.text(0.25, 9.4, "Overlap beams; match polarizations", fontsize=10)
    ax = fig.add_subplot(grid[0, 1])
    mismatch = np.linspace(0, 1.05, 300)
    ax.plot(mismatch, np.exp(-2 * mismatch), color="#166da0", lw=2)
    for x, color in [(0.1, "#26733c"), (0.6, "#b04e00")]:
        y = np.exp(-2 * x)
        ax.plot(x, y, "o", color=color)
        ax.vlines(x, 0, y, color=color, ls="--", lw=1)
        ax.annotate(f"{x:.2f} mm → {y:.3f}", (x, y), xytext=(8, 10),
                    textcoords="offset points", color=color)
    ax.set(xlim=(0, 1.05), ylim=(0, 1.08), xlabel=r"Vacuum arm mismatch $|L_2-L_1|$ (mm)",
           ylabel=r"Visibility $\mathcal{V}$ (dimensionless)")
    ax.set_title("Hypothetical coherence control\n" + r"$\mathcal{V}=e^{-|D|/L_c},\quad L_c=1$ mm", loc="left", fontsize=11)
    ax.grid(alpha=0.2)
    ax = fig.add_subplot(grid[1, :])
    ax.axis("off")
    ax.text(0.01, 0.88, "Independent air-index control", weight="bold", fontsize=12)
    ax.text(0.01, 0.49, r"Hold mirror fixed: $L=0.10$ m, $n\simeq1$, $\Delta n=10^{-7}$"
            + "\n" + r"Apparent travel $L\Delta n/n=10$ nm; record temperature and pressure.", va="center", fontsize=11)
    ax.text(0.99, 0.79, "Calculated examples only\nNot historical observations", ha="right", va="top", color="0.35")
    fig.suptitle("Preserve contrast; test what moved the fringes", fontsize=16, weight="bold")
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
