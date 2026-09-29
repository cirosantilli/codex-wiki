"""Synthetic saturating feedback model, with equilibrium and fold calculations.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media; write matching-basename opaque white PNG to CWD.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def equilibria(u, beta):
    roots = np.roots([1, -(u + beta), 1, -u])
    return sorted(r.real for r in roots if abs(r.imag) < 1e-8 and r.real >= 0)


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    beta = 1.8
    folds = sorted(z.real for z in np.roots([1, 0, 2, -2 * beta, 1]) if abs(z.imag) < 1e-8 and z.real > 0)
    x_on, x_off = folds
    u_on, u_off = [x - beta * x * x / (1 + x * x) for x in folds]
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.7), dpi=110)
    fig.suptitle("SYNTHETIC POSITIVE FEEDBACK — no biological data", weight="bold", y=0.98)
    ax = axes[0]
    x = np.linspace(0, 1.8, 1201)
    u = 0.12
    ax.plot(x, u + beta * x * x / (1 + x * x), color="#2468b4", lw=2, label="Production: u + βx²/(1+x²)")
    ax.plot(x, x, color="#334155", lw=2, label="Removal: x")
    for k, r in enumerate(equilibria(u, beta)):
        assert abs(u + beta * r * r / (1 + r * r) - r) < 1e-12
        stable = 2 * beta * r / (1 + r * r) ** 2 < 1
        ax.plot(r, r, "o", ms=8, mec="#334155", mfc="#187c64" if stable else "white", zorder=5)
        ax.text(r + 0.015, r - 0.15, ("stable" if stable else "unstable"), fontsize=10)
    ax.set(title="Same input, two stable equilibria\nu = 0.12, β = 1.8", xlabel="Activity x (normalized)", ylabel="Rate (normalized)", xlim=(0, 1.8), ylim=(0, 1.9))
    ax.legend(loc="upper left", fontsize=9)
    ax = axes[1]
    low = np.linspace(0, x_on, 500)
    middle = np.linspace(x_on, x_off, 500)
    high = np.linspace(x_off, 1.9, 500)
    for xx, style, label in ((low, "-", "β = 1.8: stable branches"), (middle, "--", "β = 1.8: unstable branch"), (high, "-", None)):
        ax.plot(xx - beta * xx * xx / (1 + xx * xx), xx, style, color="#2468b4", lw=2.4, label=label)
    inputs = np.linspace(0, 0.3, 200)
    ax.plot(inputs, [equilibria(s, 1)[0] for s in inputs], color="#7c5f9e", lw=2, label="β = 1: one stable equilibrium")
    for s, xx, label in ((u_on, x_on, f"ON: {u_on:.4f}"), (u_off, x_off, f"OFF: {u_off:.4f}")):
        roots = equilibria(s + (1e-6 if label.startswith("ON") else -1e-6), beta)
        end = roots[-1] if label.startswith("ON") else roots[0]
        ax.annotate("", (s, end), (s, xx), arrowprops={"arrowstyle": "->", "color": "#ba4a29", "lw": 2})
        ax.axvline(s, color="#94a3b8", linestyle=":", lw=1)
        ax.text(s + 0.006, 1.65 if label.startswith("ON") else 1.45, label, fontsize=10, color="#9b3c1d")
    ax.set(title="Equilibria under a slow input sweep\nArrows mark jumps at folds", xlabel="Sustained input u (normalized)", ylabel="Equilibrium activity x*", xlim=(0, 0.3), ylim=(0, 1.9))
    ax.legend(loc="upper left", bbox_to_anchor=(0, -0.19), fontsize=9, frameon=False)
    for ax in axes:
        ax.grid(alpha=0.18)
    fig.subplots_adjust(left=0.07, right=0.98, bottom=0.25, top=0.82, wspace=0.29)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
