"""Plot an illustrative dimensionless Morse potential; write the PNG to cwd.

Build: make _media/covalent-bond-energy-model.png
Self-chosen a=2, r_e=D=1; not measured or fitted H2 data.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7 (system +dfsg1).
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def potential(x):
    return (1.0 - np.exp(-2.0 * (np.asarray(x) - 1.0))) ** 2 - 1.0


def force(x):
    q = np.exp(-2.0 * (np.asarray(x) - 1.0))
    return 4.0 * (q * q - q)


def main():
    x = np.linspace(0.5, 4.0, 1401)
    xf = np.linspace(0.7, 4.0, 1321)
    q = np.exp(-2.0 * (xf - 1.0))
    repulsive = 4.0 * q * q
    attractive = -4.0 * q
    # Check the derivative numerically away from the equilibrium zero.
    h = 1e-5
    sample = np.array([0.5, 0.8, 1.0, 1.2, 1.5, 3.0])
    assert np.allclose(force(sample), -(potential(sample + h) - potential(sample - h)) / (2 * h),
                       atol=1e-8)
    curvature = (potential(1 + h) - 2 * potential(1) + potential(1 - h)) / h**2
    assert np.isclose(curvature, 8, atol=2e-5)
    assert potential(1) == -1 and force(1) == 0
    assert np.isclose(x[np.argmin(potential(x))], 1)
    assert np.all(force(sample[sample < 1]) > 0)
    assert np.all(force(sample[sample > 1]) < 0)
    assert np.allclose(repulsive + attractive, force(xf))
    assert abs(potential(20)) < 1e-15

    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, (energy_axis, force_axis) = plt.subplots(1, 2, figsize=(10, 4.7), dpi=120)
    fig.subplots_adjust(left=0.08, right=0.98, bottom=0.24, top=0.78, wspace=0.28)
    fig.suptitle("An illustrative bond: energy minimum and force balance", fontsize=15, y=0.96)
    fig.text(0.5, 0.865, "Self-chosen a = 2, re = D = 1; not measured H2 data", ha="center", fontsize=11)
    energy_axis.plot(x, potential(x), lw=2.5, color="#216b97")
    energy_axis.axhline(0, color="#666666", lw=1, ls="--")
    energy_axis.scatter([1], [-1], color="#28754f", zorder=3, s=45)
    energy_axis.annotate("Stable minimum\nx = 1, V/D = −1", xy=(1, -1), xytext=(1.65, -0.92),
                         arrowprops={"arrowstyle": "->", "color": "#28754f"},
                         color="#28754f", fontsize=10)
    energy_axis.text(2.4, 0.13, "Separated atoms: V → 0", fontsize=10)
    energy_axis.annotate("Closer: repulsion", xy=(0.58, potential(0.58)), xytext=(1.2, 1.6),
                         arrowprops={"arrowstyle": "->"}, fontsize=10)
    energy_axis.annotate("", xy=(3.7, 0), xytext=(3.7, -1),
                         arrowprops={"arrowstyle": "<->", "color": "#a44f25"})
    energy_axis.text(3.79, -0.58, "D", color="#a44f25")
    energy_axis.set(xlim=(0.5, 4), ylim=(-1.18, 2.35), xlabel=r"Separation $x=r/r_e$",
                    ylabel=r"Potential energy $u=V/D$")

    force_axis.plot(xf, repulsive, color="#a44f25", lw=1.8, ls="--", label="Positive term")
    force_axis.plot(xf, attractive, color="#75509b", lw=1.8, ls=":", label="Negative term")
    force_axis.plot(xf, force(xf), color="#216b97", lw=2.5, label=r"Net: $f=-du/dx$")
    force_axis.axhline(0, color="#666666", lw=1)
    force_axis.axvline(1, color="#28754f", lw=1, ls=":")
    force_axis.scatter([1, 1, 1], [4, -4, 0], color="#28754f", zorder=3, s=25)
    force_axis.annotate("+4 − 4 = 0", xy=(1, 0), xytext=(1.55, 3.4),
                        arrowprops={"arrowstyle": "->", "color": "#28754f"},
                        color="#28754f", fontsize=11)
    force_axis.legend(loc="upper right", frameon=False, fontsize=10)
    force_axis.set(xlim=(0.7, 4), ylim=(-8.5, 14), xlabel=r"Separation $x=r/r_e$",
                   ylabel=r"Separating force $f=Fr_e/D$")
    for axis in (energy_axis, force_axis):
        axis.grid(alpha=0.15)
    fig.text(0.5, 0.115, r"$u=(1-e^{-2(x-1)})^2-1$; $f=4e^{-4(x-1)}-4e^{-2(x-1)}$",
             ha="center", fontsize=12)
    fig.text(0.5, 0.035, "Force terms are algebraic model components, not measured microscopic forces.",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd() / "covalent-bond-energy-model.png", transparent=False)
    plt.close(fig)
    print(f"u(0.5)={potential(0.5):.8f}; u(1)={potential(1):g}; "
          f"u(1.5)={potential(1.5):.8f}; f(1)={force(1):g}; u''(1)≈{curvature:.6f}; "
          "force derivative and sign checks passed.")


if __name__ == "__main__":
    main()
