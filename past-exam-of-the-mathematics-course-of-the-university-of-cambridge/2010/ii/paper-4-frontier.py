"""Mean–variance frontier. Tested with Python 3.14 and root pyproject deps.

Write only paper-4-frontier.png to the caller's current directory.
The caller may supply MPLCONFIGDIR; this script leaves it unchanged.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

mean = np.linspace(-0.6, 2.5, 500)
minimum_mean = 0.6
variance = 1.0 + (mean - minimum_mean) ** 2 / 1.04
fig, ax = plt.subplots(figsize=(7.2, 4.3), dpi=120, facecolor="white")
ax.set_facecolor("white")
ax.fill_betweenx(mean, variance, 5.0, color="#eff3f7")
lower = mean <= minimum_mean
ax.plot(variance[lower], mean[lower], "--", color="#717b89", lw=2)
ax.plot(variance[~lower], mean[~lower], color="#145da0", lw=2.6)
ax.scatter([1], [minimum_mean], color="#222222", zorder=4, s=28)
ax.annotate("Minimum variance", (1, minimum_mean), (1.75, 0.45),
            arrowprops={"arrowstyle": "->", "color": "#444444"}, fontsize=10)
ax.text(2.4, 2.12, "Efficient frontier", color="#145da0", fontsize=11)
ax.text(3.2, 0.95, "Feasible portfolios", color="#4b5969", fontsize=10)
ax.text(2.25, -0.42, "Inefficient branch", color="#717b89", fontsize=10)
ax.set(xlim=(0, 5), ylim=(-0.65, 2.55), xlabel="Variance of terminal wealth",
       ylabel="Mean terminal wealth", title="Mean–variance frontier at a fixed budget")
ax.spines[["top", "right"]].set_visible(False)
ax.grid(alpha=0.18)
fig.tight_layout()
fig.savefig("paper-4-frontier.png", facecolor="white", transparent=False)
plt.close(fig)
