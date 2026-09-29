"""Mean/contrast decomposition of a three-coordinate cyclic representation."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    p = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    b = np.column_stack((np.array([2, -1, -1]) / np.sqrt(6),
                         np.array([0, 1, -1]) / np.sqrt(2)))
    rotation = np.array([[-0.5, -np.sqrt(3) / 2],
                         [np.sqrt(3) / 2, -0.5]])
    assert np.allclose(b.T @ b, np.eye(2))
    assert np.allclose(b.T @ p @ b, rotation)
    assert np.array_equal(np.linalg.matrix_power(p, 3), np.eye(3))
    x = np.array([4, 1, 1])
    mean = np.full(3, x.mean())
    contrast = x - mean
    assert np.array_equal(contrast, [2, -1, -1])

    fig, axes = plt.subplots(1, 2, figsize=(10.5, 5.3), dpi=120)
    fig.patch.set_facecolor("white")
    sites = np.arange(3)
    colors = ["#333e60", "#147c67", "#c76716"]
    for offset, values, color, label in zip(
            [-0.24, 0, 0.24], [x, mean, contrast], colors,
            ["original", "fixed mean", "zero-sum contrast"]):
        bars = axes[0].bar(sites + offset, values, 0.23, color=color, label=label)
        axes[0].bar_label(bars, padding=3, fontsize=11)
    axes[0].axhline(0, color="#444444", lw=0.8)
    axes[0].set_xticks(sites, ["1", "2", "3"])
    axes[0].set_xlabel("Coordinate label")
    axes[0].set_ylabel("Value")
    axes[0].set_ylim(-1.6, 4.8)
    axes[0].set_title(r"$(4,1,1)=2(1,1,1)+(2,-1,-1)$", fontsize=13)
    axes[0].legend(loc="upper center", bbox_to_anchor=(0.5, -0.24),
                   ncol=3, frameon=False, fontsize=10, columnspacing=1)
    ax = axes[1]
    ax.set_aspect("equal")
    ax.set_xlim(-3.1, 3.7)
    ax.set_ylim(-3.1, 3.1)
    t = np.linspace(0, 2 * np.pi, 400)
    ax.plot(np.sqrt(6) * np.cos(t), np.sqrt(6) * np.sin(t),
            ls="--", color="#c5cbd1", lw=1)
    vectors = [np.linalg.matrix_power(p, n) @ contrast for n in range(3)]
    labels = [r"$v=(2,-1,-1)$", r"$Pv=(-1,2,-1)$",
              r"$P^2v=(-1,-1,2)$"]
    for vector, label, color in zip(vectors, labels, colors):
        xy = b.T @ vector
        ax.annotate("", xy=xy, xytext=(0, 0),
                    arrowprops={"arrowstyle": "-|>", "color": color,
                                "lw": 2.5, "mutation_scale": 18})
        pos = xy * 1.08
        ax.text(*pos, label, color=color, fontsize=10,
                ha="right" if xy[0] >= 0 else "center",
                va="bottom" if xy[1] >= 0 else "top")
    ax.axhline(0, color="#eeeeee", zorder=0)
    ax.axvline(0, color="#eeeeee", zorder=0)
    ax.set_xlabel(r"Coefficient of $u=(2,-1,-1)/\sqrt{6}$")
    ax.set_ylabel(r"Coefficient of $v_{\rm basis}=(0,1,-1)/\sqrt{2}$")
    ax.set_title("The contrast plane: rotation by 120 degrees", fontsize=13)
    fig.suptitle("A symmetry-preserved line plus a symmetry-preserved plane",
                 fontsize=16, y=0.98)
    fig.subplots_adjust(left=0.07, right=0.98, bottom=0.24, top=0.84, wspace=0.36)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
