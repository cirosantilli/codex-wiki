"""Original square-aperture Fresnel calculations; tested with Python 3.14.

Uses the root pyproject.toml NumPy/Matplotlib dependencies, without SciPy.
Gauss-Legendre quadrature evaluates finite Fresnel integrals. Writes the PNG
basename in the current working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def fresnel(w):
    """C(w) + i S(w), with phase pi*u**2/2; signed integration limits."""
    nodes, weights = np.polynomial.legendre.leggauss(192)
    w = np.asarray(w)
    u = 0.5 * w[..., None] * (nodes + 1)
    return 0.5 * w * np.sum(weights * np.exp(0.5j * np.pi * u**2), axis=-1)


def main():
    fig, (central, section) = plt.subplots(1, 2, figsize=(10.3, 4.2), layout="constrained")
    fig.patch.set_facecolor("white")
    w = np.linspace(0, 3.1, 1000)
    ratio = 4 * np.abs(fresnel(w)) ** 4
    value = 4 * abs(fresnel(1.0)) ** 4
    central.plot(w, ratio, color="#0068a0", lw=2)
    central.axhline(1, color="#777777", ls="--", lw=1)
    central.plot(1, value, "o", color="#b55713")
    central.annotate(f"w = 1: intensity ratio {value:.3f}", xy=(1, value),
                     xytext=(1.3, 2.8), fontsize=10,
                     arrowprops={"arrowstyle": "->", "color": "#b55713"})
    central.set(xlabel=r"$w=(d/2)\sqrt{2/(\lambda R_{\rm eff})}$",
                ylabel=r"$I(0,0)/I_0(0,0)$", title="Central intensity as aperture size varies",
                xlim=(0, 3.1), ylim=(0, 3.3))

    x_mm = np.linspace(-3, 3, 1100)
    # At p=q=1 m, d=1 mm and lambda=1 micrometre, the scaled x shift equals X in mm.
    dx = fresnel(1 - x_mm) - fresnel(-1 - x_mm)
    dy = 2 * fresnel(1.0)
    profile = np.abs(dx * dy) ** 2 / 4
    section.plot(x_mm, profile, color="#0068a0", lw=2)
    section.axhline(1, color="#777777", ls="--", lw=1, label="Unobscured intensity")
    section.plot(0, value, "o", color="#b55713")
    section.set(xlabel="Observation coordinate X (mm), Y = 0",
                ylabel=r"$I(X,0)/I_0(X,0)$", title="Off-axis intensity for the given aperture",
                xlim=(-3, 3), ylim=(0, 3.3))
    section.text(0.03, 0.93, "d = 1 mm; p = q = 1 m; wavelength = 1000 nm",
                 transform=section.transAxes, fontsize=8.5)
    section.legend(loc="upper right", fontsize=9, bbox_to_anchor=(1, 0.87))
    for ax in (central, section):
        ax.grid(alpha=0.18)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"C(1)={fresnel(1).real:.10f}; S(1)={fresnel(1).imag:.10f}; I/I0={value:.10f}")


if __name__ == "__main__":
    main()
