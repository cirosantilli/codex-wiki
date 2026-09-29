"""Render the exponential-mixture example to a PNG basename in cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
The caller owns MPLCONFIGDIR; this script does not change it.
"""
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

t = np.linspace(0.0, 6.0, 601)
slow = np.exp(-t)
fast = np.exp(-2.0 * t)
survival = 0.25 * slow + 0.75 * fast
hazard = (slow + 6.0 * fast) / (slow + 3.0 * fast)

with plt.rc_context({"font.size": 11, "axes.labelsize": 12, "axes.titlesize": 12}):
    fig, axes = plt.subplots(1, 2, figsize=(8.4, 4.2), dpi=100, facecolor="white")
    fig.suptitle("Survival selection in a two-rate exponential mixture", fontsize=14, y=0.96)
    ax = axes[0]
    ax.plot(t, slow, "--", color="#5980a6", label="Rate 1 component")
    ax.plot(t, fast, "--", color="#b56544", label="Rate 2 component")
    ax.plot(t, survival, color="#172c40", linewidth=2.4, label="Mixture survival")
    ax.set(title="Weighted exponential survival", xlabel="Time", ylabel="Survival probability", xlim=(0, 6), ylim=(0, 1.04))
    ax.legend(frameon=False, fontsize=9)
    ax = axes[1]
    ax.axhline(2.0, linestyle="--", color="#b56544", linewidth=1.3, label="Rate 2")
    ax.axhline(1.0, linestyle="--", color="#5980a6", linewidth=1.3, label="Rate 1 limit")
    ax.plot(t, hazard, color="#172c40", linewidth=2.4, label="Population hazard")
    ax.scatter([0], [1.75], color="#172c40", zorder=3)
    ax.annotate("Initial hazard 1.75", xy=(0, 1.75), xytext=(0.65, 1.82), fontsize=10)
    ax.set(title="Survivors favor the slower rate", xlabel="Time", ylabel="Hazard", xlim=(0, 6), ylim=(0.88, 2.10))
    ax.legend(frameon=False, fontsize=9, loc="center right")
    for ax in axes:
        ax.set_facecolor("white")
        ax.grid(alpha=0.20)
        ax.spines[["top", "right"]].set_visible(False)
    fig.subplots_adjust(left=0.08, right=0.98, bottom=0.14, top=0.79, wspace=0.33)
    fig.savefig("paper-41-mixture-hazard.png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)
