"""Original field-content sketches of the scalar and Yang-Mills vertices."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    vertices = [
        ("Unbroken scalar coupling", [r"$W$", r"$\Phi$", r"$\Phi^\dagger$"], [1, 0, 0]),
        ("Unbroken scalar seagull", [r"$W$", r"$W$", r"$\Phi$", r"$\Phi^\dagger$"], [1, 1, 0, 0]),
        ("Scalar quartic coupling", [r"$\Phi$", r"$\Phi$", r"$\Phi^\dagger$", r"$\Phi^\dagger$"], [0, 0, 0, 0]),
        ("Broken phase: one scalar", [r"$\sigma$", r"$W_j$", r"$W_j$"], [0, 1, 1]),
        ("Broken phase: two scalars", [r"$\sigma$", r"$\sigma$", r"$W_j$", r"$W_j$"], [0, 0, 1, 1]),
        ("Broken scalar cubic", [r"$\sigma$"] * 3, [0, 0, 0]),
        ("Broken scalar quartic", [r"$\sigma$"] * 4, [0, 0, 0, 0]),
        ("Yang-Mills cubic", [r"$W_a$", r"$W_b$", r"$W_c$"], [1, 1, 1]),
        ("Yang-Mills quartic", [r"$W_a$", r"$W_b$", r"$W_c$", r"$W_d$"], [1, 1, 1, 1]),
    ]
    fig, axes = plt.subplots(3, 3, figsize=(8.2, 7.2), layout="constrained")
    for ax, (title, labels, vectors) in zip(axes.flat, vertices):
        angles = np.deg2rad([90, 210, 330] if len(labels) == 3 else [45, 135, 225, 315])
        for angle, label, vector in zip(angles, labels, vectors):
            direction = np.array([np.cos(angle), np.sin(angle)])
            normal = np.array([-direction[1], direction[0]])
            t = np.linspace(0, 0.72, 151)
            offset = 0.035 * np.sin(12 * np.pi * t / 0.72) if vector else np.zeros_like(t)
            xy = direction[:, None] * t + normal[:, None] * offset
            ax.plot(*xy, color="tab:purple" if vector else "tab:blue", lw=1.6,
                    ls="-" if vector else "--")
            ax.text(*(direction * 0.91), label, ha="center", va="center", fontsize=11)
        ax.plot(0, 0, "o", color="0.2", ms=4)
        ax.set(xlim=(-1.15, 1.15), ylim=(-1.05, 1.12), title=title, aspect="equal")
        ax.axis("off")
        ax.title.set_fontsize(10)
    fig.suptitle("Interaction field content: dashed scalar legs and wavy gauge-vector legs\nSpecies tensors and identical-field factors determine which amplitudes are nonzero", fontsize=11)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
