"""Idealized spherical-collapse sketch; Python 3.14, NumPy/Matplotlib.

Write only the basename PNG to caller CWD; respect supplied MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 5.3), dpi=140, facecolor="white")
ax.set_facecolor("white")
eta = np.linspace(0.002, 2 * np.pi, 1000)
t = (eta - np.sin(eta)) / np.pi
r = (1 - np.cos(eta)) / 2
ax.plot(t, r, "--", color="#7e8793", lw=1.8, label="Formal cold collapse")
# Exact expanding and early recollapsing branch; schematic late settling.
join_eta = 4.3
join_t = (join_eta - np.sin(join_eta)) / np.pi
join_r = (1 - np.cos(join_eta)) / 2
mask = eta <= join_eta
ax.plot(t[mask], r[mask], color="#285888", lw=2.5)
late_t = np.linspace(join_t, 2, 120)
s = (late_t - join_t) / (2 - join_t)
# Cubic Hermite curve matches the infall slope and ends with zero slope.
slope = (np.pi / 2) * np.sin(join_eta) / (1 - np.cos(join_eta))
late_r = ((2*s**3-3*s**2+1)*join_r + (s**3-2*s**2+s)*(2-join_t)*slope
          + (-2*s**3+3*s**2)*0.5)
ax.plot(late_t, late_r, color="#285888", lw=2.5)
ax.plot([2, 2.5], [0.5, 0.5], color="#285888", lw=2.5, label="Expansion and idealized virialization")
ax.axhline(0.5, color="#8892a0", lw=1, ls=":")
ax.axvline(1, color="#8892a0", lw=1, ls=":")
ax.axvline(2, color="#8892a0", lw=1, ls=":")
ax.scatter([1, 2], [1, 0.5], color="#285888", zorder=5)
ax.annotate("Turnaround", xy=(1, 1), xytext=(1.08, 1.10), fontsize=11,
            arrowprops={"arrowstyle": "->", "color": "#285888"})
ax.annotate(r"$R_{\rm vir}=R_{\rm ta}/2$", xy=(2.2, 0.5), xytext=(1.75, 0.78),
            fontsize=12, arrowprops={"arrowstyle": "->", "color": "#285888"})
ax.text(2.02, 0.03, "Formal collapse", fontsize=9, color="#67717d")
ax.set_xlabel(r"Time $t/t_{\rm ta}$", fontsize=12)
ax.set_ylabel(r"Physical radius $R/R_{\rm ta}$", fontsize=12)
ax.set_title("Spherical overdensity in an Einstein-de Sitter universe", fontsize=14, pad=12)
ax.set_xlim(0, 2.55)
ax.set_ylim(0, 1.25)
ax.legend(loc="upper right", fontsize=9, frameon=False)
ax.spines[["top", "right"]].set_visible(False)
fig.text(0.5, 0.025, "Late settling is schematic; cold collapse occurs at the nominal time 2 t_ta.",
         ha="center", fontsize=9)
fig.tight_layout(rect=(0, 0.045, 1, 1))
fig.savefig(Path.cwd() / "paper-66-spherical-collapse.png", facecolor="white", transparent=False)
plt.close(fig)
