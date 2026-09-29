"""Original synthetic line calibration exercise; Python 3.14, matplotlib 3.10, numpy 2.3."""

from pathlib import Path
import math

import matplotlib.pyplot as plt
import numpy as np


def main():
    e, h, c = 1.602176634e-19, 6.62607015e-34, 299792458.0
    epsilon = 8.8541878128e-12
    electron, proton = 9.1093837015e-31, 1.67262192369e-27
    mu = electron * proton / (electron + proton)
    hbar = h / (2 * math.pi)
    kappa = e**2 / (4 * math.pi * epsilon)
    binding = mu * kappa**2 / (2 * hbar**2)
    upper = np.arange(3, 7)
    finite = h * c / (binding * (1 / 4 - 1 / upper**2)) * 1e9
    fixed = finite * mu / electron
    chosen_offset = 0.200
    synthetic = finite + chosen_offset
    fitted_finite = synthetic[0] - finite[0]
    fitted_fixed = synthetic[0] - fixed[0]
    residual_fixed = synthetic - fitted_fixed - fixed
    residual_finite = synthetic - fitted_finite - finite
    assert np.allclose(residual_finite, 0, atol=1e-10)
    assert np.allclose(residual_fixed, (1 - mu / electron) * (finite - finite[0]), atol=1e-10)

    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.8), dpi=110,
                             gridspec_kw={"width_ratios": [1.10, 1]})
    fig.subplots_adjust(left=0.19, right=0.98, bottom=0.23, top=0.77, wspace=0.32)
    fig.suptitle("One calibration line does not test the whole series", fontsize=17, y=0.97)
    fig.text(0.5, 0.885, "Chosen synthetic example · additive wavelength offset b = +0.200 nm",
             ha="center", color="#444444")

    local, residual = axes
    rows = np.arange(4)
    local.axvline(0, color="#999999", linewidth=1)
    for row in rows:
        local.hlines(row, -0.42, 0.28, color="#eeeeee", zorder=0)
    local.scatter(fixed - finite, rows, marker="s", color="#ad512f", s=50,
                  label="Fixed nucleus prediction", zorder=3)
    local.scatter(np.zeros(4), rows, marker="o", facecolors="white", edgecolors="#235b88",
                  linewidths=2, s=65, label="Finite mass prediction", zorder=4)
    local.scatter(synthetic - finite, rows, marker="x", color="#333333", s=65,
                  label="Synthetic position", zorder=4)
    local.set_yticks(rows, [f"{n} → 2\nλ = {value:.3f} nm" for n, value in zip(upper, finite)])
    local.set_ylim(3.5, -0.5)
    local.set_xlim(-0.43, 0.29)
    local.set_xlabel("Local offset from each finite mass λ (nm)")
    local.set_title("Predictions before calibration", pad=17)
    handles, labels = local.get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", bbox_to_anchor=(0.5, 0.075),
               ncols=3, fontsize=10, frameon=False)

    residual.axhline(0, color="#888888", linewidth=1)
    residual.plot(upper, residual_fixed, "s--", color="#ad512f", label="Fixed nucleus")
    residual.plot(upper, residual_finite, "o-", color="#235b88", label="Finite mass")
    for n, value in zip(upper[1:], residual_fixed[1:]):
        residual.annotate(f"{value:.5f}", (n, value), xytext=(0, -17),
                          textcoords="offset points", ha="center", fontsize=9, color="#ad512f")
    residual.set_xticks(upper, [f"{n} → 2" for n in upper])
    residual.set_xlim(2.7, 6.3)
    residual.set_ylim(-0.18, 0.055)
    residual.set_xlabel("Transition (3 → 2 is the calibration anchor)")
    residual.set_ylabel("Synthetic − calibrated prediction (nm)")
    residual.set_title("Test the other three lines", pad=17)
    residual.legend(loc="lower left", bbox_to_anchor=(0, 1.0), ncols=2, fontsize=9,
                    frameon=False, borderaxespad=0)
    fig.text(0.5, 0.035, "No measured spectrum or intensity trace. Dispersion scale is assumed known; only the offset is fitted.",
             ha="center", fontsize=10, color="#444444")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
