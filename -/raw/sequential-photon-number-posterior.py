"""Synthetic sequential Bayesian counting: deliberately not laboratory data.

Tested with Python 3.14, matplotlib 3.10.7, and numpy 2.3.5.
Run from _media; writes the matching PNG in the current directory.
No photon loss, a finite uniform prior, fixed hidden n, and independent meters.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def synthetic_record(count=96):
    numbers = np.arange(8)
    contrast, chi, fixed_n = .8, np.pi / 4, 3
    phases = np.resize(np.array([0., -np.pi / 4, -np.pi / 2, -3 * np.pi / 4]), count)
    rng = np.random.default_rng(73)
    outcomes = rng.random(count) < (1 + contrast * np.cos(phases + fixed_n * chi)) / 2
    history = [np.full(8, 1 / 8)]
    evidences = []
    for phase, outcome in zip(phases, outcomes):
        pe = (1 + contrast * np.cos(phase + numbers * chi)) / 2
        likelihood = pe if outcome else 1 - pe
        weighted = history[-1] * likelihood
        evidences.append(weighted.sum())
        history.append(weighted / weighted.sum())
    history = np.asarray(history)
    assert np.all(history >= 0)
    assert np.allclose(history.sum(axis=1), 1, atol=1e-14)
    return numbers, phases, outcomes, history, np.asarray(evidences)


def main():
    numbers, phases, outcomes, history, _ = synthetic_record()
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(10.4, 6.3), dpi=120, facecolor="white")
    grid = fig.add_gridspec(3, 1, height_ratios=[.65, 3.1, 1.65], hspace=.14)
    record, heat, lines = [fig.add_subplot(grid[i]) for i in range(3)]
    fig.suptitle("Synthetic photon counting · not laboratory data", fontsize=17, weight="bold", y=.97)
    record.scatter(np.arange(1, len(outcomes) + 1), outcomes, c=np.where(outcomes, "#b55f12", "#246aa5"),
                   marker="|", s=50, linewidths=1.4)
    record.set(yticks=[0, 1], yticklabels=["g", "e"], ylim=(-.4, 1.4), xlim=(-.5, len(outcomes) + .5))
    record.set_ylabel("Atom", rotation=0, labelpad=28, va="center")
    record.tick_params(axis="x", bottom=False, labelbottom=False)
    record.spines[["top", "right", "bottom"]].set_visible(False)
    im = heat.imshow(history.T, origin="lower", aspect="auto", cmap="Blues", vmin=0, vmax=1,
                     extent=(-.5, len(outcomes) + .5, -.5, 7.5), interpolation="nearest")
    heat.axhline(3, color="#b55f12", ls=":", lw=1.4)
    heat.set(yticks=numbers, ylabel="Photon number n")
    heat.tick_params(axis="x", labelbottom=False)
    heat.text(3, 6.65, "uniform prior → concentration near n = 3", color="#183047",
              bbox={"facecolor": "white", "edgecolor": "none", "alpha": .9}, fontsize=10.5)
    colors = ["#8c80b5", "#6c8797", "#499183", "#b55f12", "#b55a87", "#879d3c", "#355cac", "#7d7373"]
    for n, color in zip(numbers, colors):
        lines.plot(history[:, n], color=color, lw=2.3 if n == 3 else 1.1, label=f"n={n}")
    lines.set(xlim=(-.5, len(outcomes) + .5), ylim=(-.025, 1.025), ylabel="Posterior", xlabel="Detected atoms k")
    lines.spines[["top", "right"]].set_visible(False)
    lines.set_yticks([0, .5, 1])
    lines.grid(alpha=.18)
    lines.legend(loc="center right", ncol=4, fontsize=9, framealpha=.95)
    fig.subplots_adjust(left=.10, right=.87, top=.885, bottom=.125)
    color_ax = fig.add_axes([.895, .399, .018, .333])
    fig.colorbar(im, cax=color_ax, label="Posterior probability")
    fig.text(.5, .032, r"Uniform prior on 0…7; C=0.8; χ=π/4; phases 0, −π/4, −π/2, −3π/4 cycle. Fixed n=3; no loss.",
             ha="center", fontsize=9.5, color="#536574")
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
