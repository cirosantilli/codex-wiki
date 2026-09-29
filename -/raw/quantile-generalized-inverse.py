"""Show generalized inverse CDFs with jump conventions; output a PNG to cwd."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def quantile_x(p):
    return np.array([0., 1., 3.])[np.searchsorted([.2, .7, 1.], p, side="left")]


def main():
    levels = np.array([.1, .5, .9])
    assert np.array_equal(quantile_x(levels), [0, 1, 3])
    assert quantile_x(.2) == 0 and quantile_x(.7) == 1
    # A deterministic uniform grid illustrates probability-band widths, not IID sampling.
    grid = (np.arange(1000) + .5) / 1000
    counts = [np.count_nonzero(quantile_x(grid) == outcome) for outcome in [0, 1, 3]]
    assert counts == [200, 500, 300]
    assert np.allclose(np.sqrt(levels)**2, levels)
    assert np.isclose(np.sqrt(.5), 1/np.sqrt(2))
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    fig, (discrete, continuous) = plt.subplots(1, 2, figsize=(11, 5.5), dpi=120, facecolor="white")
    colors = ["#396c99", "#298268", "#b67a2e"]
    bands = [(0, .2, 0), (.2, .7, 1), (.7, 1, 3)]
    for (left, right, outcome), color in zip(bands, colors):
        discrete.axvspan(left, right, color=color, alpha=.08)
        discrete.plot([left, right], [outcome, outcome], color=color, lw=3)
        discrete.scatter([left], [outcome], facecolor="white", edgecolor=color, s=55, zorder=5)
        discrete.scatter([right], [outcome], facecolor=color if right < 1 else "white",
                         edgecolor=color, s=55, zorder=5)
        discrete.text((left+right)/2, 3.55, f"Width {right-left:.1f}", ha="center", color=color, fontsize=11)
    for level, output in zip(levels, quantile_x(levels)):
        discrete.plot([level, level], [-.32, output], color="#a0aeb8", linestyle=":", lw=1)
        discrete.scatter([level], [output], color="#283a46", s=42, zorder=6)
    discrete.set(xlim=(-.025, 1.025), ylim=(-.38, 3.9), title="Quantiles of the three-value law",
                 xlabel="Probability level p", ylabel=r"Outcome $Q_X(p)$")
    discrete.set_yticks([0, 1, 3])
    p = np.linspace(0, 1, 800)
    continuous.plot(p, np.sqrt(p), color="#298268", lw=3)
    for level, output, color in zip(levels, np.sqrt(levels), colors):
        continuous.plot([level, level], [0, output], color="#a0aeb8", linestyle=":", lw=1)
        continuous.scatter([level], [output], color=color, s=60, zorder=5)
    continuous.scatter([0, 1], [0, 1], facecolor="white", edgecolor="#298268", s=55, zorder=6)
    continuous.annotate(r"$Q_Y(0.5)=1/\sqrt{2}$" + "\n≈ 0.70710678", xy=(.5, np.sqrt(.5)),
                        xytext=(.04, .87), fontsize=12, color="#20614c",
                        arrowprops={"arrowstyle": "->", "color": "#20614c"},
                        bbox={"facecolor": "white", "edgecolor": "none", "alpha": .9})
    continuous.set(xlim=(-.025, 1.025), ylim=(-.04, 1.08), title=r"For $F_Y(y)=y^2$: $Q_Y(p)=\sqrt{p}$",
                   xlabel="Probability level p", ylabel=r"Outcome $Q_Y(p)$")
    for ax in (discrete, continuous):
        ax.set_xticks([0, .1, .2, .5, .7, .9, 1])
        ax.grid(color="#e6eaed")
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Quantiles choose the first outcome reaching a probability level", fontsize=16, y=.985)
    fig.text(.5, .042, "A uniform draw lands in each probability band with that band's width",
             ha="center", fontsize=12)
    fig.subplots_adjust(left=.065, right=.98, bottom=.20, top=.82, wspace=.25)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
