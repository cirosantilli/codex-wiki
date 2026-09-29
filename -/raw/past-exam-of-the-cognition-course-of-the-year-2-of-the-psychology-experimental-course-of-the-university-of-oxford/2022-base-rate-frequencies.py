"""Original nested-frequency illustration. Writes matching PNG in CWD.

Python 3.14 / Matplotlib 3.10; dependencies are in the root pyproject.toml.
All counts are teaching choices, not results from an experiment.
"""

from fractions import Fraction
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    n_h, n_other = 200, 800
    hits = n_h * Fraction(3, 4)
    other_cues = n_other * Fraction(1, 4)
    posterior = hits / (hits + other_cues)
    assert (hits, other_cues, posterior) == (150, 200, Fraction(3, 7))
    fig, ax = plt.subplots(figsize=(8, 4), dpi=100, facecolor="white")
    ax.set(xlim=(0, 10), ylim=(0, 5))
    ax.axis("off")
    blue, orange, ink = "#276586", "#bc611e", "#18364c"
    ax.text(5, 4.72, "One population, then one common cue", ha="center",
            fontsize=16, weight="bold", color=ink)
    ax.text(5, 4.34, "1,000 cases before seeing the cue", ha="center", fontsize=12)
    for x, w, color, label in [(0.5, 1.8, blue, "200 H"),
                                (2.3, 7.2, orange, "800 not H")]:
        ax.add_patch(Rectangle((x, 3.62), w, .49, color=color))
        ax.text(x + w/2, 3.865, label, ha="center", va="center", color="white", fontsize=12)
    for x, label, color in [(2.0, "Cue in 75% of H\n150 cue + 50 no cue", blue),
                             (7.1, "Cue in 25% of not H\n200 cue + 600 no cue", orange)]:
        ax.text(x, 2.95, label, ha="center", va="center", color=color, fontsize=12,
                linespacing=1.6)
    ax.annotate("", (2.0, 3.27), (1.4, 3.61), arrowprops={"arrowstyle":"->", "color":blue})
    ax.annotate("", (7.1, 3.27), (6.0, 3.61), arrowprops={"arrowstyle":"->", "color":orange})
    ax.text(5, 2.14, "Among the 350 cue-positive cases", ha="center", fontsize=12)
    left_width = float(6 * posterior)
    for x, w, color, label in [(2, left_width, blue, "150 H"),
                                (2 + left_width, 6 - left_width, orange, "200 not H")]:
        ax.add_patch(Rectangle((x, 1.43), w, .49, color=color))
        ax.text(x+w/2, 1.675, label, ha="center", va="center", color="white", fontsize=12)
    ax.text(5, .83, r"$P(H\mid E)=150/(150+200)=3/7\approx0.429$",
            ha="center", fontsize=16, color=ink)
    ax.text(5, .25, "Constructed teaching counts — not participant responses",
            ha="center", fontsize=10, color="#465965")
    fig.subplots_adjust(left=.02, right=.98, top=.98, bottom=.02)
    fig.savefig(Path(__file__).with_suffix(".png").name, transparent=False,
                facecolor="white", metadata={"Software":"Matplotlib"})
    plt.close(fig)


if __name__ == "__main__":
    main()
