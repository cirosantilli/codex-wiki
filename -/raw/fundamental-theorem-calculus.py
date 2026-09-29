"""Connect an instantaneous rate with its accumulation and tangent."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 12, "axes.spines.top": False, "axes.spines.right": False})
fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.1), dpi=130, constrained_layout=True)
fig.patch.set_facecolor("white")
t = np.linspace(0, 3, 500)
axes[0].plot(t, 1+2*t, color="#204e8a", linewidth=2.6)
area_t = np.linspace(0, 2, 300)
axes[0].fill_between(area_t, 0, 1+2*area_t, color="#94b8a3", alpha=.5)
axes[0].scatter([2], [5], color="#b02b43", s=45, zorder=5)
axes[0].axvline(2, color="#555555", alpha=.45, linestyle=":")
axes[0].annotate(r"$f(2)=5$", xy=(2, 5), xytext=(.65, 6.35),
                 arrowprops={"arrowstyle": "->", "color": "#555555"})
axes[0].text(.33, 1.25, r"area to $t=2$: $A(2)=6$", fontsize=11)
axes[0].set(xlim=(0, 3), ylim=(0, 8), xlabel=r"$t$", ylabel=r"$f(t)$",
            title=r"Rate: $f(t)=1+2t$")
axes[1].plot(t, t+t*t, color="#6d4b87", linewidth=2.6)
tangent_t = np.linspace(1.2, 2.8, 150)
axes[1].plot(tangent_t, 6+5*(tangent_t-2), color="#b02b43", linewidth=2.1,
             label=r"tangent has slope $A'(2)=5$")
axes[1].scatter([2], [6], color="#b02b43", s=45, zorder=5)
axes[1].axvline(2, color="#555555", alpha=.45, linestyle=":")
axes[1].set(xlim=(0, 3), ylim=(0, 13), xlabel=r"$t$", ylabel=r"$A(t)$",
            title=r"Accumulation: $A(t)=t+t^2$")
axes[1].legend(loc="upper left", fontsize=10)
for ax in axes:
    ax.set_facecolor("white")
    ax.grid(alpha=.16)
fig.savefig(Path.cwd() / "fundamental-theorem-calculus.png", facecolor="white", transparent=False)
plt.close(fig)
