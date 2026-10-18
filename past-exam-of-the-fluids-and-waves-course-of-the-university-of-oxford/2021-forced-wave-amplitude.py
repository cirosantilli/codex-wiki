"""Draw the requested subcritical amplitude sketch in Oxford A10 (2021).

Run from the desired output directory. Tested with Python 3.14.4 and the
NumPy/Matplotlib versions in the repository's root pyproject.toml.
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    speed = np.linspace(0, 0.95, 1000)
    amplitude = 1 / (1 - speed**2)
    fig, ax = plt.subplots(figsize=(6.4, 4.1), facecolor="white")
    ax.plot(speed, amplitude, color="#176b93", lw=2.3)
    ax.plot(0, 1, "o", ms=7, mfc="white", mec="#176b93", mew=1.7, zorder=4)
    ax.axhline(1, color="0.45", ls="--", lw=1)
    ax.axvline(1, color="#b4591c", ls="--", lw=1.5)
    ax.annotate("Resonance", xy=(1, 7.0), xytext=(0.63, 7.5), arrowprops={"arrowstyle": "->", "color": "#b4591c"}, color="#b4591c")
    ax.annotate(r"$a_{\rm crit}=p_1/(\rho g)$", xy=(0.08, 1), xytext=(0.17, 2.8), arrowprops={"arrowstyle": "->", "color": "0.35"}, color="0.25")
    ax.text(0.11, 0.93, r"$a/a_{\rm crit}=1/[1-(c/c^*)^2]$", transform=ax.transAxes, fontsize=12)
    ax.set(xlim=(-0.03, 1.06), ylim=(0, 8.5), xlabel=r"Pressure-pattern speed $c/c^*$", ylabel=r"Forced amplitude $a/a_{\rm crit}$", title="Subcritical travelling-pressure response")
    ax.set_xticks((0, 0.25, 0.5, 0.75, 1))
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_facecolor("white")
    fig.tight_layout()
    fig.savefig("2021-forced-wave-amplitude.png", dpi=150, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
