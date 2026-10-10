"""Draw the five deletions for a sample mean; tested with Python 3.14.4.

Dependencies: Matplotlib and NumPy from the root pyproject.toml.
Run through make _media/jackknife-leave-one-out.png. The opaque white PNG
is written in the current directory with the script's basename (1080 x 600).
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np


def main():
    data = np.array([1., 2., 3., 4., 10.])
    n = data.size
    means = np.array([np.delete(data, i).mean() for i in range(n)])
    assert data.mean() == 4
    np.testing.assert_allclose(means, [4.75, 4.5, 4.25, 4, 2.5], atol=0, rtol=0)
    assert means.mean() == data.mean()

    blue, orange, gray = "#176b91", "#b94a15", "#707070"
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, (table, plot) = plt.subplots(
        1, 2, figsize=(9, 5), gridspec_kw={"width_ratios": [1.15, 1]},
        layout="constrained", facecolor="white")
    fig.suptitle("Jackknife: delete each observation once\n"
                 "Data (1, 2, 3, 4, 10); full mean = 4", fontsize=16)

    table.set(xlim=(-1.8, 4.65), ylim=(5.9, -1.15))
    table.axis("off")
    table.set_title("Each row retains four observations", fontsize=12, pad=14)
    table.text(-1.65, -0.65, "Omit", color=gray, va="center")
    for j in range(n):
        table.text(j, -0.65, f"x{j + 1}", ha="center", va="center", color=gray)
    for i in range(n):
        row_color = orange if i == n - 1 else blue
        table.text(-1.65, i + 0.3, f"{data[i]:g}", color=row_color, va="center")
        for j, value in enumerate(data):
            table.text(j, i + 0.3, f"{value:g}", ha="center", va="center",
                       color=gray if j == i else row_color, fontsize=15)
            if i == j:
                table.plot([j - 0.24, j + 0.24], [i + 0.12, i + 0.48],
                           color=gray, linewidth=1.5)
        table.plot([-1.75, 4.45], [i + 0.8, i + 0.8], color="#e2e2e2", lw=0.7)
    table.text(1.25, 5.6, "Crossed value is omitted for that row only",
               ha="center", fontsize=10, color=gray)

    positions = np.arange(n)
    for i, value in enumerate(means):
        color = orange if i == n - 1 else blue
        plot.plot([data.mean(), value], [i, i], color=color, linewidth=2.5)
        plot.plot(value, i, "o", color=color, markersize=8)
        plot.annotate(f"{value:g}", (value, i), xytext=(0, -16),
                      textcoords="offset points", ha="center", color=color)
    plot.axvline(data.mean(), color="#333333", linestyle="--", linewidth=1.3)
    plot.set(xlim=(2.15, 5.1), ylim=(4.85, -0.85), xlabel="Mean of retained observations")
    plot.set_yticks(positions, [f"Omit {value:g}" for value in data])
    plot.set_xticks([2.5, 3, 3.5, 4, 4.5, 5])
    plot.set_title("Deletion means: largest shift when 10 is omitted", fontsize=11, pad=14)
    plot.grid(axis="x", color="#e2e2e2", linewidth=0.6)
    plot.legend(handles=[Line2D([0], [0], color="#333333", linestyle="--",
                               label="Full mean = 4")],
                loc="lower right", fontsize=10, framealpha=1)
    plot.spines["left"].set_visible(False)
    plot.tick_params(axis="y", length=0)

    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Saved {output} (1080 x 600)")
    print(f"mean={data.mean():g}; deletion means={means.tolist()}; average={means.mean():g}")
    print(f"Deletion effects={(means - data.mean()).tolist()}")


if __name__ == "__main__":
    main()
