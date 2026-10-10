"""Weighted squared deviations for two synthetic groups; output to CWD."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def objective(c):
    return 2 * (90 - c) ** 2 + 8 * (60 - c) ** 2


def main():
    c = np.linspace(50, 90, 500)
    assert objective(66) == 1440 and objective(75) == 2250
    np.testing.assert_allclose(objective(c), 1440 + 10 * (c - 66) ** 2)
    fig, ax = plt.subplots(figsize=(9, 5.2), dpi=120)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.plot(c, objective(c), color="#2768a6", linewidth=2.4,
            label=r"$S(c)=2(90-c)^2+8(60-c)^2$")
    ax.scatter([66, 75], [1440, 2250], s=65,
               color=["#207745", "#80519d"], zorder=4)
    ax.annotate("Weighted mean\n(66, 1440)", (66, 1440), (52, 2100),
                arrowprops={"arrowstyle": "->", "color": "#207745"},
                color="#207745", fontsize=11)
    ax.annotate("Equal-weight group mean\n(75, 2250)", (75, 2250), (72, 3900),
                arrowprops={"arrowstyle": "->", "color": "#80519d"},
                color="#80519d", fontsize=11)
    ax.annotate("", (75, 2250), (75, 1440),
                arrowprops={"arrowstyle": "<->", "color": "#80519d"})
    ax.text(76, 1770, "+810", color="#80519d", fontsize=11)
    ax.hlines(1440, 66, 75, linestyle=":", color="#777777")
    ax.set(xlim=(50, 90), ylim=(900, 7600), xlabel="Common replacement value c",
           ylabel="Weighted sum of squared deviations",
           title="The weighted mean uniquely minimizes squared deviations")
    ax.grid(alpha=0.18)
    ax.legend(loc="upper left", frameon=False)
    fig.tight_layout()
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
