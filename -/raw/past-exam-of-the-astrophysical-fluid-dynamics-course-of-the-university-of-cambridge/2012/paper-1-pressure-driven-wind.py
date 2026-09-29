"""Original isothermal Parker-wind branches; no source-exam figure reused."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def mach_at(radius, supersonic):
    rhs = 4 * np.log(radius) + 4 / radius - 3
    # Solve y - log(y) = rhs using log(y) to retain small inner velocities.
    lo, hi = (0.0, 8.0) if supersonic else (-100.0, 0.0)
    for _ in range(80):
        mid = (lo + hi) / 2
        value = np.exp(mid) - mid
        if (value < rhs) == supersonic:
            lo = mid
        else:
            hi = mid
    return np.exp((lo + hi) / 4)


def main():
    radius = np.geomspace(0.15, 8.0, 501)
    wind = np.array([mach_at(x, x >= 1) for x in radius])
    other = np.array([mach_at(x, x < 1) for x in radius])
    rhs = 4 * np.log(radius) + 4 / radius - 3
    assert np.max(np.abs(wind**2 - np.log(wind**2) - rhs)) < 1e-11
    assert abs(mach_at(1, True) - 1) < 1e-7
    fig, ax = plt.subplots(figsize=(7.5, 4.4), layout="constrained")
    ax.plot(radius, wind, lw=2.4, label="Outward transonic wind")
    ax.plot(radius, other, color="0.55", ls="--", label="Other critical velocity branch")
    ax.axvline(1, color="0.7", lw=1)
    ax.axhline(1, color="0.7", lw=1)
    ax.plot(1, 1, "o", color="tab:red")
    ax.annotate("Regular sonic crossing", (1, 1), xytext=(2.1, 0.55),
                arrowprops={"arrowstyle": "->", "color": "0.3"})
    ax.set(xscale="log", ylim=(0, 3.5), xlabel=r"Radius $r/r_s$",
           ylabel=r"Speed $u/a$", title="Pressure-driven isothermal wind")
    ax.legend(loc="upper left", fontsize=9)
    ax.grid(alpha=0.18)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
