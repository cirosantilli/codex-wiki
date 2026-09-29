"""Compare two ideal resistor drives; Python 3.14 / matplotlib 3.10.7 / numpy 2.3.5.

Run from _media; the matching opaque PNG is written to the current directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14, "axes.labelsize": 12})
    resistance = np.linspace(2.5, 15, 350)
    current, voltage = 1.0, 5.0
    fig, axes = plt.subplots(2, 2, figsize=(10, 6.4), sharex=True,
                             gridspec_kw={"height_ratios": [1.5, 1]}, layout="constrained")
    fig.suptitle("Joule heating: state what the supply holds fixed", fontsize=17)
    blue, orange = "#17638d", "#bb4e20"
    axes[0, 0].plot(resistance, current**2 * resistance, color=blue, lw=2.8)
    axes[0, 1].plot(resistance, voltage**2 / resistance, color=orange, lw=2.8)
    axes[0, 0].set_title(r"Fixed current: $I_0=1\,\mathrm{A}$")
    axes[0, 1].set_title(r"Fixed voltage: $V_0=5\,\mathrm{V}$")
    axes[0, 0].text(0.04, 0.90, r"$P=I_0^2R$", transform=axes[0, 0].transAxes, fontsize=15)
    axes[0, 1].text(0.53, 0.90, r"$P=V_0^2/R$", transform=axes[0, 1].transAxes, fontsize=15)
    for ax, values, color in [(axes[0, 0], [5, 10], blue), (axes[0, 1], [5, 2.5], orange)]:
        ax.scatter([5, 10], values, color=color, s=45, zorder=4)
        for r, p in zip([5, 10], values):
            ax.annotate(f"{p:g} W", (r, p), xytext=(8, 9), textcoords="offset points", color=color)
        ax.set_ylabel("Dissipated power (W)")
        ax.set_ylim(0, 17)
    axes[1, 0].plot(resistance, current * resistance, color=blue, lw=2.5)
    axes[1, 1].plot(resistance, voltage / resistance, color=orange, lw=2.5)
    axes[1, 0].set_ylabel("Required voltage (V)")
    axes[1, 1].set_ylabel("Resulting current (A)")
    axes[1, 0].set_ylim(0, 17)
    axes[1, 1].set_ylim(0, 2.3)
    for ax, values, color in [(axes[1, 0], [5, 10], blue), (axes[1, 1], [1, 0.5], orange)]:
        ax.scatter([5, 10], values, color=color, s=45, zorder=4)
        for r, y in zip([5, 10], values):
            unit = "V" if color == blue else "A"
            ax.annotate(f"{y:g} {unit}", (r, y), xytext=(8, 7), textcoords="offset points", color=color)
        ax.set_xlabel(r"Resistance $R$ ($\Omega$)")
    for ax in axes.flat:
        ax.set_xlim(2.5, 15)
        ax.set_xticks([5, 10, 15])
        ax.grid(alpha=0.18)
        ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path(__file__).stem + ".png", dpi=130, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
