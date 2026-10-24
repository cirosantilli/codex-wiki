"""Generate 2017-point-interaction-green-function.png in the current directory."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.6), dpi=100, facecolor="white")
    x = np.unique(np.r_[np.linspace(0, np.pi, 900), 1.0])
    critical = np.pi / (np.pi - 1)
    for coefficient, label, color in [
        (0, r"$\alpha=0$", "#2563eb"),
        (1, r"$\alpha=1$", "#15803d"),
        (critical, r"$\alpha=\pi/(\pi-1)$", "#b91c1c"),
        (1.8, r"$\alpha=1.8$", "#a16207"),
    ]:
        axes[0].plot(x, x - coefficient * np.maximum(x - 1, 0), lw=2, label=label, color=color)
    axes[0].axhline(0, color="#64748b", lw=0.8)
    axes[0].scatter([np.pi], [0], color="#b91c1c", s=30, zorder=5)
    axes[0].set_title(r"Homogeneous modes: $u(0)=0$, $u'(0)=1$", fontsize=11)
    axes[0].set_ylabel(r"$u_\alpha(x)$")
    axes[0].legend(fontsize=9, loc="upper left")
    for source, color in [(0.45, "#2563eb"), (1.0, "#b91c1c"), (2.2, "#7e22ce")]:
        grid = np.unique(np.r_[x, source])
        lower, upper = np.minimum(grid, source), np.maximum(grid, source)
        u = np.minimum(lower, 1)
        v = np.where(upper <= 1, 1 + (np.pi - 2) * upper, np.pi - upper)
        axes[1].plot(grid, -u * v, color=color, lw=2, label=rf"$\xi={source:g}$")
        at_source = -min(source, 1) * (1 + (np.pi - 2) * source if source <= 1 else np.pi - source)
        axes[1].scatter([source], [at_source], color=color, s=25, zorder=5)
    axes[1].axhline(0, color="#64748b", lw=0.8)
    axes[1].set_title(r"Green kernels at $\alpha=1$: source marked by dot", fontsize=11)
    axes[1].set_ylabel(r"$G(x,\xi)$")
    axes[1].legend(fontsize=9, loc="lower right")
    for ax in axes:
        ax.axvline(1, color="#64748b", lw=1, ls="--", zorder=0)
        ax.set_xticks([0, 1, np.pi], ["0", "1", r"$\pi$"])
        ax.set_xlim(0, np.pi)
        ax.set_xlabel(r"$x$")
        ax.grid(alpha=0.15)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("A point coefficient changes the slope, not the value", fontsize=14, y=0.96)
    fig.subplots_adjust(left=0.07, right=0.98, bottom=0.14, top=0.82, wspace=0.28)
    fig.savefig("2017-point-interaction-green-function.png", dpi=100, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
