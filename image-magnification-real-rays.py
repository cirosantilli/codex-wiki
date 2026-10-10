"""Original paraxial ray diagrams; all values are predictions, not data.

Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
The PNG is written to the current directory with this script's basename.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def ray(ax, xs, ys, color):
    ax.plot(xs, ys, color=color, lw=2)
    for k in range(len(xs) - 1):
        start = np.array([xs[k], ys[k]])
        step = np.array([xs[k + 1], ys[k + 1]]) - start
        ax.annotate("", xy=start + 0.68 * step, xytext=start + 0.52 * step,
                    arrowprops={"arrowstyle": "->", "color": color, "lw": 2})


def diagram(ax, u, letter):
    f, h = 10.0, 0.5  # centimetres
    v = f * u / (u - f)
    image_h = -v * h / u
    # Check the construction using the independent paraxial lens kick.
    # Arbitrary incident rays arriving at different lens heights must agree.
    for intercept in np.linspace(-0.6, 0.6, 13):
        slope_in = (intercept - h) / u
        slope_out = slope_in - intercept / f
        assert abs(intercept + v * slope_out - image_h) < 1e-12
    ax.axhline(0, color="#777777", lw=1)
    ax.plot([0, 0], [-1.25, 0.8], color="#25475c", lw=3)
    ax.plot([v, v], [-1.25, 0.8], color="#a3a3a3", lw=5, alpha=0.6)
    ax.text(0, 0.86, "thin lens", ha="center", fontsize=10)
    ax.text(v, 0.86, "screen", ha="center", fontsize=10)
    ax.scatter([-f, f], [0, 0], color="#222222", s=20, zorder=5)
    for x, label in [(-f, "front F"), (f, "rear F")]:
        ax.text(x, -0.17 if x < 0 else 0.08, label, ha="center", fontsize=9)
    end = v  # An opaque screen intercepts the bundle here.
    ray(ax, [-u, 0, end], [h, h, h * (1 - end / f)], "#006ca8")
    ray(ax, [-u, 0, end], [h, 0, -h * end / u], "#c95a16")
    for x, height, color in [(-u, h, "#813c98"), (v, image_h, "#19764b")]:
        ax.annotate("", xy=(x, height), xytext=(x, 0),
                    arrowprops={"arrowstyle": "-|>", "color": color,
                                "lw": 3, "mutation_scale": 17})
    ax.text(-u, h + 0.11, "object: +0.50 cm", ha="center", color="#813c98",
            fontsize=10)
    ax.text(v, image_h - 0.28, f"image: {image_h:+.2f} cm", ha="center",
            color="#19764b", fontsize=10)
    m_text = "−1/2" if u == 30 else "−2"
    ax.set_title(f"{letter}   u = {u:g} cm, v = {v:g} cm, m = {m_text}",
                 loc="left", fontsize=12, pad=12)
    ax.set_xlim(-36, 38)
    ax.set_ylim(-1.48, 1.02)
    ax.set_xticks([-30, -20, -10, 0, 10, 20, 30])
    ax.set_yticks([-1, -0.5, 0, 0.5])
    ax.set_ylabel("height (cm)", fontsize=10)
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(labelsize=9)


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, axes = plt.subplots(2, 1, figsize=(9, 6.6))
    for ax, u, letter in zip(axes, [30.0, 15.0], ["A", "B"]):
        diagram(ax, u, letter)
    axes[-1].set_xlabel("x (cm); light travels to the right →", fontsize=10)
    fig.suptitle("Real images: rays meet on the screen", fontsize=15, y=0.98)
    fig.text(0.5, 0.018,
             "Ideal thin lens, f = 10 cm • same scales in both panels • vertical scale enlarged • no measured data",
             ha="center", fontsize=9)
    fig.subplots_adjust(left=0.09, right=0.97, bottom=0.11, top=0.89, hspace=0.5)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)
    print("Real-image ray geometry: 26 arbitrary-height rays checked.")


if __name__ == "__main__":
    main()
