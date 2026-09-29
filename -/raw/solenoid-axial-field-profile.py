"""Plot finite-solenoid axial fields and validate by direct Biot-Savart quadrature.

Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
Write the same-basename opaque PNG to CWD; use the root Make media target.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def axial_ratio(z, radius, length):
    """Bz/(mu0*n*I), on the axis of a continuum of circular turns only."""
    near, far = z + length / 2, z - length / 2
    return 0.5 * (near / np.hypot(radius, near)
                  - far / np.hypot(radius, far))


def biot_savart_ratio(z, radius, length):
    """Integrate dl cross R / |R|^3 over angle and source z, independently.

    Dimensionless units mu0*n*I=1. Each source slice has n*dz' turns.
    The circular wires are parameterized in physical (x,y,z) coordinates.
    """
    nodes, weights = np.polynomial.legendre.leggauss(320)
    source_z, dz_weights = nodes * length / 2, weights * length / 2
    angles = (np.arange(256) + 0.5) * (2 * np.pi / 256)
    dphi = 2 * np.pi / 256
    source = np.empty((len(nodes), len(angles), 3))
    source[:, :, 0] = radius * np.cos(angles)
    source[:, :, 1] = radius * np.sin(angles)
    source[:, :, 2] = source_z[:, None]
    tangent = np.stack((-radius * np.sin(angles), radius * np.cos(angles),
                        np.zeros_like(angles)), axis=-1)
    displacement = np.array([0.0, 0.0, z]) - source
    integrand = np.cross(tangent, displacement) / (
        np.linalg.norm(displacement, axis=-1)[..., None] ** 3)
    return np.sum(integrand * dz_weights[:, None, None], axis=(0, 1)) * dphi / (4 * np.pi)


def validate():
    maximum_error = 0.0
    for length in (2.0, 6.0, 20.0):
        for coordinate in (-1.2, -0.5, -0.23, 0, 0.23, 0.5, 1.2):
            z = coordinate * length
            direct = biot_savart_ratio(z, 1.0, length)
            expected = axial_ratio(z, 1.0, length)
            np.testing.assert_allclose(direct, [0, 0, expected], rtol=2e-11, atol=2e-13)
            maximum_error = max(maximum_error, abs(direct[2] - expected))
        np.testing.assert_allclose(axial_ratio(0.0, 1.0, length),
                                   length / np.sqrt(length**2 + 4))
        np.testing.assert_allclose(axial_ratio(length / 2, 1.0, length),
                                   length / (2 * np.sqrt(length**2 + 1)))
        assert axial_ratio(length, 1.0, length) > 0
    # Exact normalized case ell/a=2 gives centre ratio 1/sqrt(2).
    np.testing.assert_allclose(axial_ratio(0.0, 1.0, 2.0), 1 / np.sqrt(2))
    np.testing.assert_allclose(axial_ratio(5e4, 1.0, 1e5), 0.5, atol=3e-11)

    mu0, turns, length, radius, current = 1.256637e-6, 1000, 0.50, 0.025, 0.50
    density, area = turns / length, np.pi * radius**2
    field = mu0 * density * current
    inductance = mu0 * turns**2 * area / length
    flux, linkage = field * area, turns * field * area
    energy = 0.5 * inductance * current**2
    nodes, weights = np.polynomial.legendre.leggauss(8)
    charging_currents = (nodes + 1) * current / 2
    charging_work = np.dot(weights, inductance * charging_currents) * current / 2
    np.testing.assert_allclose([field, inductance, flux, linkage, energy],
                               [0.001256637, 0.004934801959286397,
                                2.4674009796431984e-6, 0.0024674009796431984,
                                0.0006168502449107996], rtol=2e-14)
    np.testing.assert_allclose(energy, charging_work)
    np.testing.assert_allclose(energy, field**2 * area * length / (2 * mu0))
    finite_millitesla = field * axial_ratio(np.array([0, length / 2, length]),
                                           radius, length) * 1000
    np.testing.assert_allclose(finite_millitesla, [1.2504, 0.6275, 0.00277], rtol=2e-3)
    print(f"21 vector Biot-Savart checks passed; max absolute normalized error {maximum_error:.3g}")
    print(f"Worked example: B(z=0,end,ell)={finite_millitesla} mT; L={inductance:.9g} H; U={energy:.9g} J")


def main():
    validate()
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(8, 5.4), dpi=120, facecolor="white")
    coordinate = np.linspace(-1.2, 1.2, 1001)
    ax.axvspan(-0.5, 0.5, color="#edf3f7", zorder=0)
    for ratio, colour in [(2, "#bc5c28"), (6, "#26846b"), (20, "#216baf")]:
        ax.plot(coordinate, axial_ratio(coordinate * ratio, 1.0, ratio),
                lw=2.5, color=colour, label=rf"$\ell/a={ratio}$")
        ax.scatter([0, 0.5], axial_ratio(np.array([0, 0.5]) * ratio, 1.0, ratio),
                   color=colour, s=22, zorder=4)
    ax.plot([-1.2, -0.5, -0.5, 0.5, 0.5, 1.2], [0, 0, 1, 1, 0, 0],
            color="#444b53", ls="--", lw=1.6, label="Ideal interior + zero exterior")
    ax.axhline(0.5, lw=0.8, color="#a5adb3", ls=":")
    ax.text(0, 1.065, "Coil interior", ha="center", color="#52616c")
    ax.set(xlim=(-1.2, 1.2), ylim=(-0.01, 1.14),
           xlabel=r"Axial position $z/\ell$ (centre at 0)",
           ylabel=r"On-axis field $B_z/(\mu_0 n I)$",
           title="Finite solenoids: a flat centre still has end effects")
    ax.set_xticks([-1, -0.5, 0, 0.5, 1], ["−1.0", "−0.5\nLeft end", "0.0", "0.5\nRight end", "1.0"])
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.34), ncol=2,
              fontsize=10, frameon=False)
    ax.grid(alpha=0.17)
    fig.text(0.5, 0.025, "Circular-turn continuum only. This profile does not describe off-axis fields.",
             ha="center", fontsize=10, color="#52616c")
    fig.subplots_adjust(left=0.105, right=0.98, top=0.9, bottom=0.34)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
