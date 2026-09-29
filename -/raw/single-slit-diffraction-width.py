"""Generate single-slit-diffraction-width.png in CWD on an opaque white background.

Tested with Python 3.14.4, numpy 2.3.5 and matplotlib 3.10.7.
The plotted scalar Fraunhofer envelope uses exact screen-angle geometry;
central width means first-minimum separation, not FWHM.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    wavelength, distance = 500e-9, 1.0
    widths = (0.1e-3, 0.2e-3)
    colors = ("#1768ac", "#c76319")
    y = np.linspace(-15e-3, 15e-3, 6001)
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, (ax, geometry) = plt.subplots(2, 1, figsize=(10.2, 7.2), dpi=110,
                                      gridspec_kw={"height_ratios": [2.2, 1]})
    fig.subplots_adjust(left=.10, right=.94, top=.86, bottom=.10, hspace=.66)
    for index, (width, color) in enumerate(zip(widths, colors)):
        theta = np.arctan(y / distance)
        # numpy.sinc(t) = sin(pi*t)/(pi*t), including value one at zero.
        intensity = np.sinc(width * np.sin(theta) / wavelength) ** 2
        first_angle = np.arcsin(wavelength / width)
        first_y = distance * np.tan(first_angle)
        assert np.isclose(np.sinc(width * np.sin(first_angle) / wavelength), 0,
                          atol=1e-14)
        ax.plot(y * 1e3, intensity, color=color, lw=2.2,
                label=f"a = {width * 1e3:.1f} mm")
        ax.vlines([-first_y * 1e3, first_y * 1e3], 0, 1,
                  color=color, lw=1, linestyle="--", alpha=.45)
        level = -.10 - .15 * index
        ax.annotate("", xy=(first_y * 1e3, level),
                    xytext=(-first_y * 1e3, level),
                    arrowprops={"arrowstyle": "<->", "color": color, "lw": 1.6})
        ax.text(0, level + .028, f"First-minimum width: {2 * first_y * 1e3:.5f} mm",
                ha="center", color=color, fontsize=10)
    ax.set(xlim=(-15, 15), ylim=(-.32, 1.06), xlabel="Screen position y (mm)",
           ylabel=r"Normalized scalar intensity $I/I_0$")
    ax.set_yticks([0, .25, .5, .75, 1])
    ax.grid(alpha=.17)
    ax.legend(loc="upper right", frameon=False)
    # z is the propagation coordinate; y is shown in mm, enlarging its scale.
    first_y_mm = distance * np.tan(np.arcsin(wavelength / widths[0])) * 1e3
    geometry.plot([0, distance], [0, 0], color=".5", lw=1, linestyle=":")
    for sign in (-1, 1):
        geometry.plot([0, distance], [0, sign * first_y_mm], color=colors[0], lw=1.8)
    geometry.plot([distance, distance], [-6, 6], color=".25", lw=2)
    geometry.scatter([0], [0], color=".25", s=30, zorder=4)
    geometry.text(0, 1.0, "Slit centre", ha="left", fontsize=10)
    geometry.text(distance, 6.6, "Screen", ha="center", fontsize=10)
    geometry.annotate("", xy=(distance + .025, first_y_mm),
                      xytext=(distance + .025, 0),
                      arrowprops={"arrowstyle": "<->", "color": colors[0]})
    geometry.text(distance + .04, 2.2, r"$y_1$", color=colors[0])
    geometry.text(.42, 3.7, r"$\theta_1 = \arcsin(\lambda/a)$", color=colors[0])
    geometry.text(.48, -1.5, r"$y_1=L\tan\theta_1$", ha="center")
    geometry.annotate("", xy=(distance, -7), xytext=(0, -7),
                      arrowprops={"arrowstyle": "<->", "color": ".3"})
    geometry.text(.5, -8.7, "L = 1 m", ha="center", fontsize=10)
    geometry.set(xlim=(-.04, 1.13), ylim=(-9.5, 8))
    geometry.axis("off")
    geometry.set_title("Screen geometry for a = 0.1 mm; vertical scale enlarged", fontsize=11)
    fig.suptitle("Single-slit diffraction: narrower opening, wider beam", fontsize=16, y=.98)
    fig.text(.5, .915, r"$\lambda=500$ nm, $L=1$ m;  $\theta=\arctan(y/L)$;  each curve has its own $I_0$",
             ha="center", fontsize=11)
    fig.text(.5, .025, "Ideal uniform coherent slit, scalar far-field model. Width is between first minima, not half-height.",
             ha="center", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
