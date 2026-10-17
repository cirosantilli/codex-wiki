"""Fixed-width top-hat inference in units of the observed parallax center."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def main():
    p = np.linspace(.5, 1.5, 801)
    density = 3*p**-4/(.5**-3-1.5**-3)
    median = (27/112)**(1/3)
    fig, ax = plt.subplots(figsize=(8, 4.5), layout="constrained")
    ax.plot(p, density, lw=2.2, label="Normalized posterior")
    ax.fill_between(p, density, where=p <= median, color="tab:blue", alpha=.15, label="Lower half of posterior probability")
    ax.plot([.5, 1.5], [1, 1], ls="--", color="tab:orange", label="Likelihood shape (scaled)")
    ax.axvline(median, color="tab:blue", ls=":", label=f"Median: {median:.4f}")
    ax.axvline(1, color="0.4", ls="--", label="Reported center")
    ax.set(xlabel=r"True parallax / reported center $p/p_0$", ylabel="Density in normalized parallax units",
           title="A volume prior shifts the posterior below the likelihood center", xlim=(.45, 1.55), ylim=(0, 6.6))
    ax.legend(loc="upper right", frameon=False); ax.grid(alpha=.18)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
