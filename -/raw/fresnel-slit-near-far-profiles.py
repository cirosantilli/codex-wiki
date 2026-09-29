"""Original numerical Fresnel slit profiles, not experimental observations.

Python 3.14, NumPy 2.3, Matplotlib 3.10. Run from _media; output in CWD.
Composite trapezoidal quadrature includes both aperture endpoints.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

WAVELENGTH = 633e-9
WIDTH = .4e-3


def amplitude(q, fresnel_number, samples=4097):
    """Dimensionless aperture integral; q = x D / (lambda z)."""
    t = np.linspace(-.5, .5, samples)
    q = np.asarray(q)
    result = np.empty(q.size, dtype=complex)
    for start in range(0, q.size, 128):
        chunk = q.ravel()[start:start + 128]
        integrand = np.exp(1j * np.pi * fresnel_number * t**2
                          - 2j * np.pi * chunk[:, None] * t)
        result[start:start + len(chunk)] = np.trapezoid(integrand, t, axis=1)
    return result.reshape(q.shape)


def main():
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.8), dpi=100)
    fig.set_facecolor("white")
    for ax, distance, extent, color in zip(axes, [.02, 2.0], [.6e-3, .012],
                                          ["#326ea8", "#ce6426"]):
        x = np.linspace(-extent, extent, 1801)
        number = WIDTH**2 / (WAVELENGTH * distance)
        q = x * WIDTH / (WAVELENGTH * distance)
        intensity = number * abs(amplitude(q, number))**2
        ax.plot(x * 1000, intensity / intensity.max(), lw=2, color=color,
                label="Fresnel integral")
        if distance == .02:
            for edge in [-WIDTH / 2, WIDTH / 2]:
                ax.axvline(edge * 1000, color="#6d7886", ls=":", lw=1.3)
            ax.text(.5, .10, "Dotted lines: projected slit edges", ha="center",
                    transform=ax.transAxes, fontsize=9)
            heading = "Near field"
        else:
            ax.plot(x * 1000, np.sinc(q)**2, color="#34445a", ls="--", lw=1.5,
                    label="Fraunhofer sinc²")
            ax.annotate("First far-field zero\nx = 3.165 mm",
                        xy=(WAVELENGTH * distance / WIDTH * 1000, 0),
                        xytext=(4.4, .38), fontsize=10,
                        arrowprops={"arrowstyle": "->", "color": "#34445a"})
            heading = "Approaching the far field"
        ax.set_title(f"{heading}\nz = {distance:g} m; N_D = {number:.5g}",
                     fontsize=12)
        ax.set_xlabel("Screen coordinate x (mm)")
        ax.set_ylabel("Intensity / peak at this distance")
        ax.set_xlim(-extent * 1000, extent * 1000)
        ax.set_ylim(0, 1.08)
        ax.grid(alpha=.2)
        ax.legend(loc="upper right", fontsize=9, frameon=False)
    fig.suptitle("Calculated uniform-slit diffraction: λ = 633 nm, D = 0.400 mm",
                 fontsize=14, y=.98)
    fig.text(.5, .025, "Original scalar paraxial model • Each curve has its own peak normalization • Horizontal scales differ",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=.065, right=.985, bottom=.16, top=.79, wspace=.25)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
