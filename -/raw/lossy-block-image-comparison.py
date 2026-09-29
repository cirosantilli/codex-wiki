"""Rounded block means lose detail; save the PNG to the current directory.

Uses the existing NumPy/Matplotlib dependencies; tested with Python 3.14.4.
This is a teaching format, not a model of PNG or JPEG compression.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def source_image():
    r, c = np.indices((16, 16))
    baseline = 40 + 10 * (r // 2) + 12 * (c // 2)
    return baseline + 20 * (-1) ** (r + c) + ((r % 2 == 0) & (c % 2 == 0))


def encode(image):
    means = image.reshape(8, 2, 8, 2).mean(axis=(1, 3))
    stored = np.floor(means + 0.5).astype(np.uint8)
    header = f"{16:08b}{16:08b}1"
    bits = header + "".join(f"{int(value):08b}" for value in stored.ravel())
    return bits, stored, means


def decode(bits):
    if len(bits) != 529 or any(bit not in "01" for bit in bits):
        raise ValueError("Expected exactly 529 binary bits before padding")
    if (int(bits[:8], 2), int(bits[8:16], 2), bits[16]) != (16, 16, "1"):
        raise ValueError("This decoder accepts only the 16 by 16 block-mean profile")
    values = np.array([int(bits[i:i + 8], 2) for i in range(17, len(bits), 8)])
    return values.reshape(8, 8).repeat(2, axis=0).repeat(2, axis=1)


def main():
    image = source_image()
    bits, stored, means = encode(image)
    reconstructed = decode(bits)
    i, j = np.indices((8, 8))
    np.testing.assert_array_equal(stored, 40 + 10 * i + 12 * j)
    np.testing.assert_array_equal(means, stored.astype(float) + 0.25)
    np.testing.assert_array_equal(image[:2, :2], [[61, 20], [20, 60]])
    assert image.min() == 20 and image.max() == 215
    mse = float(np.mean((image - reconstructed) ** 2))
    unrounded = means.repeat(2, axis=0).repeat(2, axis=1)
    mse_unrounded = float(np.mean((image - unrounded) ** 2))
    assert mse == 410.25 and mse_unrounded == 410.1875
    assert encode(reconstructed)[0] == bits  # Two distinct sources share one encoding.
    assert not np.array_equal(image, reconstructed)
    assert len(bits) - 17 == 512 and len(bits) == 529
    assert len(bits) + (-len(bits) % 8) == 536

    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 3, figsize=(12, 6.2), dpi=110)
    fig.subplots_adjust(left=0.035, right=0.965, bottom=0.32, top=0.81, wspace=0.18)
    fig.suptitle("Lossy: block means keep broad shades and discard fine detail",
                 fontsize=16, y=0.97)
    fig.text(0.5, 0.90, "All panels use the same shade scale: 0 = black, 255 = white",
             ha="center", color="#344b60")
    titles = ("Original: 16 × 16 pixels\n2048 payload bits",
              "Stored: 8 × 8 rounded means\n512 payload bits",
              "Reconstruction: 16 × 16 pixels\nCopy each value into a 2 × 2 block")
    for ax, array, title in zip(axes, (image, stored, reconstructed), titles):
        ax.imshow(array, cmap="gray", vmin=0, vmax=255, interpolation="nearest")
        n = array.shape[0]
        step = 1 if n == 8 else 2
        ax.set_xticks(np.arange(-0.5, n, step), minor=True)
        ax.set_yticks(np.arange(-0.5, n, step), minor=True)
        ax.grid(which="minor", color="#628095", linewidth=0.65, alpha=0.8)
        ax.tick_params(which="both", bottom=False, left=False,
                       labelbottom=False, labelleft=False)
        ax.set_title(title, fontsize=12, pad=10)
    for r in range(8):
        for c in range(8):
            value = int(stored[r, c])
            axes[1].text(c, r, str(value), ha="center", va="center", fontsize=8,
                         color="white" if value < 125 else "black")
    texts = ("First block\n61   20\n20   60",
             "Mean = 161 / 4 = 40.25\nRound half upward → 40\nStore 00101000 (8 bits)",
             "First reconstructed block\n40   40\n40   40")
    for ax, label in zip(axes, texts):
        ax.text(0.5, -0.07, label, transform=ax.transAxes, ha="center", va="top",
                fontsize=11, linespacing=1.45)
    fig.text(0.5, 0.125, "MSE = (21² + 20² + 20² + 20²) / 4 = 410.25 shade units²",
             ha="center", fontsize=13, weight="bold")
    fig.text(0.5, 0.065, "75% smaller payload   •   Common header: 17 bits   •   Complete sizes: 2065 → 529 bits",
             ha="center", fontsize=11)
    fig.savefig(Path.cwd() / "lossy-block-image-comparison.png", facecolor="white",
                transparent=False)
    plt.close(fig)
    print({"original_payload_bits": image.size * 8, "stored_payload_bits": stored.size * 8,
           "file_bits": len(bits), "padded_file_bits": 536, "mse": mse,
           "mse_unrounded": mse_unrounded, "identical_encoding_of_distinct_sources": True})


if __name__ == "__main__":
    main()
