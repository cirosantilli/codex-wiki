"""Synthetic quantization/sRGB illustration; no measured data.

Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Run from _media with
MPLCONFIGDIR=/tmp/codex-wiki-matplotlib; writes matching PNG basename to CWD.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def decode(s):
    s = np.asarray(s)
    return np.where(s <= .04045, s / 12.92, ((s + .055) / 1.055) ** 2.4)


def encode(light):
    light = np.asarray(light)
    return np.where(light <= .0031308, 12.92 * light, 1.055 * light ** (1 / 2.4) - .055)


def main():
    plt.rcParams.update({"font.size": 10, "axes.titlesize": 11})
    x = np.linspace(0, 1, 1024)
    q2 = np.floor(3 * x + .5) / 3
    q8 = np.floor(255 * x + .5) / 255
    assert np.unique(q2).size == 4 and np.unique(q8).size == 256
    assert np.max(abs(q2 - x)) <= 1 / 6 + 1e-14
    assert np.max(abs(q8 - x)) <= 1 / 510 + 1e-14
    fig, axes = plt.subplots(2, 2, figsize=(10, 6.7), facecolor="white", layout="constrained")
    ax = axes[0, 0]
    ax.imshow(np.vstack([q8, q2]), cmap="gray", vmin=0, vmax=1,
              origin="lower", extent=(0, 1, 0, 2), aspect="auto", interpolation="nearest")
    ax.set(yticks=[.5, 1.5], yticklabels=["8 bits: 256 codes", "2 bits: 4 codes"],
           xlabel="Input x (uniform in encoded shade)", title="A. Same spatial grid, different quantization")
    ax.tick_params(axis="y", length=0)
    ax = axes[0, 1]
    ax.plot(x, x, "--", color="#7b8088", label="Unquantized x")
    ax.plot(x, q2, color="#146caa", lw=2, label="2-bit reconstructed value")
    ax.set(xlim=(0, 1), ylim=(-.03, 1.03), xlabel="Input x", ylabel="Reconstructed value",
           title="B. Uniform step = 1/3; error ≤ 1/6")
    ax.set_yticks([0, 1/3, 2/3, 1], ["0", "⅓", "⅔", "1"])
    ax.legend(fontsize=9, loc="upper left")
    ax.grid(alpha=.2)
    ax = axes[1, 0]
    ax.plot(x, decode(x), lw=2.4, color="#bd2876", label="sRGB decoding D(s)")
    ax.plot(x, x, "--", color="#7b8088", label="Linear encoding for comparison")
    ax.scatter([.5, float(encode(.5))], [float(decode(.5)), .5], color="#146caa", zorder=3)
    ax.annotate("D(0.5) ≈ 0.214", (.5, float(decode(.5))), xytext=(.08, .37),
                arrowprops={"arrowstyle": "->", "color": "#146caa"}, fontsize=10)
    ax.annotate("E(0.5) ≈ 0.735", (float(encode(.5)), .5), xytext=(.39, .72),
                arrowprops={"arrowstyle": "->", "color": "#146caa"}, fontsize=10)
    ax.set(xlim=(0, 1), ylim=(0, 1), xlabel="Encoded neutral sRGB value s",
           ylabel="Relative luminance Y", title="C. Code spacing is not light spacing")
    ax.legend(fontsize=9, loc="upper left")
    ax.grid(alpha=.2)
    ax = axes[1, 1]
    ax.set(xlim=(0, 1), ylim=(0, 1), title="D. Equal weights on black and white")
    codes = [128, int(np.floor(255 * encode(.5) + .5))]
    assert codes == [128, 188]
    for y, q, label in zip([.62, .15], codes, ["Average encoded values", "Average linear light, then encode"]):
        ax.add_patch(Rectangle((.04, y), .28, .22, facecolor=(q/255,) * 3, edgecolor="#666"))
        ax.text(.36, y + .18, label, va="center", fontsize=10)
        ax.text(.36, y + .07, f"8-bit code {q}; Y ≈ {float(decode(q/255)):.3f}", va="center", fontsize=10)
    ax.text(.04, .02, "Swatches use rounded codes; luminance follows the stated model.", fontsize=8.7)
    ax.axis("off")
    fig.suptitle("Quantization and light encoding — calculated toy examples", fontsize=15)
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
