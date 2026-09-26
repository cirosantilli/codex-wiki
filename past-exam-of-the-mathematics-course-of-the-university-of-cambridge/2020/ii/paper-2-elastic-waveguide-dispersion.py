#!/usr/bin/env python3
"""Plot a representative rigid elastic-waveguide dispersion equation."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


OUTPUT = Path(Path(__file__).stem + ".png")

# Representative dimensionless values. The repeated tangent branches, rather
# than the particular numerical material ratio, are the point of the sketch.
c_over_cp = np.linspace(1.001, 7.0, 24000)
cp_over_cs = 1.8
kH = 1.0
a = np.sqrt(c_over_cp**2 - 1.0)
b = np.sqrt((cp_over_cs * c_over_cp) ** 2 - 1.0)
lhs = a * np.tan(a * kH)
rhs = -np.tan(b * kH) / b


def mask_branches(values: np.ndarray, cosine: np.ndarray) -> np.ndarray:
    plotted = values.copy()
    plotted[(np.abs(cosine) < 0.025) | (np.abs(plotted) > 8.0)] = np.nan
    return plotted


lhs = mask_branches(lhs, np.cos(a * kH))
rhs = mask_branches(rhs, np.cos(b * kH))

fig, ax = plt.subplots(figsize=(8.2, 4.8))
ax.plot(c_over_cp, lhs, color="#176b87", linewidth=1.35, label=r"$a\tan(akH)$")
ax.plot(c_over_cp, rhs, color="#c75146", linewidth=1.25, label=r"$-\tan(bkH)/b$")
ax.axhline(0.0, color="#555555", linewidth=0.7)
ax.set_xlim(1.0, 7.0)
ax.set_ylim(-8.0, 8.0)
ax.set_xlabel(r"phase speed $c/c_P$")
ax.set_ylabel("dispersion-equation side")
ax.set_title(r"Representative branches: $c_P/c_S=1.8$, $kH=1$")
ax.grid(alpha=0.18)
ax.legend(loc="upper right")
fig.tight_layout()
fig.savefig(OUTPUT, dpi=160, facecolor="white")
