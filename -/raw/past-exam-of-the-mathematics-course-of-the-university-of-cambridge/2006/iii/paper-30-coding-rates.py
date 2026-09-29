#!/usr/bin/env python3
"""Plot binary-channel capacity and the Gilbert–Varshamov correction guarantee.

Writes paper-30-coding-rates.png to the caller's current directory.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def entropy(p):
    p = np.asarray(p, dtype=float)
    value = np.zeros_like(p)
    mask = (p > 0) & (p < 1)
    value[mask] = -p[mask] * np.log2(p[mask]) - (1-p[mask]) * np.log2(1-p[mask])
    return value


def inverse_entropy(value):
    left, right = 0.0, 0.5
    for _ in range(64):
        mid = (left + right) / 2
        if float(entropy(mid)) < value:
            left = mid
        else:
            right = mid
    return (left + right) / 2


def main():
    p = np.linspace(0, 0.5, 501)
    q = np.linspace(0, 0.25, 251)
    rate = 0.5
    threshold = inverse_entropy(1-rate)
    fig, ax = plt.subplots(figsize=(7.4, 4.6), layout="constrained", facecolor="white")
    ax.set_facecolor("white")
    ax.plot(p, 1-entropy(p), color="#1557a0", linewidth=2.4,
            label=r"Channel capacity: $1-h_2(p)$")
    ax.plot(q, 1-entropy(2*q), color="#b34a19", linewidth=2.4,
            label=r"GV correction guarantee: $1-h_2(2p)$")
    ax.axhline(rate, color="#555555", linestyle="--", linewidth=1)
    for value, color in [(threshold/2, "#b34a19"), (threshold, "#1557a0")]:
        ax.plot([value, value], [0, rate], color=color, linestyle=":", linewidth=1.4)
        ax.plot(value, rate, "o", color=color, markersize=5)
    ax.annotate(f"GV: p = {threshold/2:.3f}", (threshold/2, rate),
                xytext=(0.012, 0.24), arrowprops={"arrowstyle": "-", "color": "#b34a19"},
                color="#b34a19", fontsize=10)
    ax.annotate(f"Shannon threshold: p = {threshold:.3f}", (threshold, rate),
                xytext=(0.19, 0.57), arrowprops={"arrowstyle": "-", "color": "#1557a0"},
                color="#1557a0", fontsize=10)
    ax.text(0.38, rate+0.025, r"Example: $R=1/2$", color="#555555", fontsize=10)
    ax.set(xlim=(0, 0.5), ylim=(0, 1.02), xlabel="Bit-error probability p",
           ylabel="Rate (bits per channel use)",
           title="Distance guarantee and random-channel capacity")
    ax.grid(alpha=0.18)
    ax.legend(loc="upper right", fontsize=9, framealpha=1)
    fig.savefig(Path.cwd() / "paper-30-coding-rates.png", dpi=150, facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
