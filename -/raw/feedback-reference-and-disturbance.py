"""Draw an ideal feedback loop and exact dimensionless responses; PNG to cwd.

Tested with Python 3.14.4, numpy 2.3.5 and matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
import numpy as np


def proportional_response(t, switch=2.0, disturbance=0.2, gain=2.0):
    t = np.asarray(t)
    elapsed = np.maximum(t - switch, 0.0)
    return -np.expm1(-gain * t) - disturbance / gain * np.expm1(-gain * elapsed)


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12})
    fig = plt.figure(figsize=(10, 7), dpi=120, facecolor="white")
    grid = fig.add_gridspec(2, 2, height_ratios=[1, 1.25])
    block = fig.add_subplot(grid[0, :])
    block.set(xlim=(0, 12), ylim=(0, 4))
    block.axis("off")
    block.set_title("Measured feedback: the command responds to what actually happened", pad=8)

    def arrow(start, end):
        block.annotate("", xy=end, xytext=start,
                       arrowprops={"arrowstyle": "->", "lw": 1.6, "color": "#35434d",
                                   "shrinkA": 0, "shrinkB": 0})

    def box(x, y, width, height, text):
        block.add_patch(Rectangle((x, y), width, height,
                                 facecolor="#edf4f7", edgecolor="#35434d", lw=1.4))
        block.text(x + width / 2, y + height / 2, text, ha="center", va="center")

    block.text(0.1, 2.6, r"Reference $r$", va="center")
    block.add_patch(Circle((2.0, 2.6), 0.27, facecolor="white", edgecolor="#35434d", lw=1.4))
    block.text(2, 2.6, r"$\Sigma$", ha="center", va="center")
    block.text(1.6, 2.9, "+", ha="center")
    block.text(1.68, 2.06, "−", ha="center")
    arrow((1.36, 2.6), (1.73, 2.6))
    arrow((2.27, 2.6), (3.3, 2.6))
    block.text(2.76, 2.95, r"$e=r-y_m$", ha="center")
    box(3.3, 2.05, 2.1, 1.1, "Controller\n" + r"$u=ke$")
    arrow((5.4, 2.6), (6.85, 2.6))
    block.text(6.1, 2.94, r"Command $u$", ha="center")
    box(6.85, 2.05, 2.15, 1.1, "Plant\n" + r"$\dot{x}=u+w$")
    arrow((7.925, 3.78), (7.925, 3.15))
    block.text(8.15, 3.62, r"Disturbance $w$", va="center")
    arrow((9, 2.6), (11.65, 2.6))
    block.text(10.4, 2.94, r"Output $y=x$", ha="center")
    block.plot([10.2, 10.2, 8.3], [2.6, 0.85, 0.85], color="#35434d", lw=1.6)
    block.scatter([10.2], [2.6], s=14, color="#35434d")
    box(5.0, 0.4, 3.3, 0.9, "Ideal measurement: " + r"$y_m=x$")
    arrow((10.2, 0.85), (8.3, 0.85))
    block.plot([5, 2, 2], [0.85, 0.85, 1.6], color="#35434d", lw=1.6)
    arrow((2, 1.6), (2, 2.33))
    block.text(3.4, 0.22, "Return actual output", ha="center", fontsize=10)

    t = np.linspace(0, 8, 1601)
    nominal_open = np.minimum(t, 1.0)
    nominal_p = proportional_response(t, disturbance=0)
    disturbed_open = nominal_open + 0.2 * np.maximum(t - 2, 0)
    disturbed_p = proportional_response(t)
    np.testing.assert_allclose(proportional_response(np.array([0, 2, 8])),
                               [0, 1 - np.exp(-4), 1.1 - np.exp(-16) - 0.1 * np.exp(-12)])
    assert disturbed_open[-1] == 2.2
    print(f"Exact checks: x_open(8)={disturbed_open[-1]:.6f}; "
          f"x_P(8)={disturbed_p[-1]:.6f}; P equilibrium=1.1")

    for col, (open_values, p_values, title) in enumerate([
        (nominal_open, nominal_p, r"No disturbance: $w=0$"),
        (disturbed_open, disturbed_p, r"Disturbance: $w=0.2$ from $t=2$"),
    ]):
        ax = fig.add_subplot(grid[1, col])
        ax.axhline(1, color="#555555", ls="--", lw=1.2, label=r"Reference $r=1$")
        ax.plot(t, open_values, color="#bd7024", lw=2.4, label="Open loop: planned pulse")
        ax.plot(t, p_values, color="#207699", lw=2.4, label=r"P feedback: $k=2$")
        ax.set(title=title, xlabel="Dimensionless time t", ylabel="Dimensionless position x",
               xlim=(0, 8), ylim=(0, 1.35 if col == 0 else 2.4))
        ax.legend(loc="lower right", frameon=True, facecolor="white", framealpha=1, fontsize=9)
        if col == 0:
            ax.annotate("Planned arrival: x(1)=1", xy=(1, 1), xytext=(2.0, 1.17),
                        fontsize=9, arrowprops={"arrowstyle": "->"})
        else:
            ax.axvline(2, color="#999999", ls=":", lw=1.2)
            ax.annotate(r"P settles at $1+0.2/2=1.1$", xy=(5.5, disturbed_p[1100]),
                        xytext=(2.65, 0.76), fontsize=9, arrowprops={"arrowstyle": "->"})
            ax.annotate("Open loop keeps drifting", xy=(6.4, 1.88), xytext=(2.6, 2.14),
                        fontsize=9, arrowprops={"arrowstyle": "->"})
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(color="#e5e9eb", lw=0.7)
        ax.set_axisbelow(True)

    fig.subplots_adjust(left=0.075, right=0.98, top=0.92, bottom=0.10, hspace=0.32, wspace=0.25)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
