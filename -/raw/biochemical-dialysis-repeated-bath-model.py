"""Original fixed-volume dialysis model; Python 3.14, matplotlib 3.10/numpy 2.3."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    sample_volume, bath_volume = 1.0, 9.0
    fraction = sample_volume / (sample_volume + bath_volume)
    cycles = np.arange(4)
    concentration = fraction**cycles
    fig, (balance, repeated) = plt.subplots(1, 2, figsize=(10.2, 4.8), dpi=120, facecolor="white", gridspec_kw={"width_ratios": [1, 1.3]})
    fig.suptitle("Ideal dialysis: conservation first, fresh baths next", fontsize=16, weight="bold", y=0.96)
    balance.bar([0, 1], [fraction, 1 - fraction], color=["#137caf", "#8cb6cc"], width=0.58)
    balance.set(xticks=[0, 1], xticklabels=["Sample\n1 mL", "First bath\n9 mL"], ylim=(0, 1.12), ylabel=r"Solute amount / initial amount $c_0V_s$", title="After the first equilibration")
    for x, value in enumerate([fraction, 1 - fraction]):
        balance.text(x, value + 0.035, f"{value:.1f}", ha="center", fontsize=13, weight="bold")
    balance.text(0.5, 1.065, "0.1 + 0.9 = 1 (conserved)", ha="center", fontsize=10)
    repeated.set_yscale("log")
    repeated.plot(cycles, concentration, "o-", color="#137caf", ms=8, lw=2, label="Permeant solute")
    repeated.plot(cycles, np.ones_like(cycles), "s--", color="#7852a5", ms=6, lw=1.6, label="Perfectly retained protein")
    repeated.set(xlim=(-0.15, 3.6), ylim=(0.00045, 2.3), xticks=cycles, xlabel="Completed equilibrations with fresh baths, n", ylabel=r"Sample concentration / initial concentration", title=r"$c_n/c_0=(1/(1+9))^n=10^{-n}$")
    repeated.set_yticks([1, 0.1, 0.01, 0.001], labels=["1", "0.1", "0.01", "0.001"])
    for n, value, label in zip(cycles[1:], concentration[1:], ["0.1", "0.01", "0.001"], strict=True):
        repeated.annotate(label, (n, value), xytext=(9, 8), textcoords="offset points", fontsize=12, weight="bold", color="#137caf")
    repeated.grid(axis="y", which="major", alpha=0.22)
    repeated.legend(loc="upper right", bbox_to_anchor=(1, 0.83), fontsize=10, framealpha=1)
    for ax in (balance, repeated):
        ax.spines[["top", "right"]].set_visible(False)
        ax.tick_params(labelsize=10)
    fig.text(0.5, 0.08, "Fixed volumes; solute-free new baths; complete equilibration; no binding or loss.", ha="center", fontsize=11)
    fig.text(0.5, 0.035, "Model endpoints, not a time course. Each species uses its own initial concentration; protein is ideally retained.", ha="center", fontsize=9.5, color="#46535d")
    fig.subplots_adjust(left=0.09, right=0.98, bottom=0.24, top=0.78, wspace=0.38)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
