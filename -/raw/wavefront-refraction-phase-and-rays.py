"""Original phase-matching model; outputs its PNG basename to the current directory.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np


def main():
    n1, n2, tangential = 1.0, 1.5, 0.5
    normals = np.sqrt(np.array([n1, n2]) ** 2 - tangential**2)
    theta2 = np.arcsin(tangential / n2)
    assert np.isclose(np.rad2deg(theta2), 19.47122063449069)
    for n, normal in zip([n1, n2], normals):
        wavefront_tangent = np.array([-tangential, normal])
        ray = np.array([normal, tangential]) / n
        assert abs(np.dot(ray, wavefront_tangent)) < 1e-14
        assert np.isclose(np.linalg.norm(ray), 1)
        assert np.isclose(np.dot([normal, tangential], ray), n)

    plt.rcParams.update({"font.size": 12, "axes.titlesize": 15})
    fig, ax = plt.subplots(figsize=(9, 6.3), dpi=120, facecolor="white")
    fig.subplots_adjust(left=0.08, right=0.97, bottom=0.2, top=0.82)
    ax.axvspan(-3.2, 0, color="#f1f6fa")
    ax.axvspan(0, 3.2, color="#fff6e8")
    y = np.linspace(-2.35, 2.35, 1000)
    for m in range(-5, 6):
        for side, normal in enumerate(normals):
            x = (m - tangential * y) / normal
            mask = (x >= -3.2) & (x <= 0) if side == 0 else (x >= 0) & (x <= 3.2)
            ax.plot(x[mask], y[mask], color="#2176ae", lw=2)
    for intercept in [-1.1, 0, 1.1]:
        for side, normal in enumerate(normals):
            x = np.linspace(-3.2, 0, 100) if side == 0 else np.linspace(0, 3.2, 100)
            ax.plot(x, intercept + tangential / normal * x, color="#b84a2b", lw=2)
            start = -1.65 if side == 0 else 1.0
            end = start + 0.65
            ax.annotate("", xy=(end, intercept + tangential / normal * end),
                        xytext=(start, intercept + tangential / normal * start),
                        arrowprops={"arrowstyle": "-|>", "color": "#b84a2b", "lw": 2})
    ax.axvline(0, color="#444444", lw=1.6)
    ax.plot([-0.65, 0.65], [0, 0], color="#555555", ls="--", lw=1.3)
    ax.text(-2.8, 1.97, r"$n_1=1$", bbox={"facecolor": "white", "edgecolor": "none"})
    ax.text(2.12, -2.12, r"$n_2=3/2$", bbox={"facecolor": "white", "edgecolor": "none"})
    ax.text(0.08, 2.08, "interface", fontsize=11, bbox={"facecolor": "white", "edgecolor": "none"})
    ax.set(xlim=(-3.2, 3.2), ylim=(-2.35, 2.35), xlabel=r"$x/\lambda_0$", ylabel=r"$y/\lambda_0$")
    ax.set_aspect("equal")
    ax.set_title("Equal-phase surfaces turn; rays follow their normals", pad=14)
    handles = [Line2D([], [], color="#2176ae", lw=2, label=r"wavefronts: $S=m\lambda_0$"),
               Line2D([], [], color="#b84a2b", lw=2, label="forward rays")]
    fig.legend(handles=handles, loc="lower center", bbox_to_anchor=(0.5, 0.075), ncol=2, frameon=False)
    fig.text(0.5, 0.94, "Original ideal plane-wave model • incident and transmitted branches", ha="center", fontsize=12)
    fig.text(0.5, 0.027, r"$\theta_1=30^\circ$    $\theta_2=19.4712^\circ$    normal spacing: $\lambda_0$ then $2\lambda_0/3$", ha="center", fontsize=12)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
