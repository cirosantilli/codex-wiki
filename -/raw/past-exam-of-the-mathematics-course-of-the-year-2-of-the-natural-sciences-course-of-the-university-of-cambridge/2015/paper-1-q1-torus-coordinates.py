"""Original circular-torus coordinates; Python 3.14, NumPy, Matplotlib. PNG to cwd."""
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc

fig = plt.figure(figsize=(10, 4.4), layout="constrained", facecolor="white")
ax = fig.add_subplot(1, 2, 1, projection="3d")
cross = fig.add_subplot(1, 2, 2)
minor = 0.45
alpha, beta = np.meshgrid(np.linspace(-np.pi, np.pi, 65), np.linspace(0, 2 * np.pi, 100))
ax.plot_surface((1 + minor * np.sin(alpha)) * np.cos(beta), (1 + minor * np.sin(alpha)) * np.sin(beta), minor * np.cos(alpha), color="#81b4d5", alpha=0.28, linewidth=0, shade=True)
a, b = np.pi / 3, -0.7
point = np.array([(1 + minor * np.sin(a)) * np.cos(b), (1 + minor * np.sin(a)) * np.sin(b), minor * np.cos(a)])
directions = [np.array([np.sin(a) * np.cos(b), np.sin(a) * np.sin(b), np.cos(a)]), np.array([np.cos(a) * np.cos(b), np.cos(a) * np.sin(b), -np.sin(a)]), np.array([-np.sin(b), np.cos(b), 0])]
for direction, color, label in zip(directions, ["#bd431c", "#368747", "#2459a2"], [r"$e_r$", r"$e_\alpha$", r"$e_\beta$"]):
    ax.quiver(*point, *direction, length=0.4, color=color, arrow_length_ratio=0.2, linewidth=2)
    ax.text(*(point + 0.46 * direction), label, color=color, fontsize=12)
ax.scatter(*point, s=25, color="black", depthshade=False)
ax.set(xlim=(-1.55, 1.75), ylim=(-1.65, 1.55), zlim=(-0.65, 0.75), xlabel="x", ylabel="y", zlabel="z", title="Orthogonal unit tangent directions")
ax.set_box_aspect((3.3, 3.2, 1.4))
ax.view_init(elev=25, azim=-62)
cross.add_patch(Circle((1, 0), minor, facecolor="#d9eaf5", edgecolor="#287cae", lw=1.8))
rho, zz = 1 + minor * np.sin(a), minor * np.cos(a)
cross.plot([1, rho], [0, zz], "--", color="0.3")
cross.scatter([1, rho], [0, zz], s=25, color="black")
cross.text((1 + rho) / 2 - 0.02, zz / 2 - 0.08, r"$r$", fontsize=12)
cross.add_patch(Arc((1, 0), 0.35, 0.35, theta1=30, theta2=90, color="black"))
cross.text(1.08, 0.16, r"$\alpha$", fontsize=12)
cross.plot([1, 1], [0, minor * 1.18], ":", color="0.4")
cross.axhline(0, color="0.6", lw=0.8)
cross.set(xlim=(0, 1.75), ylim=(-0.65, 0.75), xlabel=r"Cylindrical radius $\varpi$", ylabel="z", title="Cross-section: major radius 1, R = 0.45")
cross.set_aspect("equal")
cross.grid(alpha=0.14)
fig.savefig("paper-1-q1-torus-coordinates.png", dpi=165, facecolor="white", bbox_inches="tight")
plt.close(fig)
