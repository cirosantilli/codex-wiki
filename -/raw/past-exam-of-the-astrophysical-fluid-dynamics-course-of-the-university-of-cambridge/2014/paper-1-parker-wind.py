"""Original isothermal Parker-wind curves; write PNG to the working directory."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def log_speed_squared(rhs, upper):
    """Solve exp(y)-y=rhs on a specified side of its minimum at y=0."""
    lo, hi = (0.0, np.log(rhs + 1.0) + 3.0) if upper else (-rhs - 2.0, 0.0)
    for _ in range(85):
        mid = (lo + hi) / 2
        positive = np.exp(mid) - mid > rhs
        if positive == upper:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


x = np.geomspace(0.22, 7.0, 650)
f = 4 * np.log(x) + 4 / x - 3
wind = np.array([np.exp(log_speed_squared(y, r > 1) / 2) for r, y in zip(x, f)])
breeze = np.array([np.exp(log_speed_squared(y + 2, False) / 2) for y in f])
fig, ax = plt.subplots(figsize=(10, 4.9), dpi=100, facecolor="white")
ax.plot(x, wind, lw=2.7, label="Escaping transonic wind")
ax.plot(x, breeze, lw=2.5, label="Pressure-confined breeze (one boundary choice)")
ax.axhline(1, color="0.45", lw=1, ls="--")
ax.axvline(1, color="0.6", lw=1, ls=":")
ax.scatter([1], [1], color="black", s=30, zorder=4)
ax.annotate("Sonic point", (1, 1), (1.5, 0.65), arrowprops={"arrowstyle": "->"})
ax.set(xlabel=r"Radius $r/r_s$, with $r_s=GM/(2a^2)$", ylabel=r"Mach number $u/a$",
       xlim=(0.2, 7), ylim=(0, 2.9), title="Isothermal pressure-driven outflow")
ax.grid(alpha=0.22)
ax.legend(loc="upper left", framealpha=0.95)
fig.text(0.5, 0.035, "Maintaining constant sound speed requires heat input; a breeze needs external confinement.",
         ha="center", fontsize=10.5)
fig.subplots_adjust(left=0.09, right=0.98, top=0.9, bottom=0.19)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white")
