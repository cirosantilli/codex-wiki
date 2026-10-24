"""Render 2017-sine-power-integrability.png into the current directory."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, (left, right) = plt.subplots(1, 2, figsize=(11.5, 4.8), dpi=100,
                                     gridspec_kw={"width_ratios": [1, 1.2]},
                                     facecolor="white")
    left.hlines(1, 0, 2, color="#15803d", linewidth=7)
    left.hlines(0, 1, 2, color="#2563eb", linewidth=7)
    for x, y in [(0, 1), (2, 1), (1, 0), (2, 0)]:
        left.plot(x, y, "o", markerfacecolor="white", markeredgecolor="#334155",
                  markersize=8, markeredgewidth=1.4, zorder=4)
    left.axvline(1, color="#b91c1c", linestyle=":", linewidth=1.2)
    left.axvline(1.25, color="#7e22ce", linestyle="--", linewidth=1.1)
    left.annotate(r"$p=1$: conditional", (1, 0.5), xytext=(0.13, 0.46),
                  textcoords="axes fraction", color="#b91c1c", fontsize=10)
    left.text(1.25, 1.37, r"$p=5/4$", color="#7e22ce", ha="center", fontsize=11)
    left.set(yticks=[0, 1], yticklabels=["Absolute\n(Lebesgue)", "Signed\nimproper"],
             xticks=[0, 1, 1.25, 2], xticklabels=["0", "1", r"$5/4$", "2"],
             xlim=(-0.12, 2.3), ylim=(-0.45, 1.65), xlabel=r"Power $p>0$")
    left.set_title(r"Convergence of $\int_0^\infty \sin(x)x^{-p}\,dx$", fontsize=12)
    left.spines[["top", "right", "left"]].set_visible(False)
    left.tick_params(axis="y", length=0, pad=9)
    left.grid(axis="x", alpha=0.13)

    nodes, weights = np.polynomial.legendre.leggauss(48)
    endpoints = np.r_[1.0, np.arange(1, 241) * np.pi]
    middle = (endpoints[:-1] + endpoints[1:]) / 2
    half = np.diff(endpoints) / 2
    points = middle[:, None] + half[:, None] * nodes
    values = np.sin(points) / points
    signed = np.cumsum(half * (values @ weights))
    absolute = np.cumsum(half * (np.abs(values) @ weights))
    lower = np.r_[0.0, np.cumsum(2 / (np.arange(2, 241) * np.pi))]
    cutoffs = endpoints[1:]
    right.plot(cutoffs, absolute, color="#2563eb", linewidth=2,
               label=r"Absolute: $\int_1^T |\sin t|/t\,dt$")
    right.plot(cutoffs, lower, color="#c2410c", linewidth=1.7, linestyle=":",
               label="Divergent harmonic lower bound")
    right.plot(cutoffs, signed, color="#15803d", linewidth=1.7, linestyle="--",
               label=r"Signed: $\int_1^T \sin t/t\,dt$")
    right.set_xscale("log")
    right.set(xlabel=r"Cutoff $T=N\pi$ (log scale)", ylabel="Truncated integral", ylim=(0, None))
    right.set_title(r"Cancellation at $p=1$", fontsize=12)
    right.grid(alpha=0.2)
    right.legend(loc="upper left", fontsize=9, frameon=False)
    fig.suptitle("Oscillation permits cancellation without absolute integrability", fontsize=14)
    fig.subplots_adjust(left=0.105, right=0.98, bottom=0.17, top=0.80, wspace=0.43)
    fig.savefig("2017-sine-power-integrability.png", dpi=100, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
