"""Plot the isolated inverse-square force's escape energy budget.

Run from _media; writes the matching PNG basename to the working directory.
Tested with Python 3.14, Matplotlib 3.10.7, NumPy 2.3.5 (root pyproject.toml).
All values are synthetic: mu = 8 m^3/s^2, r0 = 2 m, test mass = 1 kg.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    mu, r0 = 8.0, 2.0
    energy_unit = mu / r0
    energies = (-0.5, 0.0, 0.5)
    colors = ("#2765a4", "#c66c0d", "#21825b")
    x = np.linspace(1.0, 8.0, 900)
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.8), layout="constrained")
    fig.set_facecolor("white")
    fig.suptitle("Radial launch: energy determines escape", fontsize=17)
    ax, kinetic = axes
    ax.plot(x, -1 / x, color="#282d34", lw=2.6, label=r"Potential $U/(m\mu/r_0)=-1/x$")
    for e, color in zip(energies, colors, strict=True):
        label = rf"$\mathcal{{E}}={e:+g}$" if e else r"$\mathcal{E}=0$ (threshold)"
        ax.axhline(e, color=color, lw=2, label=label)
        allowed_x = np.linspace(1, -1 / e if e < 0 else 8, 700)
        k = e + 1 / allowed_x
        assert np.min(k) >= -1e-14
        np.testing.assert_allclose(k - 1 / allowed_x, e, atol=1e-14)
        kinetic.plot(allowed_x, k, color=color, lw=2.4, label=label)
        ax.plot(1, e, "o", color=color, ms=6)
        kinetic.plot(1, e + 1, "o", color=color, ms=6)
    ax.plot(2, -0.5, "o", color=colors[0], ms=7)
    ax.annotate("Bound launch turns\nat $r=2r_0$", xy=(2, -0.5), xytext=(3.5, -0.77),
                arrowprops={"arrowstyle": "->", "color": colors[0]}, color=colors[0])
    kinetic.plot(2, 0, "o", color=colors[0], ms=7)
    kinetic.axhline(0.5, color=colors[2], ls=":", lw=1.3)
    kinetic.annotate(r"Positive energy: $K\to E$", xy=(7.2, 0.5), xytext=(3.1, 0.31),
                     arrowprops={"arrowstyle": "->", "color": colors[2]}, color=colors[2])
    kinetic.annotate(r"Threshold: $K\to0$", xy=(7.6, 1 / 7.6), xytext=(3.6, 0.04),
                     arrowprops={"arrowstyle": "->", "color": colors[1]}, color=colors[1])
    ax.set(title="Potential and constant total energies", ylim=(-1.1, 0.76),
           ylabel=r"Energy / $(m\mu/r_0)$")
    kinetic.set(title="Remaining kinetic energy",
                ylim=(-0.08, 1.62), ylabel=r"Kinetic energy / $(m\mu/r_0)$")
    for axis in axes:
        axis.set(xlim=(0.85, 8.15), xlabel=r"Distance $x=r/r_0$")
        axis.grid(alpha=0.18)
        axis.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="upper right", fontsize=10, framealpha=1)
    speeds = np.sqrt(2 * energy_unit * (np.array(energies) + 1))
    np.testing.assert_allclose(speeds**2, [4, 8, 12], atol=1e-13)
    assert mu / r0 == 4 and -mu / (energy_unit * energies[0]) == 4
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
