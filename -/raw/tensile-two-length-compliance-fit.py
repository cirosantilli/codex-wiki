"""Stipulated two-length inverse problem, not measured material data.

Python 3.14, matplotlib 3.10.7, numpy 2.3.5. Writes basename.png to CWD.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


force = np.array([0, 100, 200, 300, 400], dtype=float)
lengths = np.array([50, 100], dtype=float)
displacements = np.array([[.005, .040, .075, .110, .145],
                          [.008, .068, .128, .188, .248]])
fits = np.array([np.polyfit(force, x, 1) for x in displacements])
q = fits[:, 0]
length_slope, machine_compliance = np.polyfit(lengths, q, 1)
area = 2.0
modulus = 1 / (area * length_slope)
assert np.allclose(q, [.00035, .00060], rtol=1e-12)
assert np.isclose(modulus, 100000)
assert np.isclose(machine_compliance, .0001)

plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
fig, (left, right) = plt.subplots(1, 2, figsize=(11.8, 5.5))
fig.patch.set_facecolor("white")
colors = ["#2266a2", "#d16a16"]
for i, color in enumerate(colors):
    left.plot(force, np.polyval(fits[i], force), color=color, lw=2,
              label=f"$L={lengths[i]:.0f}$ mm; $q={q[i]*1000:.2f}$ mm/kN")
    left.scatter(force, displacements[i], color=color, s=38, zorder=3)
left.set(xlabel="Force $F$ (N)", ylabel="Crosshead displacement $x$ (mm)",
         xlim=(-15, 415), ylim=(-.012, .275))
left.set_title("1. Fit each displacement channel", loc="left", weight="bold", fontsize=12)
left.legend(loc="upper left", frameon=False, fontsize=10)
left.text(25, .027, "Separate fitted offsets:\n0.005 mm and 0.008 mm", fontsize=10,
          va="bottom", bbox={"facecolor": "white", "edgecolor": "none", "alpha": .85})

test_lengths = np.linspace(50, 108, 100)
right.plot(test_lengths, (machine_compliance + test_lengths * length_slope) * 1000,
           color="#253746", lw=2)
right.plot([0, 50], (machine_compliance + np.array([0, 50]) * length_slope) * 1000,
           color="#6d7c87", lw=1.8, ls="--")
right.scatter(lengths, q * 1000, c=colors, s=55, zorder=4)
right.scatter([0], [machine_compliance * 1000], marker="o", facecolors="white",
              edgecolors="#253746", s=55, zorder=4)
right.set(xlabel="Uniform deforming length $L$ (mm)",
          ylabel="Total compliance $q=dx/dF$ (mm/kN)",
          xlim=(-5, 112), ylim=(0, .73))
right.set_title("2. Separate slope and intercept", loc="left", weight="bold", fontsize=12)
right.text(8, .095, "$C_m=0.10$ mm/kN", fontsize=11, va="center")
right.text(7, .60, "Slope = 0.005 kN$^{-1}$\n$E=1/(A_0\\,\\mathrm{slope})=100$ GPa",
           linespacing=1.7, fontsize=11)
right.annotate("50 mm", (50, .35), xytext=(54, .30), fontsize=10, color=colors[0])
right.annotate("100 mm", (100, .60), xytext=(76, .51), fontsize=10, color=colors[1])
for ax in [left, right]:
    ax.grid(alpha=.18)
    ax.spines[["top", "right"]].set_visible(False)
fig.suptitle("Stipulated example: $A_0=2.00$ mm$^2$ — no experimental material data",
             fontsize=13, y=.97)
fig.subplots_adjust(left=.075, right=.98, top=.83, bottom=.22, wspace=.30)
fig.text(.5, .055, "Dashed line: model extrapolation to zero length, not an additional observation.",
         ha="center", fontsize=10, color="#425564")
fig.savefig(Path(__file__).stem + ".png", dpi=110, facecolor="white")
plt.close(fig)
