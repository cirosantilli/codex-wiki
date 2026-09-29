"""Exact two-tone deep-water gravity model, not experimental data.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media; writes the matching PNG basename to the current directory.
The periodic beat train is deliberately distinguished from a localized packet.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12})
    fig = plt.figure(figsize=(10, 7.7), layout="constrained")
    fig.set_facecolor("white")
    gs = fig.add_gridspec(3, 1, height_ratios=(1, 1, 1.3))
    axes = [fig.add_subplot(gs[i]) for i in range(3)]
    fig.suptitle("A carrier phase advances through a slower envelope", fontsize=17)
    fig.get_layout_engine().set(rect=(0, 0.055, 1, 0.94))
    k1, k2 = 0.9, 1.1
    w1, w2 = np.sqrt(k1), np.sqrt(k2)
    kbar, wbar = (k1 + k2) / 2, (w1 + w2) / 2
    dk, dw = k2 - k1, w2 - w1
    phase_speed, envelope_speed = wbar / kbar, dw / dk
    x = np.linspace(-30, 45, 3000)
    for ax, t in zip(axes[:2], (0, 16)):
        wave = np.cos(k1*x - w1*t) + np.cos(k2*x - w2*t)
        env = 2 * np.abs(np.cos((dk*x - dw*t) / 2))
        ax.set_facecolor("white")
        ax.plot(x, wave, color="#233c61", lw=1.5, label="exact sum of two tones")
        ax.plot(x, env, color="#00866b", lw=2, linestyle="--", label="envelope magnitude")
        ax.plot(x, -env, color="#00866b", lw=2, linestyle="--")
        ax.axvline(envelope_speed*t, color="#00866b", lw=1.3, linestyle="--")
        ax.axvline(phase_speed*t, color="#d55e00", lw=1.3, linestyle=":")
        if t:
            ax.annotate("envelope maximum", (envelope_speed*t, 2),
                        xytext=(-13, 2.6), color="#00866b", fontsize=10,
                        arrowprops={"arrowstyle": "->", "color": "#00866b"})
            y_phase = 2*np.cos((dk*phase_speed*t - dw*t)/2)
            ax.scatter([phase_speed*t], [y_phase], color="#d55e00", s=35, zorder=5)
            ax.annotate("carrier phase marker", (phase_speed*t, y_phase),
                        xytext=(21, 2.6), color="#d55e00", fontsize=10,
                        arrowprops={"arrowstyle": "->", "color": "#d55e00"})
        ax.set(xlim=(-30, 45), ylim=(-2.5, 3.25),
               ylabel="normalized elevation", title=f"Snapshot at t = {t}")
        ax.set_yticks([-2, 0, 2])
        ax.spines[["right", "top"]].set_visible(False)
    axes[0].legend(loc="upper right", frameon=False, fontsize=9, ncols=2)
    axes[1].set_xlabel("normalized position x")
    ax = axes[2]
    times = np.linspace(0, 16, 200)
    ax.plot(phase_speed*times, times, color="#d55e00", lw=2.5,
            label=f"carrier phase: dx/dt = {phase_speed:.5f}")
    ax.plot(envelope_speed*times, times, color="#00866b", lw=2.5, linestyle="--",
            label=f"envelope maximum: dx/dt = {envelope_speed:.5f}")
    ax.scatter([envelope_speed*16], [16], color="#00866b", s=35)
    ax.scatter([phase_speed*16], [16], color="#d55e00", s=35)
    ax.set(xlim=(-1, 22), ylim=(0, 20), xlabel="normalized position x",
           ylabel="normalized time t", title="Space–time paths of the two markers")
    ax.set_xticks([0, 5, 10, 15, 20])
    ax.set_yticks([0, 8, 16])
    ax.spines[["right", "top"]].set_visible(False)
    ax.legend(loc="lower right", frameon=False, fontsize=10)
    fig.text(0.5, 0.035,
             r"Exact analytical model: $\omega=\sqrt{k}$, $k_1=0.9$, $k_2=1.1$. Not measured data.",
             ha="center", fontsize=11)
    fig.text(0.5, 0.012,
             "Two tones make a periodic beat train, not a localized packet. Limiting group velocity at k = 1 is 0.5.",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
