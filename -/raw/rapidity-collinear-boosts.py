"""Equal collinear rapidities and velocities approaching the light-speed limit.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Writes an opaque white PNG to the current working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    n = np.arange(9)
    alpha = 0.5 * np.log(3.0)
    theta = n * alpha
    beta = np.tanh(theta)
    blue, purple = "#176b9c", "#74418b"
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.6), dpi=120)
    fig.patch.set_facecolor("white")
    ax = axes[0]
    ax.plot(n, theta, "o-", color=purple, lw=2.4, markersize=5)
    ax.set(ylabel=r"Rapidity $\theta_n$", ylim=(-0.15, 4.8),
           title=r"Rapidities add: $\theta_n=n\alpha$")
    ax.text(0.08, 0.87, r"$\alpha=\frac{1}{2}\ln 3\approx0.5493$",
            transform=ax.transAxes, color=purple, fontsize=12)
    ax.annotate(r"Each step adds $\alpha$", (4, theta[4]),
                xytext=(0.6, 3.2), fontsize=11, color=purple,
                arrowprops={"arrowstyle": "->", "color": purple})
    ax = axes[1]
    ax.plot(n, beta, "o-", color=blue, lw=2.4, markersize=5)
    ax.axhline(1, color="0.3", ls="--", lw=1.3)
    ax.text(0.25, 1.035, r"Light-speed limit $u/c=1$", fontsize=10)
    ax.set(ylabel=r"Velocity $u_n/c$", ylim=(-0.05, 1.15),
           title=r"Velocities saturate: $u_n/c=\tanh(n\alpha)$")
    for index, label, offset in [
        (1, r"$1/2$", (8, -15)),
        (2, r"$4/5$", (8, -17)),
        (3, r"$13/14$", (8, -22)),
    ]:
        ax.annotate(label, (index, beta[index]), xytext=offset,
                    textcoords="offset points", fontsize=10, color=blue)
    ax.annotate(r"$u_8/c=3280/3281$" + "\n" + r"$\approx0.99969521<1$",
                (8, beta[8]), xytext=(3.9, 0.53), fontsize=11, color=blue,
                arrowprops={"arrowstyle": "->", "color": blue})
    for ax in axes:
        ax.set_facecolor("white")
        ax.set(xlabel="Number of collinear boosts n", xlim=(-0.2, 8.3))
        ax.set_xticks(n)
        ax.grid(alpha=0.16)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Repeated relative velocities of 0.5c, starting from rest",
                 fontsize=14)
    fig.text(0.5, 0.025,
             "Each step is measured relative to the preceding rest frame.  "
             "The boost count is not elapsed time.", ha="center", fontsize=10)
    fig.tight_layout(rect=(0, 0.06, 1, 0.93), w_pad=2.5)
    fig.savefig(Path.cwd() / "rapidity-collinear-boosts.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
