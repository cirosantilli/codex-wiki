"""Draw a sampled, debounced toggle trace, writing the PNG to the CWD.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Dependencies are declared in the repository pyproject.toml.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    samples = [0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1]
    p = q = z = 0
    armed = 1
    outputs, arms, toggles, rearms = [], [], [], []
    for index, a in enumerate(samples):
        c = a & p & q
        d = (1 - a) & (1 - p) & (1 - q)
        if armed and c:
            toggles.append(index)
        if not armed and d:
            rearms.append(index)
        z, armed, p, q = z ^ (armed & c), d | (armed & (1 - c)), a, p
        outputs.append(z)
        arms.append(armed)
    assert toggles == [6, 16, 22] and rearms == [13, 19]
    fig, axes = plt.subplots(3, 1, figsize=(9.2, 4.2), dpi=100,
                             sharex=True, facecolor="white")
    positions = np.arange(len(samples) + 1)
    for ax, values, label, color in zip(axes, (samples, outputs, arms),
                                         ("Input a", "Output z", "Armed"),
                                         ("#235f91", "#7b3d92", "#247247")):
        ax.step(positions, values + [values[-1]], where="post", color=color, linewidth=2.4)
        ax.scatter(np.arange(len(values)) + 0.08, values, s=11, color=color, zorder=3)
        ax.set_ylim(-0.16, 1.18)
        ax.set_yticks((0, 1))
        ax.set_ylabel(label, rotation=0, ha="right", va="center", labelpad=20)
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(axis="x", color="#e7e7e7", linewidth=0.7)
        for index in toggles:
            ax.axvline(index, color="#a44619", linestyle="--", linewidth=1.0, alpha=0.8)
    for index in toggles:
        axes[1].annotate("toggle", xy=(index, outputs[index]), xytext=(index - 0.5, 1.10),
                         fontsize=9, color="#a44619", ha="center")
    for index in rearms:
        axes[2].annotate("rearm", xy=(index, 1), xytext=(index - 0.6, 1.10),
                         fontsize=9, color="#247247", ha="center")
    axes[-1].set_xlim(-0.15, len(samples))
    axes[-1].set_xticks(range(len(samples)))
    axes[-1].tick_params(axis="x", labelsize=8)
    axes[-1].set_xlabel("Clock-edge index; stored values shown immediately after each edge")
    fig.suptitle("Three highs toggle; three lows rearm", fontsize=15)
    fig.subplots_adjust(left=0.16, right=0.985, top=0.85, bottom=0.14, hspace=0.38)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white",
                transparent=False, metadata={"Software": "Matplotlib"})
    plt.close(fig)


if __name__ == "__main__":
    main()
