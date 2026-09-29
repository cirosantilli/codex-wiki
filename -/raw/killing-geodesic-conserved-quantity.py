"""Original straight geodesic and Killing charges, in toy units with m=1.

Run from _media; writes only the matching PNG basename to the working directory.
Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path
import os

os.environ.setdefault("MPLCONFIGDIR", "/tmp/codex-wiki-matplotlib")
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, (path, charges) = plt.subplots(1, 2, figsize=(10.4, 5.3), layout="constrained")
    t = np.linspace(-1, 3, 201)
    x, y = 1 + t, 2 - t
    blue, orange, green = "#1769aa", "#c45412", "#19804d"
    path.plot(x, y, color=blue, lw=2.3, label="Straight geodesic")
    path.scatter([0], [0], s=18, color="#444444", zorder=4)
    path.annotate("origin", (0, 0), xytext=(5, 6), textcoords="offset points", fontsize=10)
    samples = np.array([0, 1, 2])
    sx, sy = 1 + samples, 2 - samples
    path.scatter(sx, sy, color=blue, s=32, zorder=5)
    path.quiver(sx, sy, -sy, sx, angles="xy", scale_units="xy", scale=4,
                color=orange, width=0.009, label="$K_{\\rm rot}=(-y,x)$", zorder=4)
    path.quiver([2], [1], [1], [-1], angles="xy", scale_units="xy", scale=1.7,
                color=green, width=0.009, label="$U=(1,-1)$", zorder=4)
    for tt, xx, yy in zip(samples, sx, sy):
        path.annotate(f"$t={tt}$", (xx, yy), xytext=(-29, -16),
                      textcoords="offset points", fontsize=11)
    path.set(xlim=(-0.7, 4.5), ylim=(-1.6, 3.6), xlabel="$x$", ylabel="$y$")
    path.set_aspect("equal")
    path.grid(alpha=0.2)
    path.set_title("$x=1+t,\\quad y=2-t$\n$K_{\\rm rot}$ varies along the straight path", pad=12)
    path.legend(loc="upper right", fontsize=10, framealpha=1)
    vx = np.gradient(x, t)
    vy = np.gradient(y, t)
    angular_momentum = x * vy - y * vx
    np.testing.assert_allclose(vx, 1, atol=1e-12)
    np.testing.assert_allclose(angular_momentum, -3, atol=1e-12)
    charges.plot(t, vx, color=green, lw=2.6, label="$p_x=v_x=1$")
    charges.plot(t, angular_momentum, color=orange, lw=2.6,
                 label="$L_z=xv_y-yv_x=-3$")
    charges.set(xlim=(-1, 3), ylim=(-4, 2), xlabel="Affine parameter $t$ (toy time)",
                ylabel="Conserved quantity (toy units)")
    charges.set_xticks(range(-1, 4))
    charges.set_yticks(range(-4, 3))
    charges.grid(alpha=0.2)
    charges.legend(loc="center right", fontsize=11, framealpha=1)
    charges.set_title("Translation and rotation charges\nToy unit mass: $m=1$", pad=12)
    fig.suptitle("A changing Killing field can give a constant geodesic charge", fontsize=16)
    fig.supxlabel("Arrows show directions with drawing scales; the path is not a rotation flow orbit.",
                  fontsize=11)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
