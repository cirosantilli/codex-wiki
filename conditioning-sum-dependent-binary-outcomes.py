"""Restrict independent binary outcomes to pairs with exactly one success.

All masses are derived exactly from a finite stipulated model, not observations.
Run in the output directory; versions are documented in pyproject.toml.
"""

from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def model():
    joint = {(x, y): Fraction(1, 4) for x in (0, 1) for y in (0, 1)}
    selected_mass = sum(p for (x, y), p in joint.items() if x + y == 1)
    conditional = {xy: p / selected_mass if sum(xy) == 1 else Fraction(0)
                   for xy, p in joint.items()}
    ex = sum(x * p for (x, y), p in conditional.items())
    ey = sum(y * p for (x, y), p in conditional.items())
    exy = sum(x * y * p for (x, y), p in conditional.items())
    assert selected_mass == Fraction(1, 2)
    assert ex == ey == Fraction(1, 2)
    assert exy - ex * ey == -Fraction(1, 4)
    assert conditional[1, 1] == 0 and ex * ey == Fraction(1, 4)
    return joint, conditional


def main():
    fig, axes = plt.subplots(1, 2, figsize=(7.5, 4.0), dpi=130, layout="constrained")
    fig.set_facecolor("white")
    for ax, law, title in zip(axes, model(), ("All pairs: independent", r"Selected pairs: $X+Y=1$")):
        data = np.array([[float(law[x, y]) for y in (0, 1)] for x in (0, 1)])
        ax.imshow(data, cmap="Blues", vmin=0, vmax=0.6)
        for x in (0, 1):
            for y in (0, 1):
                ax.text(y, x, f"{data[x, y]:g}", ha="center", va="center", fontsize=20,
                        color="white" if data[x, y] > 0.35 else "#111111")
        ax.set_xticks((0, 1), labels=("0", "1"))
        ax.set_yticks((0, 1), labels=("0", "1"))
        ax.set(xlabel=r"$Y$", ylabel=r"$X$", title=title)
        ax.tick_params(length=0)
    fig.suptitle("Conditioning can create dependence", fontsize=14)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
