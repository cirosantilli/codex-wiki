"""Illustrate an original convex chain; tested with Python 3.14.4.

Uses the root project's matplotlib dependency. Writes its PNG basename to CWD.
"""
from pathlib import Path
import os
import tempfile

os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "paper12-matplotlib"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    fig, ax = plt.subplots(figsize=(6.4, 4.6), dpi=140)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.fill([0, 1, 1], [0, 0, 1], color="#edf3fa")
    ax.plot([0, 1, 1, 0], [0, 0, 1, 0], color="#8897aa", lw=1.3)
    xs = [0, 0.17, 0.43, 0.72, 1]
    ys = [x*x for x in xs]
    ax.plot(xs, ys, color="#b24c30", lw=2.2, zorder=3)
    ax.scatter(xs[1:-1], ys[1:-1], color="#b24c30", s=38, zorder=4)
    ax.scatter([0, 1], [0, 1], color="#203c5c", s=40, zorder=4)
    for i in range(1, 4):
        ax.annotate(rf"$z_{{{i}}}$", (xs[i], ys[i]), xytext=(-3, 10),
                    textcoords="offset points", fontsize=11)
    for i in range(4):
        xm, ym = (xs[i]+xs[i+1])/2, (ys[i]+ys[i+1])/2
        ax.annotate(rf"$s_{{{i+1}}}={xs[i]+xs[i+1]:.2f}$", (xm, ym),
                    xytext=(12 if i==3 else -5, -18),
                    textcoords="offset points", fontsize=10, color="#7c341e")
    ax.annotate(r"$P_0$", (0, 0), xytext=(-15, 10),
                textcoords="offset points", fontsize=11, color="#203c5c")
    ax.annotate(r"$P_4$", (1, 1), xytext=(8, 0),
                textcoords="offset points", fontsize=11, color="#203c5c")
    ax.text(0.02, 0.97, "Triangle: $0\\leq y\\leq x\\leq1$\n"
            "$s_1<s_2<s_3<s_4$", fontsize=10.5, va="top", transform=ax.transAxes,
            bbox=dict(facecolor="white", edgecolor="none", pad=6))
    ax.set(xlim=(-0.09, 1.16), ylim=(-0.1, 1.11), xlabel="$x$", ylabel="$y$")
    ax.set_aspect("equal")
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title("Increasing slopes characterize a convex chain", fontsize=12, pad=14)
    fig.tight_layout()
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
