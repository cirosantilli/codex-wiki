"""Dust-universe age versus density; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Write paper-55-dust-age.png to the caller's working directory.
"""
import os
import tempfile
os.environ.setdefault("MPLCONFIGDIR", tempfile.mkdtemp(prefix="paper55-age-mpl-"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# x=u**2 removes the square-root endpoint before Gaussian quadrature.
nodes, weights = np.polynomial.legendre.leggauss(160)
u = (nodes + 1) / 2
w = weights / 2
omega = np.linspace(0.02, 5.0, 600)
age = np.sum(w[None, :] * 2 * u[None, :] ** 2 /
             np.sqrt(omega[:, None] + (1 - omega[:, None]) * u[None, :] ** 2), axis=1)
fig, ax = plt.subplots(figsize=(8.5, 4.6), layout="constrained", facecolor="white")
ax.axvspan(0, 1, color="#eaf3fb")
ax.axvspan(1, 5, color="#f7eddf")
ax.plot(omega, age, color="#245981", linewidth=2.6)
ax.axhline(2 / 3, color="#565656", linestyle="--", linewidth=1)
ax.axhline(1, color="#888888", linestyle=":", linewidth=1)
ax.axvline(1, color="#565656", linestyle="--", linewidth=1)
ax.scatter([1], [2 / 3], color="#a22f32", s=48, zorder=4)
ax.annotate("Flat dust: 2/3", (1, 2 / 3), (1.8, 0.75),
            arrowprops={"arrowstyle": "->", "color": "#555555"})
ax.text(0.08, 0.44, "Open", color="#245981")
ax.text(3.9, 0.44, "Closed", color="#806136")
ax.set(xlim=(0, 5), ylim=(0.4, 1.03), xlabel=r"Present matter density $\Omega_{m,0}$",
       ylabel=r"Dimensionless age $H_0 t_0$",
       title="Expanding dust universes at the same present Hubble parameter")
ax.grid(alpha=0.2)
fig.savefig("paper-55-dust-age.png", dpi=120, facecolor="white", transparent=False)
plt.close(fig)
