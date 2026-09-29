"""Original boundary orientation diagram, not a reproduction of an exam figure."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(9, 4.3), layout="constrained")
ax = fig.add_subplot(121, projection="3d")
theta0 = np.pi/4
theta = np.linspace(theta0, theta0+2*np.pi, 181)
z = np.linspace(-1, 1, 20)
th, zz = np.meshgrid(theta, z)
ax.plot_surface(np.cos(th), .5*np.sin(th), zz, color="#91c0d7", alpha=.22, linewidth=0)
for h, sign in [(-1, 1), (1, -1)]:
    ax.plot(np.cos(theta), .5*np.sin(theta), np.full(theta.size, h), color="#205f8c")
    q = 2.3
    ax.quiver(np.cos(q), .5*np.sin(q), h, -sign*np.sin(q), .5*sign*np.cos(q), 0, length=.5, normalize=True, color="#205f8c")
ax.plot([np.cos(theta0)]*2, [.5*np.sin(theta0)]*2, [-1, 1], "--", color="#b74432", lw=2)
ax.text(np.cos(theta0)+.12, .5*np.sin(theta0), 0, "cut", color="#b74432")
ax.set(xlabel="x", ylabel="y", zlabel="z", title="Outward orientation")
ax.view_init(elev=23, azim=35)
ax.set_box_aspect((1.3, 1, 1.6))
bx = fig.add_subplot(122)
bx.plot([0, 1, 1, 0, 0], [-1, -1, 1, 1, -1], color="#205f8c", lw=1.8)
for start, end, color in [((.25, -1), (.75, -1), "#205f8c"), ((1, -.5), (1, .5), "#b74432"), ((.75, 1), (.25, 1), "#205f8c"), ((0, .5), (0, -.5), "#b74432")]:
    bx.annotate("", xy=end, xytext=start, arrowprops=dict(arrowstyle="-|>", color=color, lw=2))
bx.text(.5, -1.16, r"bottom: increasing $\theta$", ha="center")
bx.text(.5, 1.08, r"top: decreasing $\theta$", ha="center")
bx.text(-.07, 0, "cut: down", ha="right", rotation=90, va="center", color="#b74432")
bx.text(1.07, 0, "cut: up", ha="left", rotation=90, va="center", color="#b74432")
bx.set(xlim=(-.25, 1.25), ylim=(-1.4, 1.4), title="Cut-open parameter rectangle")
bx.set_xticks([0, 1], [r"$\theta_0$", r"$\theta_0+2\pi$"])
bx.set_yticks([-1, 1])
bx.set_ylabel("z")
for spine in bx.spines.values():
    spine.set_visible(False)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
plt.close(fig)
