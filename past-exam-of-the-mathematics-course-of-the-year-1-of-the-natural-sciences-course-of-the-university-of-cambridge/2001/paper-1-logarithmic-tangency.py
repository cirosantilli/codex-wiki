"""Original logarithmic curves, extrema and unique common tangent."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(9, 4.2), layout="constrained")
for ax, limits in zip(axes, [(.08, 3.5), (.55, 1.5)]):
    x = np.linspace(*limits, 1200)
    ax.plot(x, x*np.log(x), color="#287ca3", lw=2, label=r"$f=x\ln x$")
    ax.plot(x, np.log(x)/x, color="#b56529", lw=2, label=r"$g=(\ln x)/x$")
    ax.axhline(0, color="#777777", lw=.8)
    ax.set(xlabel="x", xlim=limits)
    ax.grid(alpha=.14)
axes[0].set(ylim=(-1.35, 4.5), title="Extrema and endpoint behavior")
axes[0].scatter([1/np.e, np.e, 1], [-1/np.e, 1/np.e, 0], color="#555555", s=25, zorder=4)
axes[0].annotate(r"$f$ minimum", (1/np.e, -1/np.e), xytext=(.55, -.95),
                 arrowprops=dict(arrowstyle="->", color="#666666"), fontsize=10)
axes[0].annotate(r"$g$ maximum", (np.e, 1/np.e), xytext=(1.6, 1.35),
                 arrowprops=dict(arrowstyle="->", color="#666666"), fontsize=10)
axes[0].legend(frameon=False, loc="upper left")
x = np.linspace(.55, 1.5, 100)
axes[1].plot(x, x-1, color="#777777", ls="--", lw=1.3, label=r"Common tangent $y=x-1$")
axes[1].scatter([1], [0], color="#555555", s=30, zorder=4)
axes[1].set(ylim=(-.7, .7), title="Tangency without crossing")
axes[1].legend(frameon=False, loc="upper left", fontsize=9)
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
plt.close(fig)
