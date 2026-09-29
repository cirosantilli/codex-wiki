"""Draw directional rates and exact versus linear finite changes.

Original quadratic model, not measurements. Tested with Python 3.14,
NumPy 2.3.5 and Matplotlib 3.10.7. Output basename.png to the CWD.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    fig, (left, right) = plt.subplots(1, 2, figsize=(11.4, 4.7), dpi=120)
    fig.patch.set_facecolor("white")
    degrees = np.linspace(0, 360, 721)
    theta = np.deg2rad(degrees)
    rates = 3 * np.cos(theta) + 5 * np.sin(theta)
    left.plot(degrees, rates, color="#2166ac", linewidth=2.5)
    left.axhline(0, color="#999999", linewidth=1)
    peak_angle = np.rad2deg(np.arctan2(5, 3))
    sample_angle = np.rad2deg(np.arctan2(4, 3))
    left.scatter([sample_angle, peak_angle], [5.8, np.sqrt(34)],
                 color=["#c65102", "#238b45"], s=48, zorder=5)
    left.annotate("u = (3/5, 4/5)\nrate = 5.8", (sample_angle, 5.8),
                  xytext=(7, 2.3), fontsize=10,
                  arrowprops={"arrowstyle": "->", "color": "#c65102"})
    left.annotate(r"Maximum: $\sqrt{34}$" + "\n" + r"$u=(3,5)/\sqrt{34}$",
                  (peak_angle, np.sqrt(34)), xytext=(135, 3.6), fontsize=11,
                  arrowprops={"arrowstyle": "->", "color": "#238b45"})
    left.set(xlabel="Unit-direction angle θ (degrees)", ylabel="Rate per unit input distance",
             title=r"$D_u f = 3\cos\theta + 5\sin\theta$",
             xlim=(0, 360), ylim=(-6.6, 6.7), xticks=[0, 90, 180, 270, 360])
    left.grid(alpha=0.2)

    scales = np.linspace(0, 1, 201)
    exact = 0.01 * scales + 0.0004 * scales**2
    linear = 0.01 * scales
    # Milliscale output makes the small discrepancy readable without changing
    # the model: 10 means a height change of 0.010.
    right.plot(scales, 1000*exact, color="#2166ac", linewidth=2.6,
               label=r"Exact: $0.01s+0.0004s^2$")
    right.plot(scales, 1000*linear, color="#c65102", linewidth=2, linestyle="--",
               label="Linear: 0.01s")
    for s in [0.5, 1.0]:
        right.scatter([s], [1000*(0.01*s+0.0004*s*s)], color="#2166ac", s=35, zorder=5)
        right.vlines(s, 10*s, 10*s+0.4*s*s, color="#333333", linewidth=1.3)
    right.annotate("At s = 1:\nΔf = 0.0104\ndf = 0.0100", (1, 10.4),
                   xytext=(0.5, 7.8), fontsize=11,
                   arrowprops={"arrowstyle": "->", "color": "#333333"})
    right.text(0.05, 0.74, "At s = 1/2:\nerror = 0.0001\n(one quarter of 0.0004)",
               transform=right.transAxes, fontsize=10,
               bbox={"facecolor": "white", "edgecolor": "#cccccc", "alpha": 0.97})
    right.set(xlabel="Displacement scale s", ylabel="Height change × 1000",
              title=r"$h=s(0.02,-0.01)$", xlim=(0, 1.04), ylim=(0, 11.2))
    right.grid(alpha=0.2)
    right.legend(loc="lower right", fontsize=10)
    fig.suptitle(r"Direction and local approximation: $f=x^2+xy+2y^2$ at $(1,1)$", fontsize=16)
    fig.subplots_adjust(left=0.065, right=0.985, bottom=0.15, top=0.81, wspace=0.31)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
