"""Sinusoidal phase-screen diffraction; Python 3.14, NumPy and Matplotlib.

Write only paper-80-phase-screen.png in the caller's current directory.
The caller may set MPLBACKEND and MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def main():
    n = 4096
    z = np.linspace(-np.pi, np.pi, n, endpoint=False)
    frequencies = 2 * np.pi * np.fft.fftfreq(n, d=2 * np.pi / n)
    initial_spectrum = np.fft.fft(np.exp(1j * np.cos(z)))
    fig, axes = plt.subplots(1, 2, figsize=(11.52, 4.8), dpi=100,
                             layout="constrained", facecolor="white")
    axes[0].plot(z, np.cos(z), color="#294c82", linewidth=2.4)
    axes[0].axhline(0, color="0.65", linewidth=0.8)
    axes[0].set(title="Unit-amplitude phase screen", ylabel=r"Phase $\phi(z)=\cos z$")
    axes[0].text(0, -0.55, "Negative phase curvature\nnear z = 0 causes brightening",
                 ha="center", va="center", fontsize=10,
                 bbox={"facecolor": "white", "edgecolor": "0.8", "alpha": 1})
    for tau, color in [(0.1, "#294c82"), (0.2, "#bd4d28")]:
        envelope = np.fft.ifft(initial_spectrum * np.exp(-0.5j * frequencies**2 * tau))
        exact_intensity = np.abs(envelope)**2
        approximation = 1 + tau * np.cos(z) + tau**2 * np.cos(2 * z)
        axes[1].plot(z, exact_intensity, color=color, linewidth=2,
                     label=rf"Exact paraxial, $x/k={tau}$")
        axes[1].plot(z, approximation, color=color, linestyle="--", linewidth=1.5,
                     label=rf"Quadratic, $x/k={tau}$")
    axes[1].axhline(1, color="0.6", linewidth=0.8)
    axes[1].set(title="Phase-to-intensity conversion", ylabel=r"Intensity $|E|^2$")
    axes[1].legend(loc="lower center", fontsize=9, framealpha=1)
    for ax in axes:
        ax.set(xlabel=r"Transverse coordinate $z$", xlim=(-np.pi, np.pi))
        ax.set_xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
                      [r"$-\pi$", r"$-\pi/2$", "0", r"$\pi/2$", r"$\pi$"])
        ax.set_facecolor("white")
        ax.grid(alpha=0.2)
    fig.savefig(Path.cwd() / "paper-80-phase-screen.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
