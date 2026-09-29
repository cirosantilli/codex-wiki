"""Local harmonic well, force and deterministic overdamped relaxation.

Write optical-trap-restoring-force.png to the working directory.
Uses the repository numpy/matplotlib dependencies; tested with Python 3.14.
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    q = np.linspace(-1.5, 1.5, 601)
    s = np.linspace(0, 4, 1601)
    stiffnesses = (1.0, 2.0, 4.0)
    colors = ("#2469a0", "#c76720", "#27805a")
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 3, figsize=(11.6, 4.9))
    fig.subplots_adjust(left=0.065, right=0.98, bottom=0.30, top=0.77, wspace=0.38)
    fig.suptitle("An optical trap acts like a spring near equilibrium", fontsize=17, y=0.97)
    fig.text(0.5, 0.88, "Local quadratic model • fixed drag • relative stiffness κ = 1, 2, 4", ha="center", fontsize=12)
    for kappa, color in zip(stiffnesses, colors):
        well = 0.5 * kappa * q**2
        force = -kappa * q
        position = np.exp(-kappa * s)
        # Independently differentiate sampled energy and trajectory in their interiors.
        np.testing.assert_allclose(-np.gradient(well, q)[1:-1], force[1:-1], atol=1e-11)
        np.testing.assert_allclose(np.gradient(position, s)[1:-1], -kappa * position[1:-1], rtol=2e-5)
        assert np.all(q * force <= 0)
        np.testing.assert_allclose(np.exp(-kappa * (1 / kappa)), np.exp(-1), atol=1e-15)
        axes[0].plot(q, well, color=color, lw=2.4, label=f"κ = {kappa:g}")
        axes[1].plot(q, force, color=color, lw=2.4)
        axes[2].plot(s, position, color=color, lw=2.4)
        axes[2].plot(1 / kappa, np.exp(-1), "o", color=color, ms=6)
    for ax in axes:
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(alpha=0.18)
    axes[0].set(title=r"Potential well: $U=\frac{1}{2}kx^2$", xlabel=r"Displacement $q=x/\ell$", ylabel=r"$U/(k_0\ell^2)$", ylim=(0, 4.7))
    axes[0].legend(frameon=False, fontsize=10)
    axes[0].axvline(0, color="#777777", lw=0.8, ls=":")
    axes[1].set(title=r"Restoring force: $F=-kx$", xlabel=r"Displacement $q=x/\ell$", ylabel=r"$F/(k_0\ell)$", ylim=(-6.5, 6.5))
    axes[1].axhline(0, color="#777777", lw=0.8)
    axes[1].axvline(0, color="#777777", lw=0.8, ls=":")
    axes[2].set(title=r"Relaxation: $\zeta\dot{x}=-kx$", xlabel=r"Time $s=t/(\zeta/k_0)$", ylabel=r"$x(t)/x(0)$", xlim=(0, 4), ylim=(0, 1.04))
    axes[2].axhline(np.exp(-1), color="#777777", lw=0.8, ls=":")
    fig.text(0.5, 0.115, "Stronger stiffness: steeper well, stronger restoring force, shorter relaxation time τ = ζ/k.", ha="center", fontsize=11)
    fig.text(0.5, 0.05, "Dots mark one relaxation time (x/x₀ = 1/e). Deterministic curves omit Brownian fluctuations.", ha="center", fontsize=10, color="#555555")
    fig.savefig("optical-trap-restoring-force.png", dpi=110, facecolor="white", transparent=False)
    plt.close(fig)
    drag = 6 * np.pi * 1e-3 * 0.5e-6
    print(f"Restoring force / relaxation checks passed; example ζ={drag:.9g} N s/m, τ={drag/1e-5:.9g} s")


if __name__ == "__main__":
    main()
