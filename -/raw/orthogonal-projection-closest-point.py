"""Original closest-point geometry and squared error; PNG basename to CWD."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 4.5), dpi=120)
    fig.patch.set_facecolor("white")
    ax = axes[0]
    x = np.array([3., 1.])
    p = np.array([1., 2.])
    t = np.linspace(-.2, 1.8, 101)
    ax.plot(t, 2*t, color="#888888", lw=2)
    for endpoint, color in [(x, "#2878a5"), (p, "#c05b20")]:
        ax.annotate("", endpoint, xytext=(0, 0),
                    arrowprops={"arrowstyle": "->", "lw": 2.3,
                                "color": color})
    ax.annotate("", x, xytext=p,
                arrowprops={"arrowstyle": "->", "lw": 2,
                            "linestyle": "--", "color": "#28865b"})
    a = np.array([1., 2.])/np.sqrt(5)*.18
    b = np.array([2., -1.])/np.sqrt(5)*.18
    square = np.array([p+a, p+a+b, p+b])
    ax.plot(square[:, 0], square[:, 1], color="#555555", lw=1.2)
    ax.scatter([0, p[0], x[0]], [0, p[1], x[1]], s=35,
               color=["#444444", "#c05b20", "#2878a5"], zorder=4)
    ax.text(3.08, 1.03, "x = (3, 1)", fontsize=11)
    ax.text(.1, 2.23, "p = (1, 2)", fontsize=11, color="#a74a12")
    ax.text(1.85, 1.78, "r = (2, -1)", fontsize=11, color="#22734d")
    ax.text(1.36, 3.53, "W: y = 2x", fontsize=11, color="#555555")
    ax.set_xlim(-.5, 4.1)
    ax.set_ylim(-.4, 4)
    ax.set_aspect("equal")
    ax.set_title("Residual perpendicular to the allowed line", fontsize=12)
    ax.set_xlabel("First coordinate")
    ax.set_ylabel("Second coordinate")
    ax = axes[1]
    t = np.linspace(-.4, 2.4, 501)
    error = (3-t)**2+(1-2*t)**2
    ax.plot(t, error, color="#2878a5", lw=2.4)
    ax.axhline(5, color="#888888", ls="--", lw=1.2)
    ax.scatter([1], [5], s=55, color="#c05b20", zorder=3)
    ax.annotate("unique minimum: t = 1, error = 5", (1, 5),
                xytext=(.1, 9.3), fontsize=10.5,
                arrowprops={"arrowstyle": "->", "color": "#777777"})
    ax.set_xlim(-.4, 2.4)
    ax.set_ylim(3, 16)
    ax.set_xlabel("Coefficient t of the candidate (t, 2t)")
    ax.set_ylabel("Squared Euclidean error")
    ax.set_title(r"$\|x-t(1,2)\|^2=5(t-1)^2+5$", fontsize=12)
    for ax in axes:
        ax.grid(alpha=.17)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Projection turns closest-point fitting into orthogonality",
                 fontsize=14, y=.98)
    fig.subplots_adjust(left=.065, right=.98, top=.82, bottom=.16, wspace=.28)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
