"""Original viscous-sheet force diagrams; write the PNG to the working directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge, Polygon

plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "savefig.facecolor": "white"})
fig, axes = plt.subplots(1, 2, figsize=(10, 4.5), dpi=100)
blue = "#276a9a"
red = "#ac342e"
def arrow(ax, start, end, color=red):
    ax.annotate("", xy=end, xytext=start, arrowprops={"arrowstyle": "->", "lw": 2, "color": color})

ax = axes[0]
a = .43
r1, r2 = 1.35, 2.4
ax.add_patch(Wedge((0, 0), r2, -np.degrees(a), np.degrees(a), width=r2-r1, facecolor="#d9eaf5", edgecolor=blue, lw=2))
arrow(ax, (r1, 0), (.72, 0))
arrow(ax, (r2, 0), (3.03, 0))
ax.text(.63, .20, r"$h\sigma_{rr}$", ha="center")
ax.text(2.92, .20, r"$h\sigma_{rr}$", ha="center")
for sign in [1, -1]:
    theta = sign*a
    point = 1.88*np.array([np.cos(theta), np.sin(theta)])
    tangent = sign*np.array([-np.sin(theta), np.cos(theta)])
    arrow(ax, point, point+.63*tangent)
    ax.text(point[0]-.15, sign*1.47, r"$h\sigma_{\theta\theta}$", ha="center", va="center")
ax.text(1.90, -.13, "sheet sector", ha="center", color=blue)
arrow(ax, (.90, -1.58), (2.95, -1.58), color=blue)
ax.text(1.92, -1.84, "radial direction", ha="center", color=blue)
ax.set_title("Radial and hoop tractions", pad=12)
ax.set_xlim(.4, 3.25); ax.set_ylim(-2., 1.85)
ax.set_aspect("equal"); ax.axis("off")

ax = axes[1]
# A rounded inner rim joining the two flat surfaces; fluid is to the right.
theta = np.linspace(np.pi/2, 3*np.pi/2, 100)
curve = np.column_stack([1+.38*np.cos(theta), .38*np.sin(theta)])
points = np.vstack([[3.45, .38], curve, [3.45, -.38]])
ax.add_patch(Polygon(points, closed=True, facecolor="#d9eaf5", edgecolor=blue, lw=2))
for z in [.38, -.38]:
    arrow(ax, (1.22, z), (2.30, z))
    ax.text(2.34, z, r"$\gamma$", va="center", color=red)
ax.text(.27, 0, "hole", ha="center", color=blue)
ax.text(2.72, 0, "fluid", ha="center", color=blue)
ax.annotate("", xy=(3.19, .36), xytext=(3.19, -.36), arrowprops={"arrowstyle": "<->", "color": blue})
ax.text(3.32, 0, "$h$", va="center", color=blue)
arrow(ax, (.95, -.98), (2.28, -.98))
ax.text(1.65, -1.23, r"net pull $2\gamma$ per unit rim length", ha="center", color=red)
ax.text(1.93, 1.20, r"inner normal $\mathbf{n}=-\mathbf{e}_r$", ha="center")
ax.set_title("Surface tension at the hole rim", pad=12)
ax.set_xlim(0, 3.65); ax.set_ylim(-2., 1.85)
ax.set_aspect("equal"); ax.axis("off")
fig.subplots_adjust(left=.025, right=.985, top=.89, bottom=.10, wspace=.14)
fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100)
plt.close(fig)
