"""Original triangular spectral-weight model; no CIE tables or measured data.

Run from _media with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
The matching PNG is written to the current working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def weight(wavelength_nm):
    return np.maximum(0.0, 1.0 - np.abs(np.asarray(wavelength_nm) - 555.0) / 150.0)


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white"})
    wavelength = np.linspace(380, 740, 1441)
    lines = np.array([450.0, 555.0, 650.0])
    powers_w = np.full(3, 0.001)
    weighted_lm = 683 * powers_w * weight(lines)
    np.testing.assert_allclose(weight(lines), [3 / 10, 1, 11 / 30], rtol=1e-14)
    np.testing.assert_allclose(weighted_lm, [0.2049, 0.683, 0.2504333333333333], rtol=1e-14)
    assert np.all((weight(wavelength) >= 0) & (weight(wavelength) <= 1))
    colors = ["#386ab5", "#268454", "#ba5632"]
    fig, axes = plt.subplots(2, 1, figsize=(8.4, 6.4), layout="constrained")
    fig.suptitle("Equal radiant power, different spectral weights", fontsize=16)
    ax = axes[0]
    ax.plot(wavelength, weight(wavelength), color="#3e4650", linewidth=2.5,
            label="Declared triangular weight w (not CIE V)")
    for line, color in zip(lines, colors):
        ax.vlines(line, 0, 1, color=color, linestyle="--", linewidth=1.5)
        ax.scatter(line, weight(line), s=65, color=color, zorder=3)
        offset = (25, 0) if line == 555 else (-70, 12) if line == 450 else (8, 12)
        ax.annotate(f"{line:.0f} nm\nw = {weight(line):.3f}", (line, weight(line)),
                    xytext=offset, textcoords="offset points", fontsize=10)
    ax.set(xlim=(380, 740), ylim=(0, 1.15), xlabel="Wavelength (nm)", ylabel="Dimensionless weight w")
    ax.legend(loc="upper left", fontsize=10)
    ax.grid(alpha=0.18)
    ax = axes[1]
    bars = ax.bar(["450 nm", "555 nm", "650 nm"], weighted_lm, color=colors, width=0.52)
    for bar, value in zip(bars, weighted_lm):
        ax.text(bar.get_x() + bar.get_width() / 2, value + 0.02, f"{value:.5f}", ha="center")
    ax.set(ylim=(0, 0.86), ylabel="Model weighted output (lm)")
    ax.set_title("Each ideal line carries 1 mW; model output = 683 × power × w", fontsize=11)
    ax.grid(axis="y", alpha=0.18)
    fig.text(0.5, -0.015, "Illustrative analytic model only • No measured spectra or standard visual-response data",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=130, facecolor="white",
                transparent=False, bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)
    print({"line_powers_W": powers_w.tolist(), "weights": weight(lines).tolist(),
           "model_weighted_outputs_lm": weighted_lm.tolist()})


if __name__ == "__main__":
    main()
