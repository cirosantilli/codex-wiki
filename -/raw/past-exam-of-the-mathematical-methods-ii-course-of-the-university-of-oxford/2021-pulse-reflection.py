"""Original fixed-end reflection plots; Python 3.14, NumPy 2.3, Matplotlib 3.10."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

u = np.linspace(-1.15, 0, 1801)
def triangle(s):
    return np.maximum(0, 1 - np.abs(2*s + 1))
fig, axes = plt.subplots(2, 2, figsize=(8.8, 5.4), layout="constrained")
for ax, tau, label in zip(axes.flat, [0.25, 0.5, 0.75, 1], ["(a) one quarter", "(b) one half", "(c) three quarters", "(d) complete"]):
    incident = triangle(u-tau)
    reflected = -triangle(-u-tau)
    ax.axhline(0, color="0.65", lw=0.8)
    ax.plot(u, incident, "--", color="#2980b9", lw=1.2, label="incident")
    ax.plot(u, reflected, "--", color="#db8431", lw=1.2, label="reflected")
    ax.plot(u, incident+reflected, color="#20242a", lw=2.2, label="total")
    ax.axvline(0, color="0.3", lw=3)
    ax.set(xlim=(-1.15, .04), ylim=(-1.16, 1.16), xlabel=r"$x/L$", ylabel=r"$y/H$", title=label)
    ax.set_xticks([-1, -.75, -.5, -.25, 0])
axes[0, 0].legend(loc="upper left", fontsize=8)
fig.suptitle("Fixed end at x = 0: reflected displacement is inverted", fontsize=13)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
plt.close(fig)
