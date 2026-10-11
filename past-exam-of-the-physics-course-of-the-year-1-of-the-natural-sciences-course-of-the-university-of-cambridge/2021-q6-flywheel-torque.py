"""Original gyroscopic torque geometry. Python 3.14.4; root pyproject.toml deps.

Run from the desired output directory; writes the PNG basename into cwd.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.6), layout="constrained", facecolor="white")
    ax = axes[0]
    ax.axhline(0, color="0.8", lw=0.8)
    ax.axvline(0, color="0.8", lw=0.8)
    vectors = [(1.3, 0, "#bc6b20"), (-1.3, 0, "#205e9b"), (0, -1.1, "#854b98")]
    for x, y, color in vectors:
        ax.annotate("", (x, y), (0, 0), arrowprops={"arrowstyle": "-|>", "lw": 2.8, "color": color})
    ax.text(1.3, 0.12, "$+x$: forward\nTorque on flywheel", ha="center", color="#bc6b20", fontsize=10)
    ax.text(-1.3, 0.12, "$-x$\nReaction on car", ha="center", color="#205e9b", fontsize=10)
    ax.text(0.13, -0.82, "$\\mathbf{L}_f$: car's right\n($-y$)", color="#854b98", fontsize=10)
    ax.text(0.05, 1.05, "$+y$: car's left", fontsize=10)
    ax.plot(0, 0, "o", color="white", mec="black", ms=15, zorder=5)
    ax.plot(0, 0, "k.", ms=6, zorder=6)
    ax.annotate("Turn: $\\boldsymbol{\\Omega}$ along $+z$\n(out of the page)", (0, 0), (-1.8, -1.45), arrowprops={"arrowstyle": "-", "lw": 0.8}, fontsize=10)
    ax.set(xlim=(-2.1, 2.1), ylim=(-1.65, 1.45), title="Left turn: top view\n$\\mathbf{G}_{car}=-\\boldsymbol{\\Omega}\\times\\mathbf{L}_f$")
    ax = axes[1]
    phi = np.linspace(0, 2*np.pi, 361)
    ax.plot(np.cos(phi), np.sin(phi), color="#854b98", lw=2)
    for t in [0.3, 2.4, 4.5]:
        start = (np.cos(t), np.sin(t))
        end = (np.cos(t+0.28), np.sin(t+0.28))
        ax.annotate("", end, start, arrowprops={"arrowstyle": "-|>", "color": "#854b98", "lw": 2})
    ax.plot(0, 0, "o", mfc="white", mec="#854b98", ms=17)
    ax.plot(0, 0, ".", color="#854b98", ms=8)
    ax.text(0, -1.35, "$\\mathbf{L}_f$ points toward the viewer\nSpin opposite to the rolling wheels", ha="center", fontsize=10)
    ax.set(xlim=(-1.7, 1.7), ylim=(-1.7, 1.45), title="View from the car's right side\nRequired flywheel spin: counterclockwise")
    for ax in axes:
        ax.set_aspect("equal")
        ax.set_facecolor("white")
        ax.set_axis_off()
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
