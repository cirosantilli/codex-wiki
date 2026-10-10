"""Compare the divider and its equivalent using calculated load responses."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


R1, R2, VS = 2.0, 4.0, 12.0  # kOhm, kOhm, V; currents below are mA
VOC = VS * R2 / (R1 + R2)
RTH = R1 * R2 / (R1 + R2)
fig, (ax, bx) = plt.subplots(1, 2, figsize=(10.8, 4.6), facecolor="white")
currents = np.linspace(0, 6, 400)
ax.plot(currents, VOC - RTH * currents, color="#253444", lw=2.5,
        label=r"Network: $V=8-\frac{4}{3}I$")
colors = ["#b54c2b", "#728d25", "#286bb1"]
loads = [1.0, RTH, 4.0]
labels = ["1 kΩ", "4/3 kΩ", "4 kΩ"]
for load, color, label in zip(loads, colors, labels):
    ax.plot(currents, load * currents, color=color, lw=1.5, label=label)
    current = VOC / (RTH + load)
    voltage = load * current
    ax.plot(current, voltage, "o", color=color, ms=7)
    ax.annotate(f"({current:.3g} mA, {voltage:.3g} V)",
                (current, voltage), xytext=(7, 7), textcoords="offset points",
                fontsize=9, color=color)
ax.plot([0, 6], [8, 0], "o", color="#253444", ms=5)
ax.set(xlim=(0, 6.2), ylim=(0, 9.3), xlabel="Delivered current I (mA)",
       ylabel="Terminal voltage V (V)", title="Terminal line and resistive load lines")
ax.legend(loc="upper right", fontsize=9)

load_grid = np.linspace(0, 12, 500)
equivalent = VOC * load_grid / (RTH + load_grid)
parallel = R2 * load_grid / (R2 + load_grid)
original = VS * parallel / (R1 + parallel)
np.testing.assert_allclose(original, equivalent, rtol=1e-14, atol=1e-14)
bx.plot(load_grid, equivalent, color="#253444", lw=2.5, label="Thévenin calculation")
samples = np.array([0, 0.4, 1, RTH, 2, 4, 6, 8, 10, 12])
rp = R2 * samples / (R2 + samples)
bx.plot(samples, VS * rp / (R1 + rp), "o", mfc="white", mec="#b54c2b", ms=6,
        label="Original circuit calculation")
bx.axhline(VOC, color="#6e8497", ls="--", lw=1.2, label="Open-circuit limit: 8 V")
for load, color in zip(loads, colors):
    voltage = VOC * load / (RTH + load)
    bx.plot([load, load], [0, voltage], color=color, ls=":", lw=1.2)
    bx.plot(load, voltage, "o", color=color, ms=6)
bx.annotate("Half voltage\nat 4/3 kΩ", (RTH, 4), xytext=(3.1, 2.0),
            arrowprops={"arrowstyle": "->", "color": "#728d25"}, color="#728d25", fontsize=10)
bx.set(xlim=(0, 12), ylim=(0, 9.3), xlabel="Load resistance R$_L$ (kΩ)",
       ylabel="Load voltage V$_L$ (V)", title="Increasing load resistance raises voltage")
bx.legend(loc="lower right", fontsize=9)
for panel in (ax, bx):
    panel.set_facecolor("white")
    panel.grid(alpha=0.2)
    panel.spines[["top", "right"]].set_visible(False)
fig.tight_layout(pad=1.5)
fig.savefig(Path(__file__).stem + ".png", dpi=140, facecolor="white", transparent=False)
plt.close(fig)
