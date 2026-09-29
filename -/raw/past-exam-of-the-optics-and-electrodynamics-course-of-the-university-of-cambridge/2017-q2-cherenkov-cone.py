"""Original Cherenkov ray/wavefront construction; Python 3.14 and Matplotlib."""
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle

fig, ax = plt.subplots(figsize=(7.7, 4.5), layout="constrained", facecolor="white")
speed_ratio = 1.5
current = np.array([speed_ratio, 0])
upper = np.array([1 / speed_ratio, np.sqrt(1 - 1 / speed_ratio**2)])
ax.add_patch(Circle((0, 0), 1, fill=False, ls="--", lw=1.6, color="#1565a8"))
for sign in [-1, 1]:
    point = upper * [1, sign]
    ax.plot([current[0], point[0]], [0, point[1]], color="#c35419", lw=2)
    vector = (point - current) * 0.12
    normal = -point * 0.12
    ax.plot([point[0] + vector[0], point[0] + vector[0] + normal[0], point[0] + normal[0]], [point[1] + vector[1], point[1] + vector[1] + normal[1], point[1] + normal[1]], color="0.45", lw=1)
ax.annotate("", (1.9, 0), (-1.3, 0), arrowprops={"arrowstyle": "->", "lw": 1.3, "color": "black"})
ax.annotate("", upper, (0, 0), arrowprops={"arrowstyle": "->", "color": "#368847", "lw": 2})
theta = np.rad2deg(np.arccos(1 / speed_ratio))
ax.add_patch(Arc((0, 0), 0.7, 0.7, theta1=0, theta2=theta, color="#368847"))
ax.text(0.39, 0.16, r"$\theta_C$", color="#28783a", fontsize=12)
ax.add_patch(Arc(current, 0.8, 0.8, theta1=180 - (90 - theta), theta2=180, color="#c35419"))
ax.text(0.97, 0.12, r"$\alpha$", color="#c35419", fontsize=12)
ax.scatter([0, current[0]], [0, 0], color="black", s=30, zorder=4)
ax.text(0, -0.18, "Earlier emission", ha="center", fontsize=10)
ax.text(current[0] + 0.1, -0.28, "Charge now", ha="center", fontsize=10)
ax.text(-0.98, 1.1, "Wavefront radius ct/n", color="#1565a8", fontsize=10)
ax.text(0.75, 0.8, "Light ray", color="#28783a", fontsize=11)
ax.text(1.2, 0.62, "Wavefront\nenvelope", color="#c35419", fontsize=10)
ax.text(1.95, 0.1, "Track", ha="right", fontsize=10)
ax.set(title=r"Example: $\beta n=1.5$,  $\cos\theta_C=\sin\alpha=1/(\beta n)$", xlim=(-1.4, 2), ylim=(-1.15, 1.3))
ax.set_aspect("equal")
ax.axis("off")
fig.savefig("2017-q2-cherenkov-cone.png", dpi=170, facecolor="white")
plt.close(fig)
