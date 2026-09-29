"""Original Rindler null rays and accelerated reception; write PNG to cwd.

Tested with Python 3.14, NumPy and Matplotlib; see root pyproject.toml.
Inertial axes use the initial acceleration radius R=c^2/a. All light signals
are emitted at T=0; the observer is initially at rest at X=R.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.6), facecolor="white")
    time = np.linspace(0, 3.5, 1200)
    ax = axes[0]
    for sign, color in ((1, "#1768ab"), (-1, "#bd6426")):
        for count, initial in enumerate((.12, .3, .65, 1.4, -.12, -.3, -.65, -1.4)):
            position = initial * np.exp(sign*time)
            inside = abs(position) <= 2.05
            label = rf"$x=C e^{{{'+' if sign == 1 else '-'}\alpha t}}$" if count == 0 else None
            ax.plot(position[inside], time[inside], lw=1.25, color=color, label=label)
    ax.axvline(0, color="#697781", ls="--", lw=1)
    ax.set(xlim=(-2.05, 2.05), ylim=(0, 3.5), xlabel=r"$x/x_{\rm ref}$", ylabel=r"$\alpha t$")
    ax.set_title("Null paths in the accelerated chart", fontsize=11)
    ax.legend(frameon=False, fontsize=10, loc="upper right")

    ax = axes[1]
    rapidity = np.linspace(0, 2.05, 700)
    ax.plot(np.cosh(rapidity), np.sinh(rapidity), color="#1768ab", lw=2.1,
            label="Accelerated observer")
    inertial_time = np.linspace(0, 3.9, 700)
    for separation, color, style, label in (
            (.4, "#28744b", "-", r"$d=0.4R$: received"),
            (1., "#697781", "--", r"$d=R$: limiting ray"),
            (1.3, "#bd6426", "-", r"$d=1.3R$: never received")):
        initial = 1-separation
        ax.plot(initial + inertial_time, inertial_time, color=color, ls=style, lw=1.4, label=label)
        ax.scatter([initial], [0], s=22, color=color, zorder=4)
    eta_receive = -np.log(.6)
    receiver_x = np.cosh(eta_receive)
    receiver_t = np.sinh(eta_receive)
    ax.scatter([receiver_x], [receiver_t], s=35, color="#28744b", zorder=5)
    ax.annotate("Reception", xy=(receiver_x, receiver_t), xytext=(1.45, .45),
                arrowprops={"arrowstyle": "->", "color": "#28744b"}, fontsize=9)
    ax.scatter([1], [0], s=30, color="#1768ab", zorder=5)
    ax.set(xlim=(-.45, 4.05), ylim=(-.07, 3.9), xlabel=r"$X/R$", ylabel=r"$cT/R$", aspect="equal")
    ax.set_title("Straight light rays in an inertial frame", fontsize=11)
    ax.legend(frameon=False, fontsize=8.7, loc="upper left")
    for ax in axes:
        ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout(w_pad=2)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=125, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
