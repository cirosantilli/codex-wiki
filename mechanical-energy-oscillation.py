"""Draw mechanical-energy-oscillation.png in the current working directory.

Run from _media; dependencies are declared in the root pyproject.toml.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
The figure is an original calculation, with an opaque white background.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    mass, stiffness, amplitude = 0.5, 2.0, 0.3
    omega = np.sqrt(stiffness / mass)
    period = 2 * np.pi / omega
    energy = stiffness * amplitude**2 / 2
    time = np.linspace(0, period, 1201)
    position = amplitude * np.cos(omega * time)
    velocity = -amplitude * omega * np.sin(omega * time)
    potential = stiffness * position**2 / 2
    kinetic = mass * velocity**2 / 2
    np.testing.assert_allclose([omega, period, energy], [2, np.pi, 0.09])
    np.testing.assert_allclose(potential + kinetic, energy, atol=1e-14)

    blue, orange, dark = "#1765a8", "#bf5808", "#30363d"
    plt.rcParams.update({
        "font.size": 11,
        "axes.titlesize": 12,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "savefig.facecolor": "white",
    })
    fig, axes = plt.subplots(2, 2, figsize=(10, 7.3))
    fig.subplots_adjust(left=0.09, right=0.98, bottom=0.09, top=0.83,
                        hspace=0.50, wspace=0.33)
    fig.suptitle("One oscillator: motion, phase ellipse and energy", y=0.98, fontsize=16)
    fig.text(0.5, 0.925,
             r"$m=0.5$ kg, $k=2$ N/m, $A=0.3$ m; "
             r"$\omega=2$ s$^{-1}$, $P=\pi$ s, $E=0.09$ J",
             ha="center", fontsize=12)
    fig.text(0.5, 0.875, "Released from rest at x = +0.3 m; no damping or drive",
             ha="center", fontsize=11, color=dark)

    ticks = np.arange(5) * period / 4
    ticklabels = ["0", r"$\pi/4$", r"$\pi/2$", r"$3\pi/4$", r"$\pi$"]

    def time_axis(ax):
        ax.set_xlim(0, period)
        ax.set_xticks(ticks, ticklabels)
        ax.set_xlabel("Time t (s)")
        ax.grid(alpha=0.18)

    ax = axes[0, 0]
    ax.plot(time, position, color=blue, lw=2.5)
    ax.axhline(0, color="#8a929a", lw=0.8)
    ax.scatter(ticks, amplitude * np.cos(omega * ticks), color=dark, s=22, zorder=3)
    ax.set(title=r"Position: $x=0.3\cos(2t)$", ylabel="Displacement x (m)",
           ylim=(-0.37, 0.37), yticks=[-0.3, 0, 0.3])
    time_axis(ax)

    ax = axes[0, 1]
    ax.plot(time, velocity, color=orange, lw=2.5)
    ax.axhline(0, color="#8a929a", lw=0.8)
    ax.scatter(ticks, -amplitude * omega * np.sin(omega * ticks),
               color=dark, s=22, zorder=3)
    ax.set(title=r"Velocity: $v=-0.6\sin(2t)$", ylabel="Velocity v (m/s)",
           ylim=(-0.74, 0.74), yticks=[-0.6, 0, 0.6])
    time_axis(ax)

    ax = axes[1, 0]
    ax.plot(position, velocity, color=blue, lw=2.5)
    ax.axhline(0, color="#8a929a", lw=0.8)
    ax.axvline(0, color="#8a929a", lw=0.8)
    ax.scatter(position[::300], velocity[::300], color=dark, s=24, zorder=3)
    for phase in [np.pi / 4, 3 * np.pi / 4, 5 * np.pi / 4, 7 * np.pi / 4]:
        before, after = phase - 0.10, phase + 0.10
        ax.annotate("", xy=(amplitude * np.cos(after), -amplitude * omega * np.sin(after)),
                    xytext=(amplitude * np.cos(before), -amplitude * omega * np.sin(before)),
                    arrowprops={"arrowstyle": "->", "color": dark, "lw": 1.8,
                                "mutation_scale": 16})
    labels = [(0.3, 0, "t = 0", (8, 8)),
              (0, -0.6, r"$t=\pi/4$", (6, -16)),
              (-0.3, 0, r"$t=\pi/2$", (6, 10)),
              (0, 0.6, r"$t=3\pi/4$", (6, 10))]
    for x, v, label, offset in labels:
        ax.annotate(label, (x, v), xytext=offset, textcoords="offset points", fontsize=10)
    ax.set(title="Phase ellipse: same energy at every point",
           xlabel="Displacement x (m)", ylabel="Velocity v (m/s)",
           xlim=(-0.42, 0.42), ylim=(-0.83, 0.83),
           xticks=[-0.3, 0, 0.3], yticks=[-0.6, 0, 0.6])
    ax.grid(alpha=0.18)

    ax = axes[1, 1]
    ax.plot(time, potential, color=blue, lw=2.3, label=r"$V=0.09\cos^2(2t)$")
    ax.plot(time, kinetic, color=orange, lw=2.3, label=r"$T=0.09\sin^2(2t)$")
    ax.axhline(energy, color=dark, lw=1.8, ls="--", label=r"$E=T+V=0.09$ J")
    ax.set(title="Energy exchange: two cycles per period", ylabel="Energy (J)",
           ylim=(-0.006, 0.15), yticks=[0, 0.045, 0.09])
    time_axis(ax)
    ax.legend(loc="upper center", frameon=False, fontsize=9)

    fig.savefig(Path.cwd() / "mechanical-energy-oscillation.png", dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
