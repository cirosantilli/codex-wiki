"""Exact cut expectation ledger; Python 3.14, matplotlib 3.10.7.

Checks every one of the 3**5 partial assignments against independent completion
enumeration, including 405 parent/child averaging identities, before plotting.
"""

from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path

import matplotlib.pyplot as plt


VERTICES = "ABCDE"
EDGES = ("AB", "BC", "CD", "DE", "EA", "AC", "BD")


def formula(partial):
    fixed_crossing = sum(u in partial and v in partial and partial[u] != partial[v]
                         for u, v in EDGES)
    unresolved = sum(u not in partial or v not in partial for u, v in EDGES)
    return fixed_crossing + Fraction(unresolved, 2)


def enumerate_completions():
    # Score by counting edges across explicit sets, independently of formula().
    completions = []
    for bits in product((0, 1), repeat=len(VERTICES)):
        side_zero = {v for v, bit in zip(VERTICES, bits) if bit == 0}
        crossing = [edge for edge in EDGES if len(set(edge) & side_zero) == 1]
        completions.append((dict(zip(VERTICES, bits)), len(crossing)))
    return completions


def verify_and_ledger():
    completions = enumerate_completions()
    averaging_checks = 0
    for state in product((None, 0, 1), repeat=len(VERTICES)):
        partial = {v: bit for v, bit in zip(VERTICES, state) if bit is not None}
        scores = [score for labels, score in completions
                  if all(labels[v] == bit for v, bit in partial.items())]
        direct_average = Fraction(sum(scores), len(scores))
        assert formula(partial) == direct_average, (partial, direct_average)
        for v in VERTICES:
            if v not in partial:
                q0, q1 = (formula(partial | {v: bit}) for bit in (0, 1))
                assert (q0 + q1) / 2 == direct_average
                averaging_checks += 1
    distribution = Counter(score for _, score in completions)
    assert distribution == {0: 2, 2: 2, 3: 12, 4: 10, 5: 4, 6: 2}
    assert len(completions) == 32 and max(distribution) == 6
    assert sum(score for _, score in completions) == 112
    assert averaging_checks == 405

    partial, rows, path = {}, [], [formula({})]
    for v in VERTICES:
        q0, q1 = (formula(partial | {v: bit}) for bit in (0, 1))
        bit = int(q1 > q0)  # Deterministic tie rule: zero.
        prefix = "".join(str(partial[u]) for u in partial) or "Empty"
        parent = formula(partial)
        partial[v] = bit
        retained = formula(partial)
        assert retained >= parent
        rows.append((prefix, v, q0, q1, bit, retained))
        path.append(retained)
    assert tuple(partial.values()) == (0, 1, 0, 0, 1)
    assert path == [Fraction(7, 2), Fraction(7, 2), 4, 4, 4, 5]
    return rows, path


def number(value):
    return str(int(value)) if value.denominator == 1 else f"{float(value):.1f}"


def main():
    rows, path = verify_and_ledger()
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    ink, teal, pale = "#213547", "#167486", "#d9efed"
    fig = plt.figure(figsize=(10, 6.5), dpi=125, facecolor="white")
    fig.suptitle("Keep the conditional expected cut from falling", fontsize=19,
                 weight="bold", color=ink, y=0.965)
    fig.text(0.5, 0.905, "Vertex order A, B, C, D, E; ties choose 0; all values count edges",
             ha="center", color=ink)
    ax = fig.add_axes((0.06, 0.47, 0.88, 0.37))
    ax.axis("off")
    cells = [[prefix, v, number(q0), number(q1), str(bit), number(retained)]
             for prefix, v, q0, q1, bit, retained in rows]
    table = ax.table(cellText=cells,
                     colLabels=("Fixed prefix", "Next vertex", "If 0", "If 1", "Choose", "Retain"),
                     cellLoc="center", bbox=(0, 0, 1, 1),
                     colWidths=(0.21, 0.19, 0.14, 0.14, 0.16, 0.16))
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    for (r, c), cell in table.get_celld().items():
        cell.set_edgecolor("#d3dee3")
        cell.get_text().set_color(ink)
        if r == 0:
            cell.set_facecolor("#eaf0f4")
            cell.get_text().set_weight("bold")
        elif c in (4, 5) or c == rows[r - 1][4] + 2:
            cell.set_facecolor(pale)
            cell.get_text().set_color(teal)
            cell.get_text().set_weight("bold")
        else:
            cell.set_facecolor("white")
    plot = fig.add_axes((0.105, 0.14, 0.83, 0.24), facecolor="white")
    plot.plot(range(6), list(map(float, path)), "o-", lw=2.4, ms=7, color=teal)
    plot.axhline(3.5, color="#8b9298", ls="--", lw=1, zorder=0)
    for i, value in enumerate(path):
        plot.annotate(number(value), (i, float(value)), xytext=(0, 11),
                      textcoords="offset points", ha="center", color=teal, weight="bold")
    plot.set(xlim=(-0.2, 5.2), ylim=(3.2, 5.55), yticks=(3.5, 4, 5),
             xticks=range(6), xticklabels=("Start", "A = 0", "B = 1", "C = 0", "D = 0", "E = 1"))
    plot.set_ylabel("Expected edges", color=ink)
    plot.spines[["top", "right"]].set_visible(False)
    plot.spines[["left", "bottom"]].set_color("#8b9298")
    plot.tick_params(colors=ink)
    fig.text(0.5, 0.045, "Initial average 3.5  →  final actual cut 5. No random sampling is needed.",
             ha="center", color=ink, fontsize=12)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)
    print("Verified: 32 completions; 243 partial assignments; 405 averaging identities; optimum 6.")


if __name__ == "__main__":
    main()
