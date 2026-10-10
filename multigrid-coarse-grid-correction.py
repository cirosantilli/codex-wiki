"""Original constructed coarse-correction diagram; write PNG basename to CWD.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Uses A_h = h**(-2) tridiag(-1, 2, -1), R = P.T/2, A_H = R A_h P.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np


def main():
    n, m, h = 7, 3, 1 / 8
    a = (2 * np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)) / h**2
    p = np.zeros((n, m))
    for i in range(m):
        p[2 * i + 1, i] = 1
        p[2 * i, i] = p[2 * i + 2, i] = 0.5
    r = p.T / 2
    ah = r @ a @ p
    z = np.array([1., 2., 1.])
    e = p @ z
    residual = a @ e
    coarse_residual = r @ residual
    correction = p @ np.linalg.solve(ah, coarse_residual)
    exact_remainder = e - correction
    half_remainder = e - correction / 2
    x = np.arange(n + 2) * h
    pad = lambda q: np.r_[0, q, 0]
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig = plt.figure(figsize=(10, 7.5), layout="constrained")
    gs = fig.add_gridspec(3, 1, height_ratios=[0.7, 1, 1])
    flow = fig.add_subplot(gs[0])
    flow.set(xlim=(0, 1), ylim=(0, 1))
    flow.axis("off")
    labels = [r"Fine residual $r_h$" + "\n[0, 0, 0, 64, 0, 0, 0]",
              r"Coarse residual $Rr_h$" + "\n[0, 32, 0]",
              r"Solve $A_Hz_H=Rr_h$" + "\n" + r"$z_H=[1,2,1]^T$",
              r"Prolong $Pz_H$" + "\n" + r"Then $v_h\leftarrow v_h+Pz_H$"]
    for i, label in enumerate(labels):
        left = 0.008 + 0.254 * i
        flow.add_patch(FancyBboxPatch((left, 0.30), 0.222, 0.49,
                                     boxstyle="round,pad=0.008", linewidth=1,
                                     edgecolor="#8fa8b7", facecolor="#f0f6f9"))
        flow.text(left + 0.111, 0.545, label, ha="center", va="center", fontsize=10)
        if i < 3:
            flow.annotate("", xy=(left + 0.245, 0.545), xytext=(left + 0.222, 0.545),
                          arrowprops={"arrowstyle": "->", "color": "#304d60", "lw": 1.4})
    flow.text(0.5, 0.09, r"$A_h=64\,\mathrm{tridiag}(-1,2,-1)$     "
              r"$R=P^T/2$     $A_H=16\,\mathrm{tridiag}(-1,2,-1)$",
              ha="center", fontsize=11)
    ax = fig.add_subplot(gs[1])
    ax.plot(x, pad(e), "o-", color="#166b9a", lw=2, ms=6,
            label=r"Constructed fine error $e_h=P[1,2,1]^T$")
    ax.scatter(x[2:-1:2], z, s=105, marker="s", facecolors="white",
               edgecolors="#b34b19", linewidths=2, zorder=4, label="Coarse correction values")
    ax.set(xlim=(0, 1), ylim=(-0.12, 2.4), ylabel="Error / correction value",
           title="Linear interpolation reconstructs this particular error exactly")
    ax.legend(loc="upper right", fontsize=9, framealpha=1)
    ax.set_xticks(x)
    ax.tick_params(labelbottom=False)
    ax.grid(axis="x", alpha=0.15)
    ax = fig.add_subplot(gs[2])
    ax.plot(x, pad(e), color="#969fa8", ls=":", lw=2, label="Initial error")
    ax.plot(x, pad(half_remainder), "o--", color="#b34b19", lw=2, ms=5,
            label="Half the exact coarse correction: remaining error = e / 2")
    ax.plot(x, pad(exact_remainder), "o-", color="#166b9a", lw=2, ms=4,
            label="Exact coarse correction: remaining error = 0")
    ax.set(xlim=(0, 1), ylim=(-0.15, 2.45), xticks=x, xlabel="Position x",
           ylabel="Remaining signed error", title="An approximate coarse solve leaves a coarse-solve defect")
    ax.grid(axis="x", alpha=0.15)
    ax.legend(loc="upper right", fontsize=9, framealpha=1)
    fig.suptitle("Coarse-grid correction: a seven-point Poisson example", fontsize=16)
    fig.supxlabel("Constructed model • homogeneous boundary corrections • exact arithmetic values • no measured data",
                  fontsize=10)
    fig.savefig(Path(Path(__file__).stem + ".png"), dpi=120, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
