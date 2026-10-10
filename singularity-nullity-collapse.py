"""Exact toy geometry of diag(1,t); output an opaque PNG basename to CWD.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 3, figsize=(10.5, 4.6), dpi=120)
    fig.subplots_adjust(left=0.065, right=0.985, bottom=0.24, top=0.77, wspace=0.29)
    for ax, t in zip(axes, [1, 0.15, 0]):
        a = np.diag([1., t])
        samples = np.array([[0.4, -0.8], [0.4, 0], [0.4, 0.8]])
        mapped = samples @ a.T
        np.testing.assert_allclose(mapped[:, 0], 0.4)
        np.testing.assert_allclose(mapped[:, 1], t * samples[:, 1])
        ax.set_facecolor("white")
        ax.axhline(0, color="#bbbbbb", lw=0.8)
        ax.axvline(0, color="#bbbbbb", lw=0.8)
        ax.add_patch(Rectangle((-1, -1), 2, 2, fill=False, ec="#aaaaaa",
                               ls="--", lw=1.3))
        if t:
            ax.add_patch(Rectangle((-1, -t), 2, 2*t, fc="#dcebf5",
                                   ec="#246c9b", lw=2))
            ax.plot(mapped[:, 0], mapped[:, 1], color="#bd572f", lw=2)
            ax.scatter(mapped[:, 0], mapped[:, 1], c="#bd572f", s=35, zorder=4)
        else:
            ax.plot([-1, 1], [0, 0], color="#246c9b", lw=4)
            ax.scatter([0.4], [0], c="#bd572f", s=65, zorder=4)
            ax.annotate("All three inputs\nmeet at (0.4, 0)", (0.4, 0),
                        xytext=(-0.2, 0.48), ha="center", fontsize=10,
                        arrowprops={"arrowstyle": "->", "color": "#bd572f"})
        ax.set(xlim=(-1.25, 1.25), ylim=(-1.25, 1.25),
               xticks=[-1, 0, 1], yticks=[-1, 0, 1], xlabel="Output coordinate 1")
        ax.set_aspect("equal")
        ax.set_title(f"t = {t:g}\n" + ("Rank 2; nullity 0" if t else "Rank 1; nullity 1"),
                     fontsize=12, pad=12)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set_ylabel("Output coordinate 2")
    fig.suptitle(r"$A(t)(x,y)=(x,ty)$: compression becomes information loss only at $t=0$",
                 fontsize=14, y=0.97)
    fig.text(0.5, 0.105, "Dashed: original square [−1, 1]².  Blue: its image under A(t).",
             ha="center", fontsize=11)
    fig.text(0.5, 0.055, "Orange: images of (0.4, −0.8), (0.4, 0), (0.4, 0.8).  Exact toy geometry, not measured data.",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
