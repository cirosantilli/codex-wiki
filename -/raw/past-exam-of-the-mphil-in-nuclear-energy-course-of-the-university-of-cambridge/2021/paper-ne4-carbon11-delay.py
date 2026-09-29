"""Original NE4 solution plot. Python 3.14; numpy and matplotlib.
Run in the desired output directory; writes only the named PNG to cwd.
"""
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
half_minutes = 20.3
hours = np.linspace(0, 4, 600)
a = 1e14 * 2 ** (-hours * 60 / half_minutes)
fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.2), layout="constrained")
for ax in axes:
    ax.plot(hours, a, color="#175782", lw=2.3)
    ax.set(xlabel="Guaranteed residence time (hours)", xlim=(0, 4), ylabel="Activity concentration (Bq per cubic metre)")
    ax.grid(alpha=0.23)
axes[0].ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
axes[0].set_title("Linear scale: rapid initial decay")
axes[1].set_yscale("log")
axes[1].set_title("Log scale: constant half-life")
for days, col in [(250, "#aa6526"), (365, "#63528d")]:
    annual_in = days * 6 * 3600 * 3.7e-7 * 1e14
    minimum_h = half_minutes * np.log2(annual_in / 1e12) / 60
    axes[1].axvline(minimum_h, color=col, ls="--", lw=1.3, label=f"{days}-day minimum: {minimum_h:.3f} h")
axes[1].scatter([3], [1e14 * 2 ** (-180 / half_minutes)], color="#1a6d47", zorder=5)
axes[1].annotate("3-hour example", (3, 1e14 * 2 ** (-180 / half_minutes)), xytext=(2.1, 2e12), arrowprops={"arrowstyle": "->", "color": "#1a6d47"}, color="#1a6d47")
axes[1].legend(loc="upper right", fontsize=9)
fig.suptitle("Carbon-11 gas retention: ideal guaranteed-delay model", fontsize=13)
fig.savefig(Path.cwd() / "paper-ne4-carbon11-delay.png", dpi=150, facecolor="white")
plt.close(fig)
