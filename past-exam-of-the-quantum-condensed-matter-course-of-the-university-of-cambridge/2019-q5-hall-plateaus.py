"""Original schematic Hall plateaus; write PNG to cwd.

Tested with Python 3.14, NumPy and Matplotlib; see root pyproject.toml.
Plateau widths and transitions are illustrative, not a fit to exam data.
The plotted quantity is transverse Hall resistance, not longitudinal Rxx.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fields, hall = [], []
    for filling in range(12, 0, -1):
        fields.extend([1/(filling+.3), 1/(filling-.3)])
        hall.extend([1/filling, 1/filling])
    fields[-1] = 1.15
    fig, ax = plt.subplots(figsize=(6.6, 3.8), facecolor="white")
    field = np.linspace(0, 1.15, 600)
    ax.plot(field, field, lw=1.4, ls="--", color="#9ba5ae", label=r"Classical $B/(n_s e)$")
    ax.plot(fields, hall, lw=2.1, color="#1768ab", label="Integer quantum Hall sketch")
    for filling in (1, 2, 3, 4):
        ax.text(min(1/(filling-.16), .98), 1/filling+.025, rf"$\nu={filling}$", fontsize=9, color="#1768ab")
    ax.set(xlim=(0, 1.15), ylim=(0, 1.18), xlabel=r"$B/B_1$, $B_1=n_s h/e$",
           ylabel=r"$|R_{xy}|/(h/e^2)$")
    ax.set_title("Transverse plateaus accompany longitudinal resistance minima", fontsize=10)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(frameon=False, fontsize=9, loc="upper left")
    fig.tight_layout()
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=125, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
