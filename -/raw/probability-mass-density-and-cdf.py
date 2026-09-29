"""Render discrete masses, a continuous density, and their CDFs to cwd."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def discrete_cdf(x):
    values = np.array([0., 1., 3.])
    masses = np.array([.2, .5, .3])
    return ((np.asarray(x)[..., None] >= values) * masses).sum(axis=-1)


def main():
    values = np.array([0., 1., 3.])
    masses = np.array([.2, .5, .3])
    assert np.isclose(masses.sum(), 1)
    assert np.isclose(discrete_cdf(1) - discrete_cdf(0), .5)
    assert np.isclose(discrete_cdf(1), .7)
    assert np.isclose(discrete_cdf(np.nextafter(1, 0)), .2)
    assert np.isclose(.75**2 - .25**2, .5)
    assert np.isclose(.9**2 - .7**2, .32)
    y = np.linspace(0, 1, 1001)
    assert np.isclose(np.trapezoid(2*y, y), 1)
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    fig, axes = plt.subplots(2, 2, figsize=(11.6, 8.2), dpi=120, facecolor="white")
    mass, density, discrete, continuous = axes.ravel()
    mass.vlines(values, 0, masses, color="#246ea0", lw=3)
    mass.scatter(values, masses, color="#246ea0", s=65, zorder=4)
    for value, probability in zip(values, masses):
        mass.text(value, probability+.025, f"{probability:.1f}", ha="center", color="#246ea0")
    mass.set(xlim=(-.4, 3.6), ylim=(-.025, .6), title="Discrete X: probability at a point",
             xlabel="Outcome x", ylabel="Probability mass")
    mass.set_xticks(values, ["0", "1", "3"])
    density.plot(y, 2*y, color="#2c8467", lw=3, label=r"$f_Y(y)=2y$")
    interval = np.linspace(.25, .75, 200)
    density.fill_between(interval, 0, 2*interval, color="#2c8467", alpha=.22)
    density.text(.12, 1.75, "Shaded probability = 0.5", color="#20614c", fontsize=12)
    density.annotate("Height = 1.6", xy=(.8, 1.6), xytext=(.05, 1.1), color="#20614c",
                     arrowprops={"arrowstyle": "->", "color": "#20614c"}, fontsize=11,
                     bbox={"facecolor": "white", "edgecolor": "none", "alpha": .9})
    density.scatter([.8], [1.6], color="#2c8467", s=45, zorder=4)
    density.set(xlim=(0, 1.04), ylim=(0, 2.1), title="Continuous Y: probability is area",
                xlabel="Outcome y", ylabel="Probability density")
    levels = [0, .2, .7, 1]
    edges = [-.4, 0, 1, 3, 3.6]
    for left, right, height in zip(edges[:-1], edges[1:], levels):
        discrete.plot([left, right], [height, height], color="#246ea0", lw=2.8)
    for i, value in enumerate(values):
        discrete.plot([value, value], [levels[i], levels[i+1]], color="#a7b5bf", linestyle=":", lw=1)
        discrete.scatter([value], [levels[i]], facecolor="white", edgecolor="#246ea0", s=55, zorder=5)
        discrete.scatter([value], [levels[i+1]], color="#246ea0", s=55, zorder=5)
    discrete.text(1.2, .39, "Jump at 1 = 0.5", color="#246ea0", fontsize=12)
    discrete.set(xlim=(-.4, 3.6), ylim=(-.045, 1.08), title="Discrete CDF: include each jump's upper value",
                 xlabel="Threshold x", ylabel=r"$F_X(x)=P(X\leq x)$")
    discrete.set_xticks(values, ["0", "1", "3"])
    continuous.plot(y, y*y, color="#2c8467", lw=3)
    continuous.scatter([.25, .75], [.25**2, .75**2], color="#2c8467", s=60, zorder=4)
    for value in [.25, .75]:
        continuous.plot([value, value], [0, value*value], color="#9aacb4", linestyle=":", lw=1)
    continuous.annotate("CDF increase = 0.5", xy=(.75, .75**2), xytext=(.10, .83), color="#20614c",
                        arrowprops={"arrowstyle": "->", "color": "#20614c"}, fontsize=12)
    continuous.set(xlim=(0, 1.04), ylim=(-.03, 1.08), title="Continuous CDF: accumulated area",
                   xlabel="Threshold y", ylabel=r"$F_Y(y)=y^2$ on $[0,1]$")
    for ax in axes.ravel():
        ax.grid(color="#e6eaed")
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Two probability laws, two ways to accumulate probability", fontsize=16, y=.985)
    fig.text(.5, .025, "Point probabilities are jumps; density heights contribute through integration",
             ha="center", fontsize=12)
    fig.subplots_adjust(left=.075, right=.975, bottom=.115, top=.9, hspace=.42, wspace=.28)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
