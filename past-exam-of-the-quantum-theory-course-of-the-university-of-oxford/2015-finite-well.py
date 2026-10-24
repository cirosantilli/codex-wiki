"""Graph the matching equations in Oxford 2015 A11 Q1(b).

Run with the intended _media topic directory as CWD; the PNG is written to CWD.
Tested: Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7 (root pyproject.toml).
"""
from pathlib import Path
import os
os.environ.setdefault("MPLCONFIGDIR", "/tmp/codex-wiki-matplotlib")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def matching_root(rho):
    lo, hi = 0.0, min(rho, np.pi / 2)
    for _ in range(90):
        mid = (lo + hi) / 2
        if mid / np.cos(mid) < rho:
            lo = mid
        else:
            hi = mid
    beta = (lo + hi) / 2
    return beta, beta * np.tan(beta)


def main():
    fig, axes = plt.subplots(1, 2, figsize=(8.5, 3.6), layout="constrained")
    for ax, rho in zip(axes, (0.8, 2.5)):
        end = min(rho, np.pi / 2)
        x = np.linspace(0, end * (1 - 1e-6), 700)
        circle_x = np.linspace(0, rho, 700)
        ax.plot(x, x * np.tan(x), color="#1d679d", lw=2.2, label=r"$\alpha=\beta\tan\beta$")
        ax.plot(circle_x, np.sqrt(np.maximum(rho*rho-circle_x*circle_x, 0)), color="#bd5228", lw=2.2, label=r"$\alpha=\sqrt{\rho^2-\beta^2}$")
        beta, alpha = matching_root(rho)
        ax.scatter([beta], [alpha], color="#222222", s=28, zorder=5)
        ax.annotate(r"$\beta_*=%.3f$" % beta, (beta, alpha), xytext=(8, 10), textcoords="offset points", fontsize=10)
        ax.set(xlim=(0, rho), ylim=(0, rho*1.45), xlabel=r"$\beta=\kappa a$", ylabel=r"$\alpha=ka$", title=r"$\rho=%.1f$" % rho)
        ax.grid(alpha=.15)
        ax.legend(loc="upper right", frameon=False, fontsize=9)
        ax.spines[["top", "right"]].set_visible(False)
        ax.set_facecolor("white")
    fig.suptitle(r"An even bound state for every positive well strength $\rho$", fontsize=12)
    out = Path.cwd() / Path(__file__).with_suffix(".png").name
    fig.savefig(out, dpi=120, facecolor="white")
    plt.close(fig)
    print(out)


if __name__ == "__main__":
    main()
