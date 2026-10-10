"""A noncentral-force model; tested with Python 3.14 / Matplotlib 3.10.7 / NumPy 2.3.5.

Run from _media; writes the matching PNG basename to the working directory.
R=1, m=1, theta=t+t^2/2: radial force=-(1+t)^2, tangential force=1.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white"})
    fig, (orbit, rate) = plt.subplots(1, 2, figsize=(9.6, 4.8), layout="constrained", gridspec_kw={"width_ratios": [1.05, 1]})
    colors = ["#2877ad", "#d58120", "#558c45"]
    boundaries = np.arange(4) / 2
    theta = lambda t: t + t**2 / 2
    circle = np.linspace(0, 2 * np.pi, 800)
    orbit.plot(np.cos(circle), np.sin(circle), color="#6f7780", lw=1.3)
    for index, color in enumerate(colors):
        ts = np.linspace(boundaries[index], boundaries[index + 1], 4001)
        angles = theta(ts)
        xy = np.column_stack((np.cos(angles), np.sin(angles)))
        orbit.add_patch(Polygon(np.vstack(([0, 0], xy, [0, 0])), facecolor=color, alpha=0.30, edgecolor="none"))
        orbit.plot(xy[:, 0], xy[:, 1], color=color, lw=3)
        middle = theta((boundaries[index] + boundaries[index + 1]) / 2)
        area = (angles[-1] - angles[0]) / 2
        polygon_area = 0.5 * np.sum(xy[:-1, 0] * xy[1:, 1] - xy[:-1, 1] * xy[1:, 0])
        assert abs(polygon_area - area) < 3e-8
        orbit.text(0.58 * np.cos(middle), 0.58 * np.sin(middle), f"{area:.4f}", color="#17212b", ha="center", va="center", fontsize=10)
        rate.plot(ts, (1 + ts) / 2, color=color, lw=3)
        rate.fill_between(ts, 0, (1 + ts) / 2, color=color, alpha=0.18)
        print(f"interval {boundaries[index]} to {boundaries[index+1]}: area={area:.8f}; polygon={polygon_area:.8f}")
    for t in boundaries:
        angle = theta(t)
        orbit.plot([0, np.cos(angle)], [0, np.sin(angle)], color="#68717b", lw=1)
        orbit.scatter(np.cos(angle), np.sin(angle), s=22, color="#17212b", zorder=5)
        orbit.text(1.16 * np.cos(angle), 1.16 * np.sin(angle), f"t={t:g}", ha="center", va="center", fontsize=10)
    # Transverse acceleration/force, tangent to the circle at t=1.
    angle = theta(1.0)
    position = np.array([np.cos(angle), np.sin(angle)])
    tangent = np.array([-np.sin(angle), np.cos(angle)])
    orbit.annotate("", xy=position + 0.5 * tangent, xytext=position, arrowprops={"arrowstyle": "->", "color": "#8c334c", "lw": 2})
    orbit.text(-0.49, 1.23, r"$F_\theta=1$", color="#8c334c", ha="center")
    orbit.scatter(0, 0, color="#17212b", s=24)
    orbit.text(0.03, -0.16, "O", fontsize=11)
    orbit.set(xlim=(-1.45, 1.45), ylim=(-1.37, 1.50), xlabel="x / R", ylabel="y / R", title="Equal times, increasing sector areas")
    orbit.set_aspect("equal")
    rate.plot([0, 1.5], [0.5, 0.5], "--", lw=1.4, color="#69717c", label="zero-torque comparison")
    rate.text(0.85, 1.29, r"$\dot A=(1+t)/2$", ha="center", fontsize=12)
    rate.annotate(r"slope $\ddot A=\tau_z/(2m)=0.5$", xy=(1.1, 1.05), xytext=(0.05, 0.87), arrowprops={"arrowstyle": "->", "lw": 1}, fontsize=10)
    rate.set(xlim=(0, 1.5), ylim=(0, 1.42), xticks=boundaries, xlabel="time t", ylabel=r"signed areal velocity $\dot A$", title="Tangential force changes the area rate")
    rate.legend(loc="lower right", fontsize=9)
    rate.grid(alpha=0.18)
    for ax in [orbit, rate]:
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle(r"Illustrative unit circle: $R=m=1,\ \theta=t+t^2/2,\ \Delta t=0.5$", fontsize=14)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
