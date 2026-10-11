"""Original accreting-drop curves. Python 3.14.4; root pyproject.toml deps.

The optional quadratic drag has dimensionless strength eta=2, not exam data.
Run from the desired output directory; writes the PNG basename into cwd.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def drag_curve(tau, eta=2.0):
    """RK4 for w'=1-3w/(1+tau)-eta*w**2/(1+tau)."""
    w = np.zeros_like(tau)
    def rhs(t, y):
        return 1 - (3 * y + eta * y * y) / (1 + t)
    for j, dt in enumerate(np.diff(tau)):
        t, y = tau[j], w[j]
        k1 = rhs(t, y)
        k2 = rhs(t + dt / 2, y + dt * k1 / 2)
        k3 = rhs(t + dt / 2, y + dt * k2 / 2)
        k4 = rhs(t + dt, y + dt * k3)
        w[j + 1] = y + dt * (k1 + 2*k2 + 2*k3 + k4) / 6
    return w


def main():
    tau = np.linspace(0, 24, 12001)
    w = ((1 + tau) - (1 + tau)**-3) / 4
    wd = drag_curve(tau)
    fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.5), layout="constrained")
    fig.patch.set_facecolor("white")
    for ax, xmax, ymax in zip(axes, [2, 24], [1.8, 7]):
        ax.set_facecolor("white")
        ax.plot(tau, w, color="#205b9e", lw=2.2, label="Growing drop, no drag")
        ax.plot(tau, tau, color="0.4", lw=1.3, ls=":", label="No growth or drag: $w=\\tau$")
        ax.plot(tau, (1 + tau) / 4, color="#c77820", lw=1.3, ls="-.", label="Late asymptote: $w=(1+\\tau)/4$")
        ax.plot(tau, wd, color="#b03c6a", lw=2, ls="--", label="Growing drop + quadratic drag ($\\eta=2$)")
        ax.set(xlim=(0, xmax), ylim=(0, ymax), xlabel=r"Time $\tau=\mu t/r_0$", ylabel=r"Speed $w=\mu v/(gr_0)$")
        ax.grid(alpha=0.2)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set_title("Initial slope is 1; growth reduces acceleration")
    axes[1].set_title("Continued growth: drag need not give a horizontal limit")
    axes[1].legend(loc="upper left", fontsize=8.6)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
