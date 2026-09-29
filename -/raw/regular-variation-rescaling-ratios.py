"""Generate regular-variation-rescaling-ratios.png in the current directory."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False})
    t = np.geomspace(10, 1e8, 450)
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 4.7), dpi=120,
                             facecolor="white")
    left, right = axes
    left.loglog(t, t**2, color="#2875ad", linewidth=2.3, label=r"$q(t)=t^2$")
    left.loglog(t, t**2 * np.log(t), color="#d4652b", linewidth=2.3,
                label=r"$q(t)=t^2\log t$")
    left.set(xlabel=r"Argument $t$", ylabel=r"Value $q(t)$",
             title="The correction keeps growing")
    left.legend(loc="upper left", fontsize=11)
    right.semilogx(t, np.full_like(t, 4), color="#2875ad", linewidth=2.3,
                  label=r"$t^2$: ratio exactly $4$")
    right.semilogx(t, 4 * (1 + np.log(2) / np.log(t)), color="#d4652b",
                  linewidth=2.3, label=r"$t^2\log t$: ratio $\to4$")
    sample_t = np.array([1e2, 1e4, 1e6])
    sample_y = 4 * (1 + np.log(2) / np.log(sample_t))
    right.scatter(sample_t, sample_y, color="#d4652b", s=32, zorder=3)
    for x, y in zip(sample_t, sample_y):
        right.annotate(f"{y:.3f}", (x, y), xytext=(3, 8),
                       textcoords="offset points", fontsize=10)
    right.set(xlabel=r"Argument $t$", ylabel=r"Doubling ratio $q(2t)/q(t)$",
              ylim=(3.9, 5.4), title="The scaling exponent stays the same")
    right.legend(loc="upper right", fontsize=10)
    for ax in axes:
        ax.grid(alpha=0.2)
    fig.suptitle("Regular variation: a power law with a changing correction",
                 fontsize=15, y=0.98)
    fig.subplots_adjust(left=0.08, right=0.98, bottom=0.19, top=0.82, wspace=0.33)
    fig.text(0.5, 0.04, "Each doubling ratio uses the same fixed rescaling u = 2.",
             ha="center", fontsize=11)
    fig.savefig(Path.cwd() / "regular-variation-rescaling-ratios.png",
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
