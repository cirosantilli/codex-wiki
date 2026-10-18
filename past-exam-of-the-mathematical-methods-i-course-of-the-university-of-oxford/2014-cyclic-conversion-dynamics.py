"""Original three-component linear conversion plots for June 2014 CP3 Q11.

Uniformization evaluates the matrix exponential without an eigenbasis, so it
also works at a defective repeated eigenvalue. Writes a matching PNG to CWD.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def trajectory(t, a, b, c):
    m = np.array([[-a, 0, c], [a, -b, 0], [0, b, -c]], dtype=float)
    rate = max(a, b, c)
    transition = np.eye(3) + m / rate
    weight = np.exp(-rate * t)
    v = np.array([1.0, 0.0, 0.0])
    result = v[:, None] * weight[None, :]
    for j in range(1, 200):
        weight = weight * (rate * t) / j
        v = transition @ v
        result += v[:, None] * weight[None, :]
    return result


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white", "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4), layout="constrained")
    t = np.linspace(0, 8, 801)
    for ax, rates, title in zip(axes, [(1, 1, 1), (1, 4, 1)],
                               ["Equal rates: complex decay modes", "Rates (1, 4, 1): repeated-root transient"]):
        a, b, c = rates
        values = trajectory(t, a, b, c)
        equilibrium = np.array([b*c, c*a, a*b]) / (a*b+b*c+c*a)
        for j, (name, color) in enumerate(zip(["A", "B", "C"], ["#0072B2", "#D55E00", "#009E73"])):
            ax.plot(t, values[j], label=name, color=color, linewidth=1.7)
            ax.axhline(equilibrium[j], linestyle=":", color=color, linewidth=1.2, alpha=.8)
        ax.plot(t, values.sum(axis=0), color="0.3", linestyle="--", linewidth=1, label="total")
        ax.set(xlabel="time in reciprocal rate units", ylabel="fraction of conserved total",
               ylim=(-0.02, 1.06), xlim=(0, 8), title=title)
        ax.legend(loc="upper right", fontsize=10)
        ax.grid(alpha=.2)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
