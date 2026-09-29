"""Synthetic linear-velocity model: 3 m displacement but 5 m traveled."""
from fractions import Fraction
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def position(t):
    return t**2 - 2*t


def main():
    first = position(Fraction(1)) - position(Fraction(0))
    second = position(Fraction(3)) - position(Fraction(1))
    assert (first, second, first+second, abs(first)+abs(second)) == (-1, 4, 3, 5)
    t = np.linspace(0, 3, 1201)
    velocity = 2*t - 2
    s = position(t)
    distance = np.where(t <= 1, -s, s + 2)
    assert np.all(np.diff(distance) >= 0)
    assert np.isclose(np.trapezoid(velocity, t), 3, atol=1e-12)
    assert np.isclose(np.trapezoid(np.abs(velocity), t), 5, atol=1e-12)
    assert np.isclose(np.abs(np.diff(s)).sum(), 5, atol=1e-12)
    assert np.isclose(np.trapezoid(velocity[::-1], t[::-1]), -3, atol=1e-12)
    assert np.isclose(np.trapezoid(np.abs(velocity[::-1]), t[::-1]), -5, atol=1e-12)
    # A central difference must recover the prescribed rate for this quadratic.
    h = .001
    assert np.allclose((position(t+h)-position(t-h))/(2*h), velocity, atol=1e-10)

    plt.rcParams.update({"font.size": 12, "axes.spines.top": False, "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 4.5), dpi=120, layout="constrained")
    fig.patch.set_facecolor("white")
    fig.suptitle("Synthetic motion model (not measured data)", fontsize=14)
    for ax in axes:
        ax.set_facecolor("white")
        ax.axhline(0, color="#555555", linewidth=1)
        ax.axvline(1, color="#888888", linestyle=":", linewidth=1.3)
        ax.set(xlim=(0, 3), xlabel="time t (s)")
        ax.set_xticks([0, 1, 2, 3])
        ax.grid(axis="y", alpha=.15)
    axes[0].plot(t, velocity, color="#252525", linewidth=2.3)
    axes[0].fill_between(t, 0, velocity, where=velocity <= 0, interpolate=True, color="#d56b35", alpha=.4)
    axes[0].fill_between(t, 0, velocity, where=velocity >= 0, interpolate=True, color="#277da8", alpha=.35)
    axes[0].set(ylim=(-2.5, 4.7), ylabel="velocity v (m/s)", title=r"Rate: $v(t)=2t-2$")
    axes[0].text(.4, -.62, "−1 m", ha="center", color="#8c3d1d", fontsize=14)
    axes[0].text(2.35, 1.1, "+4 m", ha="center", color="#165b7e", fontsize=14)
    axes[0].text(.12, 3.6, "Sign changes at t = 1 s", fontsize=11)
    axes[1].plot(t, s, color="#277da8", linewidth=2.5, label=r"position $s(t)=t^2-2t$")
    axes[1].plot(t, distance, color="#9b5c20", linewidth=2.5, label=r"distance $D(t)=\int_0^t |v(u)|\,du$")
    axes[1].scatter([1, 3, 3], [-1, 3, 5], color=["#277da8", "#277da8", "#9b5c20"], zorder=3)
    axes[1].set(ylim=(-1.55, 6.4), ylabel="accumulated length (m)", title="Same rate, two different totals")
    axes[1].annotate("3 m displacement", xy=(3, 3), xytext=(1.15, 3.4), color="#165b7e", fontsize=11)
    axes[1].annotate("5 m distance", xy=(3, 5), xytext=(1.55, 5.25), color="#794716", fontsize=11)
    axes[1].text(.7, -1.35, "turning point", color="#165b7e", fontsize=10)
    axes[1].legend(loc="upper left", fontsize=9, framealpha=1)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)
    print({"negative_displacement_m": -1, "positive_displacement_m": 4,
           "displacement_m": 3, "distance_m": 5, "reversed_velocity_integral_m": -3,
           "reversed_speed_integral_m": -5, "monotone_distance": True,
           "position_variation_m": float(np.abs(np.diff(s)).sum()), "derivative_check": True})


if __name__ == "__main__":
    main()
