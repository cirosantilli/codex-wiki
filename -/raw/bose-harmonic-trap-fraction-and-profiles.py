"""Original ideal-trap prediction and normalized synthetic profile illustration.

Tested with Python 3.14, matplotlib 3.10.7 and NumPy 2.3.5.
Run from _media; emits bose-harmonic-trap-fraction-and-profiles.png in CWD.
The two Gaussian widths are chosen illustration parameters, not fitted data
or a prediction of the interacting condensate expansion.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ZETA3 = 1.2020569031595943
HBAR = 1.054571817e-34
KB = 1.380649e-23
N = 100_000
OMEGA = 2 * np.pi * 100


def gaussian(x, width):
    return np.exp(-.5 * (x / width)**2) / (np.sqrt(2 * np.pi) * width)


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.9), dpi=120, facecolor="white")
    blue, orange, ink = "#2166ac", "#b35806", "#183042"
    t = np.linspace(0, 1.25, 501)
    axes[0].plot(t, np.maximum(1 - t**3, 0), color=blue, linewidth=2.8)
    axes[0].axvline(1, color=".6", linewidth=1, linestyle="--")
    axes[0].plot([.8], [1-.8**3], "o", color=orange, markersize=7)
    axes[0].annotate(r"$T/T_c=0.8$" + "\n" + r"$N_0/N=0.488$",
                     xy=(.8, .488), xytext=(.08, .24), fontsize=12,
                     arrowprops={"arrowstyle": "->", "color": orange})
    axes[0].set(xlabel=r"Temperature $T/T_c$", ylabel=r"Condensate fraction $N_0/N$",
                xlim=(0, 1.25), ylim=(0, 1.06), title="Ideal 3D harmonic trap")
    axes[0].text(.08, .72, r"$N_0/N=1-(T/T_c)^3$", transform=axes[0].transAxes,
                 fontsize=12, color=blue)
    x = np.linspace(-4.5, 4.5, 2001)
    for ratio, style in [(1.1, "--"), (.95, "-"), (.8, "-")]:
        f = max(1-ratio**3, 0)
        profile = (1-f) * gaussian(x, 1) + f * gaussian(x, .20)
        axes[1].plot(x, profile, style, linewidth=2,
                     label=rf"$T/T_c={ratio:g}$; $f_0={f:.3f}$")
    axes[1].set(xlabel=r"Position $u$ (chosen units)", ylabel="Normalized line density",
                xlim=(-4, 4), ylim=(0, 1.28), title="Synthetic two-width profiles")
    axes[1].legend(frameon=False, fontsize=10, loc="upper right")
    axes[1].text(.03, .86, r"$\sigma_t=1,\quad \sigma_c=0.20$",
                 transform=axes[1].transAxes, fontsize=11)
    tc = HBAR * OMEGA / KB * (N / ZETA3)**(1/3)
    fig.suptitle("Saturation predicts a population; imaging resolves a shape", fontsize=16,
                 color=ink, weight="bold")
    fig.text(.5, .075, rf"Chosen example: $N=10^5$, $\bar\omega/(2\pi)=100$ Hz, "
             rf"$T_c={tc*1e9:.1f}$ nK.  No measured data.", ha="center", fontsize=11)
    fig.text(.5, .025, "Profile widths are fixed for illustration; the cubic law controls only the component weights.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=.075, right=.98, bottom=.23, top=.82, wspace=.3)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
