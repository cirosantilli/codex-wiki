"""Draw Q5(b)'s logarithmic keyhole; Python 3.14, NumPy 2.3, Matplotlib 3.10.

Run from the desired output directory; the PNG is written in that directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, ax = plt.subplots(figsize=(6.5, 5.0), layout="constrained")
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    radius, inner, angle, a = 3.2, 0.32, 0.07, 1.35
    color = "#175b9e"
    theta = np.linspace(-np.pi + angle, np.pi - angle, 700)
    ax.plot(radius * np.cos(theta), radius * np.sin(theta), color=color, lw=2)
    theta_inner = np.linspace(np.pi - angle, -np.pi + angle, 300)
    ax.plot(inner * np.cos(theta_inner), inner * np.sin(theta_inner), color=color, lw=2)
    for sign in (-1, 1):
        theta_bank = sign * (np.pi - angle)
        x = np.array([inner, radius]) * np.cos(theta_bank)
        y = np.array([inner, radius]) * np.sin(theta_bank)
        ax.plot(x, y, color=color, lw=2)
    def arrow(start, end):
        ax.annotate("", xy=end, xytext=start,
                    arrowprops={"arrowstyle": "->", "color": color, "lw": 2})
    for theta_mark in (0.45, 1.7, -1.5):
        start = radius * np.array([np.cos(theta_mark), np.sin(theta_mark)])
        end = radius * np.array([np.cos(theta_mark + .18), np.sin(theta_mark + .18)])
        arrow(start, end)
    arrow((-2.25, .157), (-1.7, .119))
    arrow((-1.7, -.119), (-2.25, -.157))
    arrow((0, -inner), (-.17, -.27))
    ax.plot([-radius - .4, 0], [0, 0], color="#b45334", lw=1.5, ls="--")
    ax.axhline(0, color="0.8", lw=.65, zorder=0)
    ax.axvline(0, color="0.8", lw=.65, zorder=0)
    ax.scatter([1, 0, 0], [0, a, -a], color="#a52e37", s=30, zorder=4)
    for x, y, label in [(1, 0, "$1$"), (0, a, "$ia$"), (0, -a, "$-ia$")]:
        ax.annotate(label, (x, y), xytext=(8, 7), textcoords="offset points", fontsize=12)
    ax.text(-2.6, .45, r"$\log x+i\pi$", fontsize=12)
    ax.text(-2.6, -.65, r"$\log x-i\pi$", fontsize=12)
    ax.text(2.4, 2.25, "$R$", color=color, fontsize=12)
    ax.annotate(r"$\varepsilon$", (.27, .17), xytext=(.65, .6),
                arrowprops={"arrowstyle": "-", "color": "0.4"}, fontsize=12)
    ax.text(.7, -1.95, "all three poles\nare enclosed", color="#a52e37", fontsize=10)
    ax.set_title("Principal logarithm: a keyhole about the negative axis", fontsize=12, pad=12)
    ax.set_aspect("equal")
    ax.set_xlim(-4, 3.7)
    ax.set_ylim(-3.55, 3.6)
    ax.set_axis_off()
    fig.savefig(Path.cwd() / "2021-q5-keyhole.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
