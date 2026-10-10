"""Original ideal gap-matrix cuts and a stipulated damped collective oscillator."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

DAMPING = 0.08


def normalized_absorbed_power(frequency, natural_frequency):
    return (4 * DAMPING ** 2 * frequency ** 2 /
            ((natural_frequency ** 2 - frequency ** 2) ** 2 + 4 * DAMPING ** 2 * frequency ** 2))


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12})
    fig = plt.figure(figsize=(13.6, 4.7), layout="constrained")
    grid = fig.add_gridspec(1, 3, width_ratios=(1.05, 1.1, 1.1))
    polar = fig.add_subplot(grid[0], projection="polar")
    field_ax = fig.add_subplot(grid[1])
    power_ax = fig.add_subplot(grid[2])
    theta = np.linspace(0, 2 * np.pi, 721)
    polar.set_theta_zero_location("N")
    polar.plot(theta, np.ones_like(theta), label="B model: constant gap", color="#285c9e", linewidth=2.4)
    polar.plot(theta, np.abs(np.sin(theta)), label=r"A model: $|\sin\theta|$", color="#b54a39", linewidth=2.4)
    polar.set(ylim=(0, 1.12), yticks=[0.5, 1.0], title="Specified gap matrices\nmeridional cuts, gap / maximum")
    polar.legend(loc="lower center", bbox_to_anchor=(0.5, -0.30), frameon=False, fontsize=10)
    field = np.linspace(0, 5, 501)
    field_ax.plot(field, field, "--", label=r"$K=0$", color="#6d6d6d", linewidth=2)
    field_ax.plot(field, np.sqrt(field ** 2 + 1), label=r"$K/I=1$", color="#285c9e", linewidth=2.4)
    field_ax.plot([2, 2], [2, np.sqrt(5)], color="#b54a39", marker="o", markersize=4)
    field_ax.annotate(r"$2\to\sqrt{5}$", (2, np.sqrt(5)), xytext=(7, 15), textcoords="offset points")
    field_ax.set(title="Chosen collective curvature", xlabel=r"$\omega_L$ (chosen frequency unit)",
                 ylabel=r"$\omega_0$ (same unit)", xlim=(0, 5), ylim=(0, 5.4))
    field_ax.legend(frameon=False)
    field_ax.grid(alpha=0.22)
    frequency = np.unique(np.r_[np.linspace(1.2, 3.0, 1501), 2.0, np.sqrt(5)])
    for natural, color, style, label in [(2.0, "#6d6d6d", "--", r"$K=0$: peak 2"),
                                         (np.sqrt(5), "#285c9e", "-", r"$K/I=1$: peak $\sqrt{5}$")]:
        power_ax.plot(frequency, normalized_absorbed_power(frequency, natural), color=color,
                      linestyle=style, label=label, linewidth=2.2)
    power_ax.set(title=r"Absorption at $\omega_L=2$, $\Gamma=0.08$", xlabel=r"Drive frequency $\omega$ (same unit)",
                 ylabel="Absorbed power / peak power", xlim=(1.2, 3.0), ylim=(0, 1.08))
    power_ax.legend(frameon=False, fontsize=10)
    power_ax.grid(alpha=0.22)
    fig.suptitle("Pairing directions and a scalar collective-response model — not experimental data", fontsize=14)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
