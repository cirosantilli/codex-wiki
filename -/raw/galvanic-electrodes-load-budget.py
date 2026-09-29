"""Toy constant-emf cell model and charge/available-work budget, not data.

Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
The PNG basename is written to the current working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    emf, internal_r, load_r, interval = 1.10, 100.0, 100.0, 600.0
    faraday = 6.02214076e23 * 1.602176634e-19
    current = emf / (internal_r + load_r)
    voltage = current * load_r
    charge = current * interval
    extent = charge / (2 * faraday)
    available = emf * charge
    delivered = voltage * charge
    dissipated = current**2 * internal_r * interval
    assert np.isclose(available, delivered + dissipated)
    assert np.isclose(2 * faraday * extent, charge)

    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig = plt.figure(figsize=(10.2, 6.1), dpi=110, facecolor="white")
    fig.suptitle("Open circuit and load: a calculated toy model",
                 fontsize=17, weight="bold", y=0.965)
    fig.text(0.5, 0.885,
             "Chosen inputs: emf = 1.10 V, internal r = 100 Ω, load R = 100 Ω",
             ha="center", fontsize=12)
    ax = fig.add_axes((0.085, 0.32, 0.39, 0.49))
    grid_i = np.linspace(0, emf / internal_r, 200)
    ax.plot(1000 * grid_i, emf-internal_r * grid_i, color="#1565a8", lw=2.5)
    ax.scatter([0], [emf], facecolor="white", edgecolor="#1565a8",
               s=80, linewidth=2, zorder=4)
    ax.scatter([1000 * current], [voltage], color="#b7581d", s=65, zorder=4)
    ax.annotate("Open circuit\nI = 0, V = 1.10 V\nload power = 0",
                xy=(0, emf), xytext=(3.6, 1.03), fontsize=10,
                arrowprops={"arrowstyle": "->", "color": "#243649"})
    ax.annotate("Chosen load\n5.50 mA, 0.550 V", xy=(1000*current, voltage),
                xytext=(0.65, 0.18), fontsize=10,
                arrowprops={"arrowstyle": "->", "color": "#243649"})
    ax.set(xlim=(-0.35, 11.4), ylim=(0, 1.2),
           xlabel="Discharge current I (mA)", ylabel="Terminal voltage V (V)")
    ax.set_title("V = emf − Ir", fontsize=13, pad=8)
    ax.grid(alpha=0.22)
    ax.spines[["top", "right"]].set_visible(False)

    budget = fig.add_axes((0.61, 0.32, 0.34, 0.49))
    budget.bar([0], [available], color="#7591aa", width=0.55)
    budget.bar([1], [delivered], color="#1565a8", width=0.55)
    budget.bar([1], [dissipated], bottom=[delivered], color="#d69358", width=0.55)
    budget.text(0, available+0.08, f"{available:.3f} J", ha="center", fontsize=11)
    budget.text(1, delivered/2, f"Load\n{delivered:.3f} J", color="white",
                ha="center", va="center", fontsize=11)
    budget.text(1, delivered+dissipated/2, f"Internal loss\n{dissipated:.3f} J",
                ha="center", va="center", fontsize=11)
    budget.set(ylim=(0, 4.2), ylabel="Available electrical work (J)",
               xticks=[0, 1], xticklabels=["emf × Q", "VQ + I²rt"])
    budget.set_title("Budget over 600 s", fontsize=13, pad=8)
    budget.spines[["top", "right"]].set_visible(False)
    fig.text(0.5, 0.19,
             f"Q = It = {charge:.2f} C      ξ = Q/(2F) = {extent*1e6:.1f} μmol",
             ha="center", fontsize=14)
    fig.text(0.5, 0.13, "ξ mol Zn consumed = ξ mol Cu deposited (ideal reaction only)",
             ha="center", fontsize=11)
    fig.text(0.5, 0.055,
             "Calculated, not measured. Fixed composition and r; no competing reactions.\n"
             "emf × Q is a free-energy budget, not the whole cell thermal budget.",
             ha="center", fontsize=10, linespacing=1.5)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
