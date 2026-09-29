"""Original energy portrait for x''=-sin(x); emit a PNG in the caller's CWD."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D


def main():
    fig, ax = plt.subplots(figsize=(9, 4.8), layout="constrained", facecolor="white")
    x = np.linspace(-2.5 * np.pi, 2.5 * np.pi, 900)
    v = np.linspace(-3.1, 3.1, 450)
    xx, vv = np.meshgrid(x, v)
    energy = vv**2 / 2 + 1 - np.cos(xx)
    ax.contour(xx, vv, energy, levels=[.25, .65, 1.1, 1.6], colors="#397da9", linewidths=1)
    ax.contour(xx, vv, energy, levels=[2.6, 3.5, 4.5], colors="#b18442", linewidths=1)
    sx = np.linspace(x[0], x[-1], 95)
    sv = np.linspace(v[0], v[-1], 55)
    mx, mv = np.meshgrid(sx, sv)
    ax.streamplot(sx, sv, mv, -np.sin(mx), color="#bfc7ce", density=.6, linewidth=.55, arrowsize=.75)
    sep = 2 * np.abs(np.cos(x / 2))
    ax.plot(x, sep, color="#333a43", linewidth=1.9)
    ax.plot(x, -sep, color="#333a43", linewidth=1.9)
    ax.scatter([-2 * np.pi, 0, 2 * np.pi], [0, 0, 0], color="#25734d", s=45, zorder=5)
    ax.scatter([-np.pi, np.pi], [0, 0], color="#b24741", marker="X", s=55, zorder=5)
    ax.scatter([0], [2], facecolors="white", edgecolors="#333a43", s=40, zorder=5)
    ax.annotate("initial separatrix point", xy=(0, 2), xytext=(1.05, 2.65), fontsize=9,
                arrowprops={"arrowstyle": "->", "color": "#333a43"})
    ax.set_xticks(np.arange(-2, 3) * np.pi, [r"$-2\pi$", r"$-\pi$", "$0$", r"$\pi$", r"$2\pi$"])
    ax.set(xlim=(x[0], x[-1]), ylim=(v[0], v[-1]), xlabel="$x$", ylabel=r"$v=\dot x$",
           title="Pendulum phase portrait: librations, separatrices and rotations")
    ax.axhline(0, color="#c5cbd0", lw=.5, zorder=0)
    ax.spines[["top", "right"]].set_visible(False)
    legend = [
        Line2D([0], [0], color="#397da9", label="Libration: 0 < H < 2"),
        Line2D([0], [0], color="#333a43", label="Separatrix: H = 2"),
        Line2D([0], [0], color="#b18442", label="Rotation: H > 2"),
    ]
    ax.legend(handles=legend, loc="lower center", fontsize=9, ncol=3, framealpha=1)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
