"""Plot the two-photon opening-angle map and its normalized density.

Tested with Python 3.14, NumPy 2.3.5, and Matplotlib 3.10.7.
The only generated artifact is the PNG in the caller's working directory.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12})
    fig, (mapping, density) = plt.subplots(1, 2, figsize=(10.5, 4.4), dpi=100)
    fig.patch.set_facecolor("white")
    z = np.linspace(-1, 1, 2001)
    for gamma, color in [(2.0, "#0072B2"), (4.0, "#D55E00")]:
        beta = np.sqrt(1 - gamma**-2)
        angle = 2 * np.arcsin(np.clip(1 / (gamma * np.sqrt(1 - beta**2 * z**2)), 0, 1))
        amin = 2 * np.arcsin(1 / gamma)
        mapping.plot(z, np.rad2deg(angle), color=color, label=rf"$\gamma={gamma:g}$")
        aa = np.linspace(amin + 1e-5, np.pi - 1e-5, 3000)
        ss = np.sin(aa / 2)
        pp = np.cos(aa / 2) / (2 * beta * gamma * ss**2 * np.sqrt(gamma**2 * ss**2 - 1))
        density.plot(np.rad2deg(aa), pp * np.pi / 180, color=color, label=rf"$\gamma={gamma:g}$")
        density.axvline(np.rad2deg(amin), color=color, lw=1, ls="--", alpha=0.6)
    mapping.set(xlim=(-1, 1), ylim=(0, 185), xlabel=r"Rest-frame direction $z=\cos\theta_*$",
                ylabel=r"Opening angle $A$ (degrees)", title="Two directions give each opening angle")
    mapping.set_yticks([0, 30, 60, 90, 120, 150, 180])
    mapping.legend(loc="upper center")
    mapping.annotate("Stationary minima at $z=0$", xy=(0, 60), xytext=(-0.85, 105),
                     arrowprops={"arrowstyle": "->", "color": "#444444"}, fontsize=10)
    density.set(xlim=(0, 180), ylim=(1e-6, 10), yscale="log", xlabel=r"Opening angle $A$ (degrees)",
                ylabel="Normalized density (per degree)", title="Compression produces integrable peaks")
    density.set_xticks([0, 30, 60, 90, 120, 150, 180])
    density.legend(loc="upper right")
    density.text(0.97, 0.12, r"$A_{\min}=2\arcsin(1/\gamma)$" + "\nDashed lines: divergent endpoints",
                 transform=density.transAxes, ha="right", va="bottom", fontsize=10)
    for ax in (mapping, density):
        ax.set_facecolor("white")
        ax.grid(alpha=0.2)
    fig.tight_layout(pad=1.1, w_pad=2)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False, metadata={"Software": "Matplotlib"})
    plt.close(fig)


if __name__ == "__main__":
    main()
