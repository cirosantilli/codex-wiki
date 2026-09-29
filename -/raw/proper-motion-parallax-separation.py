"""Generate proper-motion-parallax-separation.png in the current directory.

Use: make _media/proper-motion-parallax-separation.png
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Illustrative one-coordinate model: circular Earth orbit, full-amplitude annual
parallax projection, constant distance and proper motion, no other accelerations.
The plotted values are calculated, not catalogue observations.
"""

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 13, "savefig.facecolor": "white"})
    time = np.linspace(0, 3, 601)
    mu, parallax = 100.0, 50.0
    trend = mu * time
    annual = parallax * np.cos(2 * np.pi * time)
    observed = trend + annual
    sample_time = np.arange(0, 3.01, 0.5)
    sample_annual = parallax * np.cos(2 * np.pi * sample_time)
    fig, axes = plt.subplots(2, 1, figsize=(9.2, 7.3), sharex=True, facecolor="white")
    fig.subplots_adjust(left=0.13, right=0.97, top=0.81, bottom=0.13, hspace=0.43)
    fig.suptitle("Proper motion and parallax leave different signatures", fontsize=18, y=0.97)
    fig.text(0.5, 0.905, r"One angular coordinate: $\theta_0=0$, $\mu=100$ mas/year, $p=50$ mas ($d=20$ pc)",
             ha="center", fontsize=13)
    top, bottom = axes
    top.plot(time, observed, color="#2368ac", lw=2.8, label="Combined observed offset")
    top.plot(time, trend, color="#b85b15", lw=2.3, ls="--", label="Proper-motion trend: 100 t")
    top.scatter(sample_time, mu * sample_time + sample_annual,
                color="#2368ac", edgecolors="white", s=60, zorder=4)
    top.set(title="A. An annual wiggle riding on a steady drift",
            ylabel="Angular offset (mas)", ylim=(-25, 390))
    top.legend(loc="upper left", fontsize=11, framealpha=1)
    bottom.plot(time, annual, color="#453778", lw=2.8)
    bottom.scatter(sample_time, sample_annual, color="#453778", edgecolors="white", s=60, zorder=4)
    bottom.axhline(0, color="#777777", lw=1, ls="--")
    bottom.set(title="B. Subtract the trend: the annual projection repeats",
               ylabel="Residual (mas)", xlabel="Time from reference date (years)",
               xlim=(-0.04, 3.04), ylim=(-70, 85), yticks=[-50, 0, 50])
    bottom.annotate("+50 mas", xy=(2, 50), xytext=(2.18, 65), fontsize=12,
                    color="#453778", arrowprops={"arrowstyle": "-", "color": "#453778"})
    bottom.annotate("−50 mas", xy=(2.5, -50), xytext=(2.62, -61), fontsize=12,
                    color="#453778", arrowprops={"arrowstyle": "-", "color": "#453778"})
    for ax in axes:
        ax.set_facecolor("white")
        ax.grid(alpha=0.20)
        ax.spines[["top", "right"]].set_visible(False)
        ax.set_xticks(np.arange(0, 3.01, 0.5))
    fig.text(0.5, 0.035, "Illustrative circular-orbit projection; constant distance and proper motion; no other accelerations.",
             ha="center", fontsize=11)
    fig.savefig("proper-motion-parallax-separation.png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
