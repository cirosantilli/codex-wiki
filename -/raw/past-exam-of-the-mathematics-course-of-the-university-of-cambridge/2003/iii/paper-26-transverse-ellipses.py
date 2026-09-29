"""Original transverse-ellipse examples; Python 3.14, NumPy and Matplotlib.

Write the PNG basename to the caller's working directory. MPLCONFIGDIR is
provided by the caller; this generator leaves that environment setting intact.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def main():
    t = np.linspace(0, 2 * np.pi, 1201)
    unit = np.column_stack((np.cos(t), np.sin(t)))
    fig, axes = plt.subplots(1, 3, figsize=(10.8, 3.5), dpi=100, facecolor="white")
    examples = [
        (np.array([0.0, 0.0]), np.array([0.55, 0.4]), np.empty((0, 2)), 0),
        (np.array([0.8, 0.0]), np.array([1.0, 1.0]),
         np.array([[0.4, np.sqrt(0.84)], [0.4, -np.sqrt(0.84)]]), 2),
    ]
    major, minor = 1.4, 0.65
    x2 = (1 - 1 / minor**2) / (1 / major**2 - 1 / minor**2)
    x, y = np.sqrt(x2), np.sqrt(1 - x2)
    examples.append((np.zeros(2), np.array([major, minor]),
                     np.array([[sx * x, sy * y] for sx in (-1, 1) for sy in (-1, 1)]), 4))
    for ax, (center, semiaxes, points, count) in zip(axes, examples):
        second = center + unit * semiaxes
        ax.set_facecolor("white")
        ax.plot(unit[:, 0], unit[:, 1], color="#2463a5", lw=2.3, label="First ellipse")
        ax.plot(second[:, 0], second[:, 1], color="#dc6d20", lw=2.3, label="Second ellipse")
        if len(points):
            assert np.allclose(np.sum(points**2, axis=1), 1)
            assert np.allclose(np.sum(((points - center) / semiaxes)**2, axis=1), 1)
            g1 = 2 * points
            g2 = 2 * (points - center) / semiaxes**2
            determinants = g1[:, 0] * g2[:, 1] - g1[:, 1] * g2[:, 0]
            assert np.all(np.abs(determinants) > 1e-6)
            ax.scatter(points[:, 0], points[:, 1], color="#242424", s=22, zorder=5)
        ax.set(xlim=(-1.5, 2.05), ylim=(-1.35, 1.35), aspect="equal")
        ax.axis("off")
        ax.set_title(f"{count} intersection points", fontsize=12, pad=9)
    axes[1].legend(loc="lower center", bbox_to_anchor=(0.5, -0.16), ncol=2,
                   fontsize=9, frameon=False, handlelength=1.7)
    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.16, top=0.89, wspace=0.08)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100,
                facecolor="white", edgecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
