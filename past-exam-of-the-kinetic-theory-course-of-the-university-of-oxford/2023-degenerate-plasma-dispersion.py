"""Original classical-trajectory degenerate-plasma dispersion diagram.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
The sole output is the PNG with this script's basename in the current directory.
"""

from pathlib import Path
import math

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def response_bracket(log_delta: float) -> float:
    """Return 1 - (s/2) log((s+1)/(s-1)), s = 1 + exp(log_delta)."""
    delta = math.exp(log_delta)
    s = 1.0 + delta
    if s > 3.0:
        # Avoid cancellation at large phase speed.
        inv_s2 = 1.0 / (s * s)
        power = inv_s2
        total = 0.0
        for n in range(1, 25):
            total -= power / (2 * n + 1)
            power *= inv_s2
        return total
    # Resolve the exponentially small edge separation without computing s - 1.
    return 1.0 + 0.5 * s * (log_delta - math.log(2.0 + delta))


def branch(kappa: float) -> float:
    """Positive root omega / omega_pe at kappa = k v_Fe / omega_pe."""
    if kappa == 0.0:
        return 1.0
    low, high = -100.0, math.log(max(10.0, 10.0 / kappa))
    for _ in range(110):
        mid = 0.5 * (low + high)
        if response_bracket(mid) + kappa * kappa / 3.0 < 0.0:
            low = mid
        else:
            high = mid
    return kappa * (1.0 + math.exp(0.5 * (low + high)))


def main() -> None:
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 15})
    kappa = np.linspace(0.0, 4.0, 650)
    omega = np.array([branch(float(k)) for k in kappa])
    fig, ax = plt.subplots(figsize=(9.2, 6.4), dpi=120, facecolor="white")
    fig.suptitle("Degenerate electron plasma: Langmuir waves to zero-point sound",
                 y=0.98, fontsize=14)
    ax.set_facecolor("white")
    ax.fill_between(kappa, -kappa, kappa, color="#e7e9ed",
                    label=r"Populated resonant velocities: $|\omega/k|\leq v_{Fe}$")
    ax.plot(kappa, kappa, color="#727780", linewidth=1.2)
    ax.plot(kappa, -kappa, color="#727780", linewidth=1.2)
    ax.plot(kappa, omega, color="#145da0", linewidth=2.6,
            label="Exact electron branches in the supplied kinetic model")
    ax.plot(kappa, -omega, color="#145da0", linewidth=2.6)
    small = kappa[kappa <= 1.05]
    approx = np.sqrt(1.0 + 0.6 * small * small)
    ax.plot(small, approx, "--", color="#c35b11", linewidth=1.9,
            label=r"Long-wave approximation: $\omega^2/\omega_{pe}^2=1+3\kappa^2/5$")
    ax.plot(small, -approx, "--", color="#c35b11", linewidth=1.9)
    ax.scatter([0, 0], [1, -1], color="#145da0", s=24, zorder=4)
    ax.annotate("Undamped roots remain outside the wedge",
                xy=(1.45, branch(1.45)), xytext=(0.55, 3.05),
                arrowprops={"arrowstyle": "->", "color": "#145da0"},
                fontsize=11, color="#145da0")
    ax.text(2.5, 0.10, "Particles can resonate\ninside this wedge",
            ha="center", va="center", color="#555b63", fontsize=11)
    ax.text(2.45, -3.85, r"$\omega\to -k v_{Fe}$ from below", fontsize=11)
    ax.set(xlim=(0, 4), ylim=(-4.3, 4.3),
           xlabel=r"$\kappa=k v_{Fe}/\omega_{pe}$",
           ylabel=r"$\omega/\omega_{pe}$")
    ax.axhline(0, color="#9ca0a6", linewidth=0.7)
    ax.grid(alpha=0.18)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="lower left", bbox_to_anchor=(0, 1.01), fontsize=9,
              frameon=False, borderaxespad=0)
    fig.subplots_adjust(left=0.10, right=0.98, bottom=0.12, top=0.77)
    output = Path.cwd() / Path(__file__).with_suffix(".png").name
    fig.savefig(output, facecolor="white", transparent=False,
                metadata={"Software": "Matplotlib; original numerical diagram"})
    plt.close(fig)


if __name__ == "__main__":
    main()
