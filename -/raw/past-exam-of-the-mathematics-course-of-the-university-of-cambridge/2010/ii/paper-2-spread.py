"""Cubic-diffusion similarity profiles; Python 3.14, NumPy 2.3, Matplotlib 3.10.

Writes only paper-2-spread.png in the caller's current directory.
The caller controls MPLCONFIGDIR.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

r = np.linspace(0, 1.9, 1000)
fig, ax = plt.subplots(figsize=(7, 4.3), layout="constrained")
for t in [0.02, 0.15, 1.0]:
    lam = (6*t)**(1/6)
    density = lam**(-2) * np.sqrt(np.maximum(1-(r/lam)**2, 0))
    ax.plot(r, density, label=rf"$D_0t/r_0^2={t:g}$")
ax.set(xlabel=r"Radius $r/r_0$", ylabel=r"Density $n/n_0$", title="Mass-conserving compact spreading profiles", ylim=(0, 2.2))
ax.legend()
ax.grid(alpha=0.2)
fig.savefig("paper-2-spread.png", dpi=125, facecolor="white", transparent=False)
