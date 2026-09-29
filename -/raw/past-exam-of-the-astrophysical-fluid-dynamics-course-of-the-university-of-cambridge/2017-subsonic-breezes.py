"""Original Q4 isothermal breeze comparison; PNG basename goes to cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def mach_profile(radius, peak):
    """Invert M^2/2-log(M) on the strictly subsonic branch."""
    target = peak**2 / 2 - np.log(peak) + 2 * np.log(radius) + 2 / radius - 2
    lo = np.full_like(radius, 1e-14)
    hi = np.full_like(radius, peak)
    for _ in range(65):
        middle = (lo + hi) / 2
        value = middle**2 / 2 - np.log(middle)
        lo = np.where(value > target, middle, lo)
        hi = np.where(value > target, hi, middle)
    return (lo + hi) / 2


def main():
    radius = np.unique(np.r_[np.geomspace(0.2, 12, 700), 1.0])
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4), layout="constrained")
    fig.patch.set_facecolor("white")
    for peak, colour in [(0.25, "#17638d"), (0.5, "#b96e21"), (0.8, "#28784a")]:
        mach = mach_profile(radius, peak)
        label = rf"$\mathcal{{M}}_M={peak:g}$"
        axes[0].plot(radius, mach, color=colour, linewidth=2.1, label=label)
        axes[1].plot(radius, 1 / (radius**2 * mach), color=colour, linewidth=2.1, label=label)
        axes[0].scatter(1, peak, color=colour, s=25, zorder=4)
        axes[1].scatter(1, 1 / peak, color=colour, s=25, zorder=4)
    for ax in axes:
        ax.set_facecolor("white")
        ax.set_xscale("log")
        ax.axvline(1, color="#777777", linewidth=1, linestyle="--")
        ax.set(xlim=(0.2, 12), xlabel=r"Radius $r/r_M$")
        ax.grid(alpha=0.2, which="both")
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set(ylim=(0, 1), ylabel=r"Mach number $u/a$", title="Same radius, different peak speeds")
    axes[0].legend(fontsize=9)
    axes[1].set_yscale("log")
    axes[1].set(ylabel=r"Density $\rho/\rho_{\rm char}$", title="Same mass flux, different densities")
    fig.savefig(Path("2017-subsonic-breezes.png"), dpi=160, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
