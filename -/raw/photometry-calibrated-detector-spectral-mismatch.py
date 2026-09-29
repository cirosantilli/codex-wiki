"""Filtered-detector schematic and declared spectral-mismatch model.

No CIE tables, calibration measurements, or instrument performance claims.
Run from _media with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
The matching opaque white PNG is written to the current working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np


def weight(wavelength_nm):
    return np.maximum(0.0, 1.0 - np.abs(np.asarray(wavelength_nm) - 555.0) / 150.0)


def responsivity(wavelength_nm):
    wavelength_nm = np.asarray(wavelength_nm)
    return 0.5 * weight(wavelength_nm) * (1 + (wavelength_nm - 555.0) / 150.0)


def main():
    plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.facecolor": "white"})
    line_nm = np.array([555.0, 630.0])
    power_w = 0.001
    current_a = power_w * responsivity(line_nm)
    target_lm = 683 * power_w * weight(line_nm)
    conversion = target_lm[0] / current_a[0]
    indicated_lm = conversion * current_a
    correction = target_lm[1] / indicated_lm[1]
    np.testing.assert_allclose(current_a, [0.0005, 0.000375], rtol=1e-14)
    np.testing.assert_allclose(indicated_lm, [0.683, 0.51225], rtol=1e-14)
    np.testing.assert_allclose(correction, 2 / 3, rtol=1e-14)
    wavelength = np.linspace(380, 740, 1441)
    assert np.all(responsivity(wavelength) >= 0)
    fig = plt.figure(figsize=(10.5, 6.7), layout="constrained")
    grid = fig.add_gridspec(2, 2, height_ratios=[0.9, 1.5], width_ratios=[1.1, 1])
    fig.suptitle("A single calibration does not fix spectral mismatch", fontsize=16)
    scheme = fig.add_subplot(grid[0, :])
    scheme.set(xlim=(0, 10), ylim=(0, 2.1))
    scheme.axis("off")
    labels = ["Specified\nsource", "Shutter +\naperture", "Matching filter\n+ photodiode", "Current-to-\nvoltage readout", "Calibration\nconversion"]
    for index, label in enumerate(labels):
        x = 0.1 + 2 * index
        scheme.add_patch(FancyBboxPatch((x, 0.75), 1.65, 0.72,
                                      boxstyle="round,pad=0.04", facecolor="#edf2f8", edgecolor="#425975"))
        scheme.text(x + 0.825, 1.11, label, ha="center", va="center", fontsize=10)
        if index < 4:
            scheme.annotate("", xy=(x + 1.94, 1.11), xytext=(x + 1.72, 1.11),
                            arrowprops={"arrowstyle": "->", "color": "#425975", "lw": 1.6})
    scheme.text(5, 1.85, "Signal path schematic • Not to scale • Measure shutter-closed baseline before illumination", ha="center")
    scheme.text(5, 0.3, "Current i = illuminated − baseline; aperture and collection geometry stay fixed", ha="center")
    ax = fig.add_subplot(grid[1, 0])
    ax.plot(wavelength, weight(wavelength), label="Target weight w", color="#303e4d", linewidth=2)
    ax.plot(wavelength, responsivity(wavelength) / 0.5, label="Detector r / (0.5 A/W)", color="#b16031", linewidth=2)
    for line, color in zip(line_nm, ["#268454", "#96519b"]):
        ax.axvline(line, linestyle="--", color=color, alpha=0.75)
    ax.set(xlim=(380, 740), ylim=(0, 1.16), xlabel="Wavelength (nm)", ylabel="Dimensionless relative response")
    ax.set_title("Declared model curves (not CIE data)")
    ax.legend(fontsize=9, loc="upper left")
    ax.grid(alpha=0.18)
    ax = fig.add_subplot(grid[1, 1])
    positions = np.arange(2)
    ax.bar(positions - 0.16, target_lm, width=0.31, label="Intended model output", color="#268454")
    ax.bar(positions + 0.16, indicated_lm, width=0.31, label="Same conversion applied", color="#b16031")
    for pos, value in zip(positions - 0.16, target_lm):
        ax.text(pos, value + 0.016, f"{value:.5f}", ha="center", fontsize=9)
    for pos, value in zip(positions + 0.16, indicated_lm):
        ax.text(pos, value + 0.016, f"{value:.5f}", ha="center", fontsize=9)
    ax.set(xticks=positions, xticklabels=["Calibration\n555 nm, 0.500 mA", "Test\n630 nm, 0.375 mA"],
           ylim=(0, 1.1), ylabel="Model weighted output (lm)")
    ax.set_title("Both lines carry 1 mW")
    ax.legend(fontsize=9, loc="upper right")
    ax.text(0.5, 0.84, "Test: × 2/3 corrects 0.51225 to 0.34150", ha="center", fontsize=10)
    ax.grid(axis="y", alpha=0.18)
    fig.text(0.5, -0.015, "Stipulated model: r = 0.5 w [1 + (λ − 555 nm)/(150 nm)] A/W • Calibration C = 1366 lm/A",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=130, facecolor="white",
                transparent=False, bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)
    print({"current_A": current_a.tolist(), "model_target_lm": target_lm.tolist(),
           "indicated_lm": indicated_lm.tolist(), "calibration_lm_per_A": conversion,
           "correction": float(correction)})


if __name__ == "__main__":
    main()
