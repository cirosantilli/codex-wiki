"""Ideal coherent grating array and slit envelope; PNG output in working directory.

Uses existing numpy/matplotlib dependencies; tested with Python 3.14.
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


RATIO = 0.3  # wavelength / spacing: 600 nm / 2 micrometres


def array_factor(sine, count):
    # Reduce modulo one to evaluate removable singularities stably at every order.
    cycles = (np.asarray(sine) / RATIO + 0.5) % 1.0 - 0.5
    return (np.sinc(count * cycles) / np.sinc(cycles)) ** 2


def main():
    counts = (10, 40)
    for count in counts:
        width = RATIO / count
        np.testing.assert_allclose(array_factor(0.3, count), 1.0, atol=1e-14)
        np.testing.assert_allclose(array_factor(np.array([0.3 - width, 0.3 + width]), count), 0.0, atol=1e-25)
        samples = np.array([-0.913, -0.601, 0.0, 0.277, 0.3, 0.318, 0.719])
        phases = 2 * np.pi * samples / RATIO
        direct = np.abs(np.exp(1j * phases[:, None] * np.arange(count)).mean(axis=1)) ** 2
        np.testing.assert_allclose(array_factor(samples, count), direct, atol=1e-14)
        zeros = 0.3 + np.array([-width, width])
        print(f"N={count}: first zeros sin(theta)={zeros.tolist()}, one-sided width={width:g}")
        print("  zero angles (degrees):", np.degrees(np.arcsin(zeros)).tolist())

    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white", "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.6))
    fig.subplots_adjust(left=0.075, right=0.98, bottom=0.24, top=0.77, wspace=0.27)
    fig.suptitle("Finite coherent arrays: sharp orders inside a broad slit envelope", fontsize=17, y=0.97)
    fig.text(0.5, 0.89, "Normal incidence  •  λ = 600 nm  •  d = 2 μm", ha="center", fontsize=14)
    s = np.linspace(-1, 1, 24001)
    slit_width_nm = 500.0
    envelope = np.sinc(slit_width_nm * s / 600.0) ** 2
    axes[0].plot(s, array_factor(s, 40) * envelope, color="#246ba0", lw=1.1, label="N = 40, slit width a = 0.5 μm")
    axes[0].plot(s, envelope, color="#777777", ls="--", lw=1.8, label="Single-slit envelope")
    axes[0].set(xlim=(-1, 1), ylim=(0, 1.4), xlabel="sin θ", ylabel="Intensity / central intensity", title="Slit width sets the broad envelope")
    axes[0].legend(fontsize=10, loc="upper center")
    axes[0].set_xticks([-0.9, -0.6, -0.3, 0, 0.3, 0.6, 0.9])
    axes[0].grid(alpha=0.18)

    zoom = np.linspace(0.255, 0.345, 12001)
    for count, shade in zip(counts, ["#c76921", "#246ba0"]):
        width = RATIO / count
        axes[1].plot(zoom, array_factor(zoom, count), color=shade, lw=2, label=f"N = {count}: Δsin θ = {width:g}")
        axes[1].scatter([0.3 - width, 0.3 + width], [0, 0], color=shade, s=35, zorder=5)
        axes[1].annotate("", (0.3 + width, -0.09 if count == 10 else -0.18), (0.3 - width, -0.09 if count == 10 else -0.18), arrowprops={"arrowstyle": "<->", "color": shade, "lw": 1.6})
    axes[1].axvline(0.3, color="#aaaaaa", ls=":", lw=1)
    axes[1].set(xlim=(0.255, 0.345), ylim=(-0.23, 1.4), xlabel="sin θ, near first order", ylabel="Array factor / peak value", title="Four times as many slits: ¼ the width")
    axes[1].set_yticks([0, 0.25, 0.5, 0.75, 1])
    axes[1].legend(fontsize=10, loc="upper center")
    axes[1].grid(alpha=0.18)
    for ax in axes:
        for side in ["top", "right"]:
            ax.spines[side].set_visible(False)
    fig.text(0.5, 0.13, "Dots: first array zeros. Arrows: full zero-to-zero widths 0.06 and 0.015.", ha="center", fontsize=12)
    fig.text(0.5, 0.065, "Ideal uniform coherent illumination; right panel omits the slit envelope and normalizes both peaks to 1.", ha="center", fontsize=11, color="#555555")
    fig.savefig("finite-grating-interference.png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
