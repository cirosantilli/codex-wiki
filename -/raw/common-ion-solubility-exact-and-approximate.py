"""Compare exact stipulated AB solubility with the common-ion approximation.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; output is this script's basename with a .png extension.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

K = 1e-4  # M^2; chosen model, not measured calcium hydroxide data.
common = np.linspace(0, 0.12, 1800)
exact = 2 * K / (np.hypot(common, 2 * np.sqrt(K)) + common)
positive = common[1:]
approximate = K / positive
relative_error = exact[1:] / positive
points = np.array([0.03, 0.10])
point_exact = 2 * K / (np.hypot(points, 2 * np.sqrt(K)) + points)
plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                     "axes.spines.right": False, "figure.facecolor": "white",
                     "axes.facecolor": "white"})
fig, (ax, error_ax) = plt.subplots(2, 1, sharex=True, figsize=(9, 7.6),
                                  dpi=100, layout="constrained",
                                  gridspec_kw={"height_ratios": [1.8, 1]})
ax.plot(common, 1000 * exact, color="#293f78", lw=2.6,
        label=r"Exact: $s(s+c_0)=K_{\mathrm{sp},c}$")
ax.plot(positive, 1000 * approximate, color="#c55b24", lw=2.4, ls='--',
        label=r"Approximation: $s_{\mathrm{app}}=K_{\mathrm{sp},c}/c_0$")
ax.scatter([0], [10], color="#293f78", zorder=4, s=45)
ax.annotate("Pure water: 10 mM", xy=(0, 10), xytext=(0.014, 11.3),
            fontsize=11, arrowprops={"arrowstyle": "->", "color": "#293f78"})
ax.annotate("Approximation diverges\nas the background vanishes",
            xy=(0.0087, 11.5), xytext=(0.028, 8.1), fontsize=11,
            color="#a14318", arrowprops={"arrowstyle": "->", "color": "#c55b24"})
ax.scatter(points, 1000 * point_exact, s=50, c="#293f78", zorder=4)
ax.scatter(points, 1000 * K / points, s=40, marker='x', c="#c55b24", zorder=4)
ax.annotate("3.028 vs 3.333 mM", xy=(points[0], 1000 * point_exact[0]),
            xytext=(0.044, 5.2), fontsize=11,
            arrowprops={"arrowstyle": "->", "color": "#555555"})
ax.annotate("0.990 vs 1.000 mM", xy=(points[1], 1000 * point_exact[1]),
            xytext=(0.073, 3.15), fontsize=11,
            arrowprops={"arrowstyle": "->", "color": "#555555"})
ax.set(ylim=(0, 12.2), ylabel="Molar solubility, s (mM)",
       title=r"Common-ion suppression: stipulated $K_{\mathrm{sp},c}=10^{-4}\,\mathrm{M}^2$")
ax.legend(loc="upper right", fontsize=10, framealpha=1)
error_ax.plot(positive, 100 * relative_error, color="#a14318", lw=2.3)
error_ax.axhline(5, color="#16856e", ls=':', lw=1.8)
threshold = np.sqrt(K / (0.05 * 1.05))
error_ax.scatter([threshold], [5], c="#16856e", s=40, zorder=5)
error_ax.annotate("5% at 0.04364 M", xy=(threshold, 5), xytext=(0.052, 17),
                  fontsize=11, color="#126b59",
                  arrowprops={"arrowstyle": "->", "color": "#16856e"})
errors = 100 * point_exact / points
error_ax.scatter(points, errors, c="#a14318", s=40, zorder=4)
error_ax.annotate("10.1%", xy=(points[0], errors[0]), xytext=(0.019, 25),
                  fontsize=11, arrowprops={"arrowstyle": "->", "color": "#a14318"})
error_ax.annotate("0.990%", xy=(points[1], errors[1]), xytext=(0.094, 9),
                  fontsize=11, arrowprops={"arrowstyle": "->", "color": "#a14318"})
error_ax.set(xlim=(0, 0.12), ylim=(0, 40),
             xlabel=r"Initial common B anion concentration, $c_0$ (M)",
             ylabel="Relative overestimate (%)")
error_ax.text(0.073, 29, r"Exact error: $(s_{\mathrm{app}}-s)/s=s/c_0$", fontsize=11)
for panel in (ax, error_ax):
    panel.grid(alpha=0.18)
fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white",
            transparent=False)
plt.close(fig)
