"""Original superterminal-pebble plots. Python 3.14, NumPy 2.3.5,
Matplotlib 3.10.7; writes the same-basename PNG in the current directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    blue, orange, green = "#126782", "#b55d15", "#287d53"
    radius, rho_p, rho_w, coefficient, gravity = 0.02, 2500.0, 1000.0, 0.7, 9.81
    b = 3 * coefficient * rho_w / (8 * rho_p * radius)
    terminal = np.sqrt(gravity * (1 - rho_w / rho_p) / b)
    entry = np.sqrt(2 * gravity * 5)
    depths = np.linspace(0, 1.5, 1200)
    ratio_squared_excess = (entry**2 / terminal**2 - 1) * np.exp(-2 * b * depths)
    speeds = terminal * np.sqrt(1 + ratio_squared_excess)
    # Algebraic form avoids cancellation when the fractional excess is small.
    fractional_excess = ratio_squared_excess / (np.sqrt(1 + ratio_squared_excess) + 1)
    z1 = np.log((entry**2 / terminal**2 - 1) / (1.01**2 - 1)) / (2 * b)
    z5 = np.log((entry**2 / terminal**2 - 1) / (1.05**2 - 1)) / (2 * b)
    fig, (ax, excess) = plt.subplots(1, 2, figsize=(11.3, 5.7), gridspec_kw={"width_ratios": (1, 1.12)})
    ax.plot(depths, speeds, color=blue, lw=2.5, label=r"$v(z)$")
    ax.axhline(terminal, color=orange, lw=1.5, ls="--", label=rf"$v_t={terminal:.3f}$ m/s")
    ax.scatter([0], [entry], color=blue, s=40, zorder=4)
    ax.annotate(rf"Entry: {entry:.2f} m/s", (0, entry), (0.2, 8.2),
                arrowprops={"arrowstyle": "->", "color": blue}, color=blue)
    ax.set(xlim=(0, 1.5), ylim=(0, 10.5), xlabel="Underwater depth z (m)",
           ylabel="Downward speed (m/s)", title="The pebble decelerates after entry")
    ax.legend(frameon=False, loc="upper right")
    ax.grid(alpha=0.16)
    excess.semilogy(depths, fractional_excess, color=blue, lw=2.5)
    for tolerance, depth, color, text_x, text_y in ((0.05, z5, orange, 0.58, 0.18), (0.01, z1, green, 0.15, 0.0015)):
        excess.axhline(tolerance, color=color, lw=1.1, ls="--")
        excess.plot([depth, depth], [1e-6, tolerance], color=color, lw=1, ls=":")
        excess.scatter([depth], [tolerance], color=color, s=40, zorder=4)
        excess.annotate(f"{100*tolerance:.0f}% excess at {depth:.3f} m", (depth, tolerance),
                        (text_x, text_y), color=color, fontsize=11,
                        arrowprops={"arrowstyle": "->", "color": color})
    excess.set(xlim=(0, 1.5), ylim=(1e-6, 20), xlabel="Underwater depth z (m)",
               ylabel=r"Fractional speed excess $(v-v_t)/v_t$", title="A tolerance makes ‘reached’ precise")
    excess.grid(alpha=0.16, which="major")
    fig.suptitle("Pebble settling under quadratic drag and buoyancy", fontsize=17, y=0.97)
    fig.text(0.5, 0.13, r"$v^2(z)=v_t^2+(u^2-v_t^2)e^{-2bz}$,  $b=5.25$ m$^{-1}$; exact equality $v=v_t$ is asymptotic.",
             ha="center", fontsize=13)
    fig.text(0.5, 0.06, "Model: 5 m air fall, no air drag or entry losses; constant water drag coefficient C = 0.7.",
             ha="center", fontsize=11, color="#596672")
    fig.text(0.5, 0.022, "Time to 5 m water depth: 4.43 s; total time including the air fall: 5.44 s.",
             ha="center", fontsize=11, color="#596672")
    fig.subplots_adjust(left=0.075, right=0.975, bottom=0.26, top=0.84, wspace=0.29)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                dpi=140, facecolor="white", transparent=False,
                metadata={"Software": "Matplotlib"})
    plt.close(fig)


if __name__ == "__main__":
    main()
