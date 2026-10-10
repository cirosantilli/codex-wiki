"""Original functional schematic; tested with Python 3.14, Matplotlib 3.10.7, NumPy 2.3.5.

Run from _media. Curves are an ideal zero-temperature NIS model, not data.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
    fig, (apparatus, curve) = plt.subplots(1, 2, figsize=(11, 4.8), gridspec_kw={"width_ratios": [1.15, 1]}, layout="constrained")
    fig.patch.set_facecolor("white")
    apparatus.set(xlim=(0, 10), ylim=(0, 7))
    apparatus.axis("off")
    apparatus.set_title("A. Functional gap measurement", loc="left", weight="bold")
    apparatus.add_patch(Rectangle((0.7, 2), 8.6, 3.7, facecolor="#f0f7fc", edgecolor="#7a9daf", linestyle="--"))
    apparatus.text(5, 5.35, "Helium cooling: Al normal, Pb superconducting", ha="center", fontsize=10)
    for x, w, color, label in [(2, 2.5, "#add8e6", "Al\nnormal metal"), (4.5, 0.5, "#f8d99a", ""), (5, 2.7, "#a5cbb2", "Pb\nsuperconductor")]:
        apparatus.add_patch(Rectangle((x, 3), w, 1.25, facecolor=color, edgecolor="#273746"))
        if label:
            apparatus.text(x + w / 2, 3.62, label, ha="center", va="center")
    apparatus.annotate("Al oxide barrier", (4.75, 3), (4.75, 2.45), ha="center", arrowprops={"arrowstyle": "->"}, fontsize=10)
    apparatus.plot([2, 1.3, 1.3, 3], [3.65, 3.65, 0.9, 0.9], color="#273746")
    apparatus.plot([7.7, 8.4, 8.4, 6.9], [3.65, 3.65, 0.9, 0.9], color="#273746")
    apparatus.add_patch(Rectangle((3, 0.55), 3.9, 0.7, facecolor="white", edgecolor="#273746"))
    apparatus.text(4.95, 0.9, "Voltage bias + current readout", ha="center", va="center", fontsize=10)
    apparatus.text(5, 1.6, "Measure junction voltage; record I(V)", ha="center", fontsize=10)
    apparatus.text(5, 6.35, "Evaporate Al → air oxidation → Pb cross-strip", ha="center", fontsize=10)
    apparatus.text(5, 0.05, "Functional arrangement; geometry is not to scale", ha="center", fontsize=9, color="#455a64")
    x = np.linspace(-3, 3, 1201)
    y = np.sign(x) * np.sqrt(np.maximum(x*x - 1, 0))
    curve.plot(x, x, "--", color="#7b858b", label="Normal-state reference")
    curve.plot(x, y, color="#276c50", lw=2.5, label="Ideal NIS, T = 0")
    curve.axhline(0, color="#aab7b8", lw=0.7)
    for pos in [-1, 1]:
        curve.axvline(pos, color="#bd8234", ls=":", lw=1)
    curve.set(xlim=(-3, 3), ylim=(-3, 3), xlabel=r"Junction voltage $eV/\Delta$", ylabel=r"Quasiparticle current $eR_N I_{\rm qp}/\Delta$")
    curve.set_title("B. Stipulated model, not measured data", loc="left", weight="bold", fontsize=11)
    curve.text(0, -0.55, r"No states for $|eV|<\Delta$", ha="center", fontsize=10)
    curve.legend(loc="upper left", fontsize=9)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
