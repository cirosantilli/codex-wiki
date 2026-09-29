"""Generate expanding-comoving-grid.png in the current directory.

Use: make _media/expanding-comoving-grid.png
Tested with Python 3.14.4, Matplotlib 3.10.7, NumPy 2.3.5.
The grid is schematic: the same comoving labels scale by a = 0.5, 1, 1.5.
Bottom panels sample an extended lattice around two different observers;
arrows have a common illustrative H and represent relative recession rates.
"""

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "savefig.facecolor": "white"})
    fig = plt.figure(figsize=(10, 7), facecolor="white")
    grid = fig.add_gridspec(2, 6, left=0.045, right=0.97, top=0.83,
                           bottom=0.13, hspace=0.53, wspace=0.65)
    fig.suptitle("One expansion factor; no preferred centre", fontsize=19, y=0.97)
    fig.text(0.5, 0.913, r"Top: fixed comoving labels, $\mathbf{r}=a\mathbf{x}$; identical physical plotting scales",
             ha="center", fontsize=12)
    coordinates = np.arange(-2, 3)
    x, y = np.meshgrid(coordinates, coordinates)
    for col, a in enumerate((0.5, 1.0, 1.5)):
        ax = fig.add_subplot(grid[0, 2 * col:2 * col + 2])
        for value in coordinates:
            ax.plot(a * coordinates, np.full(5, a * value), color="#d5dde3", lw=1)
            ax.plot(np.full(5, a * value), a * coordinates, color="#d5dde3", lw=1)
        ax.scatter(a * x, a * y, s=22, color="#286b96", zorder=3)
        ax.scatter([0, a], [0, 0], s=45, color="#bf5928", zorder=4)
        ax.plot([0, a], [-3.65, -3.65], color="#bf5928", lw=1.6)
        for endpoint in (0, a):
            ax.plot([endpoint, endpoint], [-3.77, -3.53], color="#bf5928", lw=1.6)
        ax.text(a / 2, -4.15, f"spacing = {a:g}", ha="center", va="top", fontsize=11)
        ax.set_title(f"a = {a:g}", fontsize=15, pad=10)
        ax.set(xlim=(-4.2, 4.2), ylim=(-4.7, 3.5), aspect="equal")
        ax.axis("off")

    local_x, local_y = np.meshgrid(np.arange(-2, 3), np.arange(-2, 3))
    local = np.column_stack((local_x.ravel(), local_y.ravel()))
    for col, (name, origin) in enumerate((("A", (0, 0)), ("B", (1, 1)))):
        ax = fig.add_subplot(grid[1, 3 * col:3 * col + 3])
        # Subtract the observer's location explicitly; each local patch is equal.
        absolute = local + np.asarray(origin)
        relative = absolute - np.asarray(origin)
        ax.scatter(relative[:, 0], relative[:, 1], s=23, color="#286b96", zorder=3)
        nonzero = np.any(relative != 0, axis=1)
        positions = relative[nonzero]
        rates = 0.22 * positions  # Same instantaneous H for both observers.
        ax.quiver(positions[:, 0], positions[:, 1], rates[:, 0], rates[:, 1],
                  angles="xy", scale_units="xy", scale=1, color="#bf5928",
                  width=0.009, headwidth=4, headlength=4)
        ax.scatter([0], [0], s=140, marker="*", color="#233f59", zorder=5)
        ax.text(0.23, -0.32, name, fontsize=13, weight="bold")
        ax.set_title(f"Observer {name}: comoving location {origin}", fontsize=12, pad=9)
        ax.set(xlim=(-2.75, 2.75), ylim=(-2.75, 2.75), aspect="equal")
        ax.axis("off")
    fig.text(0.5, 0.06, r"Bottom: $a=1$, same $H>0$; arrows show $H(\mathbf{r}-\mathbf{r}_O)$ in each observer's local patch",
             ha="center", fontsize=12)
    fig.text(0.5, 0.025, "Schematic samples of an extended grid; the drawn boundary is not an edge of the universe.",
             ha="center", fontsize=10)
    fig.savefig("expanding-comoving-grid.png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
