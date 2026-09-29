"""Original schematic of mercury capillary depression, not a copied figure."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

gamma, theta, density, radius, gravity = 0.436, np.deg2rad(140), 1.35e4, 0.0005, 9.81
height = 2 * gamma * np.cos(theta) / (density * gravity * radius) * 1000
fig, ax = plt.subplots(figsize=(7.1, 5.0), layout="constrained")
ax.fill_between([-2.3, 2.3], -17, -15, color="#adb6c2")
for lo, hi in [(-2.3, -0.5), (0.5, 2.3)]:
    ax.fill_between([lo, hi], -17, 0, color="#adb6c2")
    ax.plot([lo, hi], [0, 0], color="#4d5868", lw=1.5)
x = np.linspace(-0.4, 0.4, 150)
meniscus = height - 1.4 * (x / 0.4)**2
ax.fill_between(x, -17, meniscus, color="#adb6c2")
ax.plot(x, meniscus, color="#4d5868", lw=2)
for lo, hi in [(-0.5, -0.4), (0.4, 0.5)]:
    ax.fill_between([lo, hi], -15, 4, color="#dcebf2", edgecolor="#7c99aa", lw=1.2)
ax.axhline(0, color="0.4", ls="--", lw=0.8)
ax.plot([-0.4, 1.45], [height, height], ls="--", color="0.4", lw=0.8)
ax.annotate("", xy=(1.35, 0), xytext=(1.35, height),
            arrowprops={"arrowstyle": "<->", "color": "#a2362b", "lw": 1.8})
ax.text(1.43, height / 2, f"{abs(height):.1f} mm", color="#a2362b", va="center")
ax.text(-2.15, 0.6, "reservoir level", fontsize=10)
ax.annotate("convex meniscus", xy=(0.0, height), xytext=(-2.2, -6),
            arrowprops={"arrowstyle": "->", "lw": 1}, fontsize=10)
ax.text(0.0, 4.6, "glass capillary", ha="center", fontsize=11)
ax.text(-1.8, -13.9, "mercury", color="#263444", fontsize=11)
ax.text(0, -17.8, "Tube width enlarged; meniscus drawn schematically.",
        ha="center", fontsize=9)
ax.set(xlim=(-2.4, 2.4), ylim=(-18.5, 6), ylabel="Height relative to reservoir (mm)",
       title=r"Nonwetting mercury: $\theta=140^\circ$, inner diameter 1 mm")
ax.set_xticks([])
ax.spines[["top", "right", "bottom"]].set_visible(False)
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
