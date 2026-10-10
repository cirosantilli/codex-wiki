"""Draw an original first-match trace; tested with Python 3.14 and matplotlib 3.10.7."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def trace(entries, target):
    checks = []
    for index, entry in enumerate(entries):
        matched = entry == target
        checks.append((index, matched))
        if matched:
            return index, checks
    return None, checks


def main():
    entries = [7, 4, 7, 2, 9]
    fig, ax = plt.subplots(figsize=(10, 5.4), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    ax.set_xlim(-2.6, 7.2)
    ax.set_ylim(-1.5, 4.8)
    ax.axis("off")
    ax.set_title("Linear search: equality checks in input order", fontsize=16, pad=17)
    for index in range(len(entries)):
        ax.text(index + 0.44, 4.2, f"index {index}", ha="center", fontsize=11)
    for y, target in zip((3.1, 1.6, 0.1), (7, 2, 6)):
        found, checks = trace(entries, target)
        by_index = dict(checks)
        ax.text(-2.35, y + 0.45, f"target {target}", va="center", fontsize=13)
        for index, entry in enumerate(entries):
            tested = index in by_index
            matched = by_index.get(index, False)
            color = "#bde4cf" if matched else "#f8dcc0" if tested else "#eceff2"
            ax.add_patch(Rectangle((index, y), 0.88, 0.9, facecolor=color, edgecolor="#465361"))
            ax.text(index + 0.44, y + 0.57, str(entry), ha="center", fontsize=17)
            label = f"#{index + 1}: {'yes' if matched else 'no'}" if tested else "not checked"
            ax.text(index + 0.44, y + 0.19, label, ha="center", fontsize=9)
        result = f"index {found}" if found is not None else "absent (None)"
        ax.text(5.25, y + 0.53, result, fontsize=13)
        ax.text(5.25, y + 0.12, f"{len(checks)} equality check{'s' if len(checks) != 1 else ''}", fontsize=11)
    ax.text(-2.35, -1.1, "Empty input: absent (None), zero equality checks", fontsize=12)
    fig.tight_layout()
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
