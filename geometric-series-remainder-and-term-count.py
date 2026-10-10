"""Original geometric tail and certified term counts; output PNG to the CWD."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
fig, (left, right) = plt.subplots(1, 2, figsize=(10.6, 4.8),
                                gridspec_kw={"width_ratios": [.8, 1.25]},
                                layout="constrained")
colours = ["#087e8b", "#2855a6", "#c45b12", "#7d3c98"]
ratios = [.5, .8, .95, .99]
counts = np.ceil(np.log(.01)/np.log(ratios)).astype(int)
left.axis("off")
left.set(xlim=(0, 1), ylim=(-.15, 1.2))
left.text(.5, 1.06, "Included total and omitted tail", ha="center",
          fontsize=14, weight="bold")
r, N = .5, 4
cursor = 0.
for k in range(N):
    width = (1-r)*r**k
    left.add_patch(Rectangle((cursor, .60), width, .22,
                            facecolor="#087e8b", edgecolor="white"))
    if k < 3:
        left.text(cursor+width/2, .71, [r"$1/2$", r"$1/4$", r"$1/8$"][k],
                  color="white", ha="center", va="center", fontsize=11)
    cursor += width
left.add_patch(Rectangle((cursor, .60), r**N, .22,
                        facecolor="#c45b12", edgecolor="white"))
left.annotate("Tail = 1/16", xy=(cursor+r**N/2, .60), xytext=(.76, .38),
              ha="center", arrowprops={"arrowstyle": "->", "color": "#c45b12"},
              color="#c45b12", fontsize=12)
left.text(.5, .22, r"Here $a=1/2$, $r=1/2$, $N=4$.", ha="center")
left.text(.5, .07, r"Whole sum $=1$; tail $=r^N$.", ha="center")
left.text(.5, -.10, "The orange part is omitted, not zero.", ha="center", fontsize=11)
grid = np.arange(501)
for r, N, colour in zip(ratios, counts, colours):
    right.semilogy(grid, r**grid, color=colour, lw=2, label=rf"$r={r:g}$: $N={N}$")
    right.scatter(N, r**N, color=colour, s=35, zorder=3)
right.axhline(.01, color="#444444", linestyle="--", linewidth=1.3)
right.text(370, .0118, "1% omitted", fontsize=11, color="#444444")
right.set(xlim=(0, 500), ylim=(.0001, 1.15),
          xlabel=r"Number of included terms $N$",
          ylabel=r"Omitted fraction $r^N$",
          title="Minimum term counts for 99% inclusion")
right.grid(alpha=.18, which="both")
right.legend(loc="upper right", frameon=True, fontsize=11)
fig.suptitle("Convergence can be fast or very slow", fontsize=17)
fig.supxlabel("Exact analytical tails for positive geometric series; each dot is the first count meeting 1%",
              fontsize=11)
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
plt.close(fig)
