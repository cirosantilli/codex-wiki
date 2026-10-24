"""Plot the analytic box density and current in Oxford 2017 A11, Q1(b).

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Dependencies and supported Python version are in the repository pyproject.toml.
"""
from pathlib import Path
import os

os.environ.setdefault("MPLCONFIGDIR", "/tmp/codex-wiki-matplotlib")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    # y=x/a. Current unit is hbar/(m*a**2); density unit is 1/a.
    y = np.linspace(0, 1, 501)
    density = 2 * np.sin(np.pi * y) ** 2
    current = np.pi * density
    fig, axes = plt.subplots(1, 2, figsize=(8.5, 3.7), layout="constrained")
    fig.set_facecolor("white")
    axes[0].plot(y, density, color="#175a9c", lw=2.8, label=r"$t=0$")
    axes[0].plot(y, density, color="#c85620", lw=1.8, ls="--", label=r"$t=t_*$")
    axes[0].set(title="Same position density", ylabel=r"$a|\Psi|^2$", ylim=(-0.1, 2.3))
    axes[1].plot(y, current, color="#175a9c", lw=2.5, label=r"$t=0$")
    axes[1].plot(y, -current, color="#c85620", lw=2.5, ls="--", label=r"$t=t_*$")
    axes[1].set(title="Opposite probability current", ylabel=r"$ma^2 j/\hbar$", ylim=(-7.6, 7.6))
    axes[1].annotate("", xy=(0.67, 3.0), xytext=(0.33, 3.0), arrowprops=dict(arrowstyle="->", color="#175a9c", lw=2))
    axes[1].annotate("", xy=(0.33, -3.0), xytext=(0.67, -3.0), arrowprops=dict(arrowstyle="->", color="#c85620", lw=2))
    for ax in axes:
        ax.set(xlabel=r"$x/a$", xlim=(0, 1))
        ax.axhline(0, lw=0.8, color="#555555")
        ax.grid(alpha=0.16)
        ax.legend(loc="upper right", frameon=False, fontsize=9)
        ax.spines[["top", "right"]].set_visible(False)
        ax.set_facecolor("white")
    fig.suptitle(r"Box reflection at $t_*=2ma^2/(\pi\hbar)$", fontsize=13)
    out = Path(__file__).with_suffix(".png").name
    fig.savefig(out, dpi=120, facecolor="white")
    plt.close(fig)
    print(out)


if __name__ == "__main__":
    main()
