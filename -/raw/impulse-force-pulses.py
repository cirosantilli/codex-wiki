"""Draw three stipulated positive net-force pulses with equal impulse.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Write impulse-force-pulses.png to the current working directory.
"""

import matplotlib.pyplot as plt
import numpy as np


def main():
    triangle_t = np.linspace(0.0, 0.5, 501)
    triangle_f = 24.0 * (1.0 - np.abs(triangle_t - 0.25) / 0.25)
    impulses = np.array([12.0 * 0.5, np.trapezoid(triangle_f, triangle_t), 3.0 * 2.0])
    delta_v = impulses / 2.0
    np.testing.assert_allclose(impulses, [6.0, 6.0, 6.0])
    np.testing.assert_allclose(delta_v, [3.0, 3.0, 3.0])
    print("Pulse impulses (N s):", impulses.tolist())
    print("Velocity changes for 2 kg (m/s):", delta_v.tolist())

    plt.rcParams.update({"font.size": 12, "savefig.facecolor": "white"})
    fig, axes = plt.subplots(1, 3, figsize=(11.5, 5.6), facecolor="white",
                             sharex=True, sharey=True)
    fig.subplots_adjust(left=0.07, right=0.985, bottom=0.27,
                        top=0.73, wspace=0.17)
    fig.suptitle("Equal impulse does not mean equal peak force", fontsize=18, y=0.965)
    fig.text(0.5, 0.86,
             "Three rightward net-force pulses, each with area 6 N s; all axes use the same scale",
             ha="center", fontsize=12)
    pulses = [([0.0, 0.5], [12.0, 12.0], "#276b9b", "Short rectangle", "12 N × 0.5 s = 6 N s"),
              (triangle_t, triangle_f, "#cf7323", "Short triangle", "½ × 24 N × 0.5 s = 6 N s"),
              ([0.0, 2.0], [3.0, 3.0], "#387f54", "Long rectangle", "3 N × 2 s = 6 N s")]
    for ax, (t, force, color, title, area_label) in zip(axes, pulses, strict=True):
        ax.fill_between(t, 0, force, color=color, alpha=0.24)
        ax.plot(t, force, color=color, lw=2.8)
        ax.plot([t[0], t[0]], [0, force[0]], color=color, lw=2.8)
        ax.plot([t[-1], t[-1]], [force[-1], 0], color=color, lw=2.8)
        ax.plot([t[-1], 2.15], [0, 0], color=color, lw=2.8)
        peak_idx = int(np.argmax(force))
        peak_x, peak = t[peak_idx], force[peak_idx]
        ax.annotate(f"Peak {peak:g} N", xy=(peak_x, peak),
                    xytext=(0.95, max(peak + 3.0, 9.0)), fontsize=11,
                    ha="center", color=color,
                    arrowprops={"arrowstyle": "->", "color": color, "lw": 1.3})
        ax.set(title=title, xlabel="Time t (s)", xlim=(-0.04, 2.15), ylim=(0, 29),
               xticks=[0, 0.5, 1, 1.5, 2], yticks=[0, 6, 12, 18, 24])
        ax.text(0.5, -0.25, area_label, transform=ax.transAxes,
                ha="center", fontsize=11, color=color)
        ax.set_facecolor("white")
        ax.set_axisbelow(True)
        ax.grid(alpha=0.17)
        ax.spines[["top", "right"]].set_visible(False)
        ax.title.set_fontsize(13)
    axes[0].set_ylabel("Net force F (N)")
    fig.text(0.5, 0.105,
             r"Same fixed mass $m=2$ kg: $\Delta v=J/m=6/2=3$ m/s for every pulse",
             ha="center", fontsize=13)
    fig.text(0.5, 0.04,
             "These are stipulated examples. Pulse shapes affect the motion during the interval, even when the final change is equal.",
             ha="center", fontsize=10)
    fig.savefig("impulse-force-pulses.png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
