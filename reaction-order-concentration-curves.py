"""Compare normalized single-species decays and their linearizing plots.

Zero-order conversion stops at depletion; its ODE applies only beforehand.
Writes reaction-order-concentration-curves.png to the current working directory.
Tested with Python 3.14.4, NumPy 2.3.5, and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    tau = np.linspace(0.0, 4.0, 2001)
    zero = np.maximum(1.0 - tau, 0.0)
    first = np.exp(-tau)
    second = 1.0 / (1.0 + tau)
    pre = np.linspace(0.0, 0.999, 1000)

    assert np.all(zero >= 0.0) and np.all(zero[tau >= 1.0] == 0.0)
    assert np.allclose(-np.gradient(1.0 - pre, pre), 1.0)
    assert np.allclose(-np.gradient(first, tau)[1:-1], first[1:-1], rtol=1e-6)
    assert np.allclose(-np.gradient(second, tau)[1:-1], second[1:-1] ** 2, rtol=5e-6)
    assert np.allclose(np.log(first), -tau)
    assert np.allclose(1.0 / second, 1.0 + tau)
    assert np.allclose([1.0 - 0.5, np.exp(-np.log(2.0)), 1.0 / (1.0 + 1.0)], 0.5)
    # The dimensionful and rescaled solutions agree for each order's own k.
    initial = 2.5
    for order, coefficient in [(0, 0.3), (1, 0.2), (2, 0.08)]:
        time = tau / (coefficient * initial ** (order - 1))
        if order == 0:
            dimensionful = np.maximum(initial - coefficient * time, 0.0)
            normalized = zero
        elif order == 1:
            dimensionful = initial * np.exp(-coefficient * time)
            normalized = first
        else:
            dimensionful = initial / (1.0 + coefficient * initial * time)
            normalized = second
        assert np.allclose(dimensionful / initial, normalized)

    plt.rcParams.update({
        "font.size": 12, "figure.facecolor": "white", "axes.facecolor": "white",
        "savefig.facecolor": "white", "axes.spines.top": False,
        "axes.spines.right": False,
    })
    fig = plt.figure(figsize=(9.0, 6.0), dpi=120)
    grid = fig.add_gridspec(2, 3, height_ratios=[1.5, 1], hspace=0.65, wspace=0.40)
    fig.subplots_adjust(left=0.08, right=0.97, bottom=0.15, top=0.82)
    top = fig.add_subplot(grid[0, :])
    axes = [fig.add_subplot(grid[1, column]) for column in range(3)]
    blue, orange, green, gray = "#236a9e", "#bc542c", "#257653", "#666666"
    fig.suptitle("Reaction order changes the shape of concentration decay", fontsize=15, y=0.97)
    fig.text(0.5, 0.90, r"$X=[\mathrm{A}]/A_0$,  $\tau=kA_0^{n-1}t$: each order uses its own time scale",
             ha="center", fontsize=11)
    top.plot(tau, zero, color=blue, lw=2.5, label=r"Zero: $X=\max(1-\tau,0)$")
    top.plot(tau, first, color=orange, lw=2.5, ls="--", label=r"First: $X=e^{-\tau}$")
    top.plot(tau, second, color=green, lw=2.5, ls="-.", label=r"Second: $X=1/(1+\tau)$")
    top.scatter([1.0], [0.0], color=blue, s=35, zorder=4)
    top.annotate("Zero-order depletion: stop here", xy=(1.0, 0.0), xytext=(1.6, 0.12),
                 color=blue, fontsize=10, arrowprops={"arrowstyle": "->", "color": blue})
    top.set(xlabel=r"Rescaled time $\tau$", ylabel=r"Remaining fraction $X$",
            xlim=(0, 4), ylim=(-0.03, 1.03))
    top.legend(loc="upper right", frameon=False, fontsize=10)
    axes[0].plot(pre, 1.0 - pre, color=blue, lw=2.5)
    axes[0].scatter([1.0], [0.0], edgecolor=blue, facecolor="white", s=35, zorder=4)
    axes[0].set(title="Zero order: before depletion", xlabel=r"$\tau$", ylabel=r"$X$",
                xlim=(0, 1.05), ylim=(-0.05, 1.05))
    axes[0].text(0.1, 0.10, "Slope −1", transform=axes[0].transAxes, color=blue, fontsize=11)
    axes[1].plot(tau, np.log(first), color=orange, lw=2.5)
    axes[1].set(title="First order", xlabel=r"$\tau$", ylabel=r"$\ln X$",
                xlim=(0, 4), ylim=(-4.2, 0.2))
    axes[1].text(0.1, 0.10, "Slope −1", transform=axes[1].transAxes, color=orange, fontsize=11)
    axes[2].plot(tau, 1.0 / second, color=green, lw=2.5)
    axes[2].set(title="Second order", xlabel=r"$\tau$", ylabel=r"$1/X$",
                xlim=(0, 4), ylim=(0.8, 5.2))
    axes[2].text(0.1, 0.80, "Slope +1", transform=axes[2].transAxes, color=green, fontsize=11)
    for axis in [top, *axes]:
        axis.grid(alpha=0.16)
        axis.tick_params(labelsize=10)
        axis.set_title(axis.get_title(), fontsize=11, pad=10)
    fig.text(0.5, 0.045, "Matching transforms give straight lines; the zero-order law ends at depletion.",
             ha="center", fontsize=11, color=gray)
    fig.savefig(Path.cwd() / "reaction-order-concentration-curves.png", transparent=False)
    plt.close(fig)
    print("At tau=1: X_zero=0, X_first=0.367879441, X_second=0.5.")
    print("Half-concentration tau: zero=0.5; first=0.693147181; second=1.")
    print("Checks passed: depletion, differential rates, linearizing transforms, dimensionful rescaling.")


if __name__ == "__main__":
    main()
