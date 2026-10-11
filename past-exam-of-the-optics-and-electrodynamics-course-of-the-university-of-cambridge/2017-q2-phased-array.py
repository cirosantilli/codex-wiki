"""Original phased-array diagram and patterns; Python 3.14, NumPy, Matplotlib."""
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

fig, (diagram, pattern) = plt.subplots(1, 2, figsize=(10, 4), layout="constrained", facecolor="white", gridspec_kw={"width_ratios": [0.9, 1.4]})
positions = (np.arange(8) - 3.5) * 0.4
diagram.scatter(positions, np.zeros(8), s=65, color="#1565a8", zorder=3)
for x in positions:
    diagram.plot([x, x], [-0.5, -0.07], color="0.6", lw=1)
    diagram.annotate("", (x + 0.6, 1.04), (x, 0), arrowprops={"arrowstyle": "->", "color": "#c35419", "lw": 1.4})
diagram.plot([0, 0], [0, 1.45], "--", color="0.5", lw=1)
diagram.add_patch(Arc((0, 0), 1.1, 1.1, theta1=60, theta2=90, color="black"))
diagram.text(0.1, 0.65, r"$\theta_0$", fontsize=12)
diagram.text(0, -0.78, "Independent phase controls", ha="center", fontsize=10)
diagram.text(0, -1.05, r"$d=\lambda/2$, 8 fixed elements", ha="center", fontsize=10)
diagram.set(xlim=(-1.8, 2.2), ylim=(-1.3, 1.9), title="Steering by relative phase")
diagram.set_aspect("equal")
diagram.axis("off")
theta = np.linspace(-np.pi / 2, np.pi / 2, 2001)
indices = np.arange(8)
for steering, color in [(-30, "#1565a8"), (0, "#368847"), (30, "#c35419")]:
    chi = np.pi * (np.sin(np.deg2rad(steering)) - np.sin(theta))
    array_factor = np.exp(1j * indices[:, None] * chi).sum(axis=0)
    pattern.plot(np.rad2deg(theta), np.abs(array_factor / 8) ** 2, color=color, lw=1.8, label=rf"$\theta_0={steering}^\circ$")
pattern.set(xlim=(-90, 90), ylim=(0, 1.05), xlabel=r"Angle from array normal $\theta$ (degrees)", ylabel=r"Normalized array intensity $|F|^2/N^2$", title="Same fixed array, three phase settings")
pattern.set_xticks(np.arange(-90, 91, 30))
pattern.grid(alpha=0.2)
pattern.legend(fontsize=9)
fig.savefig("2017-q2-phased-array.png", dpi=160, facecolor="white")
plt.close(fig)
