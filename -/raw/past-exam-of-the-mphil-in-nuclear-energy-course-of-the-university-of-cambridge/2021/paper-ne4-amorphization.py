"""Original NE4 solution plot. Python 3.14; numpy and matplotlib.
Run in the desired output directory; writes only the named PNG to cwd.
"""
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
rate_density = 5.685e14
damage_volume = 1.706e-25
seconds_per_year = 365.25 * 86400
k = rate_density * damage_volume * seconds_per_year
years = np.linspace(0, 1900, 600)
fraction = -np.expm1(-k * years)
t99 = -np.log(0.01) / k
fig, ax = plt.subplots(figsize=(7.7, 4.3), layout="constrained")
ax.plot(years, fraction * 100, color="#175782", lw=2.4, label="Independent impacts with random overlap")
short = years[years * k <= 1.03]
ax.plot(short, short * k * 100, color="#aa6526", ls="--", label="Linear accumulation misses overlap")
ax.axhline(99, color="#777777", lw=1, ls=":")
ax.axvline(t99, color="#63528d", lw=1.1, ls=":")
ax.scatter([t99], [99], color="#63528d", zorder=5)
ax.annotate(f"99% at {t99:.1f} years after 2050", (t99, 99), xytext=(680, 63), arrowprops={"arrowstyle": "->", "color": "#63528d"}, color="#63528d")
ax.set(xlabel="Time after preparation for disposal (years)", ylabel="Amorphous fraction (%)", xlim=(0, 1900), ylim=(0, 104), title="Direct-impact damage model: constant rate, no annealing")
ax.grid(alpha=0.23)
ax.legend(loc="lower right", fontsize=9)
fig.savefig(Path.cwd() / "paper-ne4-amorphization.png", dpi=150, facecolor="white")
plt.close(fig)
