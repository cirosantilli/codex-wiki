"""Population iteration; Python 3.14, NumPy 2.3, Matplotlib 3.10.

Writes only paper-2-cobweb.png in the caller's current directory.
The caller controls MPLCONFIGDIR.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

f = lambda u: 3 * u * u / (1 + u * u)
u = np.linspace(0, 3.1, 600)
fig, axes = plt.subplots(1, 2, figsize=(9, 4.3), layout="constrained")
for ax, initial, title in zip(axes, [0.2, 1.2], ["Below the threshold: extinction", "Above the threshold: persistence"]):
    ax.plot(u, u, color="0.5", ls="--", label="identity")
    ax.plot(u, f(u), color="navy", label="population map")
    x, y = initial, 0
    for _ in range(14):
        next_y = f(x)
        ax.plot([x, x, next_y], [y, next_y, next_y], color="darkorange", lw=1.5)
        x, y = next_y, next_y
    for fixed in [0, (3-np.sqrt(5))/2, (3+np.sqrt(5))/2]:
        ax.plot(fixed, fixed, "ko", ms=4)
    ax.set(xlim=(0, 3.1), ylim=(0, 3.1), xlabel=r"$u_t$", ylabel=r"$u_{t+1}$", title=title)
    ax.set_aspect("equal")
    ax.legend(fontsize=8, loc="upper left")
fig.savefig("paper-2-cobweb.png", dpi=125, facecolor="white", transparent=False)
