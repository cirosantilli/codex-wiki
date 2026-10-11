"""Original solution diagrams for the 2022 Particle and Nuclear Physics exam.

Writes the PNG basename into the current working directory.
Dependencies are declared in the repository pyproject.toml.
Tested: Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def fermion(ax, start, finish, backwards=False):
    ax.plot([start[0], finish[0]], [start[1], finish[1]], color="#333333", linewidth=1.5)
    a, b = np.array(start), np.array(finish)
    if backwards:
        a, b = b, a
    begin, end = a + 0.43 * (b - a), a + 0.59 * (b - a)
    ax.annotate("", xy=end, xytext=begin, arrowprops={"arrowstyle": "-|>", "color": "#333333", "lw": 1.4})


def wavy(ax, start, finish):
    a, b = np.array(start), np.array(finish)
    delta = b - a
    normal = np.array([-delta[1], delta[0]]) / np.linalg.norm(delta)
    t = np.linspace(0, 1, 220)
    wave = a[:, None] + delta[:, None] * t + 0.045 * normal[:, None] * np.sin(14 * np.pi * t)
    ax.plot(wave[0], wave[1], color="#275e85", linewidth=1.6)


def panel(ax, reverse):
    active_in = r"$u$" if reverse else r"$d$"
    active_out = r"$d$" if reverse else r"$u$"
    vertex, fork = (2.0, 1.0), (2.9, 2.0)
    fermion(ax, (0.4, 1.0), vertex)
    fermion(ax, vertex, (4.8, 1.0))
    fermion(ax, (0.4, 0.1), (4.8, 0.1), backwards=True)
    wavy(ax, vertex, fork)
    ax.scatter([vertex[0], fork[0]], [vertex[1], fork[1]], s=20, color="#333333", zorder=4)
    # The charged-lepton line has outgoing e+ for the reverse process.
    fermion(ax, fork, (4.8, 2.8), backwards=reverse)
    fermion(ax, fork, (4.8, 1.8), backwards=not reverse)
    for x, y, label in [(0.15, 1.0, active_in), (5.03, 1.0, active_out),
                        (0.15, 0.1, r"$\bar d$"), (5.03, 0.1, r"$\bar d$"),
                        (5.12, 2.8, r"$e^+$" if reverse else r"$e^-$"),
                        (5.12, 1.8, r"$\nu_e$" if reverse else r"$\bar\nu_e$")]:
        ax.text(x, y, label, ha="center", va="center", fontsize=14)
    ax.text(2.12, 1.65, r"$W^+$" if reverse else r"$W^-$", color="#275e85", ha="right", fontsize=13)
    ax.text(0.4, -0.45, r"Initial $\pi^+$" if reverse else r"Initial $\pi^0$: $d\bar d$ component", ha="left", fontsize=10)
    ax.text(4.8, -0.45, r"Final $\pi^0$: $d\bar d$ component" if reverse else r"Final $\pi^+$", ha="right", fontsize=10)
    ax.set_title("(ii) Allowed charged-pion beta decay" if reverse else "(i) Formal vertex; decay forbidden by masses", fontsize=12)
    ax.set_xlim(-0.1, 5.7)
    ax.set_ylim(-0.7, 3.2)
    ax.axis("off")


def main():
    fig, axes = plt.subplots(2, 1, figsize=(7.4, 7.0))
    panel(axes[0], False)
    panel(axes[1], True)
    fig.suptitle("Charged-current quark transitions with a spectator antiquark", fontsize=13)
    fig.text(0.5, 0.018, "Time runs left to right. Arrows mark fermion-number flow.", ha="center", fontsize=10)
    fig.tight_layout(rect=(0, 0.045, 1, 0.96), h_pad=2.0)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=145, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
