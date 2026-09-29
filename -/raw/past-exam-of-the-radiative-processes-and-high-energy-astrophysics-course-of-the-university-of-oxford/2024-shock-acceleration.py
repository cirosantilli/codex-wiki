"""Draw shock acceleration in the shock frame; Python 3.14, NumPy/Matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

fig, ax = plt.subplots(figsize=(9, 4.8), dpi=130, facecolor="white")
ax.set_facecolor("white")
ax.axvspan(-4, 0, color="#e9f3fc")
ax.axvspan(0, 4, color="#fff1df")
ax.axvline(0, color="#444444", lw=2.5)
ax.text(-2, 3.7, "Upstream", ha="center", fontsize=14)
ax.text(2, 3.7, "Downstream", ha="center", fontsize=14)
for y in (2.9, 0.4):
    ax.annotate("", xy=(-.45, y), xytext=(-3.6, y),
                arrowprops=dict(arrowstyle="->", color="#2166ac", lw=2.5))
    ax.annotate("", xy=(2.7, y), xytext=(1.9, y),
                arrowprops=dict(arrowstyle="->", color="#b45d00", lw=2.5))
ax.text(-2.0, 3.1, r"Fluid speed $u_1=u$", ha="center", color="#2166ac", fontsize=12)
ax.text(2.0, 3.1, r"Fluid speed $u_2=u/4$", ha="center", color="#9a5100", fontsize=12)
points = [(-3.2, 1.9), (-2.5, 2.4), (-1.9, 1.5), (-1.25, 2.3),
          (1.2, 1.5), (2.0, 2.2), (1.1, 2.6), (-1.0, 1.1),
          (-2.2, 1.6), (-1.7, .85), (1.35, 1.05), (3.3, 1.4)]
for a, b in zip(points, points[1:]):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="->", mutation_scale=11,
                                lw=1.8, color="#65358a"))
ax.text(0, -.15, "Stationary shock", ha="center", fontsize=12)
ax.text(-2.1, -.75, "Scattering randomizes direction\nin each local fluid frame", ha="center", fontsize=11)
ax.text(2.05, -.75, "Some particles are advected away\nand cease returning", ha="center", fontsize=11)
ax.text(0, 4.3, r"Relative fluid speed: $U=u_1-u_2=3u/4$", ha="center", fontsize=14)
ax.set_xlim(-4, 4)
ax.set_ylim(-1.05, 4.6)
ax.axis("off")
fig.tight_layout()
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
            facecolor="white", transparent=False, metadata={"Software": "Matplotlib"})
plt.close(fig)
