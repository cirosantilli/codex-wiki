"""Plot the exact thermal response of one nondegenerate two-level unit.

Build with: make _media/two-level-thermal-response.png
Writes the same-basename, opaque white PNG to the current working directory.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def response(theta):
    """Return excited probability, C/k_B and S/k_B for theta=k_B T/Delta."""
    x = 1.0 / np.asarray(theta)
    weight = np.exp(-x)
    p = weight / (1.0 + weight)
    heat = x * x * p * (1.0 - p)
    entropy = np.log1p(weight) + x * p
    return p, heat, entropy


def main():
    theta = np.linspace(0.025, 3.0, 1500)
    p, heat, entropy = response(theta)
    x_example = np.log(3.0)
    theta_example = 1.0 / x_example
    p0, c0, s0 = response(theta_example)
    assert np.isclose(p0, 0.25)
    assert np.isclose(c0, 3.0 * x_example**2 / 16.0)
    assert np.isclose(s0, -0.75 * np.log(0.75) - 0.25 * np.log(0.25))

    # At the maximum, x*tanh(x/2)=2. Bisection uses only NumPy/stdlib.
    low, high = 2.0, 3.0
    for _ in range(60):
        mid = (low + high) / 2.0
        if mid * np.tanh(mid / 2.0) < 2.0:
            low = mid
        else:
            high = mid
    theta_peak = 2.0 / (low + high)
    _, heat_peak, _ = response(theta_peak)
    assert np.isclose(theta_peak, 0.4167782798)
    assert np.isclose(heat_peak, 0.4392288399)

    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, axes = plt.subplots(1, 3, figsize=(10.0, 4.4), dpi=120)
    fig.subplots_adjust(left=0.07, right=0.98, bottom=0.20, top=0.77, wspace=0.38)
    fig.suptitle("One two-level unit in a heat bath", fontsize=16, y=0.97)
    fig.text(0.5, 0.86, r"Energies $0,\Delta$  |  $\Delta>0$ fixed  |  Dashed line: $\beta\Delta=\ln 3$",
             ha="center")
    curves = [(p, p0, "#236a9e", r"$p=U/\Delta$", "Excited population", 0.56),
              (heat, c0, "#bd582b", r"$C/k_B$", "Heat capacity", 0.52),
              (entropy, s0, "#277953", r"$S/k_B$", "Entropy", 0.79)]
    for ax, (values, value0, color, ylabel, title, ymax) in zip(axes, curves):
        ax.plot(theta, values, lw=2.6, color=color)
        ax.axvline(theta_example, color="#666666", lw=1, ls="--")
        ax.scatter([theta_example], [value0], color=color, zorder=4)
        ax.set(xlim=(0, 3), ylim=(0, ymax), xlabel=r"$k_B T/\Delta$",
               ylabel=ylabel, title=title)
        ax.grid(alpha=0.15)
    axes[0].axhline(0.5, lw=1.1, ls=":", color="#236a9e")
    axes[0].text(1.52, 0.515, "Limit: 1/2", fontsize=10)
    axes[1].scatter([theta_peak], [heat_peak], color="#bd582b", zorder=4)
    axes[1].annotate("Peak: 0.4392", (theta_peak, heat_peak), xytext=(1.1, 0.44),
                     fontsize=10, arrowprops={"arrowstyle": "->", "color": "#555555"})
    axes[2].axhline(np.log(2), lw=1.1, ls=":", color="#277953")
    axes[2].text(1.45, 0.71, r"Limit: $\ln 2$", fontsize=10)
    fig.text(0.5, 0.055, r"At $\beta\Delta=\ln 3$:  $p=0.25$,  $C/k_B=0.2263$,  $S/k_B=0.5623$",
             ha="center", fontsize=11)
    fig.savefig(Path.cwd() / "two-level-thermal-response.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
