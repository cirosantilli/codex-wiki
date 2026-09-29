"""Original graph of an odd polynomial times a Gaussian; output to cwd."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3.5, 3.5, 1300)
y = (x + x**3) * np.exp(-x*x)
fig, ax = plt.subplots(figsize=(6.8, 3.9), layout="constrained")
ax.plot(x, y, lw=2.2, color="#276ca0")
ax.fill_between(x, 0, y, where=x > 0, color="#86b9d3", alpha=0.35)
ax.fill_between(x, 0, y, where=x < 0, color="#d6a887", alpha=0.35)
ax.scatter([-1, 1], [-2 / np.e, 2 / np.e], color="#a34523", zorder=4)
ax.annotate(r"$(1,2/e)$", (1, 2/np.e), (1.5, 0.77), arrowprops={"arrowstyle": "->"})
ax.annotate(r"$(-1,-2/e)$", (-1, -2/np.e), (-2.6, -0.83), arrowprops={"arrowstyle": "->"})
ax.axhline(0, color="black", lw=0.7)
ax.axvline(0, color="black", lw=0.7)
ax.set(xlabel="x", ylabel="f(x)", xlim=(-3.5,3.5), ylim=(-0.95,0.95), title=r"$f(x)=(x+x^3)e^{-x^2}$")
ax.grid(alpha=0.2)
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
plt.close(fig)
