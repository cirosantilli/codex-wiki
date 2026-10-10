"""Synthetic response and atom-weighted mass; not an experimental spectrum.

Python 3.14, matplotlib 3.10.7, numpy 2.3.5. Run from _media.
NIST displayed central values: https://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl?ele=Ne
Neutral atom masses approximate singly charged ion masses only for this diagram.
Both Gaussian response widths are chosen, with unit area for each response.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

MASS_U = np.array([19.9924401762, 20.993846685, 21.991385114])
ATOM_FRACTION = np.array([0.9048, 0.0027, 0.0925])
MASS_NUMBER = np.array([20, 21, 22])
COLORS = ["#2378b8", "#a355b0", "#db741f"]


def components(x, sigma):
    return ATOM_FRACTION[:, None] * np.exp(-0.5 * ((x[None, :] - MASS_U[:, None]) / sigma) ** 2) / (sigma * np.sqrt(2 * np.pi))


def main():
    assert np.isclose(ATOM_FRACTION.sum(), 1, rtol=0, atol=1e-14)
    mean = float(ATOM_FRACTION @ MASS_U)
    assert np.isclose(mean, 20.18004638052026, rtol=0, atol=1e-12)
    x = np.linspace(16, 26, 25001)
    fig = plt.figure(figsize=(9.6, 7.8), dpi=110, facecolor="white")
    grid = fig.add_gridspec(3, 1, height_ratios=[2.4, 2, 1.3], hspace=0.55)
    sharp = fig.add_subplot(grid[0])
    broad = fig.add_subplot(grid[1])
    balance = fig.add_subplot(grid[2])
    fig.suptitle("Synthetic neon spectrum and a weighted mean", fontsize=16, y=0.985)
    fig.text(0.5, 0.925, "Not measured: chosen Gaussian widths; equal isotope response; z = +1",
             fontsize=11, ha="center")
    narrow_parts = components(x, 0.04)
    sharp.plot(x, narrow_parts.sum(axis=0), color="#263746", lw=1.5)
    for i, (a, m, f, color) in enumerate(zip(MASS_NUMBER, MASS_U, ATOM_FRACTION, COLORS, strict=True)):
        sharp.fill_between(x, 0, narrow_parts[i], color=color, alpha=0.55)
        sharp.annotate(f"Ne-{a}: area {100*f:.2f}%", xy=(m, float(narrow_parts[i].max())),
                       xytext=([19.48, 20.62, 21.30][i], [9.5, 5.2, 3.6][i]),
                       fontsize=10, color=color, arrowprops={"arrowstyle": "->", "color": color})
    sharp.set(xlim=(19.4, 22.6), ylim=(0, 10.5), ylabel="Signal per unit x")
    sharp.set_title("Narrow response: σ = 0.04, FWHM = 0.0942", loc="left", fontsize=12)
    inset = sharp.inset_axes([0.59, 0.50, 0.21, 0.40])
    inset.plot(x, narrow_parts[1], color=COLORS[1], lw=1.5)
    inset.set(xlim=(20.8, 21.2), ylim=(0, 0.03), xticks=(20.9, 21.1), yticks=(0, 0.02))
    inset.set_title("Ne-21 zoom", fontsize=9)
    inset.tick_params(labelsize=8)
    broad_parts = components(x, 0.70)
    for i, color in enumerate(COLORS):
        broad.plot(x, broad_parts[i], color=color, lw=1.2, linestyle="--")
    broad.plot(x, broad_parts.sum(axis=0), color="#263746", lw=2, label="Total signal")
    broad.set(xlim=(18, 24), ylim=(0, 0.58), ylabel="Signal per unit x",
              xlabel="x = (ion mass / u) / z  [dimensionless; neutral-mass approximation]")
    broad.set_title("Broad response: σ = 0.70, FWHM = 1.648; same component areas", loc="left", fontsize=12)
    broad.legend(frameon=False, fontsize=10, loc="upper right")
    balance.axhline(0, color="#57636f", lw=1)
    for a, m, f, color in zip(MASS_NUMBER, MASS_U, ATOM_FRACTION, COLORS, strict=True):
        balance.scatter([m], [0], s=40 + 700*f, color=color, zorder=3)
        balance.text(m, 0.29, f"{m:.6f} u", ha="center", color=color, fontsize=10)
        balance.text(m, -0.37, f"Ne-{a}\natom fraction {f:.4f}", ha="center", va="top", fontsize=10)
    balance.scatter([mean], [0], s=95, marker="v", color="#263746", zorder=4)
    balance.annotate(f"Mean = {mean:.6f} u\nNot an isotope peak", xy=(mean, 0.08),
                     xytext=(20.5, 0.75), fontsize=11,
                     arrowprops={"arrowstyle": "->", "color": "#263746"})
    balance.set(xlim=(19.4, 22.6), ylim=(-1.10, 1.13))
    balance.axis("off")
    for ax in (sharp, broad):
        ax.spines[["top", "right"]].set_visible(False)
        ax.tick_params(labelsize=10)
    fig.subplots_adjust(left=0.11, right=0.96, top=0.87, bottom=0.075)
    fig.text(0.5, 0.029, "NIST displayed fractions and masses are rounded, uncertain reference values; mean shown is their arithmetic result.",
             ha="center", fontsize=9)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
