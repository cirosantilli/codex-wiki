"""Generate covariance-process-comparison.png in cwd.

Tested with Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Covariance matrices are exact; displayed paths are seeded finite simulations.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    rng = np.random.default_rng(20261012)
    n, paths = 12, 3
    independent = rng.normal(size=(paths, n))
    shared = np.repeat(rng.normal(size=(paths, 1)), n, axis=1)
    covariances = [np.eye(n), np.ones((n, n))]
    assert np.linalg.matrix_rank(covariances[0]) == n
    assert np.linalg.matrix_rank(covariances[1]) == 1
    assert np.all(np.diag(covariances[0]) == np.diag(covariances[1]))
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(2, 2, figsize=(10, 7.2), dpi=120, facecolor="white",
                             gridspec_kw={"height_ratios": [1, 1.1]})
    colors = ["#2878ad", "#c05a2a", "#24805e"]
    titles = [r"Independent $X_n$: fresh $N(0,1)$ at each time",
              r"Shared $Y_n=Z$: one $N(0,1)$ draw for all times"]
    for column, (values, covariance, title) in enumerate(zip([independent, shared], covariances, titles)):
        ax = axes[0, column]
        for j, color in enumerate(colors):
            ax.plot(np.arange(1, n + 1), values[j], "o-", color=color,
                    markersize=3, lw=1.2)
        ax.set(title=title, xlabel="Integer time n", ylabel="Observed value", ylim=(-3.1, 3.1))
        ax.axhline(0, color="gray", lw=0.7)
        ax.grid(alpha=0.15)
        ax = axes[1, column]
        im = ax.imshow(covariance, cmap="Blues", vmin=0, vmax=1,
                       origin="lower", extent=(0.5, n + 0.5, 0.5, n + 0.5))
        ax.set(title=[r"Exact covariance $C_X(m,n)=\mathbf{1}_{m=n}$",
                      r"Exact covariance $C_Y(m,n)=1$"][column], xlabel="n", ylabel="m")
        ax.set_xticks([1, 4, 8, 12])
        ax.set_yticks([1, 4, 8, 12])
    fig.subplots_adjust(left=0.075, right=0.9, bottom=0.105, top=0.88,
                        wspace=0.32, hspace=0.48)
    bar_ax = fig.add_axes((0.925, 0.14, 0.017, 0.3))
    fig.colorbar(im, cax=bar_ax, ticks=[0, 1], label="Covariance")
    fig.suptitle("Same distribution at every time, different dependence", fontsize=15, y=0.975)
    fig.text(0.5, 0.035,
             "Top: three simulated histories of each process (seed 20261012). Bottom: exact formulas.\n"
             "At every time both models have mean 0 and variance 1; their futures are very different.",
             ha="center", fontsize=9)
    fig.savefig(Path.cwd() / "covariance-process-comparison.png", facecolor="white", transparent=False)
    plt.close(fig)
    print("For distinct m,n: Var(X_n-X_m)=2, Var(Y_n-Y_m)=0")


if __name__ == "__main__":
    main()
