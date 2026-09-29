#!/usr/bin/env python3
"""Generate paper-2-bifurcation-diagram.png."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots(figsize=(8.0, 5.2), layout="constrained")
mu0 = np.linspace(0, 2.5, 500)
mu_inner = np.linspace(1, 2, 300)
mu_axis = np.linspace(0.001, 2.5, 500)

ax.plot(mu0[mu0 <= 1], np.zeros_like(mu0[mu0 <= 1]), color="#1f77b4", linewidth=3, label="stable")
ax.plot(mu0[mu0 >= 1], np.zeros_like(mu0[mu0 >= 1]), color="#d62728", linewidth=2.2, linestyle="--", label="unstable or saddle")
ax.plot(mu_inner, np.sqrt(mu_inner - 1), color="#1f77b4", linewidth=3)
ax.plot(mu_axis[mu_axis <= 2], np.sqrt(mu_axis[mu_axis <= 2] / 2), color="#d62728", linewidth=2.2, linestyle="--")
ax.plot(mu_axis[mu_axis >= 2], np.sqrt(mu_axis[mu_axis >= 2] / 2), color="#1f77b4", linewidth=3)
ax.scatter([1, 2], [0, 1], color="black", s=45, zorder=5)
ax.annotate("pitchfork at $\\mu=1$", (1, 0), (0.6, 0.27), arrowprops={"arrowstyle": "->"})
ax.annotate("exchange at $\\mu=2$", (2, 1), (1.55, 1.28), arrowprops={"arrowstyle": "->"})
ax.text(1.42, 0.48, "$x=\\sqrt{\\mu-1}$", rotation=31)
ax.text(0.48, 0.62, "$x=\\sqrt{\\mu/2}$", rotation=28)
ax.set(xlabel="$\\mu$", ylabel="fixed-point coordinate $x$", xlim=(0, 2.5), ylim=(-0.08, 1.45), title="Fixed-point bifurcation diagram")
ax.grid(alpha=0.18)
ax.legend(loc="lower right")
fig.savefig(Path(Path(__file__).stem + ".png"), dpi=100, facecolor="white")
plt.close(fig)
