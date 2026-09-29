"""Original normal-metal gamma + beta T² example; no experimental data.

Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Run from _media.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    gamma, beta, sigma = 7e-4, 4e-4, 2e-5
    temperature = np.array([1., 2., 3.])
    x = temperature ** 2
    y = gamma + beta * x
    design = np.column_stack([np.ones(3), x])
    fit = np.linalg.lstsq(design, y, rcond=None)[0]
    covariance = sigma ** 2 * np.linalg.inv(design.T @ design)
    theta = (12 * np.pi ** 4 * 8.31446261815324 / (5 * beta)) ** (1 / 3)
    assert np.allclose(fit, [gamma, beta], rtol=1e-12)
    assert np.isclose(theta, 169.3798102764744)
    assert np.allclose(np.sqrt(np.diag(covariance)), [2e-5, 3.499271061118826e-6])
    fig, (ax, detail) = plt.subplots(1, 2, figsize=(10.5, 4.8),
                                    gridspec_kw={"width_ratios": [1.65, 1]})
    fig.suptitle("Test the lattice T³ term without losing the electrons", fontsize=15)
    xx = np.linspace(1, 9, 300)
    extrap = np.linspace(0, 1, 50)
    ax.plot(xx, gamma + beta * xx, color="#0369a1", lw=2, label="Total: γ + βT²")
    ax.plot(extrap, gamma + beta * extrap, color="#0369a1", ls="--", lw=1.5)
    ax.plot(xx, beta * xx, color="#b45309", lw=2, label="Lattice only: βT²")
    ax.plot(extrap, beta * extrap, color="#b45309", ls="--", lw=1.5)
    ax.axhline(gamma, color="#7c3aed", ls=":", lw=2, label="Electrons only: γ")
    ax.errorbar(x, y, yerr=sigma, fmt="o", color="#0f172a", capsize=4,
                label="Constructed values, assigned 1σ")
    ax.fill_between(xx, beta * xx, gamma + beta * xx, color="#ede9fe", alpha=.7)
    ax.annotate("Electronic intercept\nγ = 0.000700 J mol⁻¹ K⁻²", xy=(0, gamma),
                xytext=(.7, .0027), fontsize=10,
                arrowprops={"arrowstyle": "->", "color": "#7c3aed"})
    ax.axvspan(0, 1, color="#e2e8f0", alpha=.4)
    ax.set(xlabel="Squared temperature T² (K²)", ylabel="Molar Cₚ,ₘ/T (J mol⁻¹ K⁻²)",
           xlim=(0, 9.5), ylim=(0, .0056))
    ax.ticklabel_format(axis="y", style="plain", useOffset=False)
    ax.legend(loc="upper left", fontsize=9, frameon=False)
    ax.grid(alpha=.18)
    detail.axis("off")
    detail.text(0, .98, "Stipulated normal metal", fontsize=13, weight="bold", va="top")
    detail.text(0, .88, "Fit domain: 1 ≤ T ≤ 3 K\nT ≪ ΘD; no superconducting transition\nNo magnetic or Schottky term", linespacing=1.65, fontsize=10, va="top")
    detail.text(0, .59, "Slope β = 0.000400 J mol⁻¹ K⁻⁴\nΘD = 169.38 K (monatomic model)\nElectrons = lattice at T = 1.323 K", linespacing=1.65, fontsize=10, va="top")
    detail.text(0, .34, "Dashed segment: extrapolation to T = 0\nNo measurement at absolute zero", linespacing=1.65, fontsize=10, va="top")
    detail.text(0, .16, "Error bars: u(Cₚ,ₘ/T) = 0.000020\nJ mol⁻¹ K⁻²; temperature error neglected", linespacing=1.65, fontsize=10, va="top")
    fig.text(.5, .025, "Original constructed example, not a fit to the gold experiment  •  "
             "A straight line tests the sum of two distinct contributions", ha="center", fontsize=10)
    fig.tight_layout(rect=(0, .065, 1, .94))
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=150, facecolor="white")
    plt.close(fig)
    print(f"fit={fit.tolist()}; standard_uncertainties={np.sqrt(np.diag(covariance)).tolist()}; theta={theta:.10g} K")


if __name__ == "__main__":
    main()
