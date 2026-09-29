"""Oxford A10 (2015), Q2: source images and wall pressure deficit.

Writes 2015-source-wall-pressure.png in the current working directory.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7; root pyproject.toml.
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(-3.1, 3.1, 440)
    y = np.linspace(0, 3.2, 240)
    X, Y = np.meshgrid(x, y)
    minus = np.maximum(X**2 + (Y-1)**2, 1e-5)
    plus = X**2 + (Y+1)**2
    u = X/minus + X/plus
    v = (Y-1)/minus + (Y+1)/plus
    mask = minus < 0.012
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(9, 4.3), facecolor="white")
    ax.streamplot(x, y, np.ma.masked_where(mask, u), np.ma.masked_where(mask, v),
                  color="#176b93", density=1.0, linewidth=0.8, arrowsize=0.9)
    ax.axhspan(-1.4, 0, color="#f1f1f1")
    ax.axhline(0, color="#37474f", lw=2)
    ax.plot(0, 1, "o", color="#b4591c", ms=7)
    ax.plot(0, -1, "o", mfc="white", mec="#b4591c", mew=1.6, ms=7)
    ax.text(.16, 1.12, "Source $Q$", fontsize=10)
    ax.text(.16, -.93, "Image $Q$", fontsize=10)
    ax.set(xlim=(-3.1, 3.1), ylim=(-1.4, 3.2), aspect="equal",
           xlabel="$x/a$", ylabel="$y/a$", title="Equal-sign image: zero wall-normal velocity")
    scaled_x = np.linspace(-6, 6, 900)
    deficit = scaled_x**2/(1+scaled_x**2)**2
    bx.plot(scaled_x, deficit, color="#176b93", lw=2)
    bx.fill_between(scaled_x, deficit, color="#d8eaf3")
    bx.plot([-1, 1], [.25, .25], "o", color="#b4591c", ms=5)
    bx.text(.04, .91, r"$D=X^2/(1+X^2)^2$", transform=bx.transAxes, fontsize=12)
    bx.text(.04, .81, r"$\int_{-\infty}^{\infty}D\,dX=\pi/2$", transform=bx.transAxes, fontsize=12)
    bx.set(xlabel="$X=x/a$", ylabel=r"$D=(p_\infty-p)/(\rho Q^2/(2\pi^2a^2))$",
           title="Pressure deficit pulls the wall upward", ylim=(0, .36), xlim=(-6, 6))
    for axis in (ax, bx):
        axis.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig("2015-source-wall-pressure.png", dpi=155, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
