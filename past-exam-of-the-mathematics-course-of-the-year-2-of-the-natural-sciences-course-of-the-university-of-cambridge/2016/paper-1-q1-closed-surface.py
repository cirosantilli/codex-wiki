"""Original surfaces for NST IB 2016; Python 3.14, NumPy, Matplotlib. PNG to cwd."""
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(11.5, 3.9), layout="constrained", facecolor="white")
theta = np.linspace(0, 2 * np.pi, 72)
radii = np.linspace(0, 1, 25)
rr, tt = np.meshgrid(radii, theta)
xx, yy = rr * np.cos(tt), rr * np.sin(tt)
zz, tc = np.meshgrid(np.linspace(0, 1, 25), theta)
for panel in range(4):
    ax = fig.add_subplot(1, 4, panel + 1, projection="3d")
    if panel in [0, 3]:
        ax.plot_surface(xx, yy, 2 - rr**2, color="#4b95c6", alpha=0.8, linewidth=0, shade=True)
    if panel in [1, 3]:
        ax.plot_surface(np.cos(tc), np.sin(tc), zz, color="#e39b54", alpha=0.72, linewidth=0, shade=True)
    if panel in [2, 3]:
        ax.plot_surface(xx, yy, np.zeros_like(rr), color="#70a76b", alpha=0.82, linewidth=0, shade=True)
    ax.set(xlim=(-1.1, 1.1), ylim=(-1.1, 1.1), zlim=(0, 2.1), xlabel="x", ylabel="y", zlabel="z")
    ax.set_xticks([-1, 0, 1])
    ax.set_yticks([-1, 0, 1])
    ax.set_zticks([0, 1, 2])
    ax.tick_params(labelsize=8, pad=0)
    ax.set_title([r"$S_1$: paraboloid cap", r"$S_2$: cylindrical side", r"$S_3$: base disk", r"$S=S_1\cup S_2\cup S_3$"][panel], fontsize=11)
    ax.set_box_aspect((1, 1, 1.2))
    ax.view_init(elev=24, azim=-55)
fig.savefig("paper-1-q1-closed-surface.png", dpi=160, facecolor="white")
plt.close(fig)
