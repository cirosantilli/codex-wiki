"""Plot fitted film means and wash-cell means; write the PNG to the caller's cwd."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    response = np.array([
        3.3, 4.1, 4.9, 5.0, 3.4, 4.0, 4.2, 4.9,
        19.6, 17.5, 17.6, 20.9, 14.5, 17.0, 15.2, 17.1,
        5.5, 5.7, 5.6, 7.2, 3.7, 6.1, 5.7, 6.0,
        26.6, 31.6, 30.5, 31.4, 29.5, 30.2, 30.2, 29.6,
    ]).reshape(2, 2, 2, 4)
    fitted_means = response.mean(axis=(2, 3))
    residuals = response - fitted_means[:, :, None, None]
    standard_error = np.sqrt(np.sum(residuals**2) / 28 / 8)
    cell_means = response.mean(axis=2)
    wash_minutes = np.array([20, 30, 40, 60])
    fig, (interaction, wash) = plt.subplots(
        1, 2, figsize=(8.8, 4.4), dpi=120, sharey=True, facecolor="white"
    )
    colors = ["#3572b0", "#d27817"]
    for thickness, name in enumerate(["Thin film", "Thick film"]):
        interaction.errorbar(
            [0, 1], fitted_means[thickness], yerr=standard_error,
            color=colors[thickness], marker="o", linewidth=2, capsize=4,
            label=name,
        )
        for temperature, temperature_name in enumerate(["low", "high"]):
            wash.plot(
                wash_minutes, cell_means[thickness, temperature],
                color=colors[thickness],
                linestyle="--" if temperature == 0 else "-",
                marker="o", linewidth=1.6,
                label=f"{name}, {temperature_name} temperature",
            )
    interaction.set(
        xticks=[0, 1], xticklabels=["Low", "High"],
        xlim=(-0.12, 1.12), ylim=(0, 35), xlabel="Wash temperature",
        ylabel="Lustre", title="Fitted means and ±1 standard error",
    )
    wash.set(
        xticks=wash_minutes, xlim=(17, 63), xlabel="Wash duration (minutes)",
        title="Means of the two replicates in each cell",
    )
    interaction.legend(frameon=False, fontsize=9, loc="upper left")
    wash.legend(frameon=False, fontsize=8, loc="center", bbox_to_anchor=(0.52, 0.32))
    for ax in [interaction, wash]:
        ax.grid(alpha=0.2)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Plastic-film lustre: strong temperature–thickness interaction", fontsize=12)
    fig.text(
        0.5, 0.025,
        "Reduced model: eight observations per fitted mean; its pooled residual variance gives SE = 0.50488.",
        ha="center", fontsize=8.8, color="#354254",
    )
    fig.tight_layout(rect=(0, 0.06, 1, 0.93))
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
