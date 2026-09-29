"""Exact six-step lower and upper sums for the rate v(t)=1+2t."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 12, "axes.spines.top": False, "axes.spines.right": False})
fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.1), dpi=130, constrained_layout=True)
fig.patch.set_facecolor("white")
n = 6
width = 3/n
left = np.arange(n)*width
t = np.linspace(0, 3, 400)
for ax, right, color in zip(axes, (False, True), ("#44839c", "#d99b35")):
    heights = 1+2*(left+width if right else left)
    total = float(width*heights.sum())
    assert np.isclose(total, 12+(9/n if right else -9/n))
    ax.fill_between(t, 0, 1+2*t, color="#94b8a3", alpha=.18)
    ax.bar(left, heights, width=width, align="edge", color=color, alpha=.34,
           edgecolor=color, linewidth=1.7, label="rectangle approximation")
    ax.plot(t, 1+2*t, color="#222222", linewidth=2.5, label=r"$v(t)=1+2t$")
    ax.set(xlim=(0, 3), ylim=(0, 7.6), xlabel="time t (s)", ylabel="velocity (m/s)",
           title=("Right" if right else "Left")+f" endpoints: sum = {total:.1f} m")
    ax.text(.14, 6.45, "Exact accumulated displacement: 12 m", fontsize=10,
            bbox={"facecolor": "white", "edgecolor": "none", "alpha": .95})
    ax.legend(loc="upper left", bbox_to_anchor=(0, .78), fontsize=9)
    ax.set_facecolor("white")
fig.savefig(Path.cwd() / "integral-riemann-sums.png", facecolor="white", transparent=False)
plt.close(fig)
