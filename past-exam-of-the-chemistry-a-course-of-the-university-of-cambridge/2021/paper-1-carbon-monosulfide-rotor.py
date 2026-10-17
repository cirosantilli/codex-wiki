"""Original two-body rotor geometry; output the PNG basename to cwd."""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

fig, ax = plt.subplots(figsize=(9, 3.2), dpi=150)
fig.patch.set_facecolor("white")
carbon, sulfur = 0.0, 1.0
center = 32 / 44
ax.plot([carbon, sulfur], [0, 0], color="#596775", lw=6, zorder=1)
for x, label, color, radius in [(carbon, "C\n$m_C$", "#697a8e", .09),
                                 (sulfur, "S\n$m_S$", "#edc355", .12)]:
    ax.add_patch(Circle((x, 0), radius, facecolor=color, edgecolor="#303b46", zorder=2))
    ax.text(x, 0, label, ha="center", va="center", fontsize=14, zorder=3)
ax.axvline(center, ymin=.2, ymax=.85, color="#b04140", ls="--", lw=1.5)
ax.plot(center, 0, "o", color="#b04140", ms=5, zorder=4)
ax.text(center, .23, "center of mass", color="#92312f", ha="center", fontsize=12)
for left, right, y, label in [(0, center, -.23, "$r_1$"),
                               (center, 1, -.23, "$r_2$"),
                               (0, 1, -.43, "$r$")]:
    ax.annotate("", (left, y), (right, y), arrowprops={"arrowstyle": "<->", "color": "#303b46"})
    ax.text((left+right)/2, y+.025, label, ha="center", va="bottom", fontsize=13)
ax.text(.5, .41, "Carbon monosulfide: a linear rigid rotor", ha="center", fontsize=15)
ax.set(xlim=(-.2, 1.2), ylim=(-.53, .5), aspect="equal")
ax.axis("off")
fig.tight_layout(pad=.6)
fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
