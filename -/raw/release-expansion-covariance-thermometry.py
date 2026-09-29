"""Synthetic release-expansion widths; no historical measurements.

Python 3.14; NumPy 2.3.5; Matplotlib 3.10.7. Run from _media.
Times are ms, positions mm, so mm/ms = m/s. No SciPy required.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def model():
    t = np.linspace(0, 30, 13)
    variance = .36-.036*t+.0036*t*t
    y = variance+np.random.default_rng(27).normal(0, .012, len(t))
    full = np.linalg.lstsq(np.column_stack([np.ones_like(t), t, t*t]), y, rcond=None)[0]
    omitted = np.linalg.lstsq(np.column_stack([np.ones_like(t), t*t]), y, rcond=None)[0]
    return t, y, full, omitted


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig = plt.figure(figsize=(10, 5.4), layout="constrained")
    grid = fig.add_gridspec(2, 2, width_ratios=[1.25, 1], height_ratios=[.8, 2.3])
    ax = fig.add_subplot(grid[:, 0])
    note = fig.add_subplot(grid[0, 1])
    profiles = fig.add_subplot(grid[1, 1])
    fig.suptitle("Release-expansion thermometry: initial correlations matter", fontsize=15)
    t, y, full, omitted = model()
    fine = np.linspace(0, 30, 400)
    truth = .36-.036*fine+.0036*fine*fine
    ax.errorbar(t, y, yerr=.012, fmt="o", ms=4, color="#243f4e", label="Synthetic variance data")
    ax.plot(fine, truth, "--", color="#71985b", lw=2, label="Chosen true model")
    ax.plot(fine, full[0]+full[1]*fine+full[2]*fine*fine, color="#185fa5", lw=2, label="Full quadratic fit")
    ax.plot(fine, omitted[0]+omitted[1]*fine*fine, color="#b24b13", lw=2, label="Fit forced to zero covariance")
    ax.set(xlabel="Dark expansion time (ms)", ylabel=r"Position variance $\sigma_x^2$ (mm$^2$)", xlim=(-1, 31), ylim=(0, 2.7))
    ax.legend(fontsize=8.5, loc="upper left")
    ax.grid(alpha=.18)
    ax.text(.04, .44, r"$\sigma_x^2(t)=a+bt+ct^2$"+"\n"+r"$b=2\operatorname{Cov}(x_0,v_0)$", transform=ax.transAxes, fontsize=10)
    conv = 3.82e-26/1.380649e-23*1e6
    ax.text(.05, .04, f"Chosen true T = {conv*.0036:.2f} μK\nFull fit: {conv*full[2]:.2f} μK; forced fit: {conv*omitted[1]:.2f} μK", transform=ax.transAxes, fontsize=9, bbox={"facecolor": "white", "edgecolor": ".8"})
    x = np.linspace(-5, 5, 600)
    for time, color in [(0, "#243f4e"), (5, "#185fa5"), (30, "#b24b13")]:
        var = .36-.036*time+.0036*time*time
        density = np.exp(-x*x/(2*var))/np.sqrt(2*np.pi*var)
        profiles.plot(x, density, color=color, label=f"{time} ms, σ = {np.sqrt(var):.2f} mm")
    profiles.set(xlabel="Position relative to cloud centre (mm)", ylabel="Normalised column-density marginal (mm⁻¹)", xlim=(-5, 5), ylim=(0, .86))
    profiles.legend(fontsize=9, loc="upper right")
    profiles.grid(alpha=.18)
    note.axis("off")
    note.text(.03, .95, "3D Gaussian cloud → integrate along viewing axis\n→ integrate image along y → 1D x profile", va="top", fontsize=10)
    note.text(.03, .37, "Ideal short, uniform fluorescence probe; no blur.\nNegative covariance causes initial narrowing.", va="top", fontsize=9)
    fig.savefig(Path(__file__).stem+".png", dpi=130, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
