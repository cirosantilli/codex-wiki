"""Original polarization-transmission curves; Python 3.14, NumPy, Matplotlib."""
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

theta = np.linspace(0, 180, 1001)
factor = np.sin(2 * np.deg2rad(theta)) ** 2
fig, ax = plt.subplots(figsize=(8.2, 4), layout="constrained", facecolor="white")
for coefficient, color, label in [(0.5, "#1565a8", "Half-wave plate"), (0.25, "#c35419", "Quarter-wave plate"), (0.125, "#368847", "Linear polarizer")]:
    ax.plot(theta, coefficient * factor, color=color, lw=2, label=label)
ax.set(xlim=(0, 180), ylim=(0, 0.55), xlabel=r"Middle-element axis angle $\theta$ (degrees)", ylabel=r"Transmission $I_{\mathrm{out}}/I_{\mathrm{in}}$", title="Circular input; fixed x and y outer polarizers")
ax.set_xticks(np.arange(0, 181, 22.5))
ax.grid(alpha=0.2)
ax.legend(loc="upper center", ncols=3, fontsize=9)
fig.savefig("2017-q3-polarization-transmission.png", dpi=160, facecolor="white")
plt.close(fig)
