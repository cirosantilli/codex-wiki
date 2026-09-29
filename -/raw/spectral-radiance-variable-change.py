"""Generate spectral-radiance-variable-change.png in CWD; Python 3.14.4.

Uses matplotlib/numpy from the repository environment. Assertions compare the
analytic integral with numerical quadrature and both corresponding half-bands.
"""

from fractions import Fraction

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    c = 299792458
    per_metre = 10**9
    # Exact rational SI inputs: each wavelength half-band has radiance 50.
    bounds = [Fraction(n, 10**9) for n in (500, 550, 600)]
    for a, b in zip(bounds[:-1], bounds[1:]):
        low, high = Fraction(c) / b, Fraction(c) / a
        exact = per_metre * c * (1 / low - 1 / high)
        assert exact == per_metre * (b - a) == 50
        frequencies = np.linspace(float(low), float(high), 20001)
        numerical = np.trapezoid(per_metre * c / frequencies**2, frequencies)
        assert np.isclose(numerical, 50, rtol=1e-10, atol=0)
    colours = ["#2166ac", "#d87911"]
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 5.0), dpi=100)
    fig.subplots_adjust(left=.085, right=.975, bottom=.33, top=.74, wspace=.28)
    left, right = axes
    left.plot([490, 500, 500, 600, 600, 610], [0, 0, 1, 1, 0, 0],
              color="0.25", lw=2)
    for a, b, colour in zip([500, 550], [550, 600], colours):
        left.fill_between([a, b], 0, 1, color=colour, alpha=.28)
        left.text((a + b) / 2, .46, "area = 50", ha="center", color=colour,
                  fontsize=12, weight="bold")
        low, high = c / (b * 1e-9) / 1e12, c / (a * 1e-9) / 1e12
        nu_thz = np.linspace(low, high, 600)
        per_thz = per_metre * c / (nu_thz * 1e12)**2 * 1e12
        right.fill_between(nu_thz, 0, per_thz, color=colour, alpha=.28)
        right.text((low + high) / 2, .46, "area = 50", ha="center", color=colour,
                   fontsize=12, weight="bold")
    low, high = c / 600e-9 / 1e12, c / 500e-9 / 1e12
    nu = np.linspace(low, high, 1000)
    density = per_metre * c / (nu * 1e12)**2 * 1e12
    right.plot(nu, density, color="0.25", lw=2)
    right.plot([490, low, low], [0, 0, density[0]], color="0.25", lw=2)
    right.plot([high, high, 610], [density[-1], 0, 0], color="0.25", lw=2)
    split = c / 550e-9 / 1e12
    right.axvline(split, color="0.5", linestyle="--", lw=1)
    left.axvline(550, color="0.5", linestyle="--", lw=1)
    left.set(xlim=(490, 610), ylim=(0, 1.4), xticks=[500, 550, 600],
             xlabel=r"Wavelength $\lambda$ (nm)",
             ylabel=r"$L_\lambda$  [W/(m$^2$ sr nm)]")
    right.set(xlim=(490, 610), ylim=(0, 1.4), xticks=[500, 550, 600],
              xlabel=r"Frequency $\nu$ (THz)",
              ylabel=r"$L_\nu$  [W/(m$^2$ sr THz)]")
    left.set_title("Flat per nanometre", fontsize=13, pad=14)
    right.set_title(r"Per terahertz: $L_\nu\propto1/\nu^2$", fontsize=13, pad=14)
    right.text(low + 2, 1.26, "600 nm", fontsize=10)
    right.text(high - 2, .93, "500 nm", ha="right", fontsize=10)
    for ax in axes:
        ax.set_yticks([0, .5, 1, 1.4])
        ax.grid(alpha=.15)
    fig.suptitle("One spectral band, two densities, the same integrated radiance", fontsize=15, y=.97)
    fig.text(.5, .855, r"$\nu=c/\lambda$: reverse the bounds and include $|d\lambda/d\nu|=c/\nu^2$",
             ha="center", fontsize=12)
    fig.text(.5, .16, r"Each coloured area = 50 W/(m$^2$ sr); total = 100 W/(m$^2$ sr)",
             ha="center", fontsize=12)
    fig.text(.5, .07, "Equal 50 nm widths become unequal frequency widths:\n"
             "500–550 nm → 54.508 THz (blue); 550–600 nm → 45.423 THz (orange)",
             ha="center", fontsize=11, linespacing=1.5)
    fig.savefig("spectral-radiance-variable-change.png", facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Verified both exact half-band integrals: 50; total: 100.\n"
          f"Frequency bounds (THz): {low:.12f}, {high:.12f}.\n"
          f"Endpoint densities per Hz: {density[0] / 1e12:.12g}, {density[-1] / 1e12:.12g}.")


if __name__ == "__main__":
    main()
