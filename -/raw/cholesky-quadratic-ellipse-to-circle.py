"""Map an exact quadratic-form ellipse to a circle; output PNG to CWD."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    lower = np.array([[2., 0.], [1., 2.]])
    a = lower @ lower.T
    theta = np.linspace(0, 2*np.pi, 721)
    circle = np.vstack((np.cos(theta), np.sin(theta)))
    ellipse = np.linalg.solve(lower.T, circle)
    assert np.allclose(np.einsum("ij,ij->j", ellipse, a @ ellipse), 1)
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.3), dpi=120)
    fig.patch.set_facecolor("white")
    for ax in axes:
        ax.set_aspect("equal")
        ax.axhline(0, color="#aaaaaa", lw=.7)
        ax.axvline(0, color="#aaaaaa", lw=.7)
        ax.grid(color="#e3e3e3", lw=.6)
        ax.spines[["top", "right"]].set_visible(False)
        ax.tick_params(labelsize=11)
    axes[0].plot(*ellipse, color="#26718b", lw=2.5)
    axes[0].set(xlim=(-.7, .7), ylim=(-.7, .7), xlabel=r"$u_1$", ylabel=r"$u_2$")
    axes[0].set_title(r"$4u_1^2+4u_1u_2+5u_2^2=1$", fontsize=15, pad=15)
    axes[1].plot(*circle, color="#26718b", lw=2.5)
    axes[1].set(xlim=(-1.3, 1.3), ylim=(-1.3, 1.3), xlabel=r"$z_1$", ylabel=r"$z_2$")
    axes[1].set_title(r"$z_1^2+z_2^2=1$", fontsize=15, pad=15)
    points = [(np.array([.5, 0]), "#ba6429", (.05, -.11), (.07, -.15)), (np.array([-.25, .5]), "#62812e", (-.36, .07), (-.4, .12))]
    for u, color, off_u, off_z in points:
        z = lower.T @ u
        axes[0].scatter(*u, color=color, s=58, zorder=4)
        axes[1].scatter(*z, color=color, s=58, zorder=4)
        label_u = "(1/2, 0)" if u[0] > 0 else "(-1/4, 1/2)"
        label_z = "(1, 0)" if z[0] > .5 else "(0, 1)"
        axes[0].annotate(label_u, u, xytext=u+off_u, fontsize=11, color=color)
        axes[1].annotate(label_z, z, xytext=z+off_z, fontsize=11, color=color)
    fig.suptitle(r"Cholesky coordinates: $z=L^Tu=(2u_1+u_2,\ 2u_2)^T$", fontsize=18, weight="bold")
    fig.text(.5, .035, r"The same points satisfy $u^TAu=\|L^Tu\|_2^2=\|z\|_2^2=1$.", ha="center", fontsize=13)
    fig.subplots_adjust(left=.08, right=.97, top=.81, bottom=.17, wspace=.32)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
