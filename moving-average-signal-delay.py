"""Exact steady sinusoidal inputs demonstrate cancellation and causal delay."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    m = 5
    n = np.arange(0, 101)
    f_slow, f_fast = .025, .2
    slow = lambda indices: np.sin(2 * np.pi * f_slow * indices)
    fast = lambda indices: .45 * np.sin(2 * np.pi * f_fast * indices)
    signal = lambda indices: slow(indices) + fast(indices)
    output = np.mean([signal(n - j) for j in range(m)], axis=0)
    h = np.ones(m) / m
    full_input = signal(np.arange(-(m - 1), n[-1] + 1))
    assert np.allclose(output, np.convolve(full_input, h, mode="valid"))
    gain = np.sin(np.pi * m * f_slow) / (m * np.sin(np.pi * f_slow))
    delay = (m - 1) / 2
    predicted = gain * slow(n - delay)
    assert np.allclose(output, predicted, atol=2e-14)
    assert np.allclose(np.mean([fast(n - j) for j in range(m)], axis=0), 0, atol=2e-14)
    fig, axes = plt.subplots(3, 1, figsize=(11.2, 7), layout="constrained", sharex=True)
    axes[0].plot(n, slow(n), color="#167e8d", lw=2, label="Slow component: f = 0.025")
    axes[0].plot(n, fast(n), color="#c26030", lw=1.5, label="Fast component: f = 0.2")
    axes[0].set_title("Two known input components; frequencies are cycles per sample")
    axes[1].plot(n, signal(n), color="#8996a1", lw=1.3, label="Input: sum of the components")
    axes[1].plot(n, output, color="#167e8d", lw=2.4, label="Five-sample trailing mean")
    axes[1].set_title("The fast component cancels; the slow component survives with delay")
    axes[2].plot(n, slow(n), "--", color="#697a89", lw=1.7, label="Original slow component")
    axes[2].plot(n, predicted, color="#167e8d", lw=2.4,
                 label=f"Filtered: gain {gain:.4f}, delay {delay:g} samples")
    axes[2].annotate("", xy=(12, gain), xytext=(10, gain),
                     arrowprops={"arrowstyle": "<->", "color": "#c26030", "lw": 1.8})
    axes[2].text(14, .8, "Peak shifts by 2 samples", color="#a74d25", fontsize=10)
    for ax in axes:
        ax.set(ylabel="Amplitude", ylim=(-1.6, 1.6))
        ax.grid(alpha=.18)
        ax.spines[["top", "right"]].set_visible(False)
        ax.legend(loc="lower left", fontsize=9, ncol=2)
    axes[-1].set(xlabel="Sample index n", xlim=(0, 100))
    fig.suptitle("A moving average changes timing as well as amplitude", fontsize=17)
    fig.get_layout_engine().set(rect=(0, .04, 1, .96))
    fig.text(.5, .015, "Input sinusoids are defined for all integer indices; early outputs use their specified past.",
             ha="center", fontsize=10)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=100, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
