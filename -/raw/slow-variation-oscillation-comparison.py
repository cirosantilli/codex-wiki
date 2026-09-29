"""Generate slow-variation-oscillation-comparison.png in the current directory."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    s = np.linspace(2, 40, 1200)
    shift = np.pi / 2
    slow = np.exp(np.sin(np.log(s)))
    fast = 2 + np.sin(s)
    slow_ratio = np.exp(np.sin(np.log(s + shift)) - np.sin(np.log(s)))
    fast_ratio = (2 + np.sin(s + shift)) / fast
    fig, axes = plt.subplots(2, 2, figsize=(10.2, 6.5), dpi=120,
                             facecolor="white", sharex=True)
    axes[0, 0].plot(s, slow, color="#2875ad", linewidth=2.2)
    axes[0, 1].plot(s, fast, color="#d4652b", linewidth=2.2)
    axes[0, 0].set(title=r"$\ell(t)=\exp(\sin(\log\log t))$",
                   ylabel="Function value", ylim=(0.2, 3.2))
    axes[0, 1].set(title=r"$h(t)=2+\sin(\log t)$", ylim=(0.2, 3.2))
    axes[1, 0].plot(s, slow_ratio, color="#2875ad", linewidth=2.2)
    axes[1, 1].plot(s, fast_ratio, color="#d4652b", linewidth=2.2)
    axes[1, 0].set(ylabel=r"Rescaling ratio $\ell(ut)/\ell(t)$",
                   xlabel=r"Logarithmic input $s=\log t$")
    axes[1, 1].set(ylabel=r"Rescaling ratio $h(ut)/h(t)$",
                   xlabel=r"Logarithmic input $s=\log t$")
    for ax in axes[1]:
        ax.axhline(1, color="#555555", linestyle="--", linewidth=1.1)
        ax.set_ylim(0.25, 2.8)
    for ax in axes.flat:
        ax.grid(alpha=0.2)
        ax.set_xlim(2, 40)
    fig.suptitle("Oscillation can be compatible with slow variation",
                 fontsize=15, y=0.98)
    fig.subplots_adjust(left=0.09, right=0.98, bottom=0.23, top=0.87,
                        wspace=0.30, hspace=0.26)
    fig.text(0.5, 0.035,
             "Fixed u = exp(π/2).  Left ratio → 1; right ratio keeps oscillating.\n"
             "Neither function converges.  A finite plot illustrates, rather than proves, the limits.",
             ha="center", fontsize=11, linespacing=1.5)
    fig.savefig(Path.cwd() / "slow-variation-oscillation-comparison.png",
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
