"""Original MANOVA geometry; Python 3.14.4 / NumPy 2.3.5 / Matplotlib 3.10.7.
Output the basename PNG to CWD; respect the caller's MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse


def main():
    covariance = np.array([[1.0, 0.94], [0.94, 1.0]])
    means = [np.array([-0.35, 0.35]), np.array([0.35, -0.35])]
    colors = ["#2369a5", "#cd6325"]
    values, vectors = np.linalg.eigh(covariance)
    major = vectors[:, -1]
    angle = np.degrees(np.arctan2(major[1], major[0]))
    fig, axes = plt.subplots(1, 3, figsize=(12, 4.5), dpi=100, facecolor="white", constrained_layout=True)
    for mean, color, name in zip(means, colors, ["Group A", "Group B"]):
        axes[0].add_patch(Ellipse(mean, 2*np.sqrt(values[-1]), 2*np.sqrt(values[0]), angle=angle, facecolor=color, alpha=0.14, edgecolor=color, lw=2))
        axes[0].plot(*mean, "o", color=color, label=name)
    axes[0].set(xlim=(-1.8, 1.8), ylim=(-1.8, 1.8), xlabel="Response 1", ylabel="Response 2", title="One-SD covariance contours")
    axes[0].set_aspect("equal")
    axes[0].legend(loc="upper left", fontsize=9)
    projections = [np.array([1., 0.]), np.array([1., -1.])/np.sqrt(2)]
    for ax, direction, title in zip(axes[1:], projections, ["Overlapping marginal response", "A low-variance joint contrast"]):
        variance = direction @ covariance @ direction
        grid = np.linspace(-3, 3, 900)
        for mean, color in zip(means, colors):
            projected_mean = mean @ direction
            density = np.exp(-(grid-projected_mean)**2/(2*variance))/np.sqrt(2*np.pi*variance)
            ax.plot(grid, density, color=color, lw=2)
        ax.set(xlabel="Response 1" if ax is axes[1] else r"$(X_1-X_2)/\sqrt{2}$", ylabel="Density", title=title)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Joint mean separation depends on covariance geometry", fontsize=15)
    fig.savefig(Path.cwd() / "paper-46-manova-geometry.png", facecolor="white", transparent=False)
    plt.close(fig)

if __name__ == "__main__":
    main()
