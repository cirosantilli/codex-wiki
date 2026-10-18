"""Original censored-normal posterior illustration for the Oxford 2021 solution.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7 (root pyproject.toml).
Run from any CWD; writes only the same-basename opaque PNG into that CWD.
The proper illustrative priors are mu~U(0,60), sigma~U(1,20); not inferred data.
"""
from pathlib import Path
import math
import numpy as np
from numpy.polynomial.legendre import leggauss
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

LATE = {20: 1, 21: 3, 25: 3, 27: 1, 32: 2}
EARLY = {29: 1, 34: 1, 36: 3, 37: 1, 38: 1, 39: 1, 43: 1, 44: 1}
normal_cdf = np.vectorize(lambda z: 0.5 * math.erfc(-float(z) / math.sqrt(2)), otypes=[float])


def log_likelihood(mu, sigma):
    result = np.zeros(np.broadcast_shapes(np.shape(mu), np.shape(sigma)))
    for counts, sign in [(LATE, 1), (EARLY, -1)]:
        for threshold, count in counts.items():
            with np.errstate(divide="ignore"):
                result += count * np.log(normal_cdf(sign * (mu - threshold) / sigma))
    return result


def main():
    nodes, weights = leggauss(256)
    mu = 30 * (nodes + 1)
    sigma = 1 + 9.5 * (nodes + 1)
    weighted = np.exp(log_likelihood(mu[:, None], sigma[None, :])) * weights[:, None] * weights[None, :] / 4
    evidence = weighted.sum()
    pi = normal_cdf((mu[:, None] - 30) / sigma[None, :])
    single = (weighted * pi).sum() / evidence
    repeated = (weighted * pi ** 5).sum() / evidence

    plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(9.2, 3.8), dpi=100, gridspec_kw={"width_ratios": [1.3, 1]})
    fig.patch.set_facecolor("white")
    mus = np.linspace(20, 42, 250)
    sigmas = np.linspace(1, 20, 220)
    xx, yy = np.meshgrid(mus, sigmas)
    posterior_density = np.exp(log_likelihood(xx, yy)) / (60 * 19 * evidence)
    contour = ax.contourf(xx, yy, posterior_density, levels=12, cmap="Blues")
    fig.colorbar(contour, ax=ax, label="Posterior density (min⁻²)", pad=0.025)
    ax.set(xlabel="Mean duration μ (min)", ylabel="Standard deviation σ (min)", title="Shared parameter uncertainty")
    values = [single ** 5, repeated]
    bars = bx.bar([0, 1], values, color=["#8899aa", "#215e8a"], width=0.6)
    bx.set_xticks([0, 1], ["Power of single-day\nprobability", "Integrated five-day\nprobability"])
    bx.set(ylim=(0, 0.19), ylabel="Probability of five late days", title="Integrate after taking the power")
    for bar, value in zip(bars, values):
        bx.text(bar.get_x() + bar.get_width() / 2, value + 0.006, f"{value:.4f}", ha="center")
    fig.suptitle("Illustrative priors: μ ∼ Uniform(0, 60), σ ∼ Uniform(1, 20)", fontsize=11)
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False,
                metadata={"Software": "NumPy/Matplotlib; original Oxford 2021 solution figure"})
    plt.close(fig)


if __name__ == "__main__":
    main()
