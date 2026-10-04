"""Generate the homologous stellar-energy sketch; output is relative to CWD.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
import os
import tempfile

if "MPLCONFIGDIR" not in os.environ:
    os.environ["MPLCONFIGDIR"] = tempfile.mkdtemp(prefix="paper-62-matplotlib-")

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.07, 4.5, 900)
fig, ax = plt.subplots(figsize=(8.2, 4.9), layout="constrained")
for a, color, label in [
    (2.0, "#167343", r"Stable: $\gamma=5/3$, minimum"),
    (0.5, "#bd3933", r"Unstable: $\gamma=7/6$, maximum"),
    (1.0, "#68707c", r"Marginal: $\gamma=4/3$"),
]:
    energy = x ** (-a) - a / x
    ax.plot(x, energy, color=color, linewidth=2.2, label=label)
    ax.plot([1], [1 - a], "o", color=color, markersize=6)
ax.axvline(1, color="#aab1bb", linestyle=":", linewidth=1)
ax.set(xlim=(0.07, 4.5), ylim=(-2.5, 3.2), xlabel=r"Expansion factor $x=R/R_0$", ylabel=r"Total energy $E/U_0$")
ax.set_title(r"Homologous adiabatic stellar energy: $E/U_0=x^{-a}-a/x$, $a=3(\gamma-1)$")
ax.annotate(r"$E\to+\infty$", xy=(0.334, 3.0), xytext=(0.9, 2.3), arrowprops={"arrowstyle": "->", "color": "#167343"}, color="#167343")
ax.annotate(r"$E\to-\infty$", xy=(0.085, -2.45), xytext=(0.75, -1.85), arrowprops={"arrowstyle": "->", "color": "#bd3933"}, color="#bd3933")
ax.grid(alpha=0.22)
ax.legend(loc="upper right", fontsize=9)
fig.savefig("paper-62-energy.png", dpi=130, facecolor="white", transparent=False)
plt.close(fig)
