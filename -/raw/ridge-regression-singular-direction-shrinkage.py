"""Exact two-direction synthetic ridge shrinkage; matching PNG in the CWD.

Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media with MPLBACKEND=Agg and a writable MPLCONFIGDIR.
This illustrates an algebraic fit, not measured generalization performance.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def constructed_data():
    u1 = np.array([1, -1, 1, -1], dtype=float) / 2
    u2 = np.array([1, 1, -1, -1], dtype=float) / 2
    u3 = np.array([1, -1, -1, 1], dtype=float) / 2
    design = np.column_stack((3 * u1, u2))
    response = 2 + 3 * u1 + u2 + u3 / 2
    return design, response, np.column_stack((u1, u2, u3))


def fit_coordinates(penalty):
    penalty = np.asarray(penalty)
    return 27 / (9 + penalty), 1 / (1 + penalty)


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12})
    fig, (ax_path, ax_factor) = plt.subplots(
        1, 2, figsize=(10.8, 5.4), dpi=100, facecolor="white", layout="constrained",
    )
    fig.suptitle("Ridge shrinks weak singular directions more strongly", fontsize=15)
    design, response, basis = constructed_data()
    assert np.allclose(basis.T @ basis, np.eye(3))
    assert np.allclose(design.T @ design, np.diag([9, 1]))
    penalties = np.linspace(0, 1000, 2400)
    a, b = fit_coordinates(penalties)
    ax_path.plot(a, b, color="#444444", lw=2)
    ax_path.plot([a[-1], 0], [b[-1], 0], color="#444444", ls="dotted")
    colors = ["#222222", "#cf6425", "#6c4895"]
    labels = [r"$\lambda=0$: $(3,1)$", r"$\lambda=1$: $(27/10,1/2)$",
              r"$\lambda=9$: $(3/2,1/10)$"]
    offsets = [(-142, 13), (-190, 9), (-105, 30)]
    for penalty, color, label, offset in zip([0, 1, 9], colors, labels, offsets):
        a, b = fit_coordinates(penalty)
        slopes = np.array([a / 3, b])
        assert np.allclose((design.T @ design + penalty * np.eye(2)) @ slopes,
                           design.T @ (response - 2))
        ax_path.scatter([a], [b], color=color, s=65, zorder=4)
        ax_path.annotate(label, (a, b), xytext=offset, textcoords="offset points",
                         color=color, fontsize=10)
    ax_path.annotate("Increasing penalty", (2.05, 1 / (1 + (27 / 2.05 - 9))),
                     xytext=(2.8, 0.24), arrowprops={"arrowstyle": "->", "color": "#444444"},
                     fontsize=10, ha="center")
    ax_path.set(xlabel=r"Fitted coordinate along $u_1$ ($d_1^2=9$)",
                ylabel=r"Fitted coordinate along $u_2$ ($d_2^2=1$)",
                xlim=(-0.1, 3.3), ylim=(-0.07, 1.17), title="Fitted centered response coordinates")
    ax_path.text(0.06, 0.89, "Free intercept = 2\nUnfittable component = $u_3/2$",
                 transform=ax_path.transAxes, fontsize=10, va="top")
    ax_path.text(0.03, 0.02, "RSS at penalties 0, 1, 9:\n1/4, 59/100, 331/100",
                 transform=ax_path.transAxes, fontsize=10, va="bottom",
                 bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    penalty_grid = np.linspace(0, 18, 300)
    for strength, color in [(9, "#185f9b"), (1, "#ba3d35")]:
        ax_factor.plot(penalty_grid, strength / (strength + penalty_grid), lw=2.5,
                       color=color, label=rf"$d^2={strength}$")
        for penalty in [1, 9]:
            ax_factor.scatter([penalty], [strength / (strength + penalty)], color=color,
                              s=50, zorder=4)
    ax_factor.axvline(1, color="#888888", lw=1, ls="dotted")
    ax_factor.axvline(9, color="#888888", lw=1, ls="dotted")
    ax_factor.annotate(r"$9/10$", (1, 0.9), xytext=(8, 0), textcoords="offset points", color="#185f9b")
    ax_factor.annotate(r"$1/2$", (1, 0.5), xytext=(8, 0), textcoords="offset points", color="#ba3d35")
    ax_factor.annotate(r"$1/2$", (9, 0.5), xytext=(8, 4), textcoords="offset points", color="#185f9b")
    ax_factor.annotate(r"$1/10$", (9, 0.1), xytext=(8, -17), textcoords="offset points", color="#ba3d35")
    ax_factor.set(xlabel=r"Penalty $\lambda$", ylabel=r"Retained fraction $d^2/(d^2+\lambda)$",
                  xlim=(-0.5, 18.5), ylim=(-0.02, 1.08), title="Small singular values lose more of their fit")
    ax_factor.legend(loc="upper right", facecolor="white", framealpha=1)
    for ax in (ax_path, ax_factor):
        ax.set_facecolor("white")
        ax.grid(alpha=0.18)
        ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
