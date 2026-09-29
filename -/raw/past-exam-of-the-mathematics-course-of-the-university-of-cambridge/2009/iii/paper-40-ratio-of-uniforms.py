"""Normal ratio-of-uniforms region. Python 3.14; NumPy 2.3.5; Matplotlib 3.10.7.

Run from the desired output directory. Writes paper-40-ratio-of-uniforms.png
in the caller's CWD; honors a caller-supplied MPLCONFIGDIR.
"""
import os
from pathlib import Path
import tempfile

if "MPLCONFIGDIR" not in os.environ:
    cache = Path(tempfile.gettempdir()) / "codex-wiki-matplotlib"
    cache.mkdir(parents=True, exist_ok=True)
    os.environ["MPLCONFIGDIR"] = str(cache)

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

u = np.linspace(0.000001, 1.0, 1400)
v = 2.0 * u * np.sqrt(-np.log(u))
width = np.sqrt(2.0 / np.e)
peak_u = np.exp(-0.5)
fig, ax = plt.subplots(figsize=(6.2, 4.4), layout="constrained", facecolor="white")
ax.set_facecolor("white")
ax.fill_between(u, -width, width, color="#ededed", label="Proposal rectangle")
ax.fill_between(u, -v, v, color="#91c6e4", label="Accepted region")
ax.plot(u, v, color="#176a96", linewidth=2)
ax.plot(u, -v, color="#176a96", linewidth=2)
ax.plot([0, 1, 1, 0, 0], [-width, -width, width, width, -width],
        color="#555555", linestyle="--", linewidth=1.2)
ax.scatter([peak_u, peak_u], [width, -width], color="#176a96", s=24, zorder=5)
ax.axhline(0, color="#777777", linewidth=0.6)
ax.text(0.40, 0.04, r"$|v|/\sigma \leq 2u\sqrt{-\log u}$", fontsize=11)
ax.set(xlim=(-0.025, 1.04), ylim=(-1.01, 1.01), xlabel=r"$u$",
       ylabel=r"$v/\sigma$", title="Normal ratio-of-uniforms sampling")
ax.set_xticks([0, peak_u, 1], ["0", r"$e^{-1/2}$", "1"])
ax.set_yticks([-width, 0, width], [r"$-\sqrt{2/e}$", "0", r"$\sqrt{2/e}$"])
ax.legend(loc="upper left", framealpha=1, facecolor="white", fontsize=9)
fig.savefig(Path.cwd() / "paper-40-ratio-of-uniforms.png", dpi=160,
            facecolor="white", transparent=False)
plt.close(fig)
