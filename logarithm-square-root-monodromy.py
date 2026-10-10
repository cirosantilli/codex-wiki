"""Compare a source loop with its continued square-root and logarithm values.

Tested with Python 3.14, NumPy 2.3.5, and Matplotlib 3.10.7.
Write an opaque white same-basename PNG in the current working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    t = np.linspace(0, 2 * np.pi, 4097)
    z, w, logarithm = np.exp(1j * t), np.exp(0.5j * t), 1j * t
    assert np.max(np.abs(w**2 - z)) < 1e-14
    assert np.max(np.abs(np.exp(logarithm) - z)) < 1e-14
    assert abs(z[-1] - z[0]) < 1e-14
    assert abs(w[-1] + w[0]) < 1e-14
    period = np.trapezoid(1j * z / z, t)
    assert abs(period - 2j * np.pi) < 1e-13
    assert abs(logarithm[-1] - logarithm[0] - period) < 1e-13
    twice = np.exp(0.5j * 4 * np.pi)
    assert abs(twice - 1) < 1e-14

    blue, green, red, gray = "#186a9a", "#237b53", "#b63a40", "#687682"
    fig, axes = plt.subplots(1, 3, figsize=(10.4, 4.8), dpi=130)
    fig.patch.set_facecolor("white")
    for ax in axes:
        ax.set_facecolor("white")
        ax.axhline(0, color="0.78", lw=0.8)
        ax.axvline(0, color="0.78", lw=0.8)
        ax.spines[["top", "right"]].set_visible(False)
    for ax, values, title in zip(
        axes, [z, w, logarithm],
        [r"Source: $z(t)=e^{it}$", r"Lift: $w(t)=e^{it/2}$", r"Lift: $L(t)=it$"],
    ):
        ax.plot(values.real, values.imag, color=blue, lw=2.5)
        for fraction in [0.20, 0.57, 0.83]:
            k = int(fraction * (len(t) - 1))
            j = k + 90
            ax.annotate("", (values[j].real, values[j].imag),
                        (values[k].real, values[k].imag),
                        arrowprops={"arrowstyle": "-|>", "color": blue, "lw": 2})
        ax.set_title(title, fontsize=12, pad=12)
        ax.set_xlabel("Real part")
        ax.set_ylabel("Imaginary part")
        ax.scatter([values[0].real], [values[0].imag], color=green, s=65, zorder=5)

    axes[0].scatter([1], [0], facecolors="none", edgecolors=red, s=150, lw=2, zorder=6)
    axes[0].scatter([0], [0], marker="x", color=gray, s=45, zorder=5)
    axes[0].annotate("Start = end\n$z=1$", (1, 0), (0.35, -0.75), fontsize=10,
                     arrowprops={"arrowstyle": "->", "color": gray})
    for ax in axes[:2]:
        ax.set(xlim=(-1.45, 1.45), ylim=(-1.15, 1.4))
        ax.set_aspect("equal")
        ax.set_xticks([-1, 0, 1])
        ax.set_yticks([-1, 0, 1])
    axes[1].scatter([-1], [0], color=red, s=65, zorder=5)
    axes[1].text(0.7, -0.35, "Start: 1", color=green, ha="center", fontsize=10)
    axes[1].text(-0.75, -0.35, "End: −1", color=red, ha="center", fontsize=10)
    axes[2].scatter([0], [2 * np.pi], color=red, s=65, zorder=5)
    axes[2].text(0.15, 0.3, "Start: 0", color=green, fontsize=10)
    axes[2].text(0.15, 2 * np.pi - 0.45, r"End: $2\pi i$", color=red, fontsize=10)
    axes[2].set(xlim=(-0.65, 1.3), ylim=(-0.6, 7.1), xticks=[0, 1],
                yticks=[0, np.pi, 2 * np.pi], yticklabels=["0", r"$\pi$", r"$2\pi$"])
    captions = ["Closed source loop", "Different endpoints: sign changes",
                r"Different endpoints: add $2\pi i$"]
    for ax, caption in zip(axes, captions):
        ax.text(0.5, -0.28, caption, transform=ax.transAxes,
                ha="center", fontsize=10, color="0.25")
    fig.suptitle(r"One counterclockwise turn, $0\leq t\leq2\pi$: follow continuation, not a principal-value reset",
                 fontsize=12.5, y=0.98)
    fig.subplots_adjust(left=0.06, right=0.97, bottom=0.26, top=0.81, wspace=0.53)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Verified both lifts on {len(t)} samples; endpoints z={z[-1]:.12g}, "
          f"sqrt={w[-1]:.12g}, log={logarithm[-1]:.12g}; loop integral={period:.12g}.")


if __name__ == "__main__":
    main()
