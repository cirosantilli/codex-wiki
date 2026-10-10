"""Original circles/ellipses of projection error; PNG basename to CWD."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 5), dpi=120)
    fig.patch.set_facecolor("white")
    x = np.array([3., 1.])
    e = np.array([1., 2.])
    theta = np.linspace(0, 2*np.pi, 601)
    cases = [
        (np.array([1., 1.]), "Ordinary dot product", "(1, 2)",
         r"$\|x-p\|^2=5$"),
        (np.array([4., 1.]), "Weight first-coordinate errors by 4",
         "(7/4, 7/2)", r"$\|x-p\|_M^2=25/2$"),
    ]
    for ax, (weights, title, label, footer) in zip(axes, cases):
        p = e*np.sum(weights*x*e)/np.sum(weights*e*e)
        residual = x-p
        squared_distance = np.sum(weights*residual**2)
        radius = np.sqrt(squared_distance/weights)
        contour = x[:, None] + radius[:, None]*np.array(
            [np.cos(theta), np.sin(theta)])
        ax.plot(contour[0], contour[1], color="#2878a5", lw=2)
        t = np.linspace(-1.5, 2.55, 201)
        ax.plot(t, 2*t, color="#888888", lw=2)
        ax.plot([p[0], x[0]], [p[1], x[1]], color="#28865b",
                lw=2, ls="--")
        ax.scatter([x[0]], [x[1]], color="#2878a5", s=45, zorder=4)
        ax.scatter([p[0]], [p[1]], color="#c05b20", s=50, zorder=4)
        ax.text(3.12, 1.05, "x = (3, 1)", fontsize=11)
        ax.annotate("p = " + label, p,
                    xytext=(.06, .89 if weights[0] == 4 else .7),
                    textcoords="axes fraction", fontsize=11,
                    color="#a74a12",
                    arrowprops={"arrowstyle": "->", "color": "#a74a12"})
        ax.text(.5, -.25, footer, transform=ax.transAxes,
                ha="center", fontsize=12)
        ax.set_xlim(-.6, 5.5)
        ax.set_ylim(-3, 5)
        ax.set_aspect("equal")
        ax.set_xlabel("First coordinate")
        ax.set_ylabel("Second coordinate")
        ax.set_title(title, fontsize=11.5, pad=12)
        ax.grid(alpha=.17)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("The smallest error contour touches the allowed line at the optimum",
                 fontsize=13, y=.98)
    fig.subplots_adjust(left=.07, right=.98, top=.83, bottom=.25, wspace=.23)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
