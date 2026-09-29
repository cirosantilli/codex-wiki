"""Cored-lens mapping. Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Writes only paper-72-cored-lens.png in the caller's current directory.
Uses the caller's MPLCONFIGDIR without overriding it.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

CORE = 0.3
STRENGTH = 1.0


def mapping(theta):
    return theta * (1 - STRENGTH / np.sqrt(theta**2 + CORE**2))


def bisect_source(left, right, source):
    fl = mapping(left) - source
    assert fl * (mapping(right) - source) < 0
    for _ in range(70):
        mid = (left + right) / 2
        fm = mapping(mid) - source
        if fl * fm <= 0:
            right = mid
        else:
            left, fl = mid, fm
    return (left + right) / 2


def main():
    radial = np.sqrt((STRENGTH * CORE**2)**(2/3) - CORE**2)
    tangential = np.sqrt(STRENGTH**2 - CORE**2)
    caustic = CORE * ((STRENGTH / CORE)**(2/3) - 1)**1.5
    source = caustic / 2
    roots = np.array([bisect_source(-2, -radial, source),
                      bisect_source(-radial, 0, source),
                      bisect_source(tangential, 2, source)])
    assert np.max(np.abs(mapping(roots) - source)) < 1e-14
    # Include the exact critical positions and image positions in the sampled grids.
    theta = np.unique(np.r_[np.linspace(-1.6, 1.6, 900), -radial, radial,
                             -tangential, 0, tangential, roots])
    r = np.unique(np.r_[np.linspace(0, 1.6, 600), radial, tangential])
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.2), facecolor="white")
    ax = axes[0]
    ax.plot(theta, mapping(theta), color="#365f9c", label=r"Lens map $\beta(\theta)$")
    ax.axhline(source, color="#a65722", label=r"Source $\beta=\beta_c/2$")
    ax.scatter(roots, np.full(3, source), color="#a65722", zorder=5)
    for i, root in enumerate(roots):
        ax.annotate(("Intermediate", "Central", "Outer")[i], (root, source),
                    xytext=(0, 10 if i != 1 else -22), textcoords="offset points",
                    ha="center", fontsize=9)
    ax.scatter([-radial, radial], mapping(np.array([-radial, radial])),
               facecolors="white", edgecolors="#365f9c", zorder=4)
    ax.set_xlabel(r"Signed image angle $\theta/\theta_E$")
    ax.set_ylabel(r"Source angle $\beta/\theta_E$")
    ax.set_title(r"Three intersections inside the radial caustic")
    ax.legend(loc="lower right", fontsize=9)
    ax = axes[1]
    ax.plot(r, 1 - STRENGTH / np.sqrt(r*r + CORE*CORE), color="#365f9c",
            label=r"Tangential $\lambda_t$")
    ax.plot(r, 1 - STRENGTH * CORE**2 / (r*r + CORE*CORE)**1.5, color="#268565",
            label=r"Radial $\lambda_r$")
    for critical, color, label in [(radial, "#268565", r"$\theta_r$"),
                                    (tangential, "#365f9c", r"$\theta_t$")]:
        ax.axvline(critical, color=color, linestyle=":")
        ax.scatter([critical], [0], color=color, zorder=5)
        ax.annotate(label, (critical, 0), xytext=(7, -20), textcoords="offset points")
    ax.set_title(r"Critical radii: Jacobian eigenvalue zeros")
    ax.set_xlabel(r"Image radius $r/\theta_E$")
    ax.set_ylabel("Mapping eigenvalue")
    ax.legend(loc="lower right", fontsize=9)
    for ax in axes:
        ax.set_facecolor("white")
        ax.axhline(0, color="#555555", linewidth=.8)
        ax.grid(alpha=.2)
    fig.suptitle(r"Softened isothermal lens: $\theta_c/\theta_E=0.3$", fontsize=12)
    fig.tight_layout()
    fig.savefig(Path.cwd() / "paper-72-cored-lens.png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
