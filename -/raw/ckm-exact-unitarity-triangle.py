"""Draw an illustrative exact CKM triangle; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def mixing_matrix():
    """Standard three-angle convention, with chosen rather than fitted parameters."""
    s12, s23, s13 = 1 / 4, 1 / 10, 1 / 100
    c12, c23, c13 = np.sqrt(1 - np.array([s12, s23, s13]) ** 2)
    e = np.exp(1j * np.pi / 3)
    return np.array([
        [c12 * c13, s12 * c13, s13 / e],
        [-s12 * c23 - c12 * s23 * s13 * e,
         c12 * c23 - s12 * s23 * s13 * e, s23 * c13],
        [s12 * s23 - c12 * c23 * s13 * e,
         -c12 * s23 - s12 * c23 * s13 * e, c23 * c13],
    ])


def main():
    v = mixing_matrix()
    a = v[0, 0] * v[0, 2].conjugate()
    b = v[1, 0] * v[1, 2].conjugate()
    c = v[2, 0] * v[2, 2].conjugate()
    z = -a / b
    j = (v[0, 0] * v[1, 1] * v[0, 1].conjugate()
         * v[1, 0].conjugate()).imag
    assert np.max(np.abs(v.conj().T @ v - np.eye(3))) < 1e-14
    assert abs(a + b + c) < 1e-14
    assert abs(abs(z.imag) / 2 - abs(j) / (2 * abs(b) ** 2)) < 1e-13

    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(9, 5.6), dpi=120)
    fig.subplots_adjust(left=0.10, right=0.97, bottom=0.29, top=0.79)
    ax.set_facecolor("white")
    ax.fill([0, 1, z.real], [0, 0, z.imag], color="#e3f1fa")
    vertices = [0j, z, 1 + 0j, 0j]
    colors = ["#156b9c", "#af5420", "#465766"]
    for start, end, color in zip(vertices, vertices[1:], colors):
        ax.annotate("", xy=(end.real, end.imag), xytext=(start.real, start.imag),
                    arrowprops={"arrowstyle": "->", "lw": 2.4, "color": color,
                                "shrinkA": 0, "shrinkB": 0, "mutation_scale": 16})
    ax.scatter([0, 1, z.real], [0, 0, z.imag], s=24, color="#253d4c", zorder=3)
    ax.text(z.real + 0.025, z.imag + 0.026,
            rf"$z=\bar\rho+i\bar\eta={z.real:.4f}+{z.imag:.4f}i$", fontsize=12)
    ax.text(-0.025, -0.065, "$0$", ha="center")
    ax.text(1.015, -0.065, "$1$", ha="center")
    ax.text(0.005, 0.22, "$-a/b$", color=colors[0], rotation=60)
    ax.text(0.62, 0.22, "$-c/b$", color=colors[1], rotation=-23)
    ax.text(0.56, -0.07, "$-1$", color=colors[2])
    ax.annotate("", xy=(z.real, z.imag), xytext=(z.real, 0),
                arrowprops={"arrowstyle": "<->", "color": "#777777", "lw": 1.2})
    ax.text(z.real - 0.018, 0.14, r"$\bar\eta$", ha="right", color="#555555")
    ax.text(0.38, 0.075, r"Normalized area $=|\bar\eta|/2$", fontsize=12)
    ax.set(xlim=(-0.08, 1.09), ylim=(-0.10, 0.44), xlabel="Real part", ylabel="Imaginary part")
    ax.set_aspect("equal")
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1])
    ax.set_yticks([0, 0.2, 0.4])
    ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Exact CKM unitarity closes the triangle", fontsize=18, y=0.96)
    fig.text(0.5, 0.865,
             r"$a=V_{ud}V_{ub}^*,\quad b=V_{cd}V_{cb}^*,\quad c=V_{td}V_{tb}^*,\quad a+b+c=0$",
             ha="center", fontsize=14)
    fig.text(0.5, 0.155,
             rf"Original area $=|J|/2={abs(j)/2:.7f}$; normalized area $=|J|/(2|b|^2)={z.imag/2:.6f}$",
             ha="center", fontsize=12)
    fig.text(0.5, 0.09,
             r"Chosen inputs: $s_{12}=1/4,\ s_{23}=1/10,\ s_{13}=1/100,\ \delta=\pi/3$",
             ha="center", fontsize=12)
    fig.text(0.5, 0.035, "Illustrative exact parametrization; no fitted data", ha="center", color="#555555")
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
