#!/usr/bin/env python3
"""Plot the effective potentials for 2018 Part II Paper 2, question 37."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


mu = 1.0
a = np.linspace(0.16, 4.0, 1000)
fig, axes = plt.subplots(2, 2, figsize=(11.0, 8.0), layout="constrained")

ax = axes[0, 0]
potential = -mu / a
ax.plot(a, potential, color="black", linewidth=2.2, label=r"$V=-\mu/a$")
for energy, label, color in (
    (-1.0, r"$k=+1$", "#d62728"),
    (0.0, r"$k=0$", "#2ca02c"),
    (1.0, r"$k=-1$", "#1f77b4"),
):
    ax.axhline(energy, color=color, linestyle="--", label=label)
ax.set_title(r"$\Lambda=0$")
ax.set_ylim(-3.0, 1.4)
ax.legend(fontsize=8)

ax = axes[0, 1]
positive_lambda = 0.55
ax.plot(
    a,
    -mu / a - positive_lambda * a**2 / 3.0,
    color="black",
    linewidth=2.2,
)
ax.axhline(1.0, color="#1f77b4", linestyle="--", label=r"$C=1,\ k=-1$")
ax.set_title(r"$\Lambda>0,\ k=-1$: no turning point")
ax.set_ylim(-4.0, 1.5)
ax.legend(fontsize=8)

ax = axes[1, 0]
negative_lambda = 0.55
negative_potential = -mu / a + negative_lambda * a**2 / 3.0
ax.plot(a, negative_potential, color="black", linewidth=2.2)
ax.axhline(0.0, color="#2ca02c", linestyle="--", label=r"$C=0,\ k=0$")
turning = (3.0 * mu / negative_lambda) ** (1.0 / 3.0)
ax.scatter((turning,), (0.0,), color="#d62728", zorder=3)
ax.annotate(r"$a_{\max}$", (turning, 0.0), xytext=(8, 8), textcoords="offset points")
ax.set_title(r"$\Lambda<0,\ k=0$: recollapse")
ax.set_ylim(-3.0, 2.0)
ax.legend(fontsize=8)

ax = axes[1, 1]
critical_lambda = 4.0 / 9.0
for lam, label, color in (
    (0.20, "subcritical", "#1f77b4"),
    (critical_lambda, "critical", "#2ca02c"),
    (0.90, "supercritical", "#d62728"),
):
    ax.plot(
        a,
        -mu / a - lam * a**2 / 3.0,
        color=color,
        linewidth=2.0,
        label=label,
    )
ax.axhline(-1.0, color="black", linestyle="--", label=r"$C=-1,\ k=+1$")
ax.set_title(r"$\Lambda>0,\ k=+1$")
ax.set_ylim(-3.0, 0.0)
ax.legend(fontsize=8)

for ax in axes.flat:
    ax.set_xlim(a[0], a[-1])
    ax.set_xlabel(r"scale factor $a$")
    ax.set_ylabel(r"effective potential $V(a)$")
    ax.grid(alpha=0.2)

output = Path(Path(__file__).stem + ".png")
fig.savefig(output, dpi=100, facecolor="white")
plt.close(fig)
