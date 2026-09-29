"""Draw SI sample paths; write the PNG in the caller's working directory."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def sample_path(population, initial_fraction, rate, horizon, rng):
    susceptible = round(population * initial_fraction)
    time = 0.0
    times = [time]
    fractions = [susceptible / population]
    while susceptible:
        event_rate = rate * susceptible * (population - susceptible) / population
        if not event_rate:
            break
        time += rng.exponential(1 / event_rate)
        if time > horizon:
            break
        susceptible -= 1
        times.append(time)
        fractions.append(susceptible / population)
    times.append(horizon)
    fractions.append(fractions[-1])
    return np.asarray(times), np.asarray(fractions)


def main():
    rng = np.random.default_rng(200636)
    initial_fraction = 0.8
    rate = 1.0
    horizon = 6.0
    fig, ax = plt.subplots(figsize=(8, 4.2), dpi=120, facecolor="white")
    for population, color in [(50, "#d27817"), (200, "#429a73"), (800, "#3572b0")]:
        times, fractions = sample_path(
            population, initial_fraction, rate, horizon, rng
        )
        ax.step(
            times, fractions, where="post", color=color, linewidth=1.4,
            label=f"Stochastic SI model, n = {population}",
        )
    times = np.linspace(0, horizon, 601)
    decay = np.exp(-rate * times)
    limit = initial_fraction * decay / (1 - initial_fraction + initial_fraction * decay)
    ax.plot(times, limit, "--", color="#20242a", linewidth=2.0, label="Deterministic fluid limit")
    ax.set(
        xlim=(0, horizon), ylim=(0, 0.84),
        xlabel="Time", ylabel="Susceptible fraction",
        title="SI epidemic: susceptible fractions and their fluid limit",
    )
    ax.grid(alpha=0.2)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(frameon=False, fontsize=9.5)
    fig.text(
        0.5, 0.035,
        "One realization per population size; initially 80% susceptible, infection rate λ = 1.",
        ha="center", fontsize=9.5, color="#354254",
    )
    fig.tight_layout(rect=(0, 0.065, 1, 1))
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
