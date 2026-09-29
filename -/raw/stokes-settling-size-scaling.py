"""Stokes sphere settling and its diameter-based Reynolds-number check.

Outputs basename PNG in CWD. Tested with Python 3.14.4,
numpy 2.3.5 and matplotlib 3.10.7 (repository dependencies).
Build: make _media/stokes-settling-size-scaling.png
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


rho_f, rho_p, mu, g = 1000.0, 2500.0, 1e-3, 9.81


def settling(radius):
    speed = 2 * (rho_p - rho_f) * g * radius**2 / (9 * mu)
    reynolds = 2 * radius * rho_f * speed / mu
    return speed, reynolds


example_a = np.array([5, 10, 20, 50]) * 1e-6
example_u, example_re = settling(example_a)
assert np.allclose(example_u * 1e3, [0.08175, 0.327, 1.308, 8.175])
assert np.allclose(example_re, [0.0008175, 0.00654, 0.05232, 0.8175])
weight = 4 * np.pi * example_a**3 * (rho_p - rho_f) * g / 3
drag = 6 * np.pi * mu * example_a * example_u
assert np.allclose(weight, drag, rtol=1e-14, atol=0)
assert np.isclose(1e-3 / example_u[1], 3.0581039755)

plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
fig, axes = plt.subplots(1, 2, figsize=(10.5, 5.8), dpi=120)
fig.subplots_adjust(left=0.075, right=0.975, top=0.76, bottom=0.29, wspace=0.30)
radius_um = np.geomspace(1, 100, 401)
speed, reynolds = settling(radius_um * 1e-6)
re_one_radius = (9 * mu**2 / (4 * rho_f * (rho_p - rho_f) * g))**(1 / 3) * 1e6
blue, orange = "#1766a0", "#ad4e12"
for ax in axes:
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(1, 100)
    ax.set_xticks([1, 5, 10, 20, 50, 100], labels=["1", "5", "10", "20", "50", "100"])
    ax.set_xlabel(r"Sphere radius $a$ ($\mu$m)")
    ax.grid(True, which="both", color="#dce1e5", lw=0.5)
    ax.axvspan(re_one_radius, 100, color="#fbe4d9", alpha=0.9)
    ax.axvline(re_one_radius, color=orange, lw=1, linestyle=":")

ax = axes[0]
ax.plot(radius_um, speed * 1e3, color=blue, lw=2.4)
ax.scatter(example_a * 1e6, example_u * 1e3, color=blue, zorder=4)
ax.set_title(r"Terminal-speed prediction: $U_s\propto a^2$", fontsize=13, pad=12)
ax.set_ylabel(r"Downward speed $U_s$ (mm/s)")
ax.annotate("10 µm → 0.327 mm/s", xy=(10, 0.327), xytext=(2.0, 1.9),
            fontsize=11, arrowprops={"arrowstyle": "->", "color": blue})
ax.annotate("20 µm → 1.308 mm/s", xy=(20, 1.308), xytext=(2.0, 6.0),
            fontsize=11, arrowprops={"arrowstyle": "->", "color": blue})
ax.set_ylim(0.002, 60)

ax = axes[1]
ax.plot(radius_um, reynolds, color=orange, lw=2.4)
ax.scatter(example_a * 1e6, example_re, color=orange, zorder=4)
ax.set_title(r"Validity check: $\mathrm{Re}_d\propto a^3$", fontsize=13, pad=12)
ax.set_ylabel(r"Diameter-based $\mathrm{Re}_d=2a\rho_f U_s/\mu$")
ax.axhline(1, color=orange, ls="--", lw=1.2)
ax.text(1.25, 1.3, "Re = 1; require Re ≪ 1", color=orange, fontsize=10.5)
ax.annotate("10 µm → 0.00654", xy=(10, 0.00654), xytext=(1.5, 0.045),
            fontsize=11, arrowprops={"arrowstyle": "->", "color": orange})
ax.annotate("50 µm → 0.8175", xy=(50, 0.8175), xytext=(9, 4.5),
            fontsize=11, arrowprops={"arrowstyle": "->", "color": orange})
ax.set_ylim(3e-6, 20)

fig.suptitle("Larger spheres settle faster — until inertia matters", y=0.97, fontsize=18)
fig.text(0.5, 0.885, r"$\rho_f=1000,\ \rho_p=2500\ \mathrm{kg/m^3};\quad\mu=1.00\times10^{-3}\ \mathrm{Pa\,s};\quad g=9.81\ \mathrm{m/s^2}$", ha="center", fontsize=12)
fig.text(0.5, 0.135, "Double the radius: 4× the predicted speed, 8× the Reynolds number.", ha="center", fontsize=12)
fig.text(0.5, 0.075, f"All curves use the Stokes formula. Shading starts at Re = 1 (a ≈ {re_one_radius:.1f} µm); it is not a sharp cutoff.", ha="center", fontsize=10.5)
fig.text(0.5, 0.035, "Rigid isolated no-slip spheres in water; wall effects and release transients are excluded.", ha="center", fontsize=10.5)
output = Path.cwd() / f"{Path(__file__).stem}.png"
fig.savefig(output, facecolor="white", transparent=False)
plt.close(fig)
print(f"{output.name}: speeds (mm/s)={example_u * 1e3}; Re_d={example_re}")
print(f"10 µm radius: force={weight[1]:.9g} N; 1 mm fall time={1e-3 / example_u[1]:.9g} s")
