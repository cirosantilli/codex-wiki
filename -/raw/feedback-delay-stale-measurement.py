"""Draw feedback-delay-stale-measurement.png in the current directory.

Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
An exact dimensionless toy solution, not experimental measurements.
"""

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


DELAY = 1.2
GAIN = 1.0
BLUE = "#1769aa"
ORANGE = "#b95700"


def trajectory(t):
    """Exact constant-history solution through two delay intervals."""
    t = np.asarray(t, dtype=float)
    if np.any(t > 2 * DELAY + 1e-12):
        raise ValueError("This formula is valid only through t=2*delay.")
    return np.where(t < 0, 1.0, 1 - GAIN * t + 0.5 * GAIN**2 * np.maximum(t - DELAY, 0)**2)


def check():
    # Independent centered-difference check, away from history/interval joins.
    probes = np.array([0.2, 0.75, 1.1, 1.4, 1.9, 2.3])
    epsilon = 1e-5
    derivative = (trajectory(probes + epsilon) - trajectory(probes - epsilon)) / (2 * epsilon)
    residual = float(np.max(np.abs(derivative + GAIN * trajectory(probes - DELAY))))
    assert residual < 1e-9
    assert abs(float(trajectory(1.4)) + 0.38) < 1e-14
    assert abs(float(trajectory(1.4 - DELAY)) - 0.8) < 1e-14
    assert abs(float(trajectory(1.0))) < 1e-14
    assert abs(float(trajectory(2.2 - DELAY))) < 1e-14
    return {"max_dde_residual_by_centered_difference": residual, "at_t_1_4": {"actual": -0.38, "measured": 0.8, "command": -0.8}, "opposite_sign_interval": [1.0, 2.2]}


def main():
    checks = check()
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False, "savefig.facecolor": "white"})
    fig = plt.figure(figsize=(8.6, 6.0), facecolor="white")
    grid = fig.add_gridspec(2, 1, height_ratios=[1, 2.1], hspace=0.23)
    schematic = fig.add_subplot(grid[0])
    schematic.set(xlim=(0, 10), ylim=(0, 3.1))
    schematic.axis("off")
    schematic.set_title("Feedback acts on the old measurement", loc="left", fontweight="bold", pad=8)

    def box(x, width, label, color):
        schematic.add_patch(FancyBboxPatch((x, 1.5), width, 0.85, boxstyle="round,pad=0.05", linewidth=1.3, edgecolor=color, facecolor="white"))
        schematic.text(x + width / 2, 1.925, label, ha="center", va="center", color=color)

    def arrow(start, end, **kwargs):
        schematic.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=13, color="#444444", linewidth=1.4, **kwargs))

    box(0.5, 2.1, "Measurement delay\n" + r"$y_m(t)=x(t-\tau)$", ORANGE)
    box(3.7, 2.1, "Controller\n" + r"$u=-k y_m$", ORANGE)
    box(6.9, 2.1, "Ideal plant\n" + r"$x'=u$", BLUE)
    arrow((2.65, 1.925), (3.63, 1.925))
    schematic.text(3.13, 2.12, r"$y_m$", ha="center")
    arrow((5.85, 1.925), (6.83, 1.925))
    schematic.text(6.33, 2.12, r"$u$", ha="center")
    schematic.plot([9.06, 9.5, 9.5, 0.12, 0.12], [1.925, 1.925, 0.52, 0.52, 1.925], color="#444444", linewidth=1.4)
    arrow((0.12, 1.925), (0.43, 1.925))
    schematic.text(5.0, 0.72, "Current output returns through a delay", ha="center", color=BLUE)
    schematic.text(9.55, 2.05, r"$x(t)$", ha="center", color=BLUE)

    ax = fig.add_subplot(grid[1])
    t = np.linspace(0, 2 * DELAY, 1201)
    ax.axvspan(1.0, 2.2, color="#fff0df", zorder=0)
    ax.axhline(0, color="#333333", linewidth=0.9)
    ax.plot(t, trajectory(t), color=BLUE, linewidth=2.6, label=r"Actual output $x(t)$")
    ax.plot(t, trajectory(t - DELAY), color=ORANGE, linestyle="--", linewidth=2.3, label=r"Measured output $x(t-\tau)$")
    ax.axvline(1.4, color="#888888", linestyle=":", linewidth=1)
    ax.scatter([1.4], [-0.38], color=BLUE, s=42, zorder=4)
    ax.scatter([1.4], [0.8], color=ORANGE, s=42, zorder=4)
    ax.annotate(r"Old value $+0.8$", (1.4, 0.8), xytext=(1.62, 1.1), color=ORANGE, arrowprops={"arrowstyle": "->", "color": ORANGE})
    ax.annotate("Actual value −0.38\nCommand −0.8 pushes farther down", (1.4, -0.38), xytext=(0.55, -1.16), fontsize=10.5, color=BLUE, arrowprops={"arrowstyle": "->", "color": BLUE})
    ax.text(1.85, -0.1, "Opposite signs", ha="center", va="top", color="#774315", fontsize=10)
    ax.set(xlim=(0, 2.4), ylim=(-1.45, 1.28), xlabel="Time t (dimensionless)", ylabel="Output (dimensionless)")
    ax.set_title(r"Exact toy response: $k=1$, $\tau=1.2$, history $x=1$", loc="left", fontsize=11)
    ax.legend(loc="lower left", bbox_to_anchor=(-0.01, 1.02), ncol=2, frameon=False, fontsize=10)
    ax.grid(axis="y", color="#dddddd", linewidth=0.5)
    fig.subplots_adjust(left=0.1, right=0.98, bottom=0.12, top=0.93)
    fig.text(0.1, 0.025, "Synthetic model illustration • white background • no measured data", fontsize=9, color="#555555")
    path = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(path, dpi=130, facecolor="white", transparent=False)
    plt.close(fig)
    print(json.dumps({"output": path.name, "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
