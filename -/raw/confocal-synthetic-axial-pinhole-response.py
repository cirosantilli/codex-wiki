"""Synthetic Gaussian finite-pinhole axial model, explicitly not measurements.

Tested with Python 3.14, Matplotlib 3.10.7 and NumPy 2.3.5.
Run from _media with MPLBACKEND=Agg MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Writes the matching basename PNG to the current working directory.
"""

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def response(t, alpha):
    q = 1 + np.asarray(t) ** 2
    return -np.expm1(-alpha ** 2 / (2 * q)) / q


def half_width(alpha):
    lo, hi = 0.0, 3.0
    target = response(0.0, alpha) / 2
    for _ in range(60):
        mid = (lo + hi) / 2
        if response(mid, alpha) > target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    t = np.linspace(-4, 4, 2401)
    fig, axes = plt.subplots(1, 2, figsize=(11.2, 5.5))
    fig.subplots_adjust(left=0.075, right=0.98, top=0.78, bottom=0.27, wspace=0.28)
    metrics = []
    for alpha, color in [(0.5, "#245ba3"), (1.5, "#a65324"), (4.0, "#187c52")]:
        h = response(t, alpha)
        peak = float(response(0.0, alpha))
        width = 2 * half_width(alpha)
        axes[0].plot(t, h, color=color, lw=2.2,
                     label=rf"$\alpha={alpha:g}$: peak {peak:.3f}")
        axes[1].plot(t, h / peak, color=color, lw=2.2,
                     label=rf"$\alpha={alpha:g}$: FWHM {width:.3f} $z_0$")
        metrics.append({"alpha": alpha, "peak_transmission": peak,
                        "FWHM_over_z0": width,
                        "relative_signal_at_t2": float(response(2.0, alpha) / peak)})
    for ax in axes:
        ax.plot(t, 1 / (1 + t ** 2), color="#626c75", ls="--", lw=1.5,
                label="All collected emission accepted")
        ax.set(xlim=(-4, 4), ylim=(0, 1.05), xlabel=r"Axial displacement $t=z/z_0$")
        ax.axvline(0, color="#c1c6cb", lw=0.8)
        ax.grid(alpha=0.2)
        ax.legend(fontsize=9, frameon=False, loc="upper right")
    axes[0].set(title="Common signal scale: throughput stays visible",
                ylabel="Response / excitation-only in-focus signal")
    axes[1].set(title="Each peak = 1: compare response widths",
                ylabel="Response / its own peak")
    axes[1].axhline(0.5, color="#949ca3", lw=0.8, ls=":")
    fig.suptitle("Synthetic axial pinhole response — Gaussian toy model", fontsize=15)
    fig.text(0.5, 0.85, r"$E(t)=1/(1+t^2)$,  $D_\alpha(t)=1-\exp[-\alpha^2/(2(1+t^2))]$,  $H_\alpha=E D_\alpha$",
             ha="center", fontsize=12)
    fig.text(0.5, 0.065,
             "α = pinhole radius / in-focus detection Gaussian standard deviation; not Airy units.\n"
             "The reference keeps the same scanned excitation. It is not uniform widefield illumination.\n"
             "No instrument data, physical length calibration, noise or bleaching is included.",
             ha="center", va="center", fontsize=10)
    path = Path(__file__).stem + ".png"
    fig.savefig(path, dpi=110, facecolor="white", transparent=False)
    plt.close(fig)
    print(json.dumps({"path": path, "dimensions": [1232, 605], "data": "synthetic model",
                      "apertures": metrics, "small_pinhole_limit_FWHM_over_z0":
                      float(2 * np.sqrt(np.sqrt(2) - 1)), "open_pinhole_limit_FWHM_over_z0": 2.0}))


if __name__ == "__main__":
    main()
