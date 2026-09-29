"""Original I/Q geometry and exact finite-window rejection.

Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Run from _media; PNG goes to CWD.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(10, 4.8), layout="constrained",
                                 facecolor="white", width_ratios=[1, 1.25])
    blue, orange = "#1663a6", "#c45111"
    phi = np.pi / 3
    x, y = 0.2, 0.2 * np.sqrt(3)
    circle = np.linspace(0, 2 * np.pi, 500)
    ax.plot(0.4 * np.cos(circle), 0.4 * np.sin(circle), color="#c9cdd1", lw=1.3)
    ax.axhline(0, color="#7c8288", lw=0.8)
    ax.axvline(0, color="#7c8288", lw=0.8)
    ax.annotate("", xy=(x, y), xytext=(0, 0),
                arrowprops={"arrowstyle": "->", "lw": 2.4, "color": blue})
    ax.plot([x, x], [0, y], ls="--", color=blue)
    ax.plot([0, x], [y, y], ls="--", color=blue)
    arc = np.linspace(0, phi, 100)
    ax.plot(0.12 * np.cos(arc), 0.12 * np.sin(arc), color=blue)
    ax.text(0.13, 0.07, "60°", color=blue, fontsize=11)
    ax.text(0.012, y + 0.012, "Y = 0.346410 V", fontsize=10)
    ax.text(0.15, -0.062, "X = 0.200 V", fontsize=10)
    ax.text(-0.21, 0.21, "R = 0.400 V", color=blue, fontsize=11)
    ax.annotate("", xy=(x + 0.1, y), xytext=(x, y),
                arrowprops={"arrowstyle": "->", "lw": 2, "color": orange})
    ax.plot([0, x + 0.1], [0, y], ls=":", lw=2, color=orange)
    ax.text(0.25, 0.41, "+0.100 V\nsynchronized", color=orange, ha="center", fontsize=10)
    ax.set(xlim=(-0.45, 0.48), ylim=(-0.45, 0.48), xlabel="X (V)", ylabel="Y (V)")
    ax.set_aspect("equal")
    ax.set_title("Two coordinates retain amplitude and phase", fontsize=12)

    u = np.linspace(-3, 3, 2401)
    # u = (f - f0) T, f0 T = 4; psi = 0. np.sinc is sin(pi u)/(pi u).
    difference = np.exp(1j * np.pi * u) * np.sinc(u)
    sum_term = np.exp(-1j * np.pi * (8 + u)) * np.sinc(8 + u)
    response = np.abs(difference + sum_term)
    bx.plot(u, response, color=blue, lw=2, label="Exact real-input response")
    bx.plot(u, abs(difference), color=orange, ls="--", lw=1.7,
            label="Difference-frequency term only")
    example = 32 / (17 * np.pi)
    bx.scatter([0.5], [example], color=blue, zorder=4, s=30)
    bx.annotate("u = 0.5\nexact: 0.599172", xy=(0.5, example), xytext=(1.1, 0.76),
                arrowprops={"arrowstyle": "->", "color": blue}, fontsize=10)
    bx.set(xlim=(-3, 3), ylim=(0, 1.12), xlabel=r"Detuning $u=(f-f_0)T$",
           ylabel=r"Recovered amplitude / input amplitude $|Z_T|/B$")
    bx.set_title("Four reference cycles give finite rejection", fontsize=12)
    bx.legend(loc="upper right", fontsize=9)
    bx.grid(alpha=0.2)
    for a in (ax, bx):
        a.set_facecolor("white")
    fig.get_layout_engine().set(rect=(0, 0.09, 1, 0.91))
    fig.text(0.5, 0.024, "Constructed model • peak convention • right panel: ψ = 0, f₀T = 4",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
