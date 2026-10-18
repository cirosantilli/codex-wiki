"""Original H/T constructions and three-wire Grover circuit.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7, using the
root dependencies. Run from the desired output directory: the only file
written is Path.cwd() / Path(__file__).with_suffix('.png').name.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Rectangle


INK = "#233746"
BLUE = "#126782"
PALE_BLUE = "#edf5f8"
ORANGE = "#b55d15"
PALE_ORANGE = "#fff3e7"
GREEN = "#287d53"


def label(ax, x, y, text, size=13, **kwargs):
    ax.text(x, y, text, fontsize=size, ha="center", va="center",
            color=kwargs.pop("color", INK), **kwargs)


def gate(ax, x, low, high, text, width=0.7, color=BLUE, fill=PALE_BLUE, size=15):
    ax.add_patch(Rectangle((x - width / 2, low), width, high - low,
                           facecolor=fill, edgecolor=color, linewidth=1.6, zorder=3))
    label(ax, x, (low + high) / 2, text, size, color=color, zorder=4)


def measurement(ax, x, y):
    gate(ax, x, y - 0.30, y + 0.30, "", fill="white")
    ax.add_patch(Arc((x, y - 0.08), 0.44, 0.35, theta1=0, theta2=180,
                     color=INK, lw=1.2, zorder=4))
    ax.annotate("", (x + 0.15, y + 0.17), (x - 0.02, y - 0.09),
                arrowprops={"arrowstyle": "->", "color": INK, "lw": 1.1}, zorder=5)


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white",
                         "axes.facecolor": "white", "mathtext.fontset": "dejavusans"})
    fig = plt.figure(figsize=(12.5, 7.5))
    layout = fig.add_gridspec(2, 1, height_ratios=(1, 2.5), hspace=0.28)
    constructions = layout[0].subgridspec(1, 3, width_ratios=(1.0, 1.7, 2.6), wspace=0.23)
    sequences = [("Z", [r"$T^4$"]),
                 ("X", [r"$H$", r"$T^4$", r"$H$"]),
                 ("Y (exact)", [r"$T^6$", r"$H$", r"$T^4$", r"$H$", r"$T^2$"])]
    for index, (title, gates) in enumerate(sequences):
        ax = fig.add_subplot(constructions[0, index])
        count = len(gates)
        ax.set(xlim=(0, count + 1), ylim=(-0.7, 1.6))
        ax.set_axis_off()
        ax.plot([0.1, count + 0.9], [0, 0], color=INK, lw=1.4, zorder=1)
        ax.annotate("", (count + 0.95, 0), (count + 0.70, 0),
                    arrowprops={"arrowstyle": "->", "color": INK, "lw": 1.4})
        for position, text in enumerate(gates, 1):
            gate(ax, position, -0.38, 0.38, text, width=0.72, size=16)
        label(ax, (count + 1) / 2, 1.05, title, 16, weight="bold")

    ax = fig.add_subplot(layout[1])
    ax.set(xlim=(0, 15.5), ylim=(-0.55, 6.1))
    ax.set_axis_off()
    label(ax, 7.75, 5.9, "One Grover iteration: two search qubits and one oracle ancilla", 17, weight="bold")
    wires = [(4.15, r"Search $q_0$", r"$|0\rangle$"),
             (3.05, r"Search $q_1$", r"$|0\rangle$"),
             (1.5, "Ancilla", r"$|1\rangle$")]
    for y, name, state in wires:
        ax.text(0.03, y, name, ha="left", va="center", color=INK, fontsize=11)
        label(ax, 1.55, y, state, 15)
        end = 11.15 if y > 2 else 14.3
        ax.plot([1.95, end], [y, y], color=INK, lw=1.4, zorder=1)
        gate(ax, 2.55, y - 0.32, y + 0.32, r"$H$", width=0.68)
    # U_f acts on all three wires; D has support on the search register only.
    gate(ax, 4.65, 1.10, 4.55, r"$U_f$", width=1.45,
         color=ORANGE, fill=PALE_ORANGE, size=22)
    label(ax, 4.65, 5.02, "Phase-kickback oracle", 13, color=ORANGE)
    ax.annotate("", (4.65, 4.57), (4.65, 4.82),
                arrowprops={"arrowstyle": "->", "color": ORANGE})
    label(ax, 3.42, 1.89, r"$|-\rangle$", 13)
    gate(ax, 8.25, 2.65, 4.55, r"$D=2|s\rangle\langle s|-I$", width=3.5, size=17)
    label(ax, 8.25, 4.98, "Diffusion on search qubits", 13, color=BLUE)
    label(ax, 8.25, 2.20, r"$|s\rangle=H^{\otimes 2}|00\rangle$", 12, color=BLUE)
    label(ax, 8.1, 0.88, "Ancilla untouched by diffusion", 12, color=GREEN)
    ax.annotate("", (8.25, 1.46), (8.25, 1.08),
                arrowprops={"arrowstyle": "->", "color": GREEN})
    for y, bit in ((4.15, "1"), (3.05, "0")):
        measurement(ax, 11.15, y)
        ax.plot([11.5, 12.75], [y + 0.045, y + 0.045], color=INK, lw=1.0)
        ax.plot([11.5, 12.75], [y - 0.045, y - 0.045], color=INK, lw=1.0)
        label(ax, 13.05, y, bit, 16, color=GREEN)
    label(ax, 11.5, 5.02, "Computational basis", 12)
    label(ax, 11.5, 4.69, "measurements", 12)
    label(ax, 14.65, 1.5, r"$|-\rangle$", 16, color=GREEN)
    ax.plot([13.5, 13.7, 13.7, 13.5], [4.35, 4.35, 2.85, 2.85], color=GREEN, lw=1.4)
    label(ax, 14.55, 3.65, r"$|10\rangle$", 18, color=GREEN)
    label(ax, 14.15, 4.98, r"For $f_{10}$", 13, color=GREEN)
    label(ax, 7.75, -0.04,
          r"$U_f\left(|x\rangle|-\rangle\right)=(-1)^{f(x)}|x\rangle|-\rangle$", 15)
    label(ax, 7.75, -0.46,
          r"$f_{10}(x)=1$ exactly when $x=10$; the search register reaches $|10\rangle$ before measurement.", 12)
    fig.suptitle("H and T gates; Grover search with phase kickback", fontsize=19, y=0.975)
    fig.text(0.5, 0.905,
             r"Read every circuit from left to right.   $T=\mathrm{diag}(1,e^{i\pi/4})$;   the Y construction is exact.",
             fontsize=13, ha="center", color=INK)
    fig.subplots_adjust(left=0.035, right=0.98, bottom=0.045, top=0.875)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                dpi=140, facecolor="white", transparent=False,
                metadata={"Software": "Matplotlib"})
    plt.close(fig)


if __name__ == "__main__":
    main()
