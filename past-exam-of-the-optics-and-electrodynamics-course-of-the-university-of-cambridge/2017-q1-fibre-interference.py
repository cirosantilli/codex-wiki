"""Original coherence plot; Python 3.14, NumPy and Matplotlib. Save to cwd."""
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

phase_cycles = np.linspace(-2, 2, 1400)
fig, ax = plt.subplots(figsize=(8, 3.6), layout="constrained", facecolor="white")
for visibility, color, label in [(1, "#1565a8", "Ideal: V = 1"), (0.5, "#c35419", "Finite linewidth: V = 0.5")]:
    ax.plot(phase_cycles, 2 * (1 + visibility * np.cos(2 * np.pi * phase_cycles)), color=color, lw=2, label=label)
ax.set(xlabel=r"Relative fringe phase $\Phi/(2\pi)$", ylabel=r"Intensity $I/I_0$", xlim=(-2, 2), ylim=(-0.1, 4.2))
ax.set_xticks(np.arange(-2, 2.01, 0.5))
ax.grid(alpha=0.2)
ax.legend(loc="upper right", framealpha=0.94)
fig.savefig("2017-q1-fibre-interference.png", dpi=160, facecolor="white")
plt.close(fig)
