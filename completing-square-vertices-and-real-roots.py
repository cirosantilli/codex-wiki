"""Original quadratic vertex and real-root comparisons; output PNG to CWD."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white"})
fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.8), layout="constrained")
cases = [(-3, 4, 1, (-6, 0), (0, 15), r"$x^2+6x+13=(x+3)^2+4$", "Minimum 4; no real roots"),
         (2, 3, -2, (-.2, 4.2), (-6, 5), r"$-2x^2+8x-5=-2(x-2)^2+3$", "Maximum 3; two real roots")]
for ax, (h, k, a, limits, ylimits, title, note) in zip(axes, cases):
    x = np.linspace(*limits, 501)
    ax.plot(x, a*(x-h)**2+k, color="#2563eb", lw=2)
    ax.axhline(0, color="#64748b", lw=1)
    ax.axvline(h, color="#64748b", ls="--", lw=1, label="Axis of symmetry")
    ax.scatter([h], [k], color="#c2410c", zorder=4)
    ax.annotate(f"Vertex ({h}, {k})", (h, k), xytext=(12, 16), textcoords="offset points", fontsize=11, bbox={"facecolor": "white", "edgecolor": "none", "alpha": .9, "pad": 2})
    if -k/a > 0:
        r = np.sqrt(-k/a)
        ax.scatter([h-r, h+r], [0, 0], color="#059669", zorder=4)
        for root in [h-r, h+r]:
            ax.annotate(f"{root:.3f}", (root, 0), xytext=(0, -20), textcoords="offset points", ha="center", color="#047857", fontsize=10)
    ax.set(xlim=limits, ylim=ylimits, xlabel="x", ylabel="Polynomial value", title=title)
    ax.grid(alpha=.18); ax.spines[["top", "right"]].set_visible(False)
    ax.text(.5, .96, note, ha="center", va="top", transform=ax.transAxes, fontsize=10)
fig.suptitle(r"In $a(x-h)^2+k$, the vertex and the sign of $a$ tell the story", fontsize=15)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
plt.close(fig)
