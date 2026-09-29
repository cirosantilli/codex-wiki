"""Original hybridised-band and fixed-density Fermi-radius plots; save to cwd.

Tested with Python 3.14, NumPy and Matplotlib; see root pyproject.toml.
The Fermi radii use two positive finite band curvatures and spin degeneracy two.
"""

from pathlib import Path
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def radii_at_fixed_density(coupling, light=1.0, heavy=0.05):
    offset = light - heavy

    def radii(mu):
        center = (light + heavy) * mu - light * offset
        split = np.sqrt(((light - heavy) * mu - light * offset)**2
                        + 4 * light * heavy * coupling**2)
        squared = np.array([center + split, center - split]) / (2 * light * heavy)
        return np.sqrt(np.maximum(squared, 0))

    lo = (offset - np.sqrt(offset**2 + 4 * coupling**2)) / 2 - 1
    hi = 5 + coupling
    for _ in range(90):
        mu = (lo + hi) / 2
        if np.sum(radii(mu)**3) < 2:
            lo = mu
        else:
            hi = mu
    return radii((lo + hi) / 2)


def main():
    fig, axes = plt.subplots(2, 2, figsize=(9.5, 6.8), facecolor="white")
    momentum = np.linspace(-1.65, 1.65, 1400)
    parabola = momentum**2
    for ax, alpha, label in zip(axes.flat, (0, 0.12, 1.0),
                               ("Uncoupled bands", "Weak hybridisation", "Strong hybridisation")):
        split = np.sqrt((parabola - 1)**2 + 4 * alpha**2)
        lower, upper = (parabola + 1 - split) / 2, (parabola + 1 + split) / 2
        ax.plot(momentum, parabola, color="#a5adb5", lw=1, ls="--")
        ax.axhline(1, color="#a5adb5", lw=1, ls="--")
        ax.plot(momentum, lower, color="#1768ab", lw=2, label=r"$E_-$")
        ax.plot(momentum, upper, color="#bf6225", lw=2, label=r"$E_+$")
        for cross in (-1, 1):
            ax.axvline(cross, color="#c8ced4", lw=0.6, ls=":")
        ax.set(xlim=(-1.65, 1.65), ylim=(-0.8, 3.4), xlabel=r"$k/k_c$", ylabel=r"$E/E_{\rm fl}$")
        ax.set_title(label + rf" ($\alpha/E_{{\rm fl}}={alpha:g}$)", fontsize=10)
        if alpha:
            upper_min = (1 + np.sqrt(1 + 4 * alpha**2)) / 2
            ax.axhspan(1, upper_min, color="#84b68a", alpha=0.20)
        ax.legend(frameon=False, fontsize=9, loc="upper center")

    ax = axes[1, 1]
    alphas = np.linspace(0, 0.45, 320)
    radii = np.array([radii_at_fixed_density(alpha) for alpha in alphas])
    ax.plot(alphas / 0.95, radii[:, 0], color="#1768ab", lw=2, label="Outer Fermi radius")
    ax.plot(alphas / 0.95, radii[:, 1], color="#bf6225", lw=2, label="Inner Fermi radius")
    ax.axhline(2**(1/3), color="#46654b", ls="--", lw=1,
               label=r"Single-pocket limit $2^{1/3}k_0$")
    ax.set(xlim=(0, 0.45 / 0.95), ylim=(-0.04, 1.42),
           xlabel=r"$\alpha/C$", ylabel=r"Fermi radius $k_F/k_0$")
    ax.set_title(r"Fixed density, finite mass ratio $m_h/m_\ell=20$", fontsize=10)
    ax.legend(frameon=False, fontsize=8.4, loc="lower right")
    for ax in axes.flat:
        ax.set_facecolor("white")
        ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout(h_pad=1.8, w_pad=1.8)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=125, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
