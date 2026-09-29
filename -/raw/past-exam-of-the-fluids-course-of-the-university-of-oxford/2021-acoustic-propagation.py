"""Original acoustic pulse and harmonic profiles; Python 3.14, numpy/matplotlib."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    x = np.linspace(-4, 4, 1201)
    initial = np.exp(-x*x/0.3)
    t = 1.8
    right = np.exp(-(x-t)**2/0.3)/2
    left = np.exp(-(x+t)**2/0.3)/2
    fig, axes = plt.subplots(3, 1, figsize=(9, 8), layout="constrained")
    ax = axes[0]
    ax.plot(x, initial, color="#126782", lw=2.5, label="initial excess pressure / peak")
    for pos in (-0.65, 0.65):
        acceleration = 1 if pos > 0 else -1
        ax.annotate("", xy=(pos+acceleration*0.7, 0.4), xytext=(pos, 0.4),
                    arrowprops={"arrowstyle": "->", "lw": 2.2, "color": "#d16b18"})
    ax.text(0, 0.62, "compression", ha="center")
    ax.text(2.2, 0.56, "outward acceleration\nfrom the pressure gradient", ha="center", fontsize=10)
    ax.set_title("A localized compression initially released from rest", loc="left")
    ax.set_ylim(-0.08, 1.2)
    ax.legend(loc="upper right", fontsize=9)
    ax = axes[1]
    ax.plot(x, right+left, color="#126782", lw=2.5, label=r"$p_1/(c_0^2\rho_{\rm peak})$ at $c_0t=1.8$")
    ax.plot(x, right-left, color="#d16b18", lw=2, ls="--", label=r"$v_1/(c_0\rho_{\rm peak}/\rho_0)$")
    ax.annotate("", xy=(-2.5, 0.65), xytext=(-1.5, 0.65), arrowprops={"arrowstyle": "->", "lw": 1.7})
    ax.annotate("", xy=(2.5, 0.65), xytext=(1.5, 0.65), arrowprops={"arrowstyle": "->", "lw": 1.7})
    ax.set_title("Later: two outward pulses, each with half the initial pressure peak", loc="left")
    ax.set_ylim(-0.65, 1.0)
    ax.legend(loc="upper center", fontsize=9)
    ax = axes[2]
    xx = np.linspace(-2.05, 2.05, 1601)
    density = np.cos(2*np.pi*xx)
    ax.plot(xx, density, color="#126782", lw=3, label=r"$\rho_1/(\rho_0 A)=p_1/(\rho_0c_0^2 A)$")
    # Separate the two source-free sides so no artificial connecting segment appears.
    for mask in (xx < 0, xx > 0):
        ax.plot(xx[mask], np.sign(xx[mask])*density[mask], color="#d16b18", lw=1.8,
                ls="--", label=r"$v_1/(c_0 A)$" if xx[mask][0] < 0 else None)
    ax.axvline(0, color="0.6", ls=":", lw=1)
    ax.set_title(r"Harmonic source at rest: snapshot at $\omega t=2n\pi$ (part 2c)", loc="left")
    ax.set_xlabel(r"$x/\lambda_0$")
    ax.set_ylim(-1.45, 1.65)
    ax.legend(loc="upper center", ncol=2, fontsize=9)
    for ax in axes:
        ax.axhline(0, color="0.75", lw=0.7)
        ax.grid(alpha=0.15)
    axes[0].set_xlabel("distance (arbitrary units)")
    axes[1].set_xlabel("distance (same units)")
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                dpi=125, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
