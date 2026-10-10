"""Draw the ideal constant-force example; write the PNG basename to cwd.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
All curves are exact expressions for a 2 kg point mass initially at rest.
"""

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "savefig.facecolor": "white"})
    mass, force, distance = 2.0, 3.0, 4.0
    acceleration = force / mass
    final_time = np.sqrt(2 * distance / acceleration)
    x = np.linspace(0, distance, 401)
    velocity = np.sqrt(2 * force * x / mass)
    energy = force * x
    t = np.linspace(0, final_time, 401)
    power = force * acceleration * t
    mean_power = force * distance / final_time
    fig, axes = plt.subplots(1, 3, figsize=(12, 5.2), facecolor="white")
    fig.subplots_adjust(left=0.065, right=0.975, bottom=0.19, top=0.73, wspace=0.37)
    fig.suptitle("One constant force: motion, energy, and transfer rate", fontsize=18, y=0.97)
    fig.text(0.5, 0.865, "Mass 2 kg; net force 3 N to the right; starts at rest; travels 4 m",
             ha="center", fontsize=13)
    fig.text(0.5, 0.795, r"$a=1.5$ m/s²; $t_f=\sqrt{16/3}\approx 2.309401$ s", ha="center")
    blue, orange, green = "#2369a4", "#b85c17", "#34734b"
    axes[0].plot(x, velocity, color=blue, lw=2.7)
    axes[0].set(xlabel="Distance x (m)", ylabel="Rightward velocity v (m/s)",
                xlim=(0, 4.2), ylim=(0, 4), xticks=[0, 1, 2, 3, 4])
    axes[0].set_title(r"$v(x)=\sqrt{2Fx/m}$", pad=12)
    axes[0].scatter([4], [velocity[-1]], color=blue, s=45, zorder=3)
    axes[0].text(0.45, 3.6, "Final: 3.4641 m/s", color=blue, fontsize=11)
    axes[1].plot(x, energy, color=orange, lw=2.7)
    axes[1].set(xlabel="Distance x (m)", ylabel="Kinetic energy K (J)",
                xlim=(0, 4.2), ylim=(0, 14), xticks=[0, 1, 2, 3, 4], yticks=[0, 4, 8, 12])
    axes[1].set_title(r"$K(x)=Fx$", pad=12)
    axes[1].scatter([4], [12], color=orange, s=45, zorder=3)
    axes[1].text(0.45, 12.6, "Final: 12 J", color=orange, fontsize=11)
    axes[2].plot(t, power, color=green, lw=2.7)
    axes[2].fill_between(t, 0, power, color=green, alpha=0.16)
    axes[2].axhline(mean_power, color="#74518e", lw=2, ls="--")
    axes[2].set(xlabel="Time t (s)", ylabel="Power P (W)",
                xlim=(0, final_time * 1.045), ylim=(0, 12), xticks=[0, 1, 2])
    axes[2].set_title(r"$P(t)=Fat$", pad=12)
    axes[2].scatter([final_time], [power[-1]], color=green, s=45, zorder=3)
    axes[2].text(0.16, 10.8, "Final: 10.3923 W", color=green, fontsize=11)
    axes[2].text(0.14, 5.6, "Mean: 5.19615 W", color="#74518e", fontsize=11,
                 bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    axes[2].text(1.28, 1.45, "Area: 12 J", color=green, fontsize=11)
    for ax in axes:
        ax.set_facecolor("white")
        ax.grid(alpha=0.18)
        ax.spines[["top", "right"]].set_visible(False)
    fig.text(0.5, 0.045, "Velocity and energy use separate units. The mean-power line gives the same work over the same time.",
             ha="center", fontsize=11)
    fig.savefig("kinetic-energy-work-and-power.png", dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
