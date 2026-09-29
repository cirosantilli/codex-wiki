"""Original proposed experiment schematic and exact toy width values, not data.

Write matching PNG basename to CWD; run from _media with
MPLCONFIGDIR=/tmp/codex-wiki-matplotlib. Dependencies: Python 3.14,
NumPy 2.3.5, Matplotlib 3.10.7 (repository environment).
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, (setup, graph) = plt.subplots(1, 2, figsize=(10.6, 4.8),
                                      gridspec_kw={"width_ratios": (1.15, 1)})
    setup.set(xlim=(0, 10), ylim=(0, 10))
    setup.axis("off")
    setup.set_title("Proposed finite-pulse gel experiment", fontsize=12, pad=14)
    setup.add_patch(Rectangle((3.8, 8.0), 2.4, 0.9, fc="#e6eaf0", ec="#46525f"))
    setup.text(5, 8.45, "Camera", ha="center", va="center")
    setup.text(5, 7.3, "Fixed lighting and exposure", ha="center", fontsize=10)
    setup.add_patch(Rectangle((0.7, 5.1), 8.6, 1.1, fc="#edf4f7", ec="#607689"))
    setup.add_patch(Rectangle((4.65, 5.1), 0.7, 1.1, fc="#1479b8", ec="none"))
    setup.plot([0.6, 9.4], [6.32, 6.32], color="#607689", lw=1.4)
    setup.text(5, 6.6, "Covered channel; uniform temperature", ha="center", fontsize=10)
    setup.text(2.4, 5.63, "Undyed gel", ha="center", fontsize=10)
    setup.text(7.6, 5.63, "Undyed gel", ha="center", fontsize=10)
    setup.annotate("Initial dye band", xy=(5, 5.0), xytext=(5, 4.3), ha="center",
                   arrowprops={"arrowstyle": "->", "color": "#46525f"}, fontsize=10)
    setup.annotate("", xy=(8.8, 3.7), xytext=(1.2, 3.7),
                   arrowprops={"arrowstyle": "->", "color": "#46525f"})
    setup.text(5, 3.2, "Channel coordinate x; include a length scale", ha="center", fontsize=10)
    setup.text(5, 2.15, "Calibrated images → concentration profile", ha="center", fontsize=11)
    setup.text(5, 1.3, "Track total dye, centre and width", ha="center", fontsize=11)
    setup.text(5, 0.4, "Schematic, not to scale; no continuous dye supply", ha="center",
               fontsize=9, color="#454c55")
    t = np.linspace(0, 4, 201)
    sample_times = np.array([0, 0.5, 1, 2, 3, 4])
    graph.plot(t, 0.25 + 0.40*t, color="#1479b8", lw=2.2)
    graph.scatter(sample_times, 0.25 + 0.40*sample_times, s=42, color="#d66a13",
                  edgecolor="white", zorder=3, label="Exact illustrative values")
    graph.set(xlabel="Elapsed time t (h)", ylabel=r"Width squared $\sigma^2$ (mm$^2$)",
              xlim=(-0.15, 4.3), ylim=(0, 2.05))
    graph.set_title("Width squared grows linearly", fontsize=12, pad=14)
    graph.grid(alpha=0.18)
    graph.text(0.05, 0.88, r"$\sigma^2 = 0.25 + 0.40t$", transform=graph.transAxes, fontsize=13)
    graph.text(0.05, 0.75, "Slope = 2D = 0.40 mm²/h\nD = 0.20 mm²/h", transform=graph.transAxes,
               fontsize=11, linespacing=1.5)
    graph.annotate("Initial width squared\n0.25 mm²", xy=(0, 0.25), xytext=(1.4, 0.30),
                   arrowprops={"arrowstyle": "->", "color": "#46525f"}, fontsize=10)
    graph.legend(loc="lower right", bbox_to_anchor=(1, -0.32), frameon=False, fontsize=10)
    fig.suptitle("From a spreading band to a diffusion coefficient", fontsize=15, y=0.98)
    fig.text(0.5, 0.015, "Illustrative calculation only: points are not experimental measurements",
             ha="center", fontsize=10, color="#454c55")
    fig.subplots_adjust(left=0.025, right=0.97, bottom=0.22, top=0.82, wspace=0.26)
    fig.savefig(Path(__file__).stem + ".png", dpi=110, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
