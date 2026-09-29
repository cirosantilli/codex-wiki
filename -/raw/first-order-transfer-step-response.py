"""Plot two initial conditions for tau*y' + y = K*u with a unit step.

Run from _media; the opaque-white PNG is written by basename to cwd.
Tested with Python 3.14.4, NumPy 2.3.5, and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    gain, tau = 2.0, 3.0
    time = np.linspace(0.0, 18.0, 901)
    decay = np.exp(-time / tau)
    zero = gain * (1.0 - decay)
    one = zero + decay
    blue, orange = "#1769aa", "#bd5500"
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(8.0, 4.8), layout="constrained")
    ax.plot(time, zero, color=blue, linewidth=2.4,
            label=r"$y_0=0:\quad y=2(1-e^{-t/3})$")
    ax.plot(time, one, color=orange, linewidth=2.4,
            label=r"$y_0=1:\quad y=2-e^{-t/3}$")
    ax.axhline(gain, color="#555555", linestyle="--", linewidth=1.1)
    ax.text(17.7, 2.04, "Final value = 2", ha="right", fontsize=10)
    for tmark, label, textpos in [
        (tau, "63.2% of final value\nat one time constant", (4.6, 0.64)),
        (3 * tau, "95.0% of final value\nat three time constants", (10.3, 1.22)),
    ]:
        value = gain * (1.0 - np.exp(-tmark / tau))
        ax.plot([tmark, tmark], [0.0, value], color="#777777",
                linestyle=":", linewidth=1.2)
        ax.scatter([tmark], [value], s=42, color=blue, zorder=4)
        ax.annotate(label, xy=(tmark, value), xytext=textpos, color=blue,
                    arrowprops={"arrowstyle": "->", "color": blue}, fontsize=10)
    ax.set(title="Same transfer function and unit step; different initial values",
           xlabel="Time t (s)", ylabel="Output y (dimensionless)",
           xlim=(0, 18), ylim=(0, 2.22), xticks=[0, 3, 6, 9, 12, 15, 18])
    ax.legend(loc="lower right", framealpha=1.0)
    ax.grid(alpha=0.2)
    fig.suptitle(r"$G(s)=2/(3s+1)$; time constant $\tau=3$ s", fontsize=14)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
