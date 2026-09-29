"""Normalized solution of a two-population toy ODE; Python 3.14, NumPy, Matplotlib."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    precursor_decay = np.log(2) / 6.7
    daughter_decay = np.log(2) / 9.2
    peak_time = np.log(precursor_decay / daughter_decay) / (
        precursor_decay - daughter_decay
    )
    time = np.linspace(0, 70, 800)

    def response(t):
        return (np.exp(-precursor_decay * t) - np.exp(-daughter_decay * t)) / (
            daughter_decay - precursor_decay
        )

    peak_value = response(peak_time)
    fig, ax = plt.subplots(figsize=(7.2, 4), layout="constrained")
    ax.plot(time, response(time) / peak_value, linewidth=2.4, color="#236b8e",
            label="Fed daughter response")
    ax.plot(time, np.exp(-precursor_decay * time), linestyle="--", color="#888888",
            label="Remaining precursor fraction")
    ax.axvline(peak_time, linestyle=":", color="#b65e21")
    ax.scatter([peak_time], [1], color="#b65e21", zorder=4)
    ax.annotate(f"Peak at {peak_time:.2f} h", (peak_time, 1),
                xytext=(23, 0.93), arrowprops={"arrowstyle": "->"}, fontsize=10)
    ax.set(xlabel="Time after imposed source/flux removal (h)",
           ylabel="Normalized population", xlim=(0, 70), ylim=(0, 1.12),
           title="A disappearing precursor can produce a delayed daughter maximum")
    ax.legend(loc="upper right", fontsize=9)
    ax.grid(alpha=0.2)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=140, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
