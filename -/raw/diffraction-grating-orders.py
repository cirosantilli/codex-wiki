"""Normal-incidence grating directions; output a white PNG in the working directory.

Uses the repository's numpy/matplotlib dependencies; tested with Python 3.14.
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    wavelength_nm, spacing_nm = 600.0, 2000.0
    orders = np.arange(-3, 4)
    sines = orders * wavelength_nm / spacing_nm
    angles = np.degrees(np.arcsin(sines))
    assert np.all(np.abs(sines) <= 1)
    assert 4 * wavelength_nm / spacing_nm > 1
    np.testing.assert_allclose(np.sin(np.radians(angles)), sines, atol=1e-15)

    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white", "axes.facecolor": "white"})
    fig, (fan, color) = plt.subplots(1, 2, figsize=(12, 6.2), gridspec_kw={"width_ratios": [1.15, 1]})
    fig.subplots_adjust(left=0.04, right=0.97, top=0.81, bottom=0.21, wspace=0.20)
    fig.suptitle("Normal-incidence transmission grating", fontsize=19, y=0.97)
    fig.text(0.5, 0.90, "600 nm light  •  spacing d = 2 μm  •  sin θ = 0.3 m", ha="center", fontsize=15)

    fan.axvline(0, color="#777777", lw=5, ymin=0.12, ymax=0.88)
    fan.axhline(0, color="#888888", lw=1, ls="--")
    fan.annotate("", (0, 0), (-0.75, 0), arrowprops={"arrowstyle": "->", "lw": 2.5, "color": "#405b75"})
    fan.text(-0.80, -0.23, "Incident\nplane wave", ha="center", va="top", fontsize=11)
    fan.text(0, -1.19, "Grating", ha="center", color="#555555")
    for m, sine, theta in zip(orders, sines, angles):
        direction = np.array([np.sqrt(1 - sine**2), sine])
        end = 1.03 * direction
        fan.annotate("", end, (0, 0), arrowprops={"arrowstyle": "->", "lw": 2.0, "color": "#c76921"})
        label = 1.17 * direction
        fan.text(*label, f"m = {m:+d}\n{theta:+.3f}°" if m else "m = 0\n0°", ha="left", va="center", fontsize=11)
    fan.text(1.49, -0.23, "Normal", fontsize=11, color="#666666")
    fan.set(xlim=(-1.06, 1.98), ylim=(-1.28, 1.28), aspect="equal")
    fan.axis("off")
    fan.set_title("Seven allowed directions", fontsize=15, pad=14)

    wavelengths = np.array([450, 500, 550, 600, 650])
    color_angles = np.degrees(np.arcsin(wavelengths / spacing_nm))
    colors = ["#5046ad", "#007ca5", "#32904a", "#c76921", "#b02b35"]
    for nm, theta, shade in zip(wavelengths, color_angles, colors):
        color.plot([theta, theta], [0.25, 0.77], color=shade, lw=3)
        color.text(theta, 0.81, f"{nm}\nnm", ha="center", color=shade, fontsize=11)
        color.text(theta, 0.14, f"{theta:.2f}°", ha="center", color=shade, fontsize=11)
    color.set(xlim=(12, 20.1), ylim=(0, 1.15), yticks=[], xlabel="First-order angle θ (degrees)")
    color.set_title("Longer wavelengths: larger +1 angle", fontsize=14, pad=14)
    color.set_xticks([13, 15, 17, 19])
    for side in ["left", "right", "top"]:
        color.spines[side].set_visible(False)
    fig.text(0.5, 0.11, "m = ±4 would require sin θ = ±1.2: no propagating direction.", ha="center", fontsize=14)
    fig.text(0.5, 0.055, "Ray arrows mark order directions, not brightness or finite peak width.", ha="center", fontsize=12, color="#555555")
    fig.savefig("diffraction-grating-orders.png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)
    print("Orders:", list(zip(orders.tolist(), sines.tolist(), angles.tolist())))
    print("First-order colour angles:", list(zip(wavelengths.tolist(), color_angles.tolist())))


if __name__ == "__main__":
    main()
