"""Plot receiver geometry and frequency against delayed reception time.

Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
All parameters are chosen model values; no measured observations are used.
The emitter's closest passage is at emission time tau=0; reception is t=tau+R/c.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    sound_speed, source_speed, emitted_frequency = 343.0, 20.0, 500.0
    offsets = [(2.0, "#126b9b"), (10.0, "#b65b11")]
    fig, (geometry, frequency) = plt.subplots(
        2, 1, figsize=(9.4, 7.5), dpi=130, facecolor="white",
        gridspec_kw={"height_ratios": [1, 1.8]}, layout="constrained")
    fig.suptitle("Passing source: the same speed, different receiver offsets", fontsize=14)
    geometry.axhline(0, color="#b32632", lw=2)
    geometry.annotate("", (29, 0), (22, 0),
                      arrowprops={"arrowstyle": "->", "color": "#b32632", "lw": 2})
    geometry.plot(0, 0, "o", color="#b32632", ms=7)
    geometry.text(-28, 1.0, r"Source: $(v\tau,0)$, moving right at $v=20$ m/s", fontsize=10)
    for offset, color in offsets:
        geometry.plot(0, offset, "s", color=color, ms=7)
        geometry.plot([0, 0], [0, offset], color=color, ls=":", lw=1)
        geometry.text(1.4, offset + 0.3, f"receiver: b = {offset:g} m", color=color, fontsize=10)
    geometry.set(xlim=(-32, 32), ylim=(-1.5, 13.5), aspect="equal",
                 xlabel="Position along source path x (m)", ylabel="Offset y (m)")
    geometry.set_title("Geometry at closest passage (material-frame time 0)", fontsize=11)
    tau = np.linspace(-3.0, 3.0, 24001)
    for offset, color in offsets:
        distance = np.hypot(source_speed * tau, offset)
        reception_time = tau + distance / sound_speed
        received = emitted_frequency * sound_speed / (
            sound_speed + source_speed**2 * tau / distance)
        frequency.plot(reception_time, received, color=color, lw=2.2,
                       label=f"b = {offset:g} m")
        zero_time = offset / sound_speed
        frequency.plot(zero_time, emitted_frequency, "o", color=color, ms=6, zorder=5)
    upper = emitted_frequency * sound_speed / (sound_speed - source_speed)
    lower = emitted_frequency * sound_speed / (sound_speed + source_speed)
    frequency.axhline(upper, color="#777777", ls="--", lw=1)
    frequency.axhline(lower, color="#777777", ls="--", lw=1)
    frequency.axhline(emitted_frequency, color="#777777", ls=":", lw=1)
    frequency.axvline(0, color="#999999", ls=":", lw=1)
    frequency.text(1.47, upper + 1.4, f"approach limit {upper:.2f} Hz", ha="right", fontsize=10)
    frequency.text(1.47, lower - 3.8, f"recession limit {lower:.2f} Hz", ha="right", fontsize=10)
    frequency.annotate(r"zero shift received at $t=b/c$", (10 / sound_speed, 500),
                       (0.3, 514), arrowprops={"arrowstyle": "->", "color": "#444444"}, fontsize=10)
    frequency.set(xlim=(-1.5, 1.5), ylim=(465, 539),
                  xlabel=r"Reception time $t=\tau+R/c$ (s); source passes closest at time 0",
                  ylabel=r"Received frequency $f_o$ (Hz)")
    frequency.legend(loc="lower left", bbox_to_anchor=(0.02, 0.14), frameon=True)
    frequency.set_title(r"Chosen model: $f_s=500$ Hz, $c=343$ m/s; stationary receivers", fontsize=11)
    frequency.grid(alpha=0.15)
    for ax in (geometry, frequency):
        ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
