"""Original negative KdV solitary-wave profiles; save into the current directory."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-4, 13, 1400)
fig, ax = plt.subplots(figsize=(8.4, 3.5), layout="constrained")
for t, color in zip([0, 1, 2], ["tab:blue", "tab:orange", "tab:green"]):
    ax.plot(x, -2 / np.cosh(x-4*t)**2, color=color, lw=2, label=f"$t={t}$")
ax.annotate("translation at speed 4", xy=(8, -0.45), xytext=(1.5, -0.45),
            arrowprops={"arrowstyle": "->", "color": "0.3"}, fontsize=10)
ax.axhline(0, color="0.5", lw=0.8)
ax.set(xlim=(-4, 13), ylim=(-2.2, 0.25), xlabel="$x$", ylabel="$u$",
       title=r"$u(x,t)=-2\,\mathrm{sech}^2(x-4t)$")
ax.legend(loc="lower right", fontsize=10)
ax.grid(alpha=0.17)
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
