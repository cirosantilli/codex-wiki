"""Draw sequential queue states and compare membership lifetimes at overflow."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def trace():
    h, n, slots = 0, 0, [None] * 5
    rows = [(0, "start", h, n, 0, "∅", "—")]
    calls = [("+", "A"), ("+", "B"), ("−", None), ("+", "C"),
             ("+", "D"), ("−", None), ("+", "E"), ("+", "F"), ("+", "G")]
    for t, (op, item) in enumerate(calls, 1):
        result = "—"
        if op == "+":
            slots[(h + n) % 5] = item
            n += 1
        else:
            result = slots[h]
            h = (h + 1) % 5
            n -= 1
        q = " ".join(slots[(h + i) % 5] for i in range(n))
        rows.append((t, f"enqueue {item}" if op == "+" else "dequeue", h, n,
                     (h + n) % 5, q or "∅", result))
    return rows


def main():
    fig = plt.figure(figsize=(9, 8.5), dpi=120, facecolor="white")
    fig.text(0.5, 0.962, "A full slot can end an item's membership", ha="center",
             fontsize=18, weight="bold")
    fig.text(0.5, 0.928, "Capacity 5 • states after completed calls • no elapsed-time scale",
             ha="center", fontsize=11)
    ax = fig.add_axes((0.045, 0.50, 0.91, 0.40))
    ax.axis("off")
    table = ax.table(cellText=trace(), colLabels=["Step", "Call", "h", "n", "w", "Logical queue", "Returned"],
                     cellLoc="center", colWidths=[0.07, 0.23, 0.06, 0.06, 0.06, 0.30, 0.12],
                     bbox=(0, 0, 1, 1))
    table.auto_set_font_size(False)
    table.set_fontsize(10.5)
    for (r, c), cell in table.get_celld().items():
        cell.set_edgecolor("#c5ced3")
        cell.set_linewidth(0.7)
        if r == 0:
            cell.set_facecolor("#e5edf2")
            cell.get_text().set_weight("bold")
        elif r in (9, 10):
            cell.set_facecolor("#e9f3f8" if r == 9 else "#fff0d8")
    fig.text(0.5, 0.475, "Step 9 is full: h = w = 2, n = 5. Now propose H.",
             ha="center", fontsize=11, weight="bold")
    for left, title, lines, color in [
        (0.06, "Reject full: try_enqueue(H)", ["10: full; C D E F G", "11: dequeue → C; D E F G"], "#e5eef5"),
        (0.53, "Overwrite: append_latest(H)", ["10: discard C; D E F G H", "11: dequeue → D; E F G H"], "#fff0d8"),
    ]:
        box = fig.add_axes((left, 0.353, 0.41, 0.096), facecolor=color)
        box.set(xticks=[], yticks=[])
        for spine in box.spines.values():
            spine.set_color("#b1bdc5")
        box.text(0.5, 0.80, title, ha="center", fontsize=10.5, weight="bold")
        for y, line in zip([0.48, 0.17], lines):
            box.text(0.5, y, line, ha="center", fontsize=10)
    life = fig.add_axes((0.26, 0.07, 0.68, 0.22))
    life.set(xlim=(0, 12), ylim=(-0.65, 3.65), xticks=range(13),
             yticks=[3, 2, 1, 0],
             yticklabels=["C • reject", "C • overwrite", "H • reject", "H • overwrite"])
    life.set_xlabel("Completed operation number", fontsize=10)
    life.set_title("Membership: present after entry, absent after removal/discard", fontsize=11, pad=10)
    life.grid(axis="x", color="#e1e6e8", lw=0.7)
    life.set_axisbelow(True)
    for y, start, end, color in [(3, 4, 11, "#76afce"), (2, 4, 10, "#d7a34c"),
                                (0, 10, 12, "#d7a34c")]:
        life.add_patch(Rectangle((start, y - 0.18), end - start, 0.36,
                                 facecolor=color, edgecolor="none"))
        life.plot(start, y, "o", ms=5, color="#35434c")
        if end < 12:
            life.plot(end, y, "o", ms=5, mfc="white", mec="#35434c")
        else:
            life.annotate("", (12, y), (11.5, y),
                          arrowprops={"arrowstyle": "->", "color": "#35434c"})
    life.text(6.3, 1, "never accepted", ha="center", va="center", fontsize=10, color="#6b747a")
    for spine in ["top", "right", "left"]:
        life.spines[spine].set_visible(False)
    life.tick_params(axis="y", length=0)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
