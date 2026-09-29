"""Write ice-albedo-feedback-equilibria.png in CWD.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Uses a stipulated smooth Bond albedo, not an empirical freezing relation.
Bisection computes roots and fold points without additional dependencies.
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

SOLAR = 1360.0
SIGMA = 5.670374419e-8


def albedo(t):
    return 0.3 + 0.3 / (1 + np.exp((np.asarray(t) - 240.0) / 3.0))


def albedo_prime(t):
    # Equivalent expression avoiding an exponential squared in the denominator.
    fraction = (albedo(t) - 0.3) / 0.3
    return -0.1 * fraction * (1 - fraction)


def net_heating(t, solar=SOLAR):
    return solar * (1 - albedo(t)) / 4 - SIGMA * np.asarray(t)**4


def heating_prime(t, solar=SOLAR):
    return -solar * albedo_prime(t) / 4 - 4 * SIGMA * np.asarray(t)**3


def bisect(fn, lo, hi):
    flo, fhi = float(fn(lo)), float(fn(hi))
    if flo * fhi >= 0:
        raise ValueError("Bisection requires opposite endpoint signs")
    for _ in range(70):
        mid = (lo + hi) / 2
        fmid = float(fn(mid))
        if fmid == 0:
            return mid
        if flo * fmid < 0:
            hi = mid
        else:
            lo, flo = mid, fmid
    return (lo + hi) / 2


def equilibrium_solar(t):
    return 4 * SIGMA * np.asarray(t)**4 / (1 - albedo(t))


def main():
    roots = np.array([bisect(net_heating, a, b)
                      for a, b in [(220, 223), (238, 241), (253, 255)]])
    slopes = heating_prime(roots)
    assert np.max(np.abs(net_heating(roots))) < 1e-10
    assert np.allclose(roots, [221.383730421, 240.210834395, 254.301046552], atol=1e-8)
    assert np.array_equal(slopes < 0, [True, False, True])
    fold_condition = lambda t: 4 * (1 - albedo(t)) + t * albedo_prime(t)
    folds = np.array([bisect(fold_condition, 225, 240),
                      bisect(fold_condition, 240, 255)])
    limits = equilibrium_solar(folds)
    assert np.allclose(limits, [1567.800621130, 1250.481110006], atol=1e-7)
    assert np.max(np.abs(heating_prime(folds, limits))) < 1e-10

    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, (left, right) = plt.subplots(1, 2, figsize=(11.4, 5.8), dpi=100)
    fig.subplots_adjust(left=0.08, right=0.98, bottom=0.25, top=0.79, wspace=0.26)
    blue, red = "#216a9a", "#b13937"
    t = np.linspace(210, 266, 1001)
    left.axhspan(0, 48, color="#fff4d9", zorder=0)
    left.axhspan(-55, 0, color="#eaf3fa", zorder=0)
    left.plot(t, net_heating(t), color="0.2", lw=2)
    left.plot(t, net_heating(t, solar=0) + 238, "--", color="#bfa456", lw=1.2,
              label="fixed α = 0.30")
    left.plot(t, net_heating(t, solar=0) + 136, ":", color="#8caac0", lw=1.4,
              label="fixed α = 0.60")
    left.axhline(0, color="0.4", lw=1)
    for root, slope in zip(roots, slopes):
        stable = slope < 0
        left.scatter(root, 0, s=65, facecolors=blue if stable else "white",
                     edgecolors=blue if stable else red, linewidths=2, zorder=5)
    for start, end in [(213, 218), (232, 226), (245, 250), (264, 259)]:
        left.annotate("", xy=(end, 0), xytext=(start, 0),
                      arrowprops={"arrowstyle": "->", "lw": 2, "color": blue})
    for root, label, y, va in [(roots[0], "221.384 K\nstable", 10, "bottom"),
                               (roots[1], "240.211 K\nunstable", -15, "top"),
                               (roots[2], "254.301 K\nstable", 10, "bottom")]:
        left.text(root, y, label, ha="center", va=va, fontsize=10,
                  color=red if "unstable" in label else blue)
    left.text(212, 43, "F > 0: warming", color="#805811", fontsize=10)
    left.text(212, -49, "F < 0: cooling", color=blue, fontsize=10)
    left.set(xlim=(210, 267), ylim=(-55, 48), xlabel="Temperature T (K)",
             ylabel=r"Net heating F (W m$^{-2}$)")
    left.set_title("Fixed S = 1360 W m⁻²", pad=14, fontsize=13)
    left.legend(loc="upper center", bbox_to_anchor=(0.45, -0.23),
                ncol=2, frameon=False, fontsize=10)

    for lo, hi, stable in [(205, folds[0], True),
                           (folds[0], folds[1], False),
                           (folds[1], 275, True)]:
        temp = np.linspace(lo, hi, 600)
        right.plot(equilibrium_solar(temp), temp, "-" if stable else "--",
                   lw=2.3, color=blue if stable else red)
    right.axvspan(limits[1], limits[0], color="#f1f1f1", zorder=0)
    right.axvline(SOLAR, color="0.45", ls=":", lw=1.4)
    right.text(SOLAR-8, 269, "S = 1360", ha="right", va="top", fontsize=10)
    for root, slope in zip(roots, slopes):
        stable = slope < 0
        right.scatter(SOLAR, root, s=55, facecolors=blue if stable else "white",
                      edgecolors=blue if stable else red, linewidths=2, zorder=5)
    for temp, solar in zip(folds, limits):
        right.scatter(solar, temp, color="0.2", s=25, zorder=5)
    right.text(limits[0]+15, folds[0]-3, "cold branch ends\nS ≈ 1567.801", fontsize=10)
    right.text(limits[1]-15, folds[1]+5, "warm branch ends\nS ≈ 1250.481",
               ha="right", fontsize=10)
    # Vertical arrows indicate the different transition directions at static folds.
    warm_landing = bisect(lambda t: net_heating(t, limits[0]), 255, 280)
    cold_landing = bisect(lambda t: net_heating(t, limits[1]), 205, 225)
    right.annotate("", xy=(limits[0], warm_landing-0.6),
                   xytext=(limits[0], folds[0]+0.6),
                   arrowprops={"arrowstyle": "->", "color": "#a26e00", "lw": 1.8})
    right.annotate("", xy=(limits[1], cold_landing+0.6),
                   xytext=(limits[1], folds[1]-0.6),
                   arrowprops={"arrowstyle": "->", "color": "#a26e00", "lw": 1.8})
    right.set(xlim=(950, 1900), ylim=(207, 271),
              xlabel=r"Illumination S (W m$^{-2}$)", ylabel="Equilibrium temperature T (K)")
    right.set_title("Slow warming and cooling switch at different S", pad=14, fontsize=12)
    right.text(0.5, -0.30, "Solid: stable    Dashed: unstable    Arrows: fold transitions",
               transform=right.transAxes, ha="center", fontsize=10)
    fig.suptitle("A smooth ice–albedo feedback can produce two stable states", y=0.96, fontsize=15)
    fig.text(0.5, 0.87, r"$\alpha(T)=0.3+0.3/[1+\exp((T-240\ \mathrm{K})/(3\ \mathrm{K}))]$",
             ha="center", fontsize=13)
    fig.text(0.5, 0.04,
             "Illustrative model • no atmosphere • uniform T • thermal emissivity = 1 • not a modern climate forecast",
             ha="center", fontsize=10.5, color="0.3")
    fig.savefig("ice-albedo-feedback-equilibria.png", facecolor="white", transparent=False)
    plt.close(fig)
    print("Roots (K):", roots.tolist())
    print("F′ (W m⁻² K⁻¹):", slopes.tolist())
    print("Fold points (T, S):", list(zip(folds.tolist(), limits.tolist())))


if __name__ == "__main__":
    main()
