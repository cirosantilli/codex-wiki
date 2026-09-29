"""Two synthetic equal-power spectra and an illustrative detector response.

Run from _media with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
The PNG is written to the current directory with this script's basename.
All wavelength integrals here use nm; powers are converted to W for currents.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    wave_a = np.linspace(400, 600, 2001)
    wave_b = np.linspace(600, 800, 2001)
    density_a = 0.020 * (1 - np.abs(wave_a - 500) / 100)  # mW/nm
    density_b = np.full_like(wave_b, 0.010)  # mW/nm

    def response(wavelength_nm):
        return 0.2 + 0.001 * (wavelength_nm - 400)  # A/W

    totals_mw = [np.trapezoid(density_a, wave_a), np.trapezoid(density_b, wave_b)]
    currents_ma = [np.trapezoid(density_a * response(wave_a), wave_a),
                   np.trapezoid(density_b * response(wave_b), wave_b)]
    np.testing.assert_allclose(totals_mw, [2, 2], atol=1e-12)
    np.testing.assert_allclose(currents_ma, [0.6, 1.0], atol=1e-12)
    for wave, density, bounds, expected in [
        (wave_a, density_a, (450, 550), 1.5),
        (wave_b, density_b, (650, 750), 1.0),
    ]:
        mask = (wave >= bounds[0]) & (wave <= bounds[1])
        np.testing.assert_allclose(np.trapezoid(density[mask], wave[mask]), expected, atol=1e-12)

    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12})
    fig = plt.figure(figsize=(10, 6.6), layout="constrained")
    fig.patch.set_facecolor("white")
    grid = fig.add_gridspec(2, 2, height_ratios=[1.25, 1])
    axes = [fig.add_subplot(grid[0, 0]), fig.add_subplot(grid[0, 1])]
    fig.text(0.5, 0.985, "Two synthetic spectra: equal total radiant flux, different signals",
             fontsize=15, ha="center", va="top")
    colors = ["#17649c", "#bd570c"]
    for ax, wave, density, label, band, band_power, color in zip(
        axes, [wave_a, wave_b], [density_a, density_b], ["A: triangular", "B: flat band"],
        [(450, 550), (650, 750)], [1.5, 1.0], colors,
    ):
        ax.plot([350, wave[0], *wave, wave[-1], 850], [0, 0, *density, 0, 0], color=color, lw=2)
        ax.fill_between(wave, density, color=color, alpha=0.14)
        mask = (wave >= band[0]) & (wave <= band[1])
        ax.fill_between(wave[mask], density[mask], color=color, alpha=0.4)
        ax.set(title=label, xlim=(350, 850), ylim=(0, 0.026), xlabel="Wavelength λ (nm)",
               ylabel="Spectral radiant flux (mW/nm)")
        ax.text(0.5, 0.91, "Total area = 2.00 mW", transform=ax.transAxes, ha="center")
        ax.text(0.5, 0.73, f"{band[0]}–{band[1]} nm:\n{band_power:.2f} mW", transform=ax.transAxes,
                ha="center", color=color)
        ax.grid(alpha=0.18)
        ax.set_xticks([400, 500, 600, 700, 800])

    ax = fig.add_subplot(grid[1, :])
    wavelengths = np.linspace(400, 800, 401)
    ax.plot(wavelengths, response(wavelengths), color="#333333", lw=2)
    ax.scatter([500, 700], [0.3, 0.5], c=colors, s=60, zorder=4)
    ax.text(510, 0.26, "A: mean R = 0.30 A/W\nCurrent = 0.60 mA", color=colors[0], va="top")
    ax.text(690, 0.54, "B: mean R = 0.50 A/W\nCurrent = 1.00 mA", color=colors[1], ha="right", va="bottom")
    ax.set(xlim=(380, 820), ylim=(0.13, 0.68), xlabel="Wavelength λ (nm)",
           ylabel="Responsivity R (A/W)", title="Illustrative linear response: current = ∫ R(λ) Φₑ,λ(λ) dλ")
    ax.grid(alpha=0.18)
    fig.get_layout_engine().set(rect=(0, 0.035, 1, 0.90))
    fig.text(0.5, 0.009, "All curves are stipulated models • No measured spectra or real detector calibration",
             ha="center", fontsize=10, color="#444444")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
