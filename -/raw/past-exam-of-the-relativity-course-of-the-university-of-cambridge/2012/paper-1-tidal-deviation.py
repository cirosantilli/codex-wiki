"""Original differential free-fall diagram. Python 3.14; Matplotlib."""
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
fig, ax = plt.subplots(figsize=(7, 4.2), layout="constrained")
ax.add_patch(Circle((-3, 0), .35, color="#edba45"))
ax.text(-3, -.65, "central mass", ha="center")
ax.plot([-2.5, 2.6], [0, 0], ":", color=".7")
ax.plot([0, 0], [-1.7, 1.7], ":", color=".7")
ax.plot(0, 0, "o", color="black")
ax.text(.15, .15, "reference geodesic", fontsize=10)
for x, y, dx, dy in [(-1.2, 0, -.7, 0), (1.2, 0, .7, 0),
                     (0, 1.35, 0, -.45), (0, -1.35, 0, .45)]:
    ax.plot(x, y, "o", color="#1767a2")
    ax.annotate("", (x+dx, y+dy), (x, y),
                arrowprops={"arrowstyle": "->", "color": "#1767a2", "lw": 2})
ax.text(1.15, -.55, r"radial: $+2GM\,\xi_r/r^3$", ha="center")
ax.text(.3, 1.5, r"transverse: $-GM\,\xi_\perp/r^3$")
ax.text(-3.45, 2.2, "Relative acceleration after subtracting common free fall",
        weight="bold", fontsize=11)
ax.text(-3.45, -2., "One transverse direction is shown; the second behaves identically.\n"
        "Arrows represent acceleration differences, not absolute forces.", fontsize=10)
ax.set(xlim=(-3.6, 3.3), ylim=(-2.2, 2.5), aspect="equal")
ax.axis("off")
fig.savefig("paper-1-tidal-deviation.png", dpi=155, facecolor="white")
