"""Original two-level quench geometry; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; the matching PNG is written to the current working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, (ax, prob) = plt.subplots(1, 2, figsize=(10, 4.6), layout="constrained")
    theta = np.pi / 3
    c, s = np.cos(theta / 2), np.sin(theta / 2)
    colors = {"state": "#252525", "g": "#1767a5", "e": "#bd4a20"}
    for vector, color, label, offset in [
        ((1, 0), colors["state"], r"$|0\rangle$ (unchanged)", (0, -0.12)),
        ((c, s), colors["g"], r"$|g_f\rangle$", (0.03, 0.04)),
        ((-s, c), colors["e"], r"$|e_f\rangle$", (-0.04, 0.05)),
    ]:
        ax.annotate("", xy=vector, xytext=(0, 0),
                    arrowprops={"arrowstyle": "->", "color": color, "lw": 2.5})
        ax.text(vector[0] + offset[0], vector[1] + offset[1], label,
                color=color, ha="center")
    ax.plot([1, c * c], [0, c * s], "--", color=colors["g"], lw=1.4)
    ax.plot([1, s * s], [0, -s * c], "--", color=colors["e"], lw=1.4)
    ax.plot([0, c * c], [0, c * s], color=colors["g"], alpha=0.35, lw=5)
    ax.plot([0, s * s], [0, -s * c], color=colors["e"], alpha=0.35, lw=5)
    phi = np.linspace(0, theta / 2, 80)
    ax.plot(0.35 * np.cos(phi), 0.35 * np.sin(phi), color=colors["g"])
    ax.text(0.42, 0.13, r"$\theta/2=30^\circ$", fontsize=11)
    ax.axhline(0, color="0.85", lw=1, zorder=0)
    ax.axvline(0, color="0.85", lw=1, zorder=0)
    ax.set(xlim=(-0.85, 1.5), ylim=(-0.72, 1.18), aspect="equal")
    ax.set_title("Real state-amplitude plane", pad=16)
    ax.set_axis_off()
    ax.text(0.03, -0.58, r"$|0\rangle=c|g_f\rangle-s|e_f\rangle$" + "\n"
            + r"$c=\sqrt{3}/2,\quad s=1/2$", ha="center", fontsize=12)
    angles = np.linspace(0, np.pi, 301)
    prob.plot(angles / np.pi, np.cos(angles / 2) ** 2,
              color=colors["g"], lw=2.5, label=r"$p_g=\cos^2(\theta/2)$")
    prob.plot(angles / np.pi, np.sin(angles / 2) ** 2,
              color=colors["e"], lw=2.5, label=r"$p_e=\sin^2(\theta/2)$")
    prob.axvline(1 / 3, color="0.6", ls=":")
    prob.scatter([1 / 3, 1 / 3], [0.75, 0.25],
                 color=[colors["g"], colors["e"]], zorder=4)
    prob.annotate("3/4", (1 / 3, 0.75), xytext=(9, 9), textcoords="offset points")
    prob.annotate("1/4", (1 / 3, 0.25), xytext=(9, -18), textcoords="offset points")
    prob.set(xlim=(0, 1), ylim=(-0.03, 1.03), xlabel=r"Hamiltonian-axis angle $\theta/\pi$",
             ylabel="Final energy probability", title="Born probabilities after the switch")
    prob.set_xticks([0, 1 / 3, 0.5, 1], ["0", "1/3", "1/2", "1"])
    prob.grid(alpha=0.2)
    prob.legend(loc="upper right", fontsize=11)
    fig.suptitle("Sudden quench: fixed state, rotated energy eigenbasis", fontsize=15)
    fig.savefig(Path.cwd() / "sudden-quench-eigenbasis-overlaps.png", dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
