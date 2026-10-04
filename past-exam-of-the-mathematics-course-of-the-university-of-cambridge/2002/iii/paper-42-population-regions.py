"""Population-region sketches. Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Writes only paper-42-population-regions.png to the caller's working directory.
Preserves the caller's MPLCONFIGDIR setting.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.8), layout="constrained")
fig.patch.set_facecolor("white")
for ax in axes:
    ax.set_facecolor("white")
    ax.grid(alpha=0.18)
mass = np.linspace(0.2, 3.5, 1200)
a, b = 8 / mass ** 2, 10 / mass ** 2
ax = axes[0]
ax.fill_between(mass, 0, np.minimum(a, 10), color="#dde9f4", label="Main sequence")
ax.fill_between(mass, a, np.minimum(b, 10), where=a <= 10,
                color="#edbe78", interpolate=True, label="Red giants")
ax.fill_between(mass, b, 10, where=b <= 10, color="#c4c3d8",
                interpolate=True, label="White dwarfs")
ax.plot(mass, a, color="#a76710", linewidth=1.4)
ax.plot(mass, b, color="#615b8e", linewidth=1.4)
ax.set(xlim=(0.2, 3.5), ylim=(0, 10), xlabel=r"Birth mass $M/M_\odot$",
       ylabel="Present age t (Gyr)", title="Lifetime regions, clipped at 10 Gyr")
ax.text(1.12, 6.9, r"$t=8/m^2$", color="#a76710", fontsize=10)
ax.text(1.37, 8.6, r"$t=10/m^2$", color="#615b8e", fontsize=10)
ax.legend(loc="upper right", fontsize=8)
ax = axes[1]
ax.add_patch(Polygon([(0, 0), (0, 1), (1/25, 1)], facecolor="#c4c3d8", edgecolor="#615b8e"))
ax.add_patch(Polygon([(0, 0), (1/25, 1), (1/20, 1)], facecolor="#edbe78", edgecolor="#a76710"))
ax.add_patch(Polygon([(0, 0), (1/20, 1), (0.065, 1), (0.065, 0)], facecolor="#dde9f4"))
y = np.linspace(0, 1, 100)
ax.plot(y/25, y, color="#615b8e", linewidth=1.6)
ax.plot(y/20, y, color="#a76710", linewidth=1.6)
ax.set(xlim=(0, 0.065), ylim=(0, 1), xlabel=r"Upper-tail mass coordinate $X=0.04/m^2$",
       ylabel=r"Uniform age coordinate $Y=t/(10\,\mathrm{Gyr})$",
       title="Uniform square: enlarged high-mass corner")
ax.text(0.006, 0.78, "White dwarfs\nArea = 0.020", fontsize=9, color="#47426a")
ax.text(0.045, 0.2, "Main\nsequence", fontsize=9, color="#2457a7")
ax.annotate("Red giants\nArea = 0.005", xy=(0.0405, 0.9), xytext=(0.047, 0.61),
            fontsize=9, color="#8f570d", arrowprops={"arrowstyle": "->", "color": "#8f570d"})
fig.savefig("paper-42-population-regions.png", dpi=140, facecolor="white", transparent=False)
plt.close(fig)
