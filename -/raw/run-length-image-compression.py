"""Exact binary RLE example; save the PNG to the current working directory.

Uses the existing NumPy/Matplotlib dependencies; tested with Python 3.14.4.
"""

from itertools import groupby
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


ROWS = (
    "00000000", "00001111", "11110000", "00001111",
    "11110000", "00001111", "11110000", "00000000",
)


def encode(pixels):
    flat = np.asarray(pixels).ravel().tolist()
    runs = [(value, len(list(group))) for value, group in groupby(flat)]
    header = f"{8:08b}{8:08b}1"
    payload = str(flat[0]) + "".join(f"{length:07b}" for _, length in runs)
    return header + payload, runs


def decode(bits):
    if len(bits) < 18 or any(bit not in "01" for bit in bits):
        raise ValueError("Truncated header or nonbinary data")
    if (int(bits[:8], 2), int(bits[8:16], 2), bits[16]) != (8, 8, "1"):
        raise ValueError("This decoder accepts only the 8 by 8 RLE profile")
    value, offset, pixels = int(bits[17]), 18, []
    while len(pixels) < 64:
        if offset + 7 > len(bits):
            raise ValueError("Truncated run field")
        length = int(bits[offset:offset + 7], 2)
        if not 1 <= length <= 64 - len(pixels):
            raise ValueError("Zero run or run exceeds remaining pixels")
        pixels.extend([value] * length)
        value = 1 - value
        offset += 7
    # Unpacked bits have no padding; packed files have only final zero padding.
    tail = bits[offset:]
    if tail and (len(bits) % 8 or len(tail) > 7 or set(tail) != {"0"}):
        raise ValueError("Invalid final padding")
    return np.array(pixels).reshape(8, 8)


def draw_pixels(ax, pixels, title):
    ax.imshow(pixels, cmap="gray", vmin=0, vmax=1, interpolation="nearest")
    for r in range(8):
        for c in range(8):
            ax.text(c, r, str(pixels[r, c]), ha="center", va="center",
                    color="white" if pixels[r, c] == 0 else "black", fontsize=11)
    ax.set_xticks(np.arange(-0.5, 8, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, 8, 1), minor=True)
    ax.grid(which="minor", color="#8b9299", linewidth=0.5)
    ax.tick_params(which="both", bottom=False, left=False, labelbottom=False,
                   labelleft=False)
    ax.set_title(title, fontsize=13, pad=10)


def main():
    pixels = np.array([[int(bit) for bit in row] for row in ROWS])
    bits, runs = encode(pixels)
    reconstructed = decode(bits)
    assert runs == [(0, 12), (1, 8), (0, 8), (1, 8), (0, 8), (1, 8), (0, 12)]
    assert len(bits) == 67
    np.testing.assert_array_equal(reconstructed, pixels)
    packed = bits + "0" * (-len(bits) % 8)
    assert len(packed) == 72
    np.testing.assert_array_equal(decode(packed), pixels)
    row_runs = [len(list(groupby(row))) for row in ROWS]
    assert row_runs == [1, 2, 2, 2, 2, 2, 2, 1]

    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig = plt.figure(figsize=(11.5, 6.1), dpi=110)
    fig.suptitle("Lossless: seven runs recover all 64 pixels", fontsize=17, y=0.97)
    draw_pixels(fig.add_axes((0.055, 0.39, 0.285, 0.48)), pixels,
                "Original 8 × 8 image")
    draw_pixels(fig.add_axes((0.66, 0.39, 0.285, 0.48)), reconstructed,
                "Decoded image: exact match")
    ax = fig.add_axes((0.365, 0.39, 0.27, 0.48))
    ax.axis("off")
    ax.text(0.5, 0.98, "Read rows left → right,\nthen top → bottom", ha="center",
            va="top", fontsize=11)
    ax.text(0.5, 0.77, "value   length   7-bit field", ha="center",
            family="monospace", fontsize=10, weight="bold")
    for i, (value, length) in enumerate(runs):
        ax.text(0.5, 0.67 - i * 0.075, f"{value:>3}     {length:>3}     {length:07b}",
                ha="center", family="monospace", fontsize=11)
    ax.text(0.5, 0.055, "Initial bit = 0; lengths sum to 64", ha="center", fontsize=10)

    bar = fig.add_axes((0.055, 0.245, 0.89, 0.055))
    offset = 0
    for value, length in runs:
        bar.add_patch(Rectangle((offset, 0), length, 1,
                                facecolor="black" if value == 0 else "white",
                                edgecolor="#737e89", linewidth=1))
        bar.text(offset + length / 2, 0.5, f"{value} × {length}", va="center",
                 ha="center", color="white" if value == 0 else "black", fontsize=10)
        offset += length
    bar.set(xlim=(0, 64), ylim=(0, 1))
    bar.axis("off")
    fig.text(0.5, 0.325, "The flat scan joins runs across row boundaries", ha="center",
             color="#344b60", fontsize=11)
    fields = " ".join(f"{length:07b}" for _, length in runs)
    fig.text(0.5, 0.18, f"00001000 00001000 1 | 0 | {fields}", ha="center",
             family="monospace", fontsize=10)
    fig.text(0.5, 0.125, "17-bit header: width, height, mode  |  first value  |  run lengths",
             ha="center", fontsize=10, color="#344b60")
    fig.text(0.5, 0.065, "Payload: 50 vs 64 bits   •   With header: 67 vs 81 bits   •   Padded: 72 vs 88 bits",
             ha="center", fontsize=12, weight="bold")
    fig.savefig(Path.cwd() / "run-length-image-compression.png", facecolor="white",
                transparent=False)
    plt.close(fig)
    print({"runs": runs, "row_runs": row_runs, "payload_bits": len(bits) - 17,
           "file_bits": len(bits), "padded_bits": len(packed), "exact_recovery": True})


if __name__ == "__main__":
    main()
