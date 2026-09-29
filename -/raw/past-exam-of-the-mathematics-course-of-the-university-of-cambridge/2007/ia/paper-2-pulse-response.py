"""Original pulse-response sketch. Python 3.14, NumPy 2.3, Matplotlib 3.10.
Writes an opaque PNG basename to the caller's current working directory.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

t = np.linspace(-0.6, 5.0, 1600)
y = np.where(t < 0, 0.0, np.where(t <= 1, 1-np.exp(-t), (1-np.exp(-1))*np.exp(-(t-1))))
fig, axs = plt.subplots(2, 1, figsize=(6.4, 4.1), sharex=True,
                        gridspec_kw={"height_ratios": [1, 2]}, layout="constrained", facecolor="white")
for ax in axs:
    ax.set_facecolor("white")
    ax.spines[["top", "right"]].set_visible(False)
    ax.axvline(0, color="0.7", linestyle=":", lw=1)
    ax.axvline(1, color="0.7", linestyle=":", lw=1)
    ax.set_xlim(-0.6, 5)
axs[0].plot([-0.6, 0, 0, 1, 1, 5], [0, 0, 1, 1, 0, 0], color="#bd6020", lw=2)
axs[0].set_ylim(-0.12, 1.25)
axs[0].set_yticks([0, 1])
axs[0].set_ylabel("forcing")
axs[0].set_title("Response to a unit-duration pulse")
axs[1].plot(t, y, color="#1762a1", lw=2.5)
axs[1].scatter([1], [1-np.exp(-1)], color="#1762a1", s=24, zorder=3)
axs[1].annotate(r"maximum $1-e^{-1}$", xy=(1, 1-np.exp(-1)), xytext=(2.05, .64),
                arrowprops={"arrowstyle": "->", "color": "0.3"}, fontsize=10)
axs[1].set_ylim(-.05, .80)
axs[1].set_yticks([0, .3, .6])
axs[1].set_xlabel("time t")
axs[1].set_ylabel("solution y(t)")
fig.savefig("paper-2-pulse-response.png", dpi=145, transparent=False, facecolor="white")
plt.close(fig)
