"""Original Frenet-frame sketch. Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Writes paper-3-helices.png to the caller's CWD and preserves MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def frame(s, radius, pitch):
    length = np.sqrt(radius**2 + pitch**2)
    u = s / length
    tangent = np.array([-radius*np.sin(u), radius*np.cos(u), pitch]) / length
    normal = np.array([-np.cos(u), -np.sin(u), 0.0])
    binormal = np.cross(tangent, normal)
    binormal_prime = pitch / length**2 * np.array([np.cos(u), np.sin(u), 0.0])
    return tangent, normal, binormal, binormal_prime


def main():
    fig = plt.figure(figsize=(10.6, 5.1), facecolor="white")
    radius = 1.0
    colors = ["#b83d32", "#2a854f", "#345fa6", "#aa6a12"]
    labels = [r"$t$", r"$p$", r"$b$", r"$b'$"]
    for i, pitch in enumerate([.45, -.45], start=1):
        ax = fig.add_subplot(1, 2, i, projection="3d")
        ax.set_facecolor("white")
        u = np.unique(np.r_[np.linspace(-np.pi, np.pi, 600), 0])
        ax.plot(radius*np.cos(u), radius*np.sin(u), pitch*u, color="#555555", lw=2)
        point = np.array([radius, 0.0, 0.0])
        ax.scatter(*point, color="black", s=20)
        vectors = frame(0.0, radius, pitch)
        for j, (v, color, label) in enumerate(zip(vectors, colors, labels)):
            # Common scale for all four vectors: b' retains its actual magnitude.
            arrow = .85*v
            ax.quiver(*point, *arrow, color=color, arrow_length_ratio=.15, linewidth=2.2)
            endpoint = point + 1.10*arrow
            if j == 3:
                endpoint[2] -= .12
            ax.text(*endpoint, label, color=color, fontsize=13)
        ax.set_title(r"$h=" + str(pitch) + r"$: " +
                     (r"$\tau>0,\ b'=-\tau p$" if pitch > 0 else r"$\tau<0,\ b'=|\tau|p$"))
        ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("z")
        ax.set_xlim(-1.2, 1.8); ax.set_ylim(-1.3, 1.3); ax.set_zlim(-1.5, 1.5)
        ax.set_box_aspect([3, 2.6, 3])
        ax.view_init(elev=23, azim=-55)
        ax.grid(alpha=.2)
    fig.suptitle("Circular helices: frame vectors at s = 0; curve direction is increasing s", fontsize=12)
    fig.tight_layout()
    fig.savefig(Path.cwd() / "paper-3-helices.png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
