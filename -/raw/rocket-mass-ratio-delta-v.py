"""Plot ideal rocket velocity gains; write an opaque white PNG to the CWD."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    u = 2.0  # km/s
    initial_mass = 1000.0  # kg
    masses = np.linspace(initial_mass, 250.0, 501)
    gains = u * np.log(initial_mass / masses)
    half_gain = u * np.log(2.0)
    assert np.isclose(gains[-1], 2.772588722239781)
    assert np.isclose(u * np.log(1000 / 500), u * np.log(500 / 250))
    assert np.isclose(2000 * 5, 10000)

    fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.5), dpi=110)
    fig.patch.set_facecolor("white")
    blue, orange = "#245f9b", "#c56521"
    ax = axes[0]
    ratio = np.linspace(1, 4, 401)
    ax.plot(ratio, u * np.log(ratio), color=blue, lw=2.5)
    for value, color in [(2, blue), (4, orange)]:
        gain = u * np.log(value)
        ax.scatter(value, gain, color=color, zorder=5)
        ax.plot([1, value, value], [gain, gain, 0], ls="--", color=color, lw=1)
    ax.text(2.08, half_gain - .25, "R = 2: 1.3863 km/s", fontsize=10)
    ax.text(2.05, 2.85, "R = 4: 2.7726 km/s", fontsize=10, color=orange)
    ax.set(xlim=(.95, 4.15), ylim=(0, 3.2), xticks=[1, 2, 3, 4],
           xlabel=r"Mass ratio $R=M_{\rm initial}/M_{\rm final}$",
           ylabel=r"Ideal velocity gain $\Delta v$ (km/s)",
           title="Logarithmic gain")

    ax = axes[1]
    ax.plot(masses, gains, color="#404040", lw=2.5)
    ax.fill_between(masses, gains, where=masses >= 500, color=blue, alpha=.12)
    ax.fill_between(masses, gains, half_gain, where=masses <= 500,
                    color=orange, alpha=.14)
    ax.scatter([1000, 500, 250], [0, half_gain, 2 * half_gain],
               color=[blue, blue, orange], zorder=5)
    ax.axhline(half_gain, color="#999999", ls="--", lw=1)
    ax.text(950, 1.80, "1000 → 500 kg\n500 kg expelled\n+1.3863 km/s",
            color=blue, fontsize=10, va="bottom")
    ax.text(480, .28, "500 → 250 kg\n250 kg expelled\n+1.3863 km/s",
            color=orange, fontsize=10, va="bottom")
    ax.set(xlim=(1050, 200), ylim=(0, 3.2), xticks=[1000, 750, 500, 250],
           xlabel="Remaining total rocket mass (kg) — burn proceeds →",
           ylabel=r"Cumulative $\Delta v$ (km/s)",
           title="Same gain from each mass halving")
    for ax in axes:
        ax.set_facecolor("white")
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(alpha=.15)
    fig.suptitle("Ideal rocket: constant rearward relative exhaust speed u = 2 km/s",
                 fontsize=13)
    fig.tight_layout(rect=(0, 0, 1, .93))
    fig.savefig(Path.cwd() / "rocket-mass-ratio-delta-v.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
