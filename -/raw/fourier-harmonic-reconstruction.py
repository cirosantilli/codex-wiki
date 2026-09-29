"""Render a finite Fourier expansion and its real coefficients to cwd."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(-np.pi, np.pi, 2001)
    constant = np.full_like(x, .5)
    first = np.cos(x)
    second = .5 * np.sin(2*x)
    signal = constant + first + second
    # Full-period orthogonality recovers the real coefficients independently.
    coefficients_a = [np.trapezoid(signal * np.cos(n*x), x) / np.pi for n in range(5)]
    coefficients_b = [np.trapezoid(signal * np.sin(n*x), x) / np.pi for n in range(1, 5)]
    assert np.allclose(coefficients_a, [1, 1, 0, 0, 0], atol=1e-12)
    assert np.allclose(coefficients_b, [0, .5, 0, 0], atol=1e-12)
    reference = np.pi/4
    value = .5 + np.cos(reference) + .5*np.sin(2*reference)
    assert np.isclose(value, 1 + 1/np.sqrt(2))
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    fig = plt.figure(figsize=(10.8, 6.9), dpi=120, facecolor="white")
    grid = fig.add_gridspec(3, 2, width_ratios=[1, 1.35], wspace=.28, hspace=.43)
    colors = ["#7a698f", "#216ba0", "#bd7724"]
    titles = [r"Mean component: $a_0/2=1/2$", r"First cosine: $a_1\cos x=\cos x$",
              r"Second sine: $b_2\sin(2x)=\frac{1}{2}\sin(2x)$"]
    contributions = [.5, np.cos(reference), .5*np.sin(2*reference)]
    for row, (data, color, title, contribution) in enumerate(zip(
            [constant, first, second], colors, titles, contributions)):
        ax = fig.add_subplot(grid[row, 0])
        ax.plot(x, data, lw=2.8, color=color)
        ax.axvline(reference, color="#9da9b2", lw=1, linestyle=":")
        ax.scatter([reference], [contribution], color=color, s=40, zorder=4)
        ax.set(xlim=(-np.pi, np.pi), ylim=(-1.15, 1.15), title=title)
        ax.set_xticks([-np.pi, 0, np.pi], ["−π", "0", "π"])
        if row == 2: ax.set_xlabel("Angular coordinate x (radians)")
        ax.grid(color="#e6eaed")
        ax.spines[["top", "right"]].set_visible(False)
    summed = fig.add_subplot(grid[:, 1])
    summed.plot(x, signal, color="#278064", lw=3, label="Sum of all three components")
    summed.axvline(reference, color="#9da9b2", lw=1, linestyle=":")
    summed.scatter([reference], [value], color="#278064", s=65, zorder=4)
    summed.annotate(r"$x=\pi/4$" + "\n" + r"$f(x)=1+1/\sqrt{2}$" + "\n≈ 1.70710678",
                    xy=(reference, value), xytext=(-2.75, 1.60), fontsize=12,
                    arrowprops={"arrowstyle": "->", "color": "#278064"},
                    bbox={"facecolor": "white", "edgecolor": "none", "alpha": .9})
    summed.set(xlim=(-np.pi, np.pi), ylim=(-.95, 2.05), xlabel="Angular coordinate x (radians)",
               ylabel="Sum", title="Exact finite reconstruction")
    summed.set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], ["−π", "−π/2", "0", "π/2", "π"])
    summed.grid(color="#e6eaed")
    summed.spines[["top", "right"]].set_visible(False)
    fig.suptitle("A Fourier expansion separates simple oscillating patterns", fontsize=16, y=.98)
    fig.text(.5, .032, "Real coefficients: a₀ = 1, a₁ = 1, b₂ = ½; every other coefficient is zero",
             ha="center", fontsize=12)
    fig.subplots_adjust(left=.07, right=.97, top=.86, bottom=.13)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
