#!/usr/bin/env python3
"""Draw the eventual separation of two simple waves for 2020 II Paper 4, Q39."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


OUTPUT = Path(__file__).with_suffix(".svg")
plt.rcParams["svg.hashsalt"] = "codex-wiki"

# Dimensionless axes use L=c_0=1, so separation occurs at t=1/2.
t = np.linspace(0.0, 1.45, 300)
fig, ax = plt.subplots(figsize=(7.2, 4.6))

left_outer = -t
left_inner = 1.0 - t
right_inner = t
right_outer = 1.0 + t

ax.fill_betweenx(t, left_outer, left_inner, color="#79a9d1", alpha=0.42)
ax.fill_betweenx(t, right_inner, right_outer, color="#efaa61", alpha=0.42)
for x, color in (
    (left_outer, "#2f6f9f"),
    (left_inner, "#2f6f9f"),
    (right_inner, "#b86620"),
    (right_outer, "#b86620"),
):
    ax.plot(x, t, color=color, linewidth=1.6)

ax.plot([0.0, 1.0], [0.0, 0.0], color="black", linewidth=3.0)
ax.axhline(0.5, color="0.45", linestyle="--", linewidth=0.9)
ax.text(0.5, -0.075, "initial disturbance $0\\leq x\\leq L$", ha="center", va="top")
ax.text(-0.75, 1.08, "$R_+$ constant\nleft simple wave", ha="center", color="#245b83")
ax.text(1.75, 1.08, "$R_-$ constant\nright simple wave", ha="center", color="#955014")
ax.text(0.5, 1.14, "undisturbed", ha="center", color="0.25")
ax.text(-1.28, 1.28, "undisturbed", rotation=43, ha="center", color="0.35")
ax.text(2.28, 1.28, "undisturbed", rotation=-43, ha="center", color="0.35")
ax.text(2.32, 0.51, "$t=L/(2c_0)$", va="bottom", color="0.35")

ax.set_xlabel("$x/L$")
ax.set_ylabel("$c_0t/L$")
ax.set_xlim(-1.55, 2.55)
ax.set_ylim(-0.02, 1.45)
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig(OUTPUT, metadata={"Date": None})
