"""Original dimensionless beam shapes; Python 3.14, repository plotting packages."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    x = np.linspace(0, 1, 600)
    shapes = [(-(x**4-4*x**3+6*x**2)/24, "Free end", "#2563a5"),
              (-(2*x**4-5*x**3+3*x**2)/48, "Fixed height, free slope", "#c4791e"),
              (-x**2*(x-1)**2/24, "Clamped end", "#38825b")]
    fig, ax = plt.subplots(figsize=(7.4, 4.7), facecolor="white")
    ax.set_facecolor("white")
    ax.axhline(0, color="#888888", lw=1)
    for y, label, color in shapes:
        ax.plot(x, y, label=label, color=color, lw=2.2)
        ax.scatter([1], [y[-1]], color=color, s=32, zorder=4)
    ax.plot([0,0], [-0.135,0.018], color="black", lw=4)
    ax.set(xlabel=r"$x/L$", ylabel=r"$Ky/(\rho gL^4)$", xlim=(-0.025,1.03),
           title="Three beam solutions: added endpoint constraints")
    ax.legend(loc="lower left", fontsize=9)
    ax.spines[["right","top"]].set_visible(False)
    ax.grid(alpha=0.15)
    fig.tight_layout()
    fig.savefig(Path.cwd()/"2014-elastic-beam-boundaries.png", dpi=140, facecolor="white")
    plt.close(fig)
if __name__ == "__main__": main()
