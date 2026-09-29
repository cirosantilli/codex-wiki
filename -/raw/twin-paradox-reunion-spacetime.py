"""Reunited clocks and simultaneity slices; Python 3.14, NumPy 2.3.5,
Matplotlib 3.10.7. Run from _media; output basename matches this script.
All times and distances are illustrative model values, not measurements.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    beta, total = 0.6, 10.0
    turn_t = total / 2
    turn_x = beta * turn_t  # light-years, with c = 1 light-year/year
    before = turn_t - beta * turn_x
    after = turn_t + beta * turn_x
    assert np.allclose([turn_x, before, after], [3.0, 3.2, 6.8])
    assert np.isclose(total * np.sqrt(1 - beta**2), 8.0)

    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig = plt.figure(figsize=(8.0, 6.8), facecolor="white")
    ax = fig.add_axes([0.11, 0.12, 0.53, 0.80])
    ax.set_facecolor("white")
    ax.plot([0, 0], [0, total], color="#214f93", lw=3,
            label="Home: 10 years")
    ax.plot([0, turn_x, 0], [0, turn_t, total], color="#b84625", lw=3,
            label="Traveller: 8 years")
    xx = np.linspace(0, 4.1, 100)
    ax.plot(xx, turn_t + beta * (xx - turn_x), "--", color="#257e6c", lw=2)
    ax.plot(xx, turn_t - beta * (xx - turn_x), "--", color="#8c4799", lw=2)
    ax.plot([0, turn_x], [turn_t, turn_t], ":", color="0.65", lw=1.5)
    ax.scatter([0, turn_x, 0], [0, turn_t, total], s=40, color="black", zorder=5)
    ax.scatter([0, 0], [before, after], s=45,
               color=["#257e6c", "#8c4799"], zorder=6)
    ax.annotate("O: departure", (0, 0), xytext=(8, 6), textcoords="offset points")
    ax.annotate("R: reunion", (0, total), xytext=(8, -8),
                textcoords="offset points", va="top")
    ax.annotate("P: turnaround\n(3 ly, 5 yr)", (turn_x, turn_t),
                xytext=(8, -39), textcoords="offset points", fontsize=11)
    ax.text(-0.17, before, "3.2", color="#257e6c", ha="right", va="center")
    ax.text(-0.17, after, "6.8", color="#8c4799", ha="right", va="center")
    ax.set(xlim=(-0.65, 4.25), ylim=(-0.35, 10.65),
           xlabel="Position x (light-years)", ylabel="ct (light-years)")
    ax.set_aspect("equal")
    ax.set_xticks([0, 1, 2, 3, 4])
    ax.set_yticks([0, 2, 4, 6, 8, 10])
    ax.grid(alpha=0.16)
    fig.text(0.68, 0.84, "Same departure O\nand reunion R", fontsize=14, weight="bold")
    fig.text(0.68, 0.70, "Home clock\n10 years", color="#214f93")
    fig.text(0.68, 0.59, "Traveller clock\n4 + 4 = 8 years", color="#b84625")
    fig.text(0.68, 0.43, "At turnaround P:\n\nOutward frame assigns\nhome time 3.2 years", color="#257e6c", fontsize=11)
    fig.text(0.68, 0.25, "Return frame assigns\nhome time 6.8 years", color="#8c4799", fontsize=11)
    fig.text(0.68, 0.12, "Dashed lines: simultaneity\nslices, not light signals", fontsize=10)
    fig.suptitle("Twin paradox: worldlines and simultaneity", y=0.98, fontsize=15)
    out = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(out, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
