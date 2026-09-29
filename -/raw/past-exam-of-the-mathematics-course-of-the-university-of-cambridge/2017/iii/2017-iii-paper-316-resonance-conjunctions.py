"""Original mean-phase geometry; output an opaque PNG in the current directory."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

def main():
    fig, axes = plt.subplots(2, 3, figsize=(10, 5.4), dpi=100, facecolor="white")
    exterior = [[np.pi], [np.pi/2, 3*np.pi/2], [np.pi/3, np.pi, 5*np.pi/3]]
    interior = [[0], [np.pi/2, 3*np.pi/2], [0, 2*np.pi/3, 4*np.pi/3]]
    circle = np.linspace(0, 2*np.pi, 400)
    for row, phase_sets in enumerate([exterior, interior]):
        for col, phases in enumerate(phase_sets):
            ax = axes[row, col]
            ax.plot(np.cos(circle), np.sin(circle), color="#9ca3af", lw=1.4)
            ax.scatter([0], [0], color="#e9ab24", s=60, zorder=3)
            ax.plot([0, 1.25], [0, 0], "--", color="#6b7280", lw=1)
            ax.text(1.32, 0, "periapsis", ha="left", va="center", fontsize=8)
            for phase in phases:
                x, y = np.cos(phase), np.sin(phase)
                ax.plot([0, x], [0, y], color="#377eb8", lw=1.5)
                ax.scatter([x], [y], s=80, color="#176b9d", edgecolor="white", zorder=4)
            angle = r"$\pi$" if row == 0 or col == 1 else r"$0$"
            order = "q" if row == 0 else "n"
            kind = "Exterior" if row == 0 else "Interior"
            ax.set_title(f"{kind}: {order} = {col+1}, centre {angle}", fontsize=11)
            ax.set_xlim(-1.4, 2.0); ax.set_ylim(-1.3, 1.3)
            ax.set_aspect("equal"); ax.axis("off")
    fig.suptitle("Symmetric resonance: mean-conjunction phase directions", fontsize=14, y=.985)
    fig.text(.5, .035, "Small eccentricity, leading harmonic, coprime period ratios; blue dots mark allowed phases.\nThe circles show angular coordinates, not physical orbital shapes.", ha="center", fontsize=10)
    fig.subplots_adjust(left=.025, right=.985, top=.88, bottom=.13, hspace=.18, wspace=.04)
    fig.savefig(Path.cwd()/"2017-iii-paper-316-resonance-conjunctions.png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)

if __name__ == "__main__":
    main()
