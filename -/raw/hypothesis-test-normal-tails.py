"""Draw chosen normal rejection tails and observed p-value tails.

Tested with Python 3.14.4; dependencies are NumPy and Matplotlib.
Run from _media with MPLBACKEND=Agg and MPLCONFIGDIR=/tmp.
"""

from math import erfc, sqrt
from pathlib import Path
from statistics import NormalDist

import matplotlib.pyplot as plt
import numpy as np


def main():
    sigma, n, mean, null_mean, alpha = 2.0, 16, 1.2, 0.0, 0.05
    standard_error = sigma / sqrt(n)
    observed_z = (mean - null_mean) / standard_error
    critical = NormalDist().inv_cdf(1 - alpha/2)
    pvalue = erfc(abs(observed_z)/sqrt(2))
    assert abs(observed_z - 2.4) < 1e-14
    assert abs(pvalue - 0.016395071849192273) < 1e-14
    assert abs(erfc(critical/sqrt(2)) - alpha) < 1e-14
    normal = NormalDist()
    for sample_size in [16, 64]:
        shift = 1 / (sigma / sqrt(sample_size))
        beta = normal.cdf(critical-shift) - normal.cdf(-critical-shift)
        print(f"At alternative mu=1, n={sample_size}: beta={beta:.12f}, power={1-beta:.12f}")

    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.2), layout="constrained",
                             sharey=True, facecolor="white")
    blue, orange = "#146b9b", "#b33e13"
    x = np.linspace(-4.2, 4.2, 2501)
    density = np.exp(-x*x/2) / sqrt(2*np.pi)
    choices = [(critical, orange, "Rule chosen before observing data",
                r"Reject when $|Z|>1.959964\ldots$", f"Total shaded area α = {alpha:.2f}"),
               (abs(observed_z), blue, "Tail area from the observed statistic",
                r"Observed $z=1.2/0.5=2.4$", f"Total shaded area p = {pvalue:.7f}")]
    for ax, (threshold, color, title, subtitle, area) in zip(axes, choices):
        ax.plot(x, density, color="#222222", linewidth=1.7)
        ax.fill_between(x, density, where=abs(x) >= threshold, color=color, alpha=0.8)
        for sign in [-1, 1]:
            boundary = sign * threshold
            ax.axvline(boundary, color=color, linestyle="--", linewidth=1.2)
            ax.text(boundary, 0.014, f"{boundary:.2f}", color=color,
                    ha="center", va="bottom", fontsize=10,
                    bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})
        ax.set(xlim=(-4.2, 4.2), ylim=(0, 0.51), xlabel="Standardized statistic Z")
        ax.set_title(title + "\n" + subtitle, fontsize=11, pad=12)
        ax.text(0, 0.45, area, ha="center", color=color, fontsize=11)
        ax.set_xticks([-4, -2, 0, 2, 4])
    axes[0].set_ylabel("Probability density under H₀")
    fig.suptitle("Two different tail areas under the same null distribution\n"
                 r"$H_0:\mu=0$; $Z=\bar X/(2/\sqrt{16})\sim N(0,1)$ under $H_0$",
                 fontsize=13)
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Saved {output}")
    print(f"Observed z={observed_z:.12f}; p=erfc(|z|/sqrt(2))={pvalue:.12f}; alpha={alpha}")


if __name__ == "__main__":
    main()
