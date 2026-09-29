"""Original geometric-series plots; output the matching PNG to the CWD."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
fig, axes = plt.subplots(2, 3, figsize=(10.6, 5.5), layout="constrained")
indices = np.arange(12)
counts = np.arange(13)
ratios = [.5, -.5, -1.]
colours = ["#087e8b", "#2855a6", "#c45b12"]
for j, (r, colour) in enumerate(zip(ratios, colours)):
    terms = r ** indices
    sums = np.concatenate(([0], np.cumsum(terms)))
    top, bottom = axes[:, j]
    marker, stems, base = top.stem(indices, terms, basefmt=" ")
    plt.setp(marker, color=colour, markersize=4)
    plt.setp(stems, color=colour, linewidth=1.8)
    top.axhline(0, color="#888888", lw=.8)
    top.set(title=rf"$r={r:g}$", xlabel=r"Term index $n$",
            ylabel=r"Term $r^n$", ylim=(-1.15, 1.2))
    bottom.plot(counts, sums, "-o", color=colour, markersize=4, lw=1.8)
    if abs(r) < 1:
        limit = 1 / (1-r)
        bottom.axhline(limit, color="#333333", ls="--", lw=1.3)
        bottom.text(.8 if r > 0 else 6, limit+.10 if r > 0 else 1.14,
                    r"Limit $2$" if r > 0 else r"Limit $2/3$",
                    fontsize=11)
        bottom.set_ylim(-.15, 2.35 if r > 0 else 1.35)
    else:
        bottom.text(.6, 1.12, "No ordinary infinite sum", fontsize=11)
        bottom.set_ylim(-.15, 1.4)
    bottom.set(xlabel=r"Number of terms $N$", ylabel=r"Partial sum $S_N$")
    for ax in (top, bottom):
        ax.set_xlim(-.4, 12.4)
        ax.set_xticks([0, 4, 8, 12])
        ax.grid(alpha=.15)
fig.suptitle("Geometric terms and their accumulated partial sums", fontsize=17)
fig.supxlabel(r"All panels start at $a=1$; $S_0=0$ and $S_N$ includes terms $0$ to $N-1$",
              fontsize=11)
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
plt.close(fig)
