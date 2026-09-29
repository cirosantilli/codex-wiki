#!/usr/bin/env python3
"""Plot the jet-instability growth rate for 2018 Part II Paper 2, question 38."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


kh = np.linspace(0.0, 5.0, 1000)
growth = 0.5 * kh * np.sqrt(1.0 - np.exp(-4.0 * kh))

fig, ax = plt.subplots(figsize=(7.2, 4.4), layout="constrained")
ax.plot(kh, growth, linewidth=2.6, label="varicose = sinuous")
small = np.linspace(0.0, 0.9, 200)
ax.plot(small, small**1.5, linestyle="--", label=r"long wave: $(kh)^{3/2}$")
ax.plot(kh, 0.5 * kh, linestyle=":", linewidth=2.0, label=r"short wave: $kh/2$")
ax.set_xlabel(r"$kh$")
ax.set_ylabel(r"$\sigma_R h/U$")
ax.set_title("Equal-density top-hat planar jet")
ax.set_xlim(0.0, 5.0)
ax.set_ylim(0.0, 2.6)
ax.grid(alpha=0.2)
ax.legend(loc="upper left")

output = Path(Path(__file__).stem + ".png")
fig.savefig(output, dpi=100, facecolor="white")
plt.close(fig)
