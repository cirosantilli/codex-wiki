"""Generate linear-drag-terminal-velocity.png in the working directory.

Uses only the repository's NumPy and Matplotlib dependencies.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media: python ../linear-drag-terminal-velocity.py
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    mass, friction, gravity = 1.0, 2.0, 9.8
    tau, terminal = mass / friction, mass * gravity / friction
    t = np.linspace(0, 3, 601)
    velocity = terminal * (1 - np.exp(-t / tau))
    acceleration = gravity * np.exp(-t / tau)
    plt.rcParams.update({"font.size": 12, "savefig.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.5), facecolor="white")
    fig.subplots_adjust(left=0.08, right=0.97, bottom=0.20, top=0.76, wspace=0.28)
    fig.suptitle("Linear drag: motion persists as acceleration fades", fontsize=18, y=0.97)
    fig.text(0.5, 0.88, "From rest; downward positive; M = 1 kg, b = 2 kg/s, g = 9.8 m/s²", ha="center", fontsize=13)
    v1, a1 = terminal * (1 - np.exp(-1 / tau)), gravity * np.exp(-1 / tau)
    axes[0].plot(t, velocity, color="#2368ac", lw=2.7)
    axes[0].axhline(terminal, color="#666666", ls="--", lw=1.4)
    axes[0].text(1.6, terminal - 0.5, r"$v_T=4.9$ m/s", fontsize=12)
    axes[1].plot(t, acceleration, color="#bf5224", lw=2.7)
    for ax, value, color, label, text_xy in (
        (axes[0], v1, "#2368ac", f"1 s: {v1:.3f} m/s", (1.2, 2.9)),
        (axes[1], a1, "#bf5224", f"1 s: {a1:.3f} m/s²", (1.1, 4.8)),
    ):
        ax.axvline(tau, color="#8a8a8a", ls=":", lw=1.2)
        ax.scatter(1, value, color=color, edgecolors="white", s=65, zorder=4)
        ax.annotate(label, xy=(1, value), xytext=text_xy, color=color,
                    arrowprops={"arrowstyle": "-", "color": color, "lw": 1.1})
        ax.set(xlim=(0, 3), xlabel="Time (s)", xticks=[0, 0.5, 1, 2, 3])
        ax.grid(alpha=0.18)
        ax.spines[["top", "right"]].set_visible(False)
        ax.set_facecolor("white")
    axes[0].set(ylim=(0, 5.4), ylabel="Downward velocity (m/s)")
    axes[1].set(ylim=(0, 10.5), ylabel="Downward acceleration (m/s²)")
    axes[0].set_title(r"$v(t)=v_T(1-e^{-t/\tau})$", fontsize=14, pad=13)
    axes[1].set_title(r"$a(t)=g e^{-t/\tau}$", fontsize=14, pad=13)
    fig.text(0.5, 0.07, "Dotted lines: τ = 0.5 s. Illustrative constant linear drag model; buoyancy neglected.",
             ha="center", fontsize=11)
    fig.savefig("linear-drag-terminal-velocity.png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
