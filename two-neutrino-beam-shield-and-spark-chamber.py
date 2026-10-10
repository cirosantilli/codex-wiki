"""Draw a functional beam chain; run from _media to write the matching PNG."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle


plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
fig, ax = plt.subplots(figsize=(11, 6.4), dpi=120, facecolor="white")
ax.set(xlim=(0, 11), ylim=(0, 6.4))
ax.axis("off")
blue, orange, green = "#16659a", "#b35d15", "#257b53"
ax.text(5.5, 6.1, "Neutrino beam: separate production from detection", ha="center", fontsize=16, weight="bold")
ax.text(5.5, 5.73, "Functional schematic • not to scale • rare interaction illustrated", ha="center", color="#555555", fontsize=10)


def box(x, y, w, h, label, color):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05", facecolor=color, edgecolor="#555555"))
    ax.text(x + w / 2, y + h / 2, label, ha="center", va="center")


def arrow(start, end, color=blue, style="-", width=2):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=13, linewidth=width, color=color, linestyle=style))


box(.25, 4.08, 1.32, .92, "Proton\nsource", "#edf4fa")
box(2.03, 4.08, .78, .92, "Target", "#ffedda")
box(3.26, 4.08, 2.00, .92, "Meson decay\nregion", "#edf4fa")
box(5.78, 3.63, 1.25, 1.82, "", "#eeeeee")
ax.text(6.405, 5.12, "Shield", ha="center")
box(7.64, 3.63, 2.96, 1.82, "", "#f3faf5")
ax.text(9.12, 5.12, "Spark chamber", ha="center", weight="bold")
for x in [7.92, 8.31, 8.70, 9.09, 9.48, 9.87, 10.26]:
    ax.add_patch(Rectangle((x, 3.85), .09, 1.00, facecolor="#bbc3c9", edgecolor="none"))
arrow((1.61, 4.54), (1.99, 4.54))
arrow((2.85, 4.54), (3.22, 4.54), orange)
arrow((4.64, 4.54), (8.48, 4.54), blue, "--")
ax.text(7.35, 4.75, r"$\nu$", color=blue, fontsize=15)
arrow((4.64, 4.43), (6.35, 3.99), orange)
ax.text(5.10, 3.80, r"$\mu$", color=orange, fontsize=15)
ax.plot([6.24, 6.43], [3.92, 4.10], color=orange, lw=2)
ax.plot([6.24, 6.43], [4.10, 3.92], color=orange, lw=2)
ax.scatter([8.5], [4.54], color=green, s=42, zorder=5)
arrow((8.5, 4.54), (10.42, 4.05), green)
ax.text(9.68, 3.77, "New charged track", ha="center", color=green, fontsize=10)
ax.text(4.26, 3.40, r"e.g. $\pi^+\ \to\ \mu^+ + \nu_\mu$", ha="center", fontsize=13)
arrow((9.10, 3.25), (9.10, 2.90), green)

ax.text(5.5, 2.70, "Classify the outgoing pattern; the incoming neutrino is invisible", ha="center", fontsize=12)
for x0, label in [(0.60, "Track-like"), (5.96, "Shower-like")]:
    ax.text(x0 + 2.2, 2.28, label, ha="center", color=green if x0 < 1 else orange, weight="bold")
    for x in [x0 + .50, x0 + 1.12, x0 + 1.74, x0 + 2.36, x0 + 2.98, x0 + 3.60]:
        ax.add_patch(Rectangle((x, .72), .10, 1.15, color="#e1e5e8", zorder=0))
ax.plot([1.0, 4.55], [1.25, 1.48], color=green, lw=2)
ax.scatter([1.15, 1.77, 2.39, 3.01, 3.63, 4.25], [1.26, 1.30, 1.34, 1.38, 1.42, 1.46], color=green, s=20)
for xs, ys in [([6.38, 7.25, 8.15, 9.90], [1.3, 1.3, 1.66, 1.82]),
               ([7.25, 8.15, 9.90], [1.3, 1.0, .78]),
               ([8.15, 8.85, 9.90], [1.66, 1.30, 1.13]),
               ([8.15, 8.85, 9.90], [1.0, 1.35, 1.58])]:
    ax.plot(xs, ys, color=orange, lw=1.6)
ax.text(2.80, .37, r"Penetrating $\mu$: sparse sparks", ha="center", fontsize=10)
ax.text(8.16, .37, r"Energetic $e$: branching cascade", ha="center", fontsize=10)
fig.subplots_adjust(left=.02, right=.98, bottom=.02, top=.98)
fig.savefig(Path(__file__).stem + ".png", facecolor="white")
plt.close(fig)
