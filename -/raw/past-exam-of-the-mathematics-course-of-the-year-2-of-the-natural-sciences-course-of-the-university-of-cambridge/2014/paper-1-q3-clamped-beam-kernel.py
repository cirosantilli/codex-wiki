"""Original clamped beam responses; Python 3.14, NumPy, Matplotlib. PNG to cwd."""
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

def green(x, xi):
    low, high = np.minimum(x, xi), np.maximum(x, xi)
    return low**2 * (1 - high)**2 * (3 * high - (1 + 2 * high) * low) / 6

fig, (curves, kernel) = plt.subplots(1, 2, figsize=(9.5, 4), layout="constrained", facecolor="white")
x = np.linspace(0, 1, 701)
for xi, color in [(0.25, "#287cae"), (0.5, "#b85121"), (0.75, "#38864c")]:
    curves.plot(x, green(x, xi), color=color, lw=2, label=rf"$\xi={xi}$")
curves.set(xlim=(0, 1), ylim=(0, 0.0058), xlabel="Position x", ylabel=r"Unit-load displacement $G(x,\xi)$", title="Clamped at both ends")
curves.grid(alpha=0.17)
curves.legend(fontsize=9)
points = np.linspace(0, 1, 260)
xx, ss = np.meshgrid(points, points)
pic = kernel.imshow(green(xx, ss), origin="lower", extent=[0, 1, 0, 1], cmap="viridis", vmin=0, vmax=1/192, aspect="equal")
kernel.plot([0, 1], [0, 1], "--", color="white", lw=0.9, alpha=0.8)
kernel.set(xlabel="Observation point x", ylabel=r"Load point $\xi$", title=r"Reciprocity: $G(x,\xi)=G(\xi,x)$")
fig.colorbar(pic, ax=kernel, label="G", fraction=0.05)
fig.savefig("paper-1-q3-clamped-beam-kernel.png", dpi=165, facecolor="white", bbox_inches="tight")
plt.close(fig)
