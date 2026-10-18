"""Plot the regular open-dust growth mode; write only to the working directory.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from the corresponding _media directory to regenerate the PNG.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def growth(x):
    """Use a series near zero to avoid cancellation in the elementary formula."""
    x = np.asarray(x, dtype=float)
    result = np.empty_like(x)
    small = x < 0.005
    y = x[small]
    result[small] = 2*y/5 - 8*y**2/35 + 16*y**3/105 - 128*y**4/1155
    y = x[~small]
    result[~small] = 1 + 3/y - 3*np.sqrt((1+y)/y**3)*np.arcsinh(np.sqrt(y))
    return result


def main():
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 15})
    x = np.geomspace(1e-3, 1e4, 900)
    fig, ax = plt.subplots(figsize=(9, 5.2), dpi=110, layout="constrained", facecolor="white")
    ax.set_facecolor("white")
    ax.loglog(x, growth(x), color="#165a93", lw=2.8, label=r"Regular mode $\delta_2(x)$")
    early = x[x < 1.5]
    ax.loglog(early, 2*early/5, "--", color="#bf5a19", lw=1.8, label=r"Early limit: $2x/5$")
    ax.axhline(1, color="#3b7656", ls="--", lw=1.8, label="Late limit: 1")
    ax.axvline(1, color="#777777", ls=":", lw=1.5)
    ax.text(1.2, 0.001, "Matter and curvature\ncontribute equally", fontsize=11, color="#555555")
    ax.set(xlim=(1e-3, 1e4), ylim=(2e-4, 1.7), xlabel=r"Matter-to-curvature transition variable $x=(1-\Omega)a/\Omega$", ylabel=r"Density-growth mode $\delta_2$", title="Linear density growth freezes in an open dust universe")
    ax.grid(which="major", alpha=0.22)
    ax.legend(loc="upper left", framealpha=1)
    fig.savefig(Path.cwd() / "2025-open-universe-growth.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
