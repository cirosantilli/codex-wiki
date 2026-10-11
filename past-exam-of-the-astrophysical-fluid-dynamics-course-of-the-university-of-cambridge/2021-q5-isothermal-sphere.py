#!/usr/bin/env python3
"""Integrate regular isothermal spheres and plot a fixed-mass pressure fold.

Tested with Python 3.14.4, numpy 2.3.5 and matplotlib 3.10.7 (+dfsg1 build),
matching the repository pyproject.toml. Writes the PNG basename into cwd.
The Runge-Kutta integration uses only the dependencies already declared there.
"""
from pathlib import Path
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def solve(step=0.001, limit=10.0):
    start = 0.001
    count = round((limit - start) / step)
    xi = start + step * np.arange(count + 1)
    psi = np.empty(count + 1)
    slope = np.empty(count + 1)
    psi[0] = start**2 / 6 - start**4 / 120 + start**6 / 1890
    slope[0] = start / 3 - start**3 / 30 + start**5 / 315
    def rhs(x, y, v):
        return v, math.exp(-y) - 2 * v / x
    for j in range(count):
        x, y, v = xi[j], psi[j], slope[j]
        a, b = rhs(x, y, v)
        c, d = rhs(x + step / 2, y + step * a / 2, v + step * b / 2)
        e, f = rhs(x + step / 2, y + step * c / 2, v + step * d / 2)
        g, h = rhs(x + step, y + step * e, v + step * f)
        psi[j + 1] = y + step * (a + 2 * c + 2 * e + g) / 6
        slope[j + 1] = v + step * (b + 2 * d + 2 * f + h) / 6
    return xi, psi, slope


def critical_point(xi, psi, slope):
    criterion = slope**2 - 2 * np.exp(-psi)
    j = int(np.flatnonzero(criterion >= 0)[0])
    fraction = -criterion[j - 1] / (criterion[j] - criterion[j - 1])
    return tuple(values[j - 1] + fraction * (values[j] - values[j - 1])
                 for values in (xi, psi, slope))


def main():
    xi, psi, slope = solve()
    xc, pc, vc = critical_point(xi, psi, slope)
    mass = xi**2 * slope
    mc = xc**2 * vc
    # At fixed mass M and sound speed, R K/(G M)=xi/mass and
    # p_surface (4 pi G^3 M^2/K^4)=mass^2 exp(-psi).
    radius_ratio = (xi / mass) / (xc / mc)
    pressure_ratio = mass**2 * np.exp(-psi) / (mc**2 * np.exp(-pc))
    fig, axes = plt.subplots(1, 2, figsize=(8.2, 3.8), dpi=120, facecolor="white")
    left, right = axes
    for ax in axes:
        ax.set_facecolor("white")
        ax.grid(alpha=0.18)
        ax.spines[["top", "right"]].set_visible(False)
    left.semilogy(xi, np.exp(-psi), color="#0072b2", linewidth=2.2)
    left.axvline(xc, color="0.45", linestyle="--", linewidth=1)
    left.plot(xc, math.exp(-pc), "o", color="#0072b2", markersize=4)
    left.annotate(f"First critical radius\n$\\xi_c={xc:.3f}$", xy=(xc, math.exp(-pc)),
                  xytext=(1.1, 0.029), fontsize=9,
                  arrowprops={"arrowstyle": "->", "color": "0.3"})
    left.set(xlabel=r"Dimensionless radius $\xi=r/a$", ylabel=r"Density $\rho/\rho_c$",
             title="Regular equilibrium density", xlim=(0, 10), ylim=(0.02, 1.1))
    stable = (xi >= 3) & (xi <= xc)
    unstable = (xi >= xc) & (xi <= 8.5)
    right.plot(radius_ratio[stable], pressure_ratio[stable], color="#0072b2", linewidth=2.4,
               label="First stable branch")
    right.plot(radius_ratio[unstable], pressure_ratio[unstable], color="#d55e00", linewidth=2.4,
               label="Beyond first threshold")
    right.plot(1, 1, "o", color="0.2", markersize=4)
    right.annotate("Pressure turning point", xy=(1, 1), xytext=(1.25, 1.015), fontsize=9,
                   arrowprops={"arrowstyle": "->", "color": "0.3"})
    right.set(xlabel=r"Boundary radius $R/R_{\rm crit}$", ylabel=r"Surface pressure $p_s/p_{s,\rm crit}$",
              title="Fixed total mass and temperature", xlim=(0.9, 2.1), ylim=(0.3, 1.09))
    right.legend(loc="lower right", fontsize=8, frameon=False)
    fig.tight_layout()
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)
    print(f"xi_crit={xc:.10f}; central/surface density={math.exp(pc):.10f}")
    print(f"Rcrit K/(GM)={xc/mc:.10f}; mean/central density={3*vc/xc:.10f}")


if __name__ == "__main__":
    main()
