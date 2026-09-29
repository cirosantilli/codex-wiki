"""Original ideal Hahn echo phases; Python 3.14, matplotlib 3.10, NumPy 2.3.

Run from _media; writes hahn-echo-phase-refocusing.png to the working directory.
Positive gamma: free rotation R_z(-Delta*t), preparation R_u(-pi/2),
refocusing R_v(-pi). No relaxation. Vectors are magnetization projections.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig = plt.figure(figsize=(10.4, 6.4))
    grid = fig.add_gridspec(2, 4, height_ratios=[1, 1.15])
    offsets = np.array([-1.7, -0.85, 0.0, 0.85, 1.7])  # Delta*tau, radians
    colors = ["#3455a4", "#218c9b", "#333333", "#d18b19", "#bf3f59"]
    stages = [(0, False, r"Prepared: $t=0^+$"),
              (1, False, r"Spread: $t=\tau^-$"),
              (1, True, r"Reflected: $t=\tau^+$"),
              (2, True, r"Refocused: $t=2\tau$")]
    for k, (time, after, title) in enumerate(stages):
        ax = fig.add_subplot(grid[0, k])
        ax.add_patch(Circle((0, 0), 1, fill=False, color="#b5bec8"))
        ax.axhline(0, color="#dce0e5", lw=0.8)
        ax.axvline(0, color="#dce0e5", lw=0.8)
        phases = -offsets * (time - 2 if after else time)
        # At preparation/refocusing all arrows coincide; separate lengths expose colors.
        lengths = np.linspace(0.64, 1, 5) if time in (0, 2) else np.ones(5)
        for phase, color, length in zip(phases, colors, lengths):
            vector = length * np.array([-np.sin(phase), np.cos(phase)])
            ax.annotate("", vector, (0, 0),
                        arrowprops={"arrowstyle": "-|>", "color": color, "lw": 2})
        ax.text(1.08, -0.06, "$u$")
        ax.text(0.04, 1.09, "$v$")
        ax.set(xlim=(-1.22, 1.25), ylim=(-1.15, 1.3), aspect="equal", title=title)
        ax.axis("off")
    ax = fig.add_subplot(grid[1, :])
    for delta, color in zip(offsets, colors):
        left = np.linspace(0, 1, 100)
        right = np.linspace(1, 2, 100)
        ax.plot(left, -delta * left, color=color, lw=2,
                label=rf"$\Delta\tau={delta:g}$")
        ax.plot(right, -delta * (right - 2), color=color, lw=2)
        ax.plot([1, 1], [-delta, delta], color=color, ls=":", lw=1)
    ax.axvline(1, color="#6b4c91", ls="--", lw=1)
    ax.axvline(2, color="#777777", ls=":", lw=1)
    ax.axhline(0, color="#bbbbbb", lw=0.8)
    ax.set(xlim=(0, 2.12), ylim=(-2.15, 2.65),
           xlabel=r"Time $t/\tau$", ylabel=r"Phase relative to $+v$ (rad)",
           xticks=[0, 1, 2], xticklabels=["0", r"$\tau$", r"$2\tau$"])
    ax.text(1, 2.3, r"$180_v^\circ$: phase reflection", ha="center", color="#6b4c91")
    handles, labels = ax.get_legend_handles_labels()
    fig.legend(handles, labels, loc="center", bbox_to_anchor=(0.5, 0.53),
               ncol=5, fontsize=9, frameon=False)
    ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("A pulse reflects phase; free precession keeps its direction", fontsize=15, y=0.98)
    fig.subplots_adjust(left=0.075, right=0.98, top=0.86, bottom=0.16, hspace=0.32, wspace=0.2)
    fig.text(0.5, 0.015,
             r"Ideal $90_u^\circ$ then $180_v^\circ$; static detunings, no relaxation. Coincident arrows use different lengths for visibility.",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
