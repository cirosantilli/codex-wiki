"""Generate gravitational-clock-comparison.png in cwd (Python 3.14).

Dependencies: numpy and matplotlib. White, opaque output; no data downloads.
The Earth example neglects rotation and treats local g as constant. The second
panel is a dimensionless Schwarzschild vacuum exterior, never a body interior.
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


C = 299_792_458.0  # m/s, exact SI value
G_LOCAL = 9.81  # m/s^2, illustrative surface acceleration
HEIGHT = 1000.0  # m
EARTH_RADIUS = 6.371e6  # m, spherical model
DAY = 86400.0  # s


def main():
    delta = G_LOCAL * HEIGHT / C**2
    hours = np.linspace(0.0, 24.0, 241)
    gain_ns = delta * hours * 3600.0 * 1e9
    compactness = np.linspace(0.0, 0.8, 401)
    exact = np.sqrt(1.0 - compactness)
    weak = 1.0 - compactness / 2.0

    plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, (left, right) = plt.subplots(1, 2, figsize=(10, 4.5), layout="constrained")
    fig.patch.set_facecolor("white")
    left.plot(hours, gain_ns, color="#1565a8", lw=2.5)
    left.scatter([24], [gain_ns[-1]], color="#1565a8", zorder=3)
    left.annotate(f"{gain_ns[-1]:.2f} ns after 24 h", (24, gain_ns[-1]),
                  xytext=(11, 8.0), arrowprops={"arrowstyle": "->", "color": "#555"})
    left.text(0.06, 0.92, "Upper clock: 1000 m higher\n" +
              r"$\delta=gh/c^2=1.092\times10^{-13}$",
              transform=left.transAxes, va="top")
    left.set(xlabel="Elapsed time on lower clock (hours)",
             ylabel="Upper clock's accumulated gain (ns)",
             title="Earth: constant-g weak-field estimate", xlim=(0, 25), ylim=(0, 11))
    left.set_xticks([0, 6, 12, 18, 24])
    left.grid(alpha=0.2)

    right.axvspan(0, 0.1, color="#e6f2e8", zorder=0)
    right.plot(compactness, exact, color="#1565a8", lw=2.5,
               label=r"Exact: $\sqrt{1-r_s/r}$")
    right.plot(compactness, weak, color="#d26c16", lw=2, ls="--",
               label=r"First order: $1-r_s/(2r)$")
    right.text(0.05, 0.55, "Weak\nfield", ha="center", fontsize=9, color="#396b42")
    right.text(0.48, 0.92, "Vacuum exterior only\n" + r"$r>r_s$ and outside matter",
               transform=right.transAxes, va="top", ha="center", fontsize=9)
    right.set(xlabel=r"Compactness $r_s/r$", ylabel=r"Static-clock factor $d\tau/dt$",
              title="Schwarzschild: comparison to infinity", xlim=(0, 0.8), ylim=(0.4, 1.03))
    right.legend(loc="lower left", frameon=False, fontsize=9)
    right.grid(alpha=0.2)
    fig.savefig("gravitational-clock-comparison.png", dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)

    # Evaluate sqrt(1+epsilon)-1 without catastrophic cancellation at Earth scales.
    schwarzschild_radius = 2 * G_LOCAL * EARTH_RADIUS**2 / C**2
    epsilon = (schwarzschild_radius * HEIGHT /
               ((EARTH_RADIUS + HEIGHT) * (EARTH_RADIUS - schwarzschild_radius)))
    spherical_exact = epsilon / (np.sqrt(1 + epsilon) + 1)
    print(f"1 km: fractional rate excess = {delta:.12e}")
    print(f"Gain per 86400 s = {delta * DAY * 1e9:.9f} ns")
    print(f"Spherical Schwarzschild rate excess = {spherical_exact:.12e}")
    print(f"Constant-g excess relative to spherical exact = "
          f"{(delta / spherical_exact - 1) * 100:.6f}%")
    print(f"0.33 m at g=9.80: rate excess = {9.80 * 0.33 / C**2:.12e}")


if __name__ == "__main__":
    main()
