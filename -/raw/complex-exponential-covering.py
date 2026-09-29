"""Show how exp maps a vertical strip onto an annulus, repeatedly.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from the desired output directory; write a same-basename opaque PNG.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    colors = ["#23815c", "#176fa1", "#8453a3"]
    orange = "#bc6016"
    theta = np.pi / 3
    z0 = -0.5 + 1j * theta
    z1 = z0 + 2j * np.pi
    w0 = np.exp(z0)
    assert np.allclose(np.exp(z1), w0, rtol=0, atol=1e-14)
    targets = np.array([1, -1, 2 + 3j, -0.2 - 0.4j])
    k = np.arange(-3, 4)
    inverse = np.log(np.abs(targets))[:, None] + 1j * (
        np.angle(targets)[:, None] + 2 * np.pi * k
    )
    assert np.allclose(np.exp(inverse), targets[:, None], atol=1e-13)

    plt.rcParams.update({"font.size": 11})
    fig, (source, target) = plt.subplots(1, 2, figsize=(10, 5.6), dpi=130)
    fig.patch.set_facecolor("white")
    source.fill_between([-1, 1], -np.pi, np.pi, color="#e8f2fa")
    source.fill_between([-1, 1], np.pi, 3 * np.pi, color="#fff0df")
    source.axhline(0, color="0.75", lw=0.8)
    source.axvline(0, color="0.75", lw=0.8)
    y = np.linspace(-np.pi, 3 * np.pi, 600)
    t = np.linspace(-np.pi, np.pi, 600)
    for x, color in zip([-1, 0, 1], colors):
        source.plot(np.full_like(y, x), y, color=color, lw=2)
        w = np.exp(x + 1j * t)
        target.plot(w.real, w.imag, color=color, lw=2,
                    label=[r"$|w|=e^{-1}$", r"$|w|=1$", r"$|w|=e$"][x + 1])
    radial = np.exp(np.linspace(-1, 1, 300))
    for angle in np.arange(-2, 7) * np.pi / 2:
        source.plot([-1, 1], [angle, angle], color="0.55", lw=0.8, ls=":")
    for angle in np.arange(4) * np.pi / 2:
        target.plot(radial * np.cos(angle), radial * np.sin(angle),
                    color="0.55", lw=0.8, ls=":")
    for angle in [theta, theta + 2 * np.pi]:
        source.plot([-1, 1], [angle, angle], color=orange, lw=1.5)
    target.plot(radial * np.cos(theta), radial * np.sin(theta),
                color=orange, lw=1.5, label=r"$\arg w=\pi/3$")

    source.scatter([z0.real, z1.real], [z0.imag, z1.imag],
                   color=orange, s=55, zorder=5)
    source.annotate(r"$z_0=-1/2+i\pi/3$", (z0.real, z0.imag),
                    (-1.43, -1.7), fontsize=10,
                    arrowprops={"arrowstyle": "->", "color": orange})
    source.annotate(r"$z_0+2\pi i$", (z1.real, z1.imag), (0.15, 8.5),
                    arrowprops={"arrowstyle": "->", "color": orange})
    source.annotate("", (-1.2, z1.imag), (-1.2, z0.imag),
                    arrowprops={"arrowstyle": "<->", "color": orange})
    source.text(-1.3, 4.3, r"$2\pi$", rotation=90, ha="right", color=orange)
    source.set(xlim=(-1.55, 1.55), ylim=(-3.7, 10),
               xticks=[-1, 0, 1], yticks=[-np.pi, 0, np.pi, 2 * np.pi, 3 * np.pi],
               yticklabels=[r"$-\pi$", "0", r"$\pi$", r"$2\pi$", r"$3\pi$"],
               xlabel=r"$\operatorname{Re}z=x$", ylabel=r"$\operatorname{Im}z=y$",
               title="Input: two turns in one vertical strip")

    target.scatter([w0.real], [w0.imag], color=orange, s=65, zorder=5)
    target.annotate("Both marked inputs\nmap to this point", (w0.real, w0.imag),
                    (-2.6, 1.5), fontsize=10,
                    arrowprops={"arrowstyle": "->", "color": orange})
    target.scatter([0], [0], marker="o", s=40, facecolors="white",
                   edgecolors="#b63a40", linewidths=1.5, zorder=6)
    target.annotate("0 is omitted", (0, 0), (-2.5, -0.5), fontsize=10,
                    color="#b63a40", arrowprops={"arrowstyle": "->", "color": "#b63a40"})
    target.set(xlim=(-3, 3), ylim=(-3, 3), aspect="equal",
               xlabel=r"$\operatorname{Re}w$", ylabel=r"$\operatorname{Im}w$",
               title="Output: the same annulus twice")
    target.legend(loc="lower left", fontsize=9, framealpha=1)
    for ax in (source, target):
        ax.set_facecolor("white")
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle(r"$w=e^{x+iy}$: radius $e^x$, angle $y$ modulo $2\pi$", fontsize=15)
    fig.text(0.5, 0.035, r"Full vertical lines map to circles; horizontal lines map to rays.  "
             r"Every $w\ne0$ has inputs $\ln|w|+i(\arg w+2\pi k)$.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.08, right=0.98, bottom=0.16, top=0.83, wspace=0.32)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)
    print("Verified periodicity and exponential preimages for four target values.")


if __name__ == "__main__":
    main()
