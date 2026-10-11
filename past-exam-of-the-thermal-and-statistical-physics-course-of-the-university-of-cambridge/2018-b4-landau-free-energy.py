"""Original quartic Landau free-energy sketches; output PNG basename in cwd.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5 as declared in the
repository's top-level pyproject.toml. Coefficients and scales are illustrative.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    m = np.linspace(-1.35, 1.35, 650)
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 4.25), layout="constrained")
    fig.patch.set_facecolor("white")
    for ax, r, title in zip(axes, [1, -1],
                            [r"$T>T_c$: one minimum", r"$T<T_c$: two pure-phase minima"]):
        f = r * m**2 + m**4
        ax.plot(m, f, color="#236da4", lw=2.4)
        ax.axhline(0, color="#999999", lw=.7)
        ax.axvline(0, color="#aaaaaa", lw=.7, ls=":")
        ax.set(xlabel=r"Magnetization $M$ (scaled)", ylabel=r"$F-F_0$ (scaled)",
               xlim=(-1.35, 1.35), ylim=(-.42, 2.05), title=title)
        ax.spines[["top", "right"]].set_visible(False)
        if r > 0:
            ax.scatter([0], [0], color="black", zorder=5, s=30)
            ax.annotate(r"$\langle M\rangle=0$", (0, 0), (.15, .75),
                        arrowprops={"arrowstyle": "->"}, fontsize=12)
        else:
            minimum = np.sqrt(.5)
            ax.scatter([-minimum, minimum], [-.25, -.25], color="black", zorder=5, s=30)
            ax.annotate(r"$-M_0$", (-minimum, -.25), (-1.1, .55),
                        arrowprops={"arrowstyle": "->"}, fontsize=12)
            ax.annotate(r"$+M_0$", (minimum, -.25), (.75, .55),
                        arrowprops={"arrowstyle": "->"}, fontsize=12)
    fig.suptitle(r"Quartic Landau model: $F-F_0=rM^2+M^4$ with $r=+1$ and $r=-1$",
                 fontsize=12)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=140, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
