"""Generate gaussian-beam-power-profile.png in CWD.

Tested with Python 3.14.4, numpy 2.3.5 and matplotlib 3.10.7.
Uses the two-transverse-coordinate circular Gaussian model.
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    radius = np.linspace(0, 2.2, 881)
    amplitude = np.exp(-radius**2)
    intensity = np.exp(-2 * radius**2)
    power = -np.expm1(-2 * radius**2)
    blue, orange = "#2166ac", "#c45b15"
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.8), dpi=100)
    fig.subplots_adjust(left=.08, right=.98, bottom=.26, top=.79, wspace=.28)
    ax = axes[0]
    ax.plot(radius, amplitude, "--", color=blue, lw=2.3, label=r"Amplitude $e^{-(r/w)^2}$")
    ax.plot(radius, intensity, color=orange, lw=2.3, label=r"Intensity $e^{-2(r/w)^2}$")
    ax.axvline(1, color="0.6", lw=1, ls=":")
    ax.scatter([1, 1], [np.exp(-1), np.exp(-2)], color=[blue, orange], zorder=4, s=40)
    ax.annotate(r"$1/e=0.367879$", xy=(1, np.exp(-1)), xytext=(1.14, .50),
                fontsize=10, color=blue, arrowprops={"arrowstyle": "->", "color": blue})
    ax.annotate(r"$1/e^2=0.135335$", xy=(1, np.exp(-2)), xytext=(1.18, .27),
                fontsize=10, color=orange, arrowprops={"arrowstyle": "->", "color": orange})
    ax.set(xlabel=r"Radial distance $r/w(z)$", ylabel="Ratio to on-axis value",
           title="One radius, two different ratios", xlim=(0, 2.2), ylim=(0, 1.06))
    ax.legend(loc="upper right", fontsize=10)
    ax = axes[1]
    ax.plot(radius, power, color=blue, lw=2.5)
    fraction = -np.expm1(-2)
    ax.plot([0, 1, 1], [fraction, fraction, 0], "--", color="0.6", lw=1)
    ax.scatter([1, 2], [fraction, -np.expm1(-8)], color=[orange, blue], zorder=4, s=45)
    ax.annotate("At a = w: 86.4665%", xy=(1, fraction), xytext=(.17, .65),
                fontsize=11, color=orange, bbox={"facecolor": "white", "edgecolor": "none", "pad": 2},
                arrowprops={"arrowstyle": "->", "color": orange})
    ax.annotate("At a = 2w: 99.9665%", xy=(2, -np.expm1(-8)), xytext=(.74, .43),
                fontsize=11, color=blue, arrowprops={"arrowstyle": "->", "color": blue})
    ax.set(xlabel=r"Centered disk radius $a/w(z)$", ylabel="Fraction of total power",
           title=r"Enclosed power: $1-e^{-2(a/w)^2}$", xlim=(0, 2.2), ylim=(0, 1.06))
    for ax in axes:
        ax.grid(alpha=.18)
        ax.set_xticks([0, .5, 1, 1.5, 2])
    fig.suptitle("A Gaussian beam has no sharp edge", fontsize=16, y=.97)
    fig.text(.5, .88, "Circular beam with two transverse coordinates", ha="center", fontsize=12)
    fig.text(.5, .10, r"Enclosed power integrates intensity over annuli: $dA=2\pi r\,dr$.",
             ha="center", fontsize=11)
    fig.text(.5, .045, "These curves describe the incident ideal beam; aperture clipping changes later propagation.",
             ha="center", fontsize=10)
    fig.savefig("gaussian-beam-power-profile.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
