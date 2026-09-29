"""Plot a first-order response and its finite convolution history; PNG to cwd.

Tested with Python 3.14, matplotlib 3.10.7, and numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def response(time):
    return -np.expm1(-2 * np.asarray(time)) / 2


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    fig, (left, right) = plt.subplots(
        1, 2, figsize=(10.4, 4.6), dpi=120, facecolor="white"
    )
    time = np.linspace(0, 3, 1001)
    left.plot(time, np.exp(-2 * time), color="#bd7024", linewidth=2.5,
              label=r"Kernel $h(t)=e^{-2t}$")
    left.plot(time, response(time), color="#207699", linewidth=2.8,
              label=r"Response $y(t)=(1-e^{-2t})/2$")
    left.axhline(0.5, color="#858585", linestyle="--", linewidth=1.1)
    left.text(2.96, 0.52, "Limiting response: 1/2", ha="right", fontsize=10)
    snapshot = 1.0
    amount = float(response(snapshot))
    left.scatter([snapshot], [amount], color="#207699", s=45, zorder=4)
    left.annotate(f"y(1) = {amount:.4f}", xy=(snapshot, amount),
                  xytext=(1.3, 0.22), fontsize=10,
                  arrowprops={"arrowstyle": "->", "color": "#207699"})
    left.set(title=r"Unit input: $y'+2y=1$, $y(0)=0$",
             xlabel="Time t", ylabel="Kernel and response values",
             xlim=(0, 3), ylim=(0, 1.25))
    left.legend(loc="upper right", frameon=False, fontsize=10)

    history = np.linspace(0, snapshot, 601)
    contributions = np.exp(-2 * (snapshot - history))
    right.fill_between(history, 0, contributions, color="#207699", alpha=0.2)
    right.plot(history, contributions, color="#207699", linewidth=2.8,
               label=r"$h(1-\tau)f(\tau)=e^{-2(1-\tau)}$")
    right.axvline(snapshot, color="#858585", linestyle="--", linewidth=1.1)
    right.axvspan(snapshot, 1.35, color="#ededed", zorder=0)
    right.text(0.97, 0.25, f"Shaded integral\n= y(1) = {amount:.4f}",
               transform=right.transAxes, ha="right", fontsize=11,
               bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.9})
    right.text(1.175, 0.86, "Future\ninput\nexcluded", ha="center", fontsize=10,
               color="#595959")
    right.text(0.03, 0.08, "Older input", fontsize=10, color="#595959")
    right.text(0.96, 1.045, "Recent input", ha="right", fontsize=10, color="#595959")
    right.set(title=r"At $t=1$: integrate only $0\leq\tau\leq1$",
              xlabel=r"Input time $\tau$", ylabel="Contribution per unit input time",
              xlim=(0, 1.35), ylim=(0, 1.25), xticks=[0, 0.5, 1])
    right.legend(loc="upper left", frameon=False, fontsize=10)
    for ax in (left, right):
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(axis="y", color="#e5e9eb", linewidth=0.7)
        ax.set_axisbelow(True)
    fig.subplots_adjust(left=0.075, right=0.975, bottom=0.15, top=0.89, wspace=0.29)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
