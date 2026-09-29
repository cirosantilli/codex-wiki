"""Show realized binary losses and their expectation; output basename to cwd.

Run from _media with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
No sampling: expectations use the stipulated Bernoulli probability q = 0.7.
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    q = 0.7
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.8), layout="constrained")
    fig.patch.set_facecolor("white")
    fig.suptitle("An honest forecast can lose on one draw: true q = 0.7", fontsize=14)
    p_brier = np.unique(np.r_[np.linspace(0, 1, 1001), 0.2, q])
    near_zero = np.geomspace(1e-6, 0.02, 250)
    p_log = np.unique(np.r_[near_zero, np.linspace(0.02, 0.98, 1601), 1 - near_zero, 0.2, q])
    for ax, p, zero, one, name, ymax in [
        (axes[0], p_brier, p_brier**2, (1 - p_brier) ** 2, "Brier loss", 1.05),
        (axes[1], p_log, -np.log1p(-p_log), -np.log(p_log), "Logarithmic loss", 4.0),
    ]:
        ax.set_facecolor("white")
        ax.plot(p, zero, color="#2369a5", lw=2.2, label="If Y = 0 (weight 0.3)")
        ax.plot(p, one, color="#b44d18", lw=2.2, label="If Y = 1 (weight 0.7)")
        ax.plot(p, (1 - q) * zero + q * one, color="#222222", lw=2.8, label="Expected loss")
        ax.axvline(q, color="#777777", linestyle=":", lw=1.3)
        ax.set(title=name + ": LOWER is better", xlabel="Reported success probability p", ylabel="Loss (original units)", xlim=(0, 1), ylim=(0, ymax), xticks=[0, 0.2, 0.4, 0.6, 0.7, 0.8, 1])
        ax.legend(loc="upper center", fontsize=9, frameon=True, facecolor="white", framealpha=0.95)
        comparison = np.array([0.2, q])
        values = comparison**2 if name == "Brier loss" else -np.log1p(-comparison)
        ax.scatter(comparison, values, color="#2369a5", s=35, zorder=5)
        for report, value in zip(comparison, values):
            ax.annotate(f"{value:.2f}" if name == "Brier loss" else f"{value:.3f}", (report, value), xytext=(5, 8), textcoords="offset points", color="#2369a5", fontsize=10)
        minimum = q * (1 - q) if name == "Brier loss" else -q * np.log(q) - (1 - q) * np.log1p(-q)
        ax.scatter([q], [minimum], color="#222222", s=30, zorder=5)
        ax.text(0.5, -0.21, "Blue dots compare p = 0.2 and honest p = 0.7\nwhen Y = 0. The expected minimum is at p = 0.7.", ha="center", va="top", transform=ax.transAxes, fontsize=10)
        ax.grid(alpha=0.2)
        ax.spines[["top", "right"]].set_visible(False)
    axes[1].text(0.5, 0.43, "Endpoint loss is infinite if the\nobserved outcome was assigned probability zero", ha="center", transform=axes[1].transAxes, fontsize=9, bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.9})
    fig.savefig("proper-score-realized-outcomes.png", dpi=130, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
