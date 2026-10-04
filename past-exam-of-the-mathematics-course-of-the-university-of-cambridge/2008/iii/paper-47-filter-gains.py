"""Difference-filter gains; Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.

Write the opaque PNG basename to the caller's working directory. Matplotlib
honours the caller's MPLCONFIGDIR; no source-relative cache or output paths.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

lam = np.unique(np.r_[np.linspace(0, np.pi, 1601), np.arange(13) * np.pi / 12])
fig, axes = plt.subplots(1, 2, figsize=(10, 3.6), layout="constrained")
for ax, gain, title in zip(axes, (2*np.sin(lam/2), 2*np.abs(np.sin(6*lam))),
                         ("Ordinary difference", "Twelve-step seasonal difference")):
    ax.plot(lam, gain, color="#1565c0", linewidth=2)
    ax.set(xlim=(0, np.pi), ylim=(0, 2.15), ylabel="Gain", xlabel=r"Frequency $\lambda$",
           title=title, xticks=[0, np.pi/6, np.pi/2, 5*np.pi/6, np.pi],
           xticklabels=["0", r"$\pi/6$", r"$\pi/2$", r"$5\pi/6$", r"$\pi$"])
    ax.grid(alpha=0.25)
fig.savefig("paper-47-filter-gains.png", dpi=140, facecolor="white", transparent=False)
plt.close(fig)
