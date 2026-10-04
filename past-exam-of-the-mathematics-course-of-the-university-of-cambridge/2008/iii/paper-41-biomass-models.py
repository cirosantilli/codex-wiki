"""Illustrative mean curves; Python 3.14, NumPy and Matplotlib from root dependencies."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def main():
    biomass = np.linspace(0, 4, 401)
    intercepts = [3.2, 3.0, 2.8]
    labels = ["Low pH", "Medium pH", "High pH"]
    colors = ["#0072B2", "#D55E00", "#009E73"]
    fig, axes = plt.subplots(2, 2, figsize=(11, 7), dpi=100, facecolor="white")
    for column, slopes in enumerate([[-0.4] * 3, [-0.6, -0.2, -0.4]]):
        for intercept, slope, label, color in zip(intercepts, slopes, labels, colors):
            log_mean = intercept + slope * biomass
            axes[0, column].plot(biomass, log_mean, color=color, label=label, linewidth=2)
            axes[1, column].plot(biomass, np.exp(log_mean), color=color, label=label, linewidth=2)
        axes[0, column].set_title(["Additive: common log-mean slope", "Interaction: pH-specific log-mean slopes"][column])
        axes[0, column].set_ylabel("Log mean species count")
        axes[1, column].set_ylabel("Mean species count")
        for ax in axes[:, column]:
            ax.set_facecolor("white")
            ax.set_xlabel("Biomass (illustrative units)")
            ax.grid(alpha=0.2)
            ax.set_xlim(0, 4)
        axes[0, column].legend(loc="upper right")
    fig.suptitle("Schematic Poisson mean models — coefficients illustrative, not fitted", fontsize=13)
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    fig.savefig(Path.cwd() / "paper-41-biomass-models.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
