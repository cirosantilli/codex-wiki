"""Original deep-water elastic-plate illustration; write PNG to caller's cwd."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    gravity = 9.81
    ice_density, water_density = 917.0, 1025.0
    thickness, young_modulus, poisson_ratio = 1.0, 5.0e9, 0.3
    rigidity = young_modulus * thickness**3 / (12 * (1 - poisson_ratio**2))
    beta = rigidity / water_density
    alpha = ice_density * thickness / water_density
    wave_number = np.geomspace(0.003, 1.0, 16000)
    omega = np.sqrt(
        (gravity * wave_number + beta * wave_number**5)
        / (1 + alpha * wave_number)
    )
    period = 2 * np.pi / omega
    phase_speed = omega / wave_number
    group_speed = (
        gravity + 5 * beta * wave_number**4 + 4 * beta * alpha * wave_number**5
    ) / (2 * omega * (1 + alpha * wave_number) ** 2)
    order = np.argsort(period)
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(10.4, 4.4), dpi=100, facecolor="white")
    ax.set_facecolor("white")
    ax.plot(period[order], group_speed[order], color="#1565c0", linewidth=2.5,
            label=r"Group speed $c_g=d\omega/dk$")
    ax.plot(period[order], phase_speed[order], color="#b24b20", linewidth=1.8,
            linestyle="--", label=r"Phase speed $c_p=\omega/k$")
    j, q = np.argmin(group_speed), np.argmin(phase_speed)
    ax.scatter([period[j]], [group_speed[j]], color="#1565c0", zorder=5)
    ax.annotate("Group-speed minimum", (period[j], group_speed[j]),
                xytext=(16, 7), arrowprops={"arrowstyle": "->", "color": "#1565c0"},
                color="#1565c0")
    ax.scatter([period[q]], [phase_speed[q]], color="#b24b20", zorder=5)
    ax.annotate("Phase-speed minimum", (period[q], phase_speed[q]),
                xytext=(10, 25), arrowprops={"arrowstyle": "->", "color": "#b24b20"},
                color="#b24b20")
    ax.set(xlim=(2, 30), ylim=(0, 65), xlabel="Wave period (s)", ylabel="Speed (m/s)",
           title="Flexural–gravity waves: illustrative 1 m elastic ice sheet")
    ax.grid(alpha=0.18)
    ax.legend(loc="upper right", frameon=False)
    fig.tight_layout()
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
