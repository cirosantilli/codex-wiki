"""Directional phase speeds; tested with Python 3.14, NumPy and Matplotlib."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    theta = np.linspace(0.0, 2.0 * np.pi, 1001)
    fig = plt.figure(figsize=(7.6, 6.3), dpi=100, facecolor="white")
    ax = fig.add_axes((0.16, 0.22, 0.68, 0.66), projection="polar")
    ax.set_facecolor("white")
    ax.plot(theta, np.ones_like(theta), color="#1263a0", lw=2.7,
            label=r"Isotropic tangle: $v_{\rm ph}/v_A=1$")
    ax.plot(theta, np.sqrt(3.0) * np.abs(np.cos(theta)),
            color="#bb5223", lw=2.3, ls="--",
            label=r"Uniform field: $v_{\rm ph}/v_A=\sqrt{3}|\cos\theta|$")
    ax.set_ylim(0, 1.85)
    ax.set_rticks((0.5, 1.0, 1.5))
    ax.set_rlabel_position(67.5)
    ax.set_thetagrids(
        (0, 45, 90, 135, 180, 225, 270, 315),
        labels=(r"$0$", r"$\pi/4$", r"$\pi/2$", r"$3\pi/4$",
                r"$\pi$", r"$5\pi/4$", r"$3\pi/2$", r"$7\pi/4$"),
    )
    ax.grid(color="#b9b9b9", alpha=0.7)
    fig.suptitle("Transverse magnetic waves: directional phase speed",
                 y=0.97, fontsize=14)
    fig.text(0.5, 0.915, r"Equal magnetic energy: $|\mathbf{B}_0|^2"
             r"=\langle B^2\rangle=3v_A^2$", ha="center", fontsize=11)
    fig.legend(loc="center", bbox_to_anchor=(0.5, 0.125),
              frameon=False, fontsize=10)
    fig.text(0.5, 0.035,
             "Angle = wavevector direction relative to the uniform field.\n"
             "Radius = phase speed, not group velocity or displacement.",
             ha="center", va="bottom", fontsize=10)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False,
                metadata={"Software": "Codex Wiki"})
    plt.close(fig)


if __name__ == "__main__":
    main()
