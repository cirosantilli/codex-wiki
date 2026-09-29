"""Plot a beta-prior Bernoulli update to cwd; tested with Python 3.14.4.

Uses the repository's NumPy and Matplotlib dependencies. Prior and posterior
are densities; likelihood divided by its peak uses a separate labeled axis.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    theta = np.linspace(0, 1, 2001)
    prior = 6 * theta * (1 - theta)
    posterior = 2860 * theta**9 * (1 - theta)**3
    likelihood = theta**8 * (1 - theta)**2 / (0.8**8 * 0.2**2)
    fig, density = plt.subplots(figsize=(9.5, 5.3), dpi=120,
                                facecolor="white")
    relative = density.twinx()
    density.plot(theta, prior, color="#0072b2", lw=2.6,
                 label="Prior Beta(2, 2): density")
    density.plot(theta, posterior, color="#007c68", lw=2.8,
                 label="Posterior Beta(10, 4): density")
    relative.plot(theta, likelihood, color="#d55e00", lw=2.4,
                  linestyle="--", label="Likelihood / peak (right axis)")
    density.axvline(5 / 7, color="#007c68", lw=1.3, linestyle=":")
    density.annotate("Posterior mean = 5/7", xy=(5 / 7, 1.15),
                     xytext=(0.36, 0.65), fontsize=11, color="#007c68",
                     arrowprops={"arrowstyle": "->", "color": "#007c68"})
    density.set(xlim=(0, 1), ylim=(0, 4.5), xlabel="Unknown heads probability θ",
                ylabel="Prior / posterior probability density",
                title="8 heads + 2 tails: multiply by the prior, then normalize")
    relative.set(ylim=(0, 1.4), ylabel="Likelihood / peak — not a probability density")
    relative.tick_params(axis="y", colors="#a74700")
    relative.yaxis.label.set_color("#a74700")
    handles, labels = density.get_legend_handles_labels()
    other_handles, other_labels = relative.get_legend_handles_labels()
    density.legend(handles + other_handles, labels + other_labels,
                   loc="upper left", fontsize=10.5, framealpha=1)
    density.grid(color="#e6eaed")
    density.spines["top"].set_visible(False)
    relative.spines["top"].set_visible(False)
    fig.text(0.5, 0.045,
             "Each density has area 1 on the left scale. "
             "The dashed curve shows relative likelihood on the right scale.",
             ha="center", fontsize=10.5)
    fig.subplots_adjust(left=0.085, right=0.88, bottom=0.18, top=0.88)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
