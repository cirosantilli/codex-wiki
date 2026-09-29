"""Draw an original DEFLATE overlapping-copy trace.

Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; writes deflate-overlapping-copy-trace.png to the CWD.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def copy_trace(seed=b"ABC", length=9, distance=3):
    """Model sequential decoded-byte copying, not a complete DEFLATE codec."""
    if not (3 <= length <= 258 and 1 <= distance <= min(32768, len(seed))):
        raise ValueError("Reference must have a permitted length and available history")
    output = bytearray(seed)
    rows = []
    for step in range(length):
        destination = len(output)
        source = destination - distance
        value = output[source]
        output.append(value)
        rows.append((step, source, destination, value, bytes(output)))
    return rows


def main():
    trace = copy_trace()
    assert trace[-1][-1] == b"ABCABCABCABC"
    fig, ax = plt.subplots(figsize=(11.5, 7.2), dpi=100, facecolor="white")
    fig.subplots_adjust(left=0.03, right=0.99, top=0.98, bottom=0.025)
    ax.set(xlim=(-2.2, 14.5), ylim=(-1.25, 11.65))
    ax.axis("off")
    ax.text(-2.1, 11.15, "Overlapping copy: length 9, distance 3", fontsize=19,
            weight="bold", color="#18334b")
    ax.text(-2.1, 10.58, "Seed ABC; each step reads from the growing output, then appends one byte.",
            fontsize=12, color="#34495e")
    for index in range(12):
        ax.text(index + 0.45, 9.95, str(index), ha="center", va="center", fontsize=11)
    ax.text(-2.1, 9.95, "Output index", fontsize=11, va="center")

    rows = [(None, None, None, None, b"ABC")] + trace
    for row, (step, source, destination, value, output) in enumerate(rows):
        y = 9.05 - row * 0.86
        label = "Seed" if step is None else f"Step {step}"
        ax.text(-2.1, y + 0.28, label, fontsize=12, va="center")
        for index in range(12):
            face = "#f6f7f9" if index >= len(output) else "#edf0f2"
            edge, width = "#ccd4db", 0.7
            if index == source:
                face = "#d6eafb" if source < 3 else "#e4dafa"
                edge, width = "#386da8" if source < 3 else "#7750ab", 1.7
            if index == destination:
                face, edge, width = "#ffdfa7", "#a96709", 1.7
            ax.add_patch(Rectangle((index, y), 0.9, 0.56, facecolor=face,
                                   edgecolor=edge, linewidth=width))
            if index < len(output):
                ax.text(index + 0.45, y + 0.28, chr(output[index]), ha="center",
                        va="center", fontsize=13, family="monospace")
        if step is not None:
            color = "#386da8" if source < 3 else "#7750ab"
            ax.annotate("", xy=(destination + 0.45, y + 0.59),
                        xytext=(source + 0.45, y + 0.59),
                        arrowprops={"arrowstyle": "->", "color": color,
                                    "linewidth": 1.4, "connectionstyle": "arc3,rad=-0.13"})
            ax.text(12.2, y + 0.28, f"{source} → {destination}: {chr(value)}",
                    fontsize=11, va="center", color=color)

    ax.text(-2.1, -0.35, "Blue: read seed bytes     Purple: read bytes produced by this copy     Orange: append",
            fontsize=11, color="#34495e")
    ax.text(-2.1, -0.94, "Result: ABCABCABCABC   •   Source always precedes destination by 3 bytes.",
            fontsize=12, weight="bold", color="#18334b")
    fig.savefig(Path.cwd() / "deflate-overlapping-copy-trace.png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
