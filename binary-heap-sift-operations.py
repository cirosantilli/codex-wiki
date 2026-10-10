"""Compute and draw heap repairs; Python 3.14 / matplotlib 3.10.7.

Run from _media to write binary-heap-sift-operations.png there.
"""

from itertools import product
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle


INITIAL = [2, 5, 3, 9, 7, 8, 4]
INK = "#173244"
UP = "#a65000"
DOWN = "#007b78"


def check_heap(values):
    """Dense indices define complete shape; check parent/child identities."""
    for i, value in enumerate(values):
        if i:
            parent = (i - 1) // 2
            assert i in (2 * parent + 1, 2 * parent + 2)
            assert values[parent] <= value
        left, right = 2 * i + 1, 2 * i + 2
        assert right >= len(values) or left < len(values)


def sift_up(values, i):
    path = [i]
    states = [values.copy()]
    while i:
        parent = (i - 1) // 2
        if values[parent] <= values[i]:
            break
        values[i], values[parent] = values[parent], values[i]
        i = parent
        path.append(i)
        states.append(values.copy())
    return path, states


def sift_down(values, i):
    path = [i]
    states = [values.copy()]
    while 2 * i + 1 < len(values):
        child = 2 * i + 1
        if child + 1 < len(values) and values[child + 1] < values[child]:
            child += 1
        if values[i] <= values[child]:
            break
        values[i], values[child] = values[child], values[i]
        i = child
        path.append(i)
        states.append(values.copy())
    return path, states


def insert(values, key):
    values.append(key)
    return sift_up(values, len(values) - 1)


def extract_min(values):
    if not values:
        raise ValueError("empty heap")
    result = values[0]
    last = values.pop()
    if not values:
        return result, [], []
    values[0] = last
    path, states = sift_down(values, 0)
    return result, path, states


def build_heap(keys):
    values = list(keys)
    for i in range(len(values) // 2 - 1, -1, -1):
        sift_down(values, i)
    check_heap(values)
    return values


def drain(values):
    result = []
    while values:
        result.append(extract_min(values)[0])
        check_heap(values)
    return result


def verify():
    check_heap(INITIAL)
    values = INITIAL.copy()
    up_path, up_states = insert(values, 1)
    assert up_path == [7, 3, 1, 0]
    assert up_states == [[2, 5, 3, 9, 7, 8, 4, 1],
                         [2, 5, 3, 1, 7, 8, 4, 9],
                         [2, 1, 3, 5, 7, 8, 4, 9],
                         [1, 2, 3, 5, 7, 8, 4, 9]]
    check_heap(values)
    result, down_path, down_states = extract_min(values)
    assert result == 1 and down_path == [0, 1, 3]
    assert down_states == [[9, 2, 3, 5, 7, 8, 4],
                           [2, 9, 3, 5, 7, 8, 4], INITIAL]
    assert 2 * down_path[-1] + 1 >= len(values)
    assert values == INITIAL
    check_heap(values)
    extracted = drain(values)
    assert extracted == [2, 3, 4, 5, 7, 8, 9]
    cases = 0
    # All short arrays over three keys include duplicates and partial last levels.
    for length in range(8):
        for keys in product((-1, 0, 1), repeat=length):
            assert drain(build_heap(keys)) == sorted(keys)
            heap = []
            for key in keys:
                insert(heap, key)
                check_heap(heap)
            assert drain(heap) == sorted(keys)
            cases += 1
    try:
        extract_min([])
    except ValueError:
        pass
    else:
        raise AssertionError("empty extraction must fail")
    print(f"Insert path {up_path}; extract path {down_path}; returned {result}; "
          f"original restored; sorted extractions {extracted}; "
          f"{cases} exhaustive arrays checked by build and insertion")
    return up_states, down_states, up_path, down_path


def position(i):
    depth = (i + 1).bit_length() - 1
    offset = i - (2 ** depth - 1)
    return (offset + 0.5) * 8 / (2 ** depth), 3.9 - depth * 0.88


def panel(ax, values, path, title, note, color, moving_key, final=False):
    ax.set(xlim=(-0.25, 8.65), ylim=(-0.45, 6.05), aspect="equal")
    ax.axis("off")
    ax.text(0, 5.68, title, fontsize=14, weight="bold", color=INK)
    ax.text(0, 5.26, note, fontsize=11, color=color)
    ax.text(0, 4.91, "index", fontsize=9, color="#475569")
    for i, value in enumerate(values):
        x = 0.87 + i * 0.94
        ax.add_patch(Rectangle((x - 0.4, 4.28), 0.8, 0.48,
                               facecolor="#fff0db" if value == moving_key else "#f3f7fa",
                               edgecolor=color if i in path else "#aab9c5"))
        ax.text(x, 4.51, str(value), ha="center", va="center", fontsize=12)
        ax.text(x, 4.91, str(i), ha="center", fontsize=9, color="#475569")
    for i in range(1, len(values)):
        x0, y0 = position((i - 1) // 2)
        x1, y1 = position(i)
        ax.plot([x0, x1], [y0, y1], color="#b4c0ca", linewidth=1.5, zorder=1)
    for start, end in zip(path, path[1:]):
        ax.annotate("", xy=position(end), xytext=position(start),
                    arrowprops={"arrowstyle": "->", "color": color,
                                "lw": 2.6, "shrinkA": 18, "shrinkB": 18},
                    zorder=2)
    for i, value in enumerate(values):
        x, y = position(i)
        ax.add_patch(Circle((x, y), 0.24, facecolor="#fff0db" if value == moving_key else "white",
                            edgecolor=color if i in path else "#8497a7",
                            linewidth=2 if i in path else 1.3, zorder=3))
        ax.text(x, y, str(value), ha="center", va="center", fontsize=13, zorder=4)
        ax.text(x, y - 0.38, f"i={i}", ha="center", fontsize=9, color="#475569")
    path_label = " → ".join(str(i) for i in path)
    ax.text(0, 0.55, f"Key {moving_key} follows indices {path_label}", fontsize=11, color=color)
    if len(values) == 7:
        ax.text(0, 0.06, "Length 7: children of index 3 would be 7, 8 — absent.",
                fontsize=10, color=INK)
    else:
        ax.text(0, 0.06, "Heap order restored." if final else "Append at the next free index: 7.",
                fontsize=10, color=INK)


def main():
    up_states, down_states, up_path, down_path = verify()
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig, axes = plt.subplots(2, 2, figsize=(12, 8.8), facecolor="white")
    panel(axes[0, 0], up_states[0], up_path, "1. Insert: append key 1",
          "Sift up: exchange with keys 9, 5, then 2", UP, 1)
    panel(axes[0, 1], up_states[-1], up_path, "2. Insert: repaired heap",
          "Key 1 is now at the root", UP, 1, final=True)
    panel(axes[1, 0], down_states[0], down_path, "3. Extract: save key 1; move last key 9",
          "Sift down: choose key 2, then key 5", DOWN, 9)
    panel(axes[1, 1], down_states[-1], down_path, "4. Extract: repaired heap",
          "Return 1; the original array is restored", DOWN, 9, final=True)
    fig.suptitle("Heap repair follows one chain", fontsize=18, weight="bold", y=0.98, color=INK)
    fig.subplots_adjust(left=0.025, right=0.985, top=0.93, bottom=0.025,
                        wspace=0.09, hspace=0.08)
    fig.savefig(Path.cwd() / "binary-heap-sift-operations.png", dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
