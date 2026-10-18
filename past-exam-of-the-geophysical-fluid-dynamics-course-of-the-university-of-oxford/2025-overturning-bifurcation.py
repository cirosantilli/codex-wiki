"""Steady two-box overturning branches; Python 3.14, numpy and matplotlib.

Run from the desired output directory; writes only the identically named PNG.
Solid branches are stable; dashed branches unstable under salt-budget dynamics.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

A, B = 21., 196.
Ec = A * A / (4 * B)
fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.6), layout="constrained", facecolor="white")

def branches(ax, lam, color, label):
    a, b = lam * A, lam * B
    ec = a * a / (4 * b)
    # Avoid the singular E=q=0 endpoint of the reduced stationary equation.
    e = np.linspace(1e-5, ec, 500)
    d = np.sqrt(np.maximum(a * a - 4 * b * e, 0))
    ax.plot(e, (a + d) / 2, color=color, lw=2.2, label=label)
    ax.plot(e, (a - d) / 2, color=color, lw=2, ls="--")
    er = np.linspace(1e-5, .8, 500)
    ax.plot(er, (a - np.sqrt(a * a + 4 * b * er)) / 2, color=color, lw=2.2)
    ax.scatter([ec], [a / 2], s=30, color=color, zorder=4)

branches(axes[0], 1, "#1f5b85", "Stable branches")
axes[0].plot([], [], "--", color="#1f5b85", lw=2, label="Unstable branch")
axes[0].axvline(.3, color="#555555", ls=":", lw=1.4)
for q in [(A + np.sqrt(A*A - 4*B*.3))/2,
          (A - np.sqrt(A*A - 4*B*.3))/2,
          (A - np.sqrt(A*A + 4*B*.3))/2]:
    axes[0].scatter([.3], [q], color="#111111", s=22, zorder=5)
axes[0].annotate("Fold: (0.5625, 10.5)", xy=(Ec, A/2), xytext=(.37, 16),
                 arrowprops=dict(arrowstyle="->"), fontsize=10)
axes[0].text(.315, 19.4, "Present E = 0.3", fontsize=9)
axes[0].text(.43, -6.8, "Reversed circulation", fontsize=10)
axes[0].annotate("Loss of positive state", xy=(Ec, -4.35), xytext=(Ec, 8.8),
                 arrowprops=dict(arrowstyle="->", color="#b04238", lw=1.8),
                 color="#b04238", fontsize=9, rotation=90, ha="right", va="top")
axes[0].set_title("Printed parameters: A = 21 Sv, B = 196 Sv")
branches(axes[1], 1, "#b4b8bc", r"$k$")
branches(axes[1], .7, "#1f5b85", r"$0.7k$")
branches(axes[1], .45, "#b04238", r"$0.45k$")
axes[1].axvline(.3, color="#555555", ls=":", lw=1.4)
axes[1].set_title("Reducing k moves the fold towards smaller E")
for ax in axes:
    ax.set_facecolor("white")
    ax.axhline(0, color="black", lw=.7)
    ax.set(xlim=(0, .8), ylim=(-8, 24), xlabel="Freshwater transport E (Sv)",
           ylabel="Steady overturning q (Sv)")
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(alpha=.17)
    ax.legend(loc="upper right", fontsize=9)
fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=130, facecolor="white")
plt.close(fig)
