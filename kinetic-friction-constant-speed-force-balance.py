"""Draw an original horizontal sliding force balance, not measured data.

Writes a matching-basename opaque white PNG to CWD. Tested with Python
3.14.4, Matplotlib 3.10.7 and NumPy 2.3.5. Force arrows share a length scale;
the dashed velocity arrow has no force scale. The block already slides.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    mass, gravity, mu = 2.0, 9.8, 0.30
    normal = mass * gravity
    sliding_force = mu * normal
    fig, ax = plt.subplots(figsize=(8.6, 5.6), dpi=120)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.set(xlim=(-3.5, 3.5), ylim=(-2.7, 2.7), aspect="equal")
    ax.axis("off")
    ax.add_patch(Rectangle((-0.8, -0.38), 1.6, 0.76,
                           facecolor="#f1e0c3", edgecolor="#604c30", lw=1.5))
    ax.text(0, 0.15, "2 kg block", ha="center", fontsize=12)
    ax.plot([-3.25, 3.25], [-0.4, -0.4], color="#767676", lw=2, zorder=0)
    ax.text(2.05, -0.69, "stationary horizontal surface", ha="center", fontsize=10)
    scale = 0.077
    arrows = [((0, 0), (0, normal * scale), "#2166ac"),
              ((0, 0), (0, -normal * scale), "#2166ac"),
              ((0.8, 0), (0.8 + sliding_force * scale, 0), "#a43b31"),
              ((-0.8, 0), (-0.8 - sliding_force * scale, 0), "#a43b31")]
    for start, end, color in arrows:
        ax.annotate("", xy=end, xytext=start,
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=2.6,
                                    mutation_scale=18))
    ax.text(0.15, 1.1, f"N = {normal:.1f} N", color="#2166ac", fontsize=12)
    ax.text(0.15, -1.35, f"mg = {normal:.1f} N", color="#2166ac", fontsize=12)
    ax.text(1.65, 0.2, f"pull F = {sliding_force:.2f} N", ha="center",
            color="#a43b31", fontsize=12)
    ax.text(-1.7, 0.2, f"friction |fₖ| = {sliding_force:.2f} N", ha="center",
            color="#a43b31", fontsize=12)
    ax.annotate("", xy=(2.65, 1.62), xytext=(1.15, 1.62),
                arrowprops=dict(arrowstyle="->", color="#35784f", lw=2,
                                linestyle="--"))
    ax.text(1.9, 1.83, "constant velocity →", color="#35784f",
            ha="center", fontsize=12)
    ax.text(0, -2.04, "F − |fₖ| = 0     •     N − mg = 0     •     a = 0",
            ha="center", fontsize=13)
    ax.text(0, -2.46, "Stipulated model: μₖ = 0.30, g = 9.8 m/s²; already sliding",
            ha="center", color="#555555", fontsize=11)
    ax.set_title("Constant-speed sliding: balanced forces", fontsize=16, pad=13)
    fig.subplots_adjust(left=0.035, right=0.965, top=0.9, bottom=0.04)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
