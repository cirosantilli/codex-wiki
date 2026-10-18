"""Original ideal-model illustration; write the PNG into the current directory."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def final_population(n):
    n = np.asarray(n)
    return (1 - np.cos(np.pi / n) ** n) / 2


def main():
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.5), layout="constrained")
    fig.patch.set_facecolor("white")
    times = np.linspace(0, 1, 4097)
    left, right = axes
    left.plot(times, np.sin(np.pi * times / 2) ** 2, label="No intervening probes", color="0.3")
    for n, color in [(4, "#b65115"), (64, "#146eae")]:
        completed = np.minimum(np.floor(n * times).astype(int), n)
        fraction = times - completed / n
        z = np.cos(np.pi / n) ** completed
        population = (1 - z * np.cos(np.pi * fraction)) / 2
        left.plot(times, population, label=f"{n} equally spaced probes", color=color, lw=2)
    left.set(title="Final population is suppressed by repeated probes", xlabel=r"Time / resonant $\pi$-pulse duration", ylabel=r"Population of $b$", xlim=(0, 1), ylim=(0, 1.03))
    left.legend(loc="upper left", fontsize=10)
    counts = np.arange(1, 257)
    right.loglog(counts, final_population(counts), label="Final population in b", lw=2, color="#146eae")
    departure = -np.expm1(2 * counts * np.log(np.cos(np.pi / (2 * counts))))
    right.loglog(counts, departure, label="At least one b result in the record", color="#b65115", ls="--", lw=2)
    large = counts[counts >= 8]
    right.loglog(large, np.pi**2 / (4 * large), color="0.4", ls=":", label=r"Common leading term $\pi^2/(4n)$")
    right.scatter([64], [final_population(64)], s=40, color="#146eae", zorder=5)
    right.annotate("n = 64: final population 3.71%", (64, final_population(64)), xytext=(18, 0.012), arrowprops={"arrowstyle": "->", "color": "0.3"}, fontsize=10)
    right.set(title="Two different finite-probe probabilities", xlabel="Number of probes, n", ylabel="Probability", xlim=(1, 256), ylim=(0.006, 1.12))
    right.legend(loc="upper right", fontsize=9)
    for axis in axes:
        axis.grid(alpha=0.18)
    fig.suptitle("Quantum Zeno inhibition: ideal instantaneous, nonselective measurements", fontsize=15)
    fig.savefig(Path.cwd() / "5-rabi-zeno-inhibition.png", dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
