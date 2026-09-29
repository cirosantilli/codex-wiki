"""Fixed-resistance current and Joule heating power; opaque PNG to CWD.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    resistance = 2.0
    voltage = np.linspace(0, 6, 301)
    current = voltage / resistance
    power = voltage * current
    example_v = 5.0
    example_i = example_v / resistance
    example_p = example_v * example_i
    blue, orange = "#2268a5", "#bd5a22"
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.8, 5.2), dpi=100)
    left.plot(voltage, current, color=blue, linewidth=2.6,
              label=r"$I=V/R$")
    right.plot(voltage, power, color=orange, linewidth=2.6,
               label=r"$P=VI=V^2/R$")
    for ax, value, color in [(left, example_i, blue), (right, example_p, orange)]:
        ax.plot([example_v, example_v], [0, value], linestyle="--", color=color,
                linewidth=1.3, alpha=0.6)
        ax.plot([0, example_v], [value, value], linestyle="--", color=color,
                linewidth=1.3, alpha=0.6)
        ax.scatter([example_v], [value], s=60, color=color, zorder=5)
        ax.set(xlim=(0, 6), xlabel="Terminal potential difference V (V)")
        ax.set_xticks(np.arange(7))
        ax.grid(alpha=0.18)
        ax.spines[["top", "right"]].set_visible(False)
        ax.legend(loc="upper left", frameon=False)
    left.set(ylabel="Current I (A)", ylim=(0, 3.3))
    right.set(ylabel="Joule heating power P (W)", ylim=(0, 20))
    left.set_title("Current grows linearly", fontsize=13, weight="bold", pad=12)
    right.set_title("Heating power grows quadratically", fontsize=13,
                    weight="bold", pad=12)
    left.annotate("5 V, 2.5 A", (example_v, example_i), xytext=(-78, 15),
                  textcoords="offset points", color=blue, weight="bold")
    right.annotate("5 V, 12.5 W", (example_v, example_p), xytext=(-112, 12),
                   textcoords="offset points", color=orange, weight="bold")
    fig.suptitle("Ohm's law and Joule heating for R = 2 ohms", fontsize=16,
                 weight="bold", y=0.97)
    fig.text(0.5, 0.87, "Ideal model: material conditions and temperature held fixed",
             ha="center", fontsize=12)
    fig.subplots_adjust(left=0.075, right=0.97, bottom=0.16, top=0.73, wspace=0.3)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
