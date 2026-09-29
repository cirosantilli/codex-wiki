"""Original exact and asymptotic equatorial basin velocity; Python 3.14, numpy, matplotlib."""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    a, period, forcing = 1188e3, 6.4 * 86400, 1e-10
    drag, beta = 1 / period, 4 * np.pi / (period * a)
    b, length = a * np.pi / 3, a * np.deg2rad(50)
    m = np.pi / b
    lam = (beta + np.sqrt(beta**2 + 4 * drag**2 * m**2)) / (2 * drag)
    gamma = m**2 / lam
    cw = -np.expm1(-gamma * length) / -np.expm1(-(lam + gamma) * length)
    ce = -np.expm1(-lam * length) / -np.expm1(-(lam + gamma) * length)
    amplitude = -forcing / (drag * m**2)
    x = np.linspace(0, length, 1000)
    exact = amplitude * (lam * cw * np.exp(-lam * x) - gamma * ce * np.exp(gamma * (x - length)))
    delta = drag / beta
    leading = forcing / beta * (1 - length / delta * np.exp(-x / delta))
    fig, ax = plt.subplots(figsize=(8, 4.8), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    ax.plot(x / 1000, exact, color="#28639a", lw=2.4, label="Exact two-wall solution")
    ax.plot(x / 1000, leading, "--", color="#b24632", lw=1.8, label="Leading weak-drag profile")
    ax.axhline(0, color="#555555", lw=0.8)
    ax.axhline(forcing / beta, color="#318472", ls=":", lw=1.7, label="Sverdrup interior scale")
    ax.axvspan(0, delta / 1000, color="#e4edf4", alpha=0.7, zorder=-2)
    ax.annotate(f"Western peak {exact[0]:.1f} m/s", xy=(0, exact[0]), xytext=(180, -37), arrowprops={"arrowstyle": "->"}, fontsize=11)
    ax.text(760, -12, "Positive = northward\nNegative = southward", fontsize=10)
    ax.set(xlim=(0, length / 1000), ylim=(-56, 12), xlabel="Eastward distance $x$ (km)", ylabel="Northward velocity $v$ (m/s)", title="Equatorial flow: narrow return and broad interior")
    ax.legend(loc="lower right", fontsize=10)
    ax.grid(alpha=0.2)
    fig.tight_layout()
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
