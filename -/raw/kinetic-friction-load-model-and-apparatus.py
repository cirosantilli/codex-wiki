"""Draw a horizontal force-probe apparatus beside original model predictions.

Apparatus follows University of Mississippi Experiment 6, Procedure 1–7:
wooden block/plane, added masses, level force probe, LabPro and Logger Pro.
The graph is synthetic: mu=0.30, not observations from that writeup.
Writes a matching-basename opaque white PNG to CWD. Tested with Python
3.14.4, Matplotlib 3.10.7 and NumPy 2.3.5.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def main():
    fig, (setup, graph) = plt.subplots(1, 2, figsize=(10, 5.1), dpi=120,
                                     gridspec_kw={"width_ratios": [1.07, 1]})
    fig.patch.set_facecolor("white")
    setup.set_facecolor("white")
    setup.set(xlim=(0, 10), ylim=(0, 7))
    setup.axis("off")
    setup.set_title("Horizontal pulling apparatus", fontsize=13, pad=14)
    setup.add_patch(Rectangle((0.3, 2.65), 9.1, 0.25,
                              facecolor="#e1c6a0", edgecolor="#604c30"))
    setup.text(4.8, 2.25, "wooden plane (level)", ha="center", fontsize=11)
    setup.add_patch(Rectangle((1.05, 2.9), 2.4, 1.0,
                              facecolor="#f1e0c3", edgecolor="#604c30"))
    setup.text(2.25, 3.4, "wooden block", ha="center", fontsize=11)
    setup.add_patch(Rectangle((1.55, 3.9), 1.4, 0.5,
                              facecolor="#dce1e8", edgecolor="#475569"))
    setup.text(2.25, 4.68, "added loads", ha="center", fontsize=11)
    setup.plot([3.45, 5.55], [3.45, 3.45], color="#555555", lw=1.6)
    setup.text(4.5, 3.02, "level string", ha="center", fontsize=10)
    setup.add_patch(Rectangle((5.55, 3.12), 1.85, 0.66,
                              facecolor="#e5edf6", edgecolor="#2166ac"))
    setup.text(6.48, 3.45, "force probe", ha="center", fontsize=10)
    setup.annotate("", xy=(9.0, 3.45), xytext=(7.4, 3.45),
                   arrowprops=dict(arrowstyle="->", lw=2, color="#35784f"))
    setup.text(8.3, 3.95, "pull →", ha="center", color="#35784f", fontsize=11)
    setup.text(8.0, 4.63, "constant speed", ha="center", fontsize=10)
    setup.plot([6.5, 6.5, 7.8], [3.12, 1.6, 1.6],
               color="#2166ac", lw=1, linestyle="--")
    setup.text(7.85, 1.6, "LabPro\nLogger Pro", va="center", ha="center",
               fontsize=10, bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="#2166ac"))
    setup.text(0.45, 0.2, "Read mean force during steady sliding.\nInclude block + loads in total mass.",
               fontsize=11, linespacing=1.6)
    setup.text(0.45, 5.55, "Calibration: known weight on force probe.\nStarting peak is a separate static readout.",
               fontsize=10.5, linespacing=1.6)
    normal = np.linspace(0, 45, 200)
    mu = 0.30
    graph.plot(normal, mu * normal, color="#2166ac", lw=2.4)
    loads = 9.8 * np.array([2.0, 4.0])
    forces = mu * loads
    graph.scatter(loads, forces, color="#a43b31", zorder=3, s=42)
    for n, f in zip(loads, forces):
        graph.plot([n, n], [0, f], color="#bbbbbb", ls="--", lw=1)
        graph.plot([0, n], [f, f], color="#bbbbbb", ls="--", lw=1)
    graph.annotate("2 kg total\n(19.6 N, 5.88 N)", xy=(loads[0], forces[0]),
                   xytext=(7.0, 8.8), fontsize=10.5,
                   arrowprops=dict(arrowstyle="->", color="#555555"))
    graph.annotate("4 kg total\n(39.2 N, 11.76 N)", xy=(loads[1], forces[1]),
                   xytext=(23.3, 3.0), fontsize=10.5,
                   arrowprops=dict(arrowstyle="->", color="#555555"))
    graph.text(3.8, 12.5, "|fₖ| = 0.30 N\nslope = μₖ = 0.30", fontsize=11,
               color="#2166ac", linespacing=1.5)
    graph.set(xlim=(0, 45), ylim=(0, 14.5), xlabel="Normal force N (newtons)",
              ylabel="Sliding force |fₖ| (newtons)")
    graph.set_title("Stipulated model, not measurements", fontsize=13, pad=14)
    graph.grid(alpha=0.16)
    graph.spines[["top", "right"]].set_visible(False)
    fig.text(0.5, 0.04, "Original predictions: μₖ = 0.30, g = 9.8 m/s²; horizontal pull and zero acceleration",
             ha="center", fontsize=11, color="#555555")
    fig.subplots_adjust(left=0.025, right=0.975, top=0.87, bottom=0.18, wspace=0.3)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
