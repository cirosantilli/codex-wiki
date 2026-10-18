"""Original parcel-exchange diagrams; Python 3.14, NumPy 2.3, Matplotlib 3.10."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.7), layout="constrained")
    fig.set_facecolor("white")
    y = np.linspace(0, 1, 200)
    for ax, slope, title in zip(
        axes,
        (0.35, 1.05),
        ("Potential energy released", "Potential energy required"),
    ):
        for c in np.arange(-0.7, 1.1, 0.2):
            ax.plot(y, 0.8*y+c, color="#2271a2", lw=1.1, alpha=0.7)
        for z in (0.15, 0.45, 0.75):
            ax.axhline(z, color="#777777", ls=":", lw=1.3)
        start = np.array([0.20, 0.22])
        end = start + np.array([0.60, 0.60*slope])
        # b = z - 0.8 y; the colors follow the actual relative buoyancies.
        release = slope < 0.8
        for point, label, color in (
            (start, "A", "#c64332" if release else "#255f9e"),
            (end, "B", "#255f9e" if release else "#c64332"),
        ):
            ax.scatter(*point, s=115, color=color, edgecolor="white", zorder=5)
            ax.annotate(label, point, xytext=(-15, 10), textcoords="offset points",
                        weight="bold", color=color)
        ax.annotate("", xy=end, xytext=start,
                    arrowprops={"arrowstyle": "-|>", "color": "#c64332" if release else "#255f9e",
                                "lw": 2.5, "connectionstyle": "arc3,rad=-0.10"})
        ax.annotate("", xy=start, xytext=end,
                    arrowprops={"arrowstyle": "-|>", "color": "#255f9e" if release else "#c64332",
                                "lw": 2.5, "connectionstyle": "arc3,rad=-0.10"})
        ax.text(0.03, 0.96, r"$0<s<s_\rho$" if release else r"$s>s_\rho$",
                transform=ax.transAxes, va="top", bbox={"facecolor": "white", "edgecolor": "none"})
        ax.set(xlim=(0, 1), ylim=(0, 1), xlabel="Poleward distance y (schematic)",
               ylabel="Height z (schematic)", title=title, xticks=[], yticks=[])
        ax.spines[["top", "right"]].set_visible(False)
    handles = [plt.Line2D([], [], color="#2271a2", label="Isopycnals (constant buoyancy)"),
               plt.Line2D([], [], color="#777777", ls=":", label="Geopotentials (constant height)")]
    fig.legend(handles=handles, loc="outside lower center", ncol=2, frameon=False)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                dpi=140, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
