"""Plot self-pairings; run in _media with Python 3.14, matplotlib 3.10.7, NumPy 2.3.5."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white"})
    axis = np.linspace(-1.5, 1.5, 121)
    x, y = np.meshgrid(axis, axis)
    forms = [
        (x*x-y*y, r"$q=x^2-y^2$", "Bounded, indefinite", "Negative along the y axis"),
        (x*x, r"$q=x^2$", "Bounded, degenerate", "Zero along the entire y axis"),
        (2*x*x+3*y*y, r"$q=2x^2+3y^2$", "Bounded and coercive", r"$q\geq 2(x^2+y^2)$"),
    ]
    fig = plt.figure(figsize=(11.5, 6.4), layout="constrained")
    grid = fig.add_gridspec(2, 3, height_ratios=[1.1, 1])
    norm = Normalize(-2.5, 11.5)
    for col, (q, formula, name, message) in enumerate(forms):
        surface = fig.add_subplot(grid[0, col], projection="3d")
        surface.plot_surface(x, y, q, cmap="coolwarm", norm=norm, rstride=4, cstride=4, linewidth=0, alpha=1)
        surface.set(xlabel="x", ylabel="y", zlabel="q", xlim=(-1.5, 1.5), ylim=(-1.5, 1.5), zlim=(-2.5, 11.5))
        surface.set_title(name + "\n" + formula, pad=8)
        surface.set_xticks([-1, 0, 1]); surface.set_yticks([-1, 0, 1])
        surface.set_zticks([0, 5, 10]); surface.view_init(elev=25, azim=-55)
        surface.set_box_aspect((1, 1, 0.85))
        contour = fig.add_subplot(grid[1, col])
        levels = [-2, -1, 0, 1, 2, 4, 6, 8, 10]
        contour.contourf(x, y, q, levels=np.linspace(-2.5, 11.5, 29), cmap="coolwarm", norm=norm)
        lines = contour.contour(x, y, q, levels=levels, colors="#374151", linewidths=0.75)
        contour.clabel(lines, inline=True, fontsize=9)
        if col == 0:
            contour.plot(axis, axis, color="black", lw=1.1)
            contour.plot(axis, -axis, color="black", lw=1.1)
        if col == 1:
            contour.axvline(0, color="black", lw=1.8)
        contour.set(xlabel="x", ylabel="y", aspect="equal", title=message)
        contour.set_xticks([-1, 0, 1]); contour.set_yticks([-1, 0, 1])
    fig.suptitle("Upper bounds allow saddles and flat directions; coercivity forces a bowl", fontsize=15)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
