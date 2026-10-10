"""Render finite convolution contributions and circular folding to cwd."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def main():
    a = np.array([1, 2, 1])
    b = np.array([1, 1])
    c = np.convolve(a, b)
    assert c.tolist() == [1, 3, 3, 1]
    wrapped = np.array([sum(c[j::3]) for j in range(3)])
    assert wrapped.tolist() == [2, 3, 3]
    fft4 = np.fft.ifft(np.fft.fft(a, 4) * np.fft.fft(b, 4))
    fft3 = np.fft.ifft(np.fft.fft(a, 3) * np.fft.fft(b, 3))
    assert np.allclose(fft4, c) and np.allclose(fft3, wrapped)
    assert c.sum() == a.sum() * b.sum() == 8
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    fig, axes = plt.subplots(2, 2, figsize=(10.5, 6.4), dpi=120, facecolor="white")
    ax = axes[0, 0]
    for values, offset, color, label in [(a, -0.08, "#2477aa", "a = (1, 2, 1)"),
                                          (b, 0.08, "#d77c21", "b = (1, 1)")]:
        indices = np.arange(len(values))
        ax.vlines(indices + offset, 0, values, color=color, lw=2)
        ax.scatter(indices + offset, values, s=75, color=color, zorder=3, label=label)
    ax.set_title("Two finite inputs; unspecified entries are zero")
    ax.set_xlabel("Input index")
    ax.set_ylabel("Value")
    ax.set_xticks(range(4))
    ax.set_xlim(-0.5, 3.4)
    ax.set_ylim(-0.05, 2.75)
    ax.set_yticks([0, 1, 2])
    ax.legend(loc="upper right", frameon=False, fontsize=10)

    ax = axes[0, 1]
    shades = ["#d4e7f2", "#cce5d9", "#ffe2b3", "#e7d7ef"]
    for m in range(3):
        for k in range(2):
            ax.add_patch(Rectangle((k - 0.5, m - 0.5), 1, 1,
                                   facecolor=shades[m + k], edgecolor="white", linewidth=2))
            ax.text(k, m, f"{a[m] * b[k]} → n = {m + k}", ha="center", va="center")
    ax.set_title("Every pair contributes to index n = m + k")
    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1, 2])
    ax.set_xlim(-0.5, 1.5)
    ax.set_ylim(2.5, -0.5)
    ax.set_xlabel("Index k in b")
    ax.set_ylabel("Index m in a")
    ax.tick_params(length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)

    ax = axes[1, 0]
    first = np.pad(a, (0, 1))
    shifted = np.pad(a, (1, 0))
    ax.bar(np.arange(4), first, color="#2477aa", width=0.6, label=r"$a_n$")
    ax.bar(np.arange(4), shifted, bottom=first, color="#d77c21", width=0.6, label=r"$a_{n-1}$")
    for n, value in enumerate(c):
        ax.text(n, value + 0.12, str(value), ha="center", fontweight="bold")
    ax.set_title("Add an original copy and a shifted copy")
    ax.set_xlabel("Output index n")
    ax.set_ylabel("Value; divide by 8 for probability")
    ax.set_xticks(range(4))
    ax.set_yticks([0, 1, 2, 3])
    ax.set_ylim(0, 4.2)
    ax.legend(loc="upper center", ncol=2, frameon=False)

    ax = axes[1, 1]
    ax.bar(np.arange(3), c[:3], width=0.6, color="#7c98ad")
    ax.bar(0, c[3], bottom=c[0], width=0.6, color="#925baf", label="Index 3 folds into index 0")
    for n, value in enumerate(wrapped):
        ax.text(n, value + 0.12, str(value), ha="center", fontweight="bold")
    ax.set_title("Length-3 circular convolution wraps the last term")
    ax.set_xlabel("Index modulo 3")
    ax.set_ylabel("Folded value")
    ax.set_xticks(range(3))
    ax.set_yticks([0, 1, 2, 3])
    ax.set_ylim(0, 4.2)
    ax.legend(loc="upper left", frameon=False, fontsize=9)
    for ax in [axes[0, 0], axes[1, 0], axes[1, 1]]:
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(axis="y", color="#e5e9eb", zorder=0)
        ax.set_axisbelow(True)
    fig.subplots_adjust(left=0.08, right=0.97, top=0.93, bottom=0.09, wspace=0.25, hspace=0.53)
    output = Path.cwd() / Path(__file__).with_suffix(".png").name
    fig.savefig(output, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
