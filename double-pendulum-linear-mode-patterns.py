"""Draw original linear mode patterns and histories for an ideal double pendulum."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig = plt.figure(figsize=(8.32, 5.6), dpi=125)
    gs = fig.add_gridspec(2, 2, width_ratios=[1, 2.5], left=0.06, right=0.97,
                          bottom=0.22, top=0.80, hspace=0.72, wspace=0.38)
    tau = np.linspace(0, 10, 901)
    amplitude = 0.06
    colors = ["#246ba0", "#bd5127"]
    for row, sign in enumerate([1, -1]):
        shape = np.array([1, sign * np.sqrt(2)])
        omega = np.sqrt(2 - sign * np.sqrt(2))
        pattern = fig.add_subplot(gs[row, 0])
        theta = amplitude * shape
        rods = np.column_stack((np.sin(theta), -np.cos(theta)))
        points = np.vstack(([0, 0], np.cumsum(rods, axis=0)))
        points[:, 0] *= 4
        pattern.plot([0, 0], [0, -2], "--", color="#bbbbbb", lw=1)
        pattern.plot(points[:, 0], points[:, 1], color="#555555", lw=3)
        pattern.scatter(*points[0], color="#333333", s=32, zorder=3)
        for i in range(2):
            pattern.scatter(*points[i + 1], s=90, color=colors[i], zorder=3)
            direction = np.sign(points[i + 1, 0])
            pattern.annotate("", (points[i + 1, 0] + direction * 0.07, points[i + 1, 1]),
                             (-0.04 if points[i + 1, 0] > 0 else 0.04, points[i + 1, 1]),
                             arrowprops={"arrowstyle": "->", "lw": 1.6, "color": colors[i]})
        pattern.text(-0.62, -0.69, r"$\theta_1=A$", fontsize=10, color=colors[0])
        pattern.text(-0.62, -1.73,
                     r"$\theta_2=\sqrt{2}A$" if sign == 1 else r"$\theta_2=-\sqrt{2}A$",
                     fontsize=10, color=colors[1])
        pattern.set(xlim=(-0.68, 0.83), ylim=(-2.14, 0.18))
        pattern.axis("off")
        pattern.set_title("Low mode: in phase" if sign == 1 else "High mode: opposed", fontsize=12)
        history = fig.add_subplot(gs[row, 1])
        for i in range(2):
            history.plot(tau, shape[i] * np.cos(omega * tau), color=colors[i],
                         lw=2, linestyle="-" if i == 0 else "--",
                         label=rf"$\theta_{i + 1}/A$")
        history.axhline(0, color="#999999", lw=0.7)
        history.set(xlim=(0, 10), ylim=(-1.65, 1.65), yticks=[-1, 0, 1],
                    ylabel="Angle / A")
        history.set_title(r"$\omega\sqrt{\ell/g}=\sqrt{2-\sqrt{2}}$" if sign == 1 else
                          r"$\omega\sqrt{\ell/g}=\sqrt{2+\sqrt{2}}$", fontsize=13, pad=10)
        history.grid(alpha=0.16)
        history.spines[["top", "right"]].set_visible(False)
        if row == 0:
            history.legend(loc="upper right", framealpha=1, ncol=2, fontsize=10)
        else:
            history.set_xlabel(r"Same dimensionless time in both rows: $\tau=t\sqrt{g/\ell}$")
    fig.suptitle("Two patterns, two natural frequencies", y=0.97, fontsize=18)
    fig.text(0.5, 0.905, r"Equal point masses, equal rods; $A=0.06$ rad", ha="center", fontsize=12)
    fig.text(0.5, 0.035, "Pattern snapshots: horizontal offsets enlarged ×4, heights unchanged.\n"
             "Curves are predictions of the linear model, not measurements.",
             ha="center", fontsize=10, linespacing=1.5)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
