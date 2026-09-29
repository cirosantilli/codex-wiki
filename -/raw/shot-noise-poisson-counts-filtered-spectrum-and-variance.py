"""Original analytic Poisson/filter examples, not experimental or simulated data.

Python 3.14; numpy 2.3.5; matplotlib 3.10.7. Emit basename.png in CWD.
With a=lambda*tau, u=t/tau, x=tau*i_filtered/q, and nu=f*tau,
the exponential filter yields E[x]=a, Var(x)=a/2, S_x(nu)=2a/(1+(2*pi*nu)^2).
The count in a gate of length tau instead has mean a and variance a.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 10, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(1, 3, figsize=(11.3, 4.6), dpi=120, facecolor="white")
    blue, orange, green = "#17659a", "#aa5515", "#26734d"
    n = np.arange(15)
    probability = np.empty(15)
    probability[0] = np.exp(-4.0)
    for k in range(1, 15):
        probability[k] = probability[k - 1] * 4 / k
    axes[0].bar(n, probability, color=blue, width=.8)
    axes[0].set(xlabel="Count n in one gate", ylabel="Probability",
                title="A. Discrete counts: mean 4", xlim=(-.8, 14.8), ylim=(0, .245))
    axes[0].set_xticks([0, 4, 8, 12])
    axes[0].text(7.0, .205, "Poisson(4)\nmean = variance = 4", ha="center", fontsize=9)
    nu = np.geomspace(.002, 12, 500)
    for a, color in [(1, blue), (4, orange), (8, green)]:
        axes[1].loglog(nu, 2 * a / (1 + (2 * np.pi * nu) ** 2),
                       color=color, label=f"a = {a}")
    axes[1].axvline(1 / (2 * np.pi), color=".5", lw=1, ls=":")
    axes[1].set(xlabel=r"Frequency $\nu=f\tau$", ylabel=r"One-sided $S_x^{(1)}(\nu)$",
                title="B. Exponential filtering", xlim=(.002, 12), ylim=(.0002, 30))
    axes[1].legend(fontsize=9, loc="lower left")
    axes[1].text(.55, .69, r"$\nu_c=1/(2\pi)$", transform=axes[1].transAxes, fontsize=9)
    a = np.linspace(0, 10, 200)
    axes[2].plot(a, a, color=blue, label="Gate count: variance = a")
    axes[2].plot(a, a / 2, color=orange, label="Filtered x: variance = a/2")
    axes[2].scatter([4, 4], [4, 2], color=[blue, orange], s=35, zorder=4)
    axes[2].set(xlabel="Common mean a", ylabel="Variance",
                title="C. Weighting changes variance", xlim=(0, 10), ylim=(0, 10.7))
    axes[2].legend(loc="upper left", fontsize=8.5)
    for ax in axes:
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(alpha=.18, axis="y")
        ax.set_axisbelow(True)
    fig.suptitle("Exact model calculations — no experimental trace", fontsize=15, weight="bold", y=.97)
    fig.text(.5, .075, r"$a=\lambda\tau$,  $x=\tau i_{\rm filtered}/q$,  "
             r"$\int_0^\infty S_x^{(1)}(\nu)\,d\nu=a/2$;  gate duration = $\tau$.",
             ha="center", fontsize=11)
    fig.text(.5, .02, "Stationary independent equal-charge arrivals; ideal unit-gain exponential response.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=.067, right=.985, bottom=.24, top=.79, wspace=.4)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
