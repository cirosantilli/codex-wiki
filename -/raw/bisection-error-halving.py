"""Compare bisection widths, guarantees, and errors; write the PNG to cwd.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    steps = np.arange(16)
    widths, errors = [], []
    a, b = 1.0, 2.0
    for k in steps:
        m = (a + b) / 2
        widths.append(b - a)
        errors.append(abs(m - np.sqrt(2)))
        if k == steps[-1] or m**2 == 2 or m in (a, b):
            break
        if m**2 > 2:
            b = m
        else:
            a = m
    widths, errors = np.asarray(widths), np.asarray(errors)
    assert len(errors) == 16
    assert np.array_equal(widths, 2.0 ** (-steps))
    assert np.all(errors <= widths / 2)
    assert widths[9] / 2 == 1 / 1024
    assert errors[7] > errors[6]

    fig, ax = plt.subplots(figsize=(9.2, 5.3), layout="constrained")
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.semilogy(steps, widths, "--", color="#2166ac", lw=2,
                label=r"Retained width $W_k=2^{-k}$")
    ax.semilogy(steps, widths / 2, "o-", color="#25834a", lw=2,
                ms=4, label=r"Midpoint guarantee $W_k/2=2^{-(k+1)}$")
    # Logarithms cannot show zero error: mark exact hits separately if reused
    # for another function. No exact hit occurs here because sqrt(2) is irrational.
    positive = errors > 0
    ax.semilogy(steps[positive], errors[positive], "s-", color="#b43b35", lw=1.8,
                ms=4, label=r"Actual midpoint error $|m_k-\sqrt{2}|$")
    for k in steps[~positive]:
        ax.annotate("Exact root: error = 0", xy=(k, 0.03),
                    xycoords=("data", "axes fraction"), ha="center")
    ax.axhline(1e-3, color="0.4", ls=":", lw=1.5, label=r"Requested tolerance $10^{-3}$")
    ax.axvline(9, color="0.6", ls=":", lw=1)
    ax.scatter([9], [widths[9] / 2], facecolors="white", edgecolors="#25834a",
               linewidths=2, s=95, zorder=6)
    ax.annotate("9 halvings suffice\nbound = 1/1024", (9, widths[9] / 2),
                xytext=(10.1, 0.008), fontsize=10,
                arrowprops={"arrowstyle": "->", "color": "0.3"})
    ax.annotate("Actual error can rise\nwhile the guarantee falls", (7, errors[7]),
                xytext=(3.1, 0.000025), fontsize=10, color="#b43b35",
                arrowprops={"arrowstyle": "->", "color": "#b43b35"})
    ax.set(xlim=(-0.3, 15.3), ylim=(8e-7, 1.6), xticks=steps,
           xlabel="k = completed halvings (k = 0 is the initial bracket)",
           ylabel="Width or error (logarithmic scale)",
           title=r"Bisection of $x^2-2$ on $[1,2]$: predictable bounds, uneven actual errors")
    ax.legend(loc="upper right", fontsize=9, framealpha=1)
    ax.grid(which="major", alpha=0.18)
    ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path.cwd() / "bisection-error-halving.png", dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
