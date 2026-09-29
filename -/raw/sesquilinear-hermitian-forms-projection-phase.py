"""Original analytical geometry for a linear-first weighted complex inner product.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media; output is written to the current working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def arrow(ax, start, end, color, style="-", width=2.1):
    ax.annotate("", xy=end, xytext=start,
                arrowprops={"arrowstyle": "->", "color": color, "lw": width, "linestyle": style})


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12})
    fig, (ax, phase) = plt.subplots(1, 2, figsize=(11.4, 5.4), facecolor="white")
    fig.subplots_adjust(left=0.07, right=0.96, bottom=0.22, top=0.75, wspace=0.38)
    fig.suptitle("Projection and phase keep the first argument linear", y=0.966, fontsize=17)
    fig.text(0.5, 0.887, r"Analytical illustration: $H_+(z,w)=z_1\overline{w_1}+2z_2\overline{w_2}$", ha="center", fontsize=13)
    ax.set_title(r"Real slice: $u=(1,1),\ v=(2,0)$", pad=13)
    ax.set(xlim=(-0.3, 2.4), ylim=(-0.8, 1.6), xlabel=r"$x=\mathrm{Re}\,z_1$", ylabel=r"$y=\mathrm{Re}\,z_2$")
    ax.set_aspect("equal")
    t = np.linspace(-0.3, 1.6, 200)
    ax.plot(t, t, color="#aaaaaa", lw=1.4, label=r"$\mathrm{span}_{\mathbb{R}}(u)$")
    u, v, p = np.array([1., 1.]), np.array([2., 0.]), np.array([2/3, 2/3])
    arrow(ax, [0, 0], u, "#777777")
    arrow(ax, [0, 0], v, "#1767a8")
    arrow(ax, [0, 0], p, "#258252", width=3)
    arrow(ax, p, v, "#b24c19", style="--")
    ax.scatter(*p, color="#258252", s=30, zorder=5)
    ax.text(1.02, 1.06, r"$u$", color="#555555")
    ax.text(2.02, 0.08, r"$v$", color="#1767a8")
    ax.text(0.12, 0.73, r"$au=(2/3,2/3)$", color="#258252", fontsize=10)
    ax.text(1.35, 0.45, r"$r=(4/3,-2/3)$", color="#b24c19", fontsize=10)
    ax.text(-0.18, -0.54, r"$H_+(r,u)=0$ but $r\cdot u=2/3$", fontsize=11)
    ax.legend(loc="upper left", frameon=False, fontsize=10)
    ax.text(0.5, -0.25, r"$a=H_+(v,u)/H_+(u,u)=2/3$" + "\n" + r"$\|v\|^2=\|au\|^2+\|r\|^2=4/3+8/3$",
            transform=ax.transAxes, ha="center", va="top")
    phase.set_title(r"Complex coefficient: $u=(1,1),\ v=(1,i)$", pad=13)
    phase.set(xlim=(-1.05, 1.05), ylim=(-1.05, 1.05), xlabel=r"$\mathrm{Re}\,a$", ylabel=r"$\mathrm{Im}\,a$")
    phase.set_aspect("equal")
    a = (1 + 2j) / 3
    theta = np.pi / 3
    phi = np.angle(a)
    circle = np.linspace(0, 2 * np.pi, 361)
    phase.plot(abs(a) * np.cos(circle), abs(a) * np.sin(circle), color="#bbbbbb", lw=1)
    arrow(phase, [0, 0], [a.real, a.imag], "#555555", width=1.5)
    phase.text(0.39, 0.68, r"$a=(1+2i)/3$", fontsize=10)
    for direction, color, text, pos in [
        (1, "#1767a8", r"rotate $v$: $e^{i\theta}a$", (-1.0, 0.96)),
        (-1, "#b24c19", r"rotate $u$: $e^{-i\theta}a$", (-0.21, -0.4)),
    ]:
        angles = np.linspace(phi, phi + direction * theta, 100)
        xs, ys = abs(a) * np.cos(angles), abs(a) * np.sin(angles)
        phase.plot(xs, ys, color=color, lw=2.7)
        arrow(phase, [xs[-10], ys[-10]], [xs[-1], ys[-1]], color)
        phase.scatter(xs[-1], ys[-1], color=color, s=25, zorder=5)
        phase.text(*pos, text, color=color, fontsize=10)
    phase.scatter(a.real, a.imag, color="#555555", s=25, zorder=5)
    phase.text(0.5, -0.25, r"Two real coordinates of a complex scalar; $\theta=\pi/3$" + "\n" +
               r"Coefficient modulus stays $|a|=\sqrt{5}/3$",
               transform=phase.transAxes, ha="center", va="top", fontsize=10)
    for panel in (ax, phase):
        panel.axhline(0, color="#aaaaaa", lw=0.7)
        panel.axvline(0, color="#aaaaaa", lw=0.7)
        panel.grid(alpha=0.15)
        for spine in panel.spines.values():
            spine.set_color("#bbbbbb")
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
