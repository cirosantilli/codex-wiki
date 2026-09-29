"""Generate stochastic-process-paths.png in cwd.

Tested with Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
The discrete-time panels share Bernoulli draws; the continuous-time panel
simulates independent exponential gaps, not a discretized arrival grid.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    rng = np.random.default_rng(20261011)
    n = 24
    bits = rng.integers(0, 2, size=(3, n))
    walks = np.column_stack((np.zeros(3, dtype=int), np.cumsum(2 * bits - 1, axis=1)))
    assert np.all(np.abs(np.diff(walks, axis=1)) == 1)
    rate, horizon = 2.0, 4.0
    arrivals = []
    for _ in range(3):
        t, events = 0.0, []
        while True:
            t += rng.exponential(1 / rate)
            if t > horizon:
                break
            events.append(t)
        arrivals.append(np.array(events))
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(3, 1, figsize=(9.5, 8.2), dpi=120,
                             facecolor="white")
    colors = ["#2878ad", "#c05a2a", "#24805e"]
    for j, color in enumerate(colors):
        # Small offsets make coincident binary observations visible.
        axes[0].scatter(np.arange(1, n + 1), bits[j] + (j - 1) * 0.055,
                        color=color, s=25, label=f"Outcome {j + 1}")
        axes[1].plot(np.arange(n + 1), walks[j], "o-", color=color,
                     markersize=3, lw=1.3)
        times = np.concatenate(([0.0], arrivals[j], [horizon]))
        counts = np.concatenate((np.arange(len(arrivals[j]) + 1), [len(arrivals[j])]))
        axes[2].step(times, counts, where="post", color=color, lw=1.8)
    axes[0].set(title="Bernoulli process: a fresh 0 or 1 at each integer time",
                ylabel=r"$B_n$", ylim=(-0.18, 1.18), yticks=[0, 1],
                xlabel="Integer time n", xlim=(0, n + 1))
    fig.legend(*axes[0].get_legend_handles_labels(), loc="upper center",
               bbox_to_anchor=(0.5, 0.947), ncol=3, fontsize=9, frameon=False)
    axes[1].set(title=r"Random walk: accumulate the same signs $2B_n-1$",
                ylabel=r"$S_n$", xlabel="Integer time n", xlim=(0, n))
    axes[1].axhline(0, color="gray", lw=0.7)
    axes[2].set(title=r"Poisson process: count arrivals at random times ($\lambda=2$)",
                ylabel=r"$N_t$", xlabel="Continuous time t", xlim=(0, horizon))
    for ax in axes:
        ax.set_facecolor("white")
        ax.grid(alpha=0.15)
    fig.suptitle("A stochastic process describes a whole random history", fontsize=15)
    fig.text(0.5, 0.018,
             "Three simulated outcomes; seed 20261011. Binary dots are offset slightly.\n"
             "Random-walk segments connect integer observations; Poisson stairs are right-continuous.",
             ha="center", fontsize=9)
    fig.tight_layout(rect=(0, 0.055, 1, 0.92), h_pad=1.6)
    fig.savefig(Path.cwd() / "stochastic-process-paths.png", facecolor="white", transparent=False)
    plt.close(fig)
    print("Walk endpoints:", walks[:, -1].tolist())
    print("Poisson counts at t=4:", [len(x) for x in arrivals])
    print("P(S_4=0)=6/16=3/8; P(N_1=0)=exp(-2)")


if __name__ == "__main__":
    main()
