"""Generate exact regular-fiber and mixed-input examples in the CWD.

Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python3 ../critical-points-values-fibers.py
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    blue, green, red = "#2468a0", "#287a54", "#b52b39"
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
    fig, (radial, mixed) = plt.subplots(1, 2, figsize=(10, 5.1), dpi=110)
    fig.patch.set_facecolor("white")
    fig.subplots_adjust(left=0.08, right=0.97, top=0.76, bottom=0.31, wspace=0.35)
    fig.suptitle("A value is regular only if every input in its fiber is regular", y=0.98, fontsize=15)
    fig.text(0.5, 0.88, "Nonempty regular fibers have dimension = source dimension − target dimension.", ha="center")
    radial.set_title(r"$H(x,y)=x^2+y^2$: source fibers")
    theta = np.linspace(0, 2*np.pi, 401)
    for c, color in [(1, blue), (4, green)]:
        xs, ys = np.sqrt(c)*np.cos(theta), np.sqrt(c)*np.sin(theta)
        assert np.allclose(xs*xs+ys*ys, c)
        assert np.all(np.hypot(2*xs, 2*ys) > 0)
        radial.plot(xs, ys, color=color, lw=2.2)
        radial.text(0.18, np.sqrt(c)+0.11, f"c = {c}: regular", color=color)
    radial.axhline(0, color="#dddddd", lw=0.7, zorder=0)
    radial.axvline(0, color="#dddddd", lw=0.7, zorder=0)
    radial.scatter([0], [0], color=red, s=65, zorder=4)
    radial.text(-0.56, 0.35, "c = 0", color=red)
    radial.set(xlim=(-2.55, 2.55), ylim=(-2.55, 2.55), xlabel="x", ylabel="y")
    radial.set_aspect("equal", adjustable="box")

    t = np.linspace(-0.6, 1.5, 500)
    mixed.plot(t, t*t*(t-1), color="#333333", lw=2)
    mixed.axhline(0, color="#888888", ls="--", lw=1)
    mixed.scatter([0], [0], color=red, s=70, zorder=4)
    mixed.scatter([1], [0], color=blue, s=70, zorder=4)
    mixed.annotate("critical input 0\nh′(0) = 0", (0, 0), xytext=(-0.43, 0.43),
                   arrowprops={"arrowstyle": "->", "color": red}, color=red)
    mixed.annotate("regular input 1\nh′(1) = 1", (1, 0), xytext=(0.72, 0.58),
                   arrowprops={"arrowstyle": "->", "color": blue}, color=blue)
    mixed.text(0.2, -0.66, "Shared output 0 is critical:\none critical input is enough.", color=red)
    mixed.set(title=r"$h(t)=t^2(t-1)$: graph and the fiber of 0",
              xlim=(-0.6, 1.5), ylim=(-0.8, 1.15), xlabel="input t", ylabel="output h(t)")
    mixed.set_xticks([0, 0.5, 1, 1.5])
    for ax in [radial, mixed]:
        ax.set_facecolor("white")
        ax.tick_params(labelsize=10)
    fig.text(0.265, 0.105, "c > 0: regular circles, dimension 1 = 2 − 1\nc = 0: critical value, one-point fiber\nc < 0: regular values, empty fibers",
             ha="center", color="#333333")
    fig.text(0.75, 0.12, "Fiber of 0: {0, 1}\nTest all its inputs, not just input 1.", ha="center", color="#333333")
    fig.text(0.5, 0.025, "Exact polynomial examples; these curves are not measured data.",
             ha="center", fontsize=10, color="#555555")
    assert 3*0**2-2*0 == 0 and 3*1**2-2*1 == 1
    assert all(t*t*(t-1) == 0 for t in [0, 1])
    assert np.linalg.matrix_rank(np.array([[0.0, 0.0]])) == 0
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
