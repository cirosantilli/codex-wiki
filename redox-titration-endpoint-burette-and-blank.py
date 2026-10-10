"""Original endpoint/blank schematic; run from _media; output is in CWD.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Diagram geometry and colour are schematic, not measured readouts.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon, Rectangle


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "figure.facecolor": "white"})
    fig = plt.figure(figsize=(11, 7.5), dpi=120)
    ax = fig.add_axes([0.025, 0.035, 0.95, 0.86])
    ax.set(xlim=(0, 11), ylim=(0, 7))
    ax.axis("off")
    fig.suptitle("Endpoint, delivery and blank: three different accounts", fontsize=20, y=0.96)

    # A filled tip is shown: A is a possible error, not an intentional bubble.
    ax.text(1.8, 6.75, "DELIVERY", ha="center", fontsize=14, weight="bold")
    ax.add_patch(Rectangle((0.65, 3.65), 0.37, 2.65, facecolor="#e4d2ee",
                           edgecolor="#3c4f5b", lw=1.7))
    for j in range(10):
        y = 3.85 + j * 0.22
        ax.plot([0.65, 0.78 if j % 2 else 0.86], [y, y], color="#3c4f5b", lw=1)
    ax.plot([0.84, 0.84, 0.89], [3.65, 3.32, 3.12], color="#3c4f5b", lw=2)
    ax.plot([0.58, 1.10], [3.53, 3.53], color="#3c4f5b", lw=2)
    ax.plot([0.3, 0.3], [2.55, 6.4], color="#67757f", lw=2)
    ax.plot([0.3, 1.08], [5.9, 5.9], color="#67757f", lw=2)
    ax.text(1.3, 5.7, "Burette reading\nincreases downward", fontsize=11, va="center")
    ax.text(1.3, 4.7, r"$R_f-R_i=12.60$ mL" + "\n(sample titre)", fontsize=12, va="center")
    ax.annotate("Fill tip before\ninitial reading", xy=(0.86, 3.30), xytext=(1.4, 3.36),
                fontsize=11, va="center", arrowprops={"arrowstyle": "->", "color": "#3c4f5b"})
    flask = [(0.67, 2.85), (1.00, 2.85), (1.00, 2.48), (1.65, 1.60),
             (0.05, 1.60), (0.67, 2.48)]
    ax.add_patch(Polygon(flask, closed=True, facecolor="white", edgecolor="#3c4f5b", lw=1.7))
    ax.add_patch(Polygon([(0.24, 1.72), (1.45, 1.72), (1.17, 2.12), (0.52, 2.12)],
                         closed=True, facecolor="#e8d5ee", edgecolor="none"))
    ax.text(2.0, 2.15, "Swirl and inspect\nthe mixed solution", ha="center", fontsize=11)
    ax.text(1.8, 0.95, "25.00 mL Fe²⁺ aliquot\n+ excess dilute sulfuric acid", ha="center", fontsize=11)

    ax.plot([3.55, 3.55], [0.65, 6.9], color="#c4cbd0")
    ax.text(7.3, 6.75, "CONSTRUCTED VOLUME ACCOUNT", ha="center", fontsize=14, weight="bold")
    ax.text(7.3, 6.35, "At c = 0.02000 mol/L; boxes are not to scale", ha="center", fontsize=11)

    def box(x, y, w, h, text, color="#3c4f5b", fill="#f5f8fa", size=12):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.015",
                                   facecolor=fill, edgecolor=color, lw=1.4))
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=size, color=color)

    box(3.95, 5.14, 3.28, 0.88, "12.50 mL\nFe²⁺ inventory contribution", "#a14e18")
    ax.text(7.47, 5.58, "+", ha="center", va="center", fontsize=20)
    box(7.75, 5.14, 3.00, 0.88, "0.10 mL\nmatched blank contribution", "#713e91")
    ax.text(7.3, 4.82, "= 12.60 mL sample titre", ha="center", fontsize=15, weight="bold")
    ax.text(7.3, 4.43, "The 0.10 mL is not assigned wholly to colour excess.", ha="center", fontsize=11)

    box(3.95, 3.42, 6.8, 0.72,
        r"$V=V_{\rm Fe}+B_s+D_s+A+I\qquad V_b=B_b+D_b$", size=16)
    ax.text(4.05, 3.15, "B: reagent demand    D: signed endpoint offset", fontsize=11)
    ax.text(4.05, 2.83, "A: tip filling counted as delivery    I: sample-specific demand", fontsize=11)
    ax.text(7.3, 2.39, "Subtracting the blank cancels only matched contributions:", ha="center", fontsize=11)
    box(3.95, 1.48, 6.8, 0.62,
        r"$V-V_b=V_{\rm Fe}+(B_s-B_b)+(D_s-D_b)+A+I$", size=14)
    ax.text(7.3, 1.05, "Numerical account assumes Bₛ = Bᵦ, Dₛ = Dᵦ, A = I = 0.", ha="center", fontsize=11)
    ax.text(7.3, 0.69, "Colour masking can change Dₛ without consuming titrant.", ha="center", fontsize=11)
    fig.text(0.5, 0.027, "Equivalence = stoichiometric inventory match.  Endpoint = observed mixed-flask colour criterion.",
             ha="center", fontsize=12, weight="bold")
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
