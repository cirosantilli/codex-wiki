"""Original aliasing example; Python 3.14, NumPy, Matplotlib; output to cwd."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 2001)
sample = np.arange(11)/10
assert np.allclose(np.cos(2*np.pi*2*sample), np.cos(2*np.pi*8*sample))
plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
fig, ax = plt.subplots(figsize=(8.2, 3.7))
ax.plot(t, np.cos(2*np.pi*2*t), lw=2.4, label="2 Hz")
ax.plot(t, np.cos(2*np.pi*8*t), lw=1.4, color="#d97706", label="8 Hz")
ax.scatter(sample, np.cos(2*np.pi*2*sample), color="#111827",
           s=35, zorder=4, label="Shared samples (10 per second)")
ax.set(xlabel="Time (s)", ylabel="Signal", ylim=(-1.3, 1.55), xlim=(0, 1))
ax.legend(frameon=False, ncol=3, loc="upper center", fontsize=9)
ax.grid(alpha=.2)
fig.tight_layout()
fig.savefig("paper-2-aliasing.png", dpi=160, facecolor="white")
