"""Plot exact birthday and fixed-target probabilities in an ideal toy model.

Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python ../hash-collision-birthday-versus-target.py
Writes this script's basename as an opaque white PNG to the current directory.
Tested with Python 3.14.4, Matplotlib 3.10.7; no simulation or measured data.
"""

import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def collision_probability(m, n):
    """Exact formula, evaluated stably with log1p and expm1."""
    if n > m:
        return 1.0
    return -math.expm1(sum(math.log1p(-j / m) for j in range(n)))


def target_probability(m, n):
    return -math.expm1(n * math.log1p(-1 / m)) if m > 1 else float(n > 0)


def main():
    m = 256
    n = list(range(m + 1))
    exact = [collision_probability(m, k) for k in n]
    target = [target_probability(m, k) for k in n]
    approximation = [-math.expm1(-k * (k - 1) / (2 * m)) for k in n]
    collision_half = next(k for k, p in enumerate(exact) if p >= 0.5)
    target_half = next(k for k, p in enumerate(target) if p >= 0.5)
    assert (collision_half, target_half) == (20, 178)
    assert exact[0] == exact[1] == 0.0
    assert all(a <= b for a, b in zip(exact, exact[1:]))
    assert all(a <= b + 1e-15 for a, b in zip(approximation, exact))

    teal, orange, purple, gray = "#146a77", "#b85419", "#7458a5", "#586470"
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(9, 5.2), dpi=120)
    fig.subplots_adjust(left=0.095, right=0.97, bottom=0.2, top=0.77, wspace=0.31)
    fig.suptitle("Many possible pairs versus one fixed target", fontsize=16, y=0.96)
    fig.text(0.5, 0.89, "M = 256 outputs; distinct queried keys; independent uniform hash values",
             ha="center", fontsize=12)
    left, right = axes
    left.plot(n[:49], exact[:49], color=teal, linewidth=2.5, label="Exact any-pair probability")
    left.plot(n[:49], approximation[:49], color=orange, linewidth=2,
              linestyle="--", label="Exponential approximation")
    left.set(title="The birthday transition", xlim=(0, 48))
    left.legend(loc="lower right", fontsize=9, frameon=False)
    right.plot(n, exact, color=teal, linewidth=2.5, label="Any equal pair")
    right.plot(n, target, color=purple, linewidth=2.5, label="Hit a fixed target")
    right.set(title="The two search tasks", xlim=(0, 256))
    right.legend(loc="lower right", fontsize=10, frameon=False)
    for ax in axes:
        ax.set(ylim=(0, 1.03), xlabel="Number of distinct queries n", ylabel="Probability")
        ax.axhline(0.5, color=gray, linewidth=1, linestyle=":")
        ax.set_yticks([0, 0.25, 0.5, 0.75, 1], ["0%", "25%", "50%", "75%", "100%"])
        ax.grid(alpha=0.15)
        ax.spines[["top", "right"]].set_visible(False)
    left.scatter([19, 20], [exact[19], exact[20]], color=teal, s=28, zorder=5)
    left.annotate("19: 49.6%\n20: 53.3%", (20, exact[20]), xytext=(5, 0.77),
                  arrowprops={"arrowstyle": "->", "color": gray}, fontsize=10, color=gray)
    for k, values, color, position in [(20, exact, teal, (47, 0.65)),
                                        (178, target, purple, (142, 0.3))]:
        right.scatter([k], [values[k]], color=color, s=34, zorder=5)
        right.annotate(f"First at least 50%:\nn = {k}", (k, values[k]), xytext=position,
                       arrowprops={"arrowstyle": "->", "color": color}, color=color, fontsize=10)
    fig.text(0.5, 0.075, "Computed toy-model curves, not measurements or a security claim for a real hash.",
             ha="center", fontsize=11, color=gray)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
