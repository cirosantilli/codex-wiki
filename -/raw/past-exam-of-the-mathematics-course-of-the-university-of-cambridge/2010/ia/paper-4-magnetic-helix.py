"""Draw the magnetic helix; tested with Python 3.14.4.

Uses the root numpy/matplotlib dependencies. Writes the PNG basename to CWD.
"""
from pathlib import Path
import os
import tempfile

os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "paper4-matplotlib"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    t = np.linspace(0, 4 * np.pi, 600)
    x, y, z = np.cos(t), -np.sin(t), 0.26 * t
    fig = plt.figure(figsize=(6.5, 4.6), dpi=140, facecolor="white")
    ax = fig.add_subplot(111, projection="3d")
    ax.set_facecolor("white")
    ax.plot(x, y, z, color="#b54a2d", linewidth=2.2)
    ax.plot([0, 0], [0, 0], [0, 3.65], "--", color="#435c75", linewidth=1.2)
    ax.quiver(0, 0, 3.25, 0, 0, 0.4, color="#435c75", arrow_length_ratio=0.3)
    ax.text(0.08, 0.08, 3.65, "$B\\hat z$", color="#435c75", fontsize=11)
    ax.scatter([1], [0], [0], color="#23394d", s=26)
    ax.text(1.04, 0.04, 0.04, "$r(0)$", fontsize=10)
    for tt in (1.1, 5.4, 9.6):
        ax.quiver(np.cos(tt), -np.sin(tt), 0.26 * tt,
                  -np.sin(tt), -np.cos(tt), 0.26,
                  normalize=True, length=0.32, color="#b54a2d", arrow_length_ratio=0.4)
    ax.set(xlim=(-1.3, 1.3), ylim=(-1.3, 1.3), zlim=(-0.12, 3.9),
           xlabel="$x$", ylabel="$y$", zlabel="$z$")
    ax.set_box_aspect((2.6, 2.6, 4.02))
    ax.view_init(elev=23, azim=43)
    ax.set_title("Helix about the magnetic-field axis\n"
                 "$a=1,\\ \\omega=1,\\ u=-1,\\ v=0.26$", fontsize=11, pad=10)
    fig.subplots_adjust(left=0.04, right=0.92, bottom=0.15, top=0.84)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
