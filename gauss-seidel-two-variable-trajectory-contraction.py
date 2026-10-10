"""Draw original exact-system trajectory and contraction; PNG goes to the CWD.

Tested with Python 3.14, matplotlib 3.10.7, and numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    a = np.array([[4.0, 1.0], [1.0, 3.0]])
    b = np.array([1.0, 2.0])
    solution = np.linalg.solve(a, b)
    gs, jacobi = [np.zeros(2)], [np.zeros(2)]
    row_path = [gs[0].copy()]
    for _ in range(9):
        x_new = (1 - gs[-1][1]) / 4
        row_path.append(np.array([x_new, gs[-1][1]]))
        y_new = (2 - x_new) / 3
        gs.append(np.array([x_new, y_new]))
        row_path.append(gs[-1].copy())
        jacobi.append(np.array([(1 - jacobi[-1][1]) / 4, (2 - jacobi[-1][0]) / 3]))
    gs, jacobi, row_path = np.array(gs), np.array(jacobi), np.array(row_path)
    k = np.arange(len(gs))
    gs_error = np.linalg.norm(gs - solution, axis=1)
    jacobi_error = np.linalg.norm(jacobi - solution, axis=1)
    # An independent formula checks the plotted direct row updates.
    np.testing.assert_allclose(gs_error[1:], 7 * np.sqrt(10) / (11 * 12.0 ** k[1:]),
                               rtol=3e-6, atol=1e-16)
    blue, orange, gray = "#146b88", "#b05012", "#6b7280"
    fig, (ax, err) = plt.subplots(1, 2, figsize=(11, 4.8), dpi=110, facecolor="white")
    fig.suptitle("Fresh updates select a faster error mode", fontsize=18, y=0.98)
    ax.set_title("Rows move one coordinate at a time", fontsize=13, pad=11)
    x = np.linspace(-0.04, 0.30, 250)
    ax.plot(x, 1 - 4*x, color=gray, alpha=0.55, linewidth=1.2, label=r"$4x+y=1$")
    ax.plot(x, (2 - x)/3, color=gray, linestyle="--", alpha=0.8, linewidth=1.2,
            label=r"$x+3y=2$")
    ax.plot(row_path[:7, 0], row_path[:7, 1], color=blue, linewidth=2, alpha=0.85)
    for start, end in zip(row_path[:4], row_path[1:5]):
        ax.annotate("", xy=end, xytext=start,
                    arrowprops={"arrowstyle": "->", "color": blue, "lw": 1.7})
    ax.scatter(gs[:4, 0], gs[:4, 1], color=blue, s=30, zorder=4, label="Sweep endpoints")
    ax.scatter(*solution, marker="*", color=orange, s=120, zorder=5, label="Exact solution")
    ax.annotate(r"$k=0$", gs[0], xytext=(5, 8), textcoords="offset points")
    ax.annotate(r"$k=1:\ (1/4,7/12)$", gs[1], xytext=(-5, -25),
                textcoords="offset points", ha="right", color=blue)
    ax.annotate(r"$k=2$", gs[2], xytext=(25, 5), textcoords="offset points", color=blue,
                arrowprops={"arrowstyle": "-", "color": blue})
    ax.annotate(r"$(1/11,7/11)$", solution, xytext=(-48, 22), textcoords="offset points",
                color=orange, arrowprops={"arrowstyle": "-", "color": orange})
    ax.set(xlim=(-0.025, 0.30), ylim=(-0.04, 0.76), xlabel=r"$x$", ylabel=r"$y$")
    ax.legend(loc="lower left", fontsize=9, framealpha=1)
    ax.grid(alpha=0.15)
    err.set_title("Computed error norms and exact decay", fontsize=13, pad=11)
    err.semilogy(k, gs_error, "o", color=blue, markersize=5, label="Gauss–Seidel iterates")
    err.semilogy(k[1:], 7*np.sqrt(10)/(11*12.0**k[1:]), "-", color=blue,
                 linewidth=1.6, label=r"$7\sqrt{10}/(11\cdot12^k),\ k\geq1$")
    err.semilogy(k, jacobi_error, "s--", color=orange, markersize=4, linewidth=1.3,
                 label="Jacobi iterates (same start)")
    err.text(0.04, 0.10, "Gauss–Seidel: factor 1/12 after sweep 1\n"
             "Jacobi: factor 1/12 every two sweeps", transform=err.transAxes,
             fontsize=10, bbox={"facecolor": "white", "edgecolor": "#d1d5db", "pad": 7})
    err.set(xlabel=r"Completed sweeps $k$", ylabel=r"Forward error $\|z^{(k)}-z_*\|_2$",
            xticks=np.arange(0, 10), ylim=(1e-10, 2))
    err.legend(loc="upper right", fontsize=9)
    err.grid(alpha=0.2, which="major")
    fig.subplots_adjust(left=0.075, right=0.975, bottom=0.17, top=0.84, wspace=0.30)
    fig.text(0.5, 0.04, "Original constructed system: A = [[4, 1], [1, 3]], b = [1, 2] • exact-arithmetic formulas",
             ha="center", fontsize=10, color="#374151")
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
