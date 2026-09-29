"""Compare inverse relativistic and Galilean velocity composition.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Writes an opaque white PNG to the current working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    frame_beta = 0.6
    particle_beta = np.linspace(-1.0, 1.0, 801)
    composed_beta = (particle_beta + frame_beta) / (
        1.0 + frame_beta * particle_beta
    )
    blue, orange = "#176b9c", "#bf5a15"
    fig, ax = plt.subplots(figsize=(7.2, 4.8), dpi=120)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.axhspan(-1, 1, color="#eef5fa", zorder=0)
    ax.axhspan(1, 1.75, color="#fff1e9", zorder=0)
    ax.plot(particle_beta, composed_beta, color=blue, lw=2.6,
            label=r"Relativistic: $(u'/c+0.6)/(1+0.6u'/c)$")
    ax.plot(particle_beta, particle_beta + frame_beta, color=orange,
            lw=2.2, ls="--", label=r"Galilean: $u'/c+0.6$")
    for bound in (-1, 1):
        ax.axhline(bound, color="0.35", ls=":", lw=1.2)
    ax.axhline(0, color="0.65", lw=0.8)
    ax.axvline(0, color="0.65", lw=0.8)
    ax.scatter([-1, 1], [-1, 1], s=55, facecolor="white",
               edgecolor=blue, linewidth=1.7, zorder=5)
    ax.scatter([0.6], [15 / 17], color=blue, s=48, zorder=6)
    ax.scatter([0.6], [1.2], color=orange, s=48, zorder=6)
    ax.annotate(r"$u'=0.6c$: $u=15c/17$", (0.6, 15 / 17),
                xytext=(-0.30, 0.08), color=blue, fontsize=11,
                arrowprops={"arrowstyle": "->", "color": blue})
    ax.annotate(r"Galilean result: $1.2c$", (0.6, 1.2),
                xytext=(0.02, 1.42), color=orange, fontsize=11,
                arrowprops={"arrowstyle": "->", "color": orange})
    ax.text(-0.94, -0.88, r"Massive particles: $|u|<c$",
            color=blue, fontsize=11)
    ax.set(xlim=(-1.05, 1.05), ylim=(-1.13, 1.72),
           xlabel=r"Particle velocity in moving frame $S'$: $u'/c$",
           ylabel=r"Particle velocity in laboratory frame $S$: $u/c$",
           title=r"Velocity composition with $V=0.6c$")
    ax.set_xticks(np.linspace(-1, 1, 5))
    ax.set_yticks([-1, -0.5, 0, 0.5, 1, 1.5])
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(alpha=0.16)
    ax.legend(loc="upper left", framealpha=1, fontsize=9)
    fig.text(0.5, 0.025,
             "Open endpoints represent light; the blue curve stays between them "
             "for massive particles.", ha="center", fontsize=9)
    fig.tight_layout(rect=(0, 0.06, 1, 1))
    fig.savefig(Path.cwd() / "relativistic-velocity-addition.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
