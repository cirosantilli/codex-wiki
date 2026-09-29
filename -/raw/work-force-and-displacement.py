"""Draw constant-force work; write the PNG basename to the working directory.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Prescribed straight displacements illustrate three independent force directions.
"""

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "savefig.facecolor": "white"})
    fig, axes = plt.subplots(3, 2, figsize=(10, 8), facecolor="white")
    fig.subplots_adjust(left=0.08, right=0.96, top=0.85, bottom=0.10,
                        wspace=0.32, hspace=0.72)
    fig.suptitle("Work counts the force along the displacement", fontsize=18, y=0.97)
    fig.text(0.5, 0.915, "Three independent cases: force magnitude 3 N; displacement 4 m to the right",
             ha="center", fontsize=12)
    x = np.linspace(0, 4, 101)
    cases = [("Parallel", 3, (2.7, 0), "#2171a7"),
             ("Perpendicular", 0, (1.5, 0.85), "#447747"),
             ("Opposing", -3, (0.3, 0), "#b34d31")]
    for row, (name, component, tip, color) in enumerate(cases):
        direction, graph = axes[row]
        direction.set(xlim=(-0.05, 4.2), ylim=(-0.85, 1.35))
        direction.axis("off")
        direction.set_title(name, loc="left", fontsize=14, color=color, pad=4)
        direction.scatter([1.5], [0], s=60, color="#333333", zorder=4)
        direction.annotate("", xy=tip, xytext=(1.5, 0),
                           arrowprops={"arrowstyle": "-|>", "lw": 3, "color": color})
        label_x, label_y = (2.1, 0.2) if row == 0 else ((1.65, 0.65) if row == 1 else (0.65, 0.2))
        direction.text(label_x, label_y, "Force: 3 N", color=color, fontsize=12)
        direction.annotate("", xy=(4, -0.45), xytext=(0, -0.45),
                           arrowprops={"arrowstyle": "-|>", "lw": 2, "color": "#555555"})
        direction.text(2, -0.76, "Displacement: 4 m", ha="center", color="#333333")
        force = np.full_like(x, component)
        graph.axhline(0, color="#555555", lw=0.9)
        graph.plot(x, force, color=color, lw=2.5)
        graph.fill_between(x, 0, force, color=color, alpha=0.18)
        graph.set(xlim=(0, 4.15), ylim=(-4.1, 4.1), xticks=[0, 1, 2, 3, 4],
                  yticks=[-3, 0, 3], xlabel="Along-path distance x (m)",
                  ylabel="Along-path force (N)")
        graph.grid(alpha=0.17)
        graph.spines[["top", "right"]].set_visible(False)
        graph.text(2, -2 if component >= 0 else 2,
                   f"Work = {component} N × 4 m = {component * 4} J",
                   ha="center", va="center", color=color, fontsize=12,
                   bbox={"facecolor": "white", "edgecolor": "none", "pad": 3})
    fig.text(0.5, 0.025, "Signed area gives work. Arrows show directions; force and displacement have different units.",
             ha="center", fontsize=11)
    fig.savefig("work-force-and-displacement.png", dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
