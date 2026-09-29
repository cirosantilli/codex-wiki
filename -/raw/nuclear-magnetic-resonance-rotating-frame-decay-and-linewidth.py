"""Original Bloch-model calculation, not a historical experimental record.

Python 3.14; matplotlib 3.10.7; numpy 2.3.5. Run from _media.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
fig, axes = plt.subplots(1, 3, figsize=(12, 4.6), facecolor="white")
blue, orange = "#16679a", "#bd571b"
gamma = 2 * np.pi * 42.58e6
b1, t1, t2, detuning_hz = 10e-6, .8, .12, 5.
tau = np.pi / (2 * gamma * b1)

ax = axes[0]
theta = np.linspace(0, np.pi / 2, 120)
ax.plot(np.sin(theta), np.cos(theta), color=orange, lw=2)
for endpoint, color in [((0, 1), blue), ((1, 0), orange)]:
    ax.annotate("", endpoint, (0, 0), arrowprops={"arrowstyle": "->", "lw": 2.5, "color": color})
ax.annotate("", (.82, .57), (.65, .76), arrowprops={"arrowstyle": "->", "color": orange, "lw": 2})
ax.text(.1, .92, "before", color=blue)
ax.text(.68, .1, "after", color=orange)
ax.set(xlim=(-.1, 1.15), ylim=(-.1, 1.15), xlabel="$v/M_0$", ylabel="$w/M_0$",
       title="Resonant pulse in rotating axes")
ax.set_aspect("equal")
ax.text(.5, -.36, f"$B_1=10$ μT,  $\\tau={tau * 1e3:.3f}$ ms\nrelaxation neglected during pulse",
        transform=ax.transAxes, ha="center", fontsize=10)
ax.set_xticks([0, .5, 1])
ax.set_yticks([0, .5, 1])

ax = axes[1]
t = np.linspace(0, .6, 1501)
s = np.exp(-t / t2 - 2j * np.pi * detuning_hz * t)
ax.plot(t, s.real, color=blue, label="$I=\\mathrm{Re}\\,S$")
ax.plot(t, s.imag, color=orange, label="$Q=\\mathrm{Im}\\,S$")
ax.plot(t, abs(s), "--", color="#555555", lw=1, label="$|S|$")
ax.axhline(0, color="#cccccc", lw=.7)
ax.set(xlabel="Time after pulse (s)", ylabel="Normalized signal", xlim=(0, .6), ylim=(-.85, 1.1),
       title="Free quadratures at 5 Hz detuning")
ax.legend(frameon=False, fontsize=9, loc="upper right")
ax.text(.5, -.28, "$T_2=0.120$ s; calibrated phase $S(0)=1$", transform=ax.transAxes,
        ha="center", fontsize=10)

ax = axes[2]
df = np.linspace(-10, 10, 1601)
profile = 1 / (1 + (2 * np.pi * df * t2) ** 2)
hwhm = 1 / (2 * np.pi * t2)
ax.plot(df, profile, color=blue, lw=2)
ax.hlines(.5, -hwhm, hwhm, color=orange, lw=2)
ax.plot([-hwhm, hwhm], [.5, .5], "o", color=orange, ms=5)
ax.annotate("", (hwhm, .32), (-hwhm, .32), arrowprops={"arrowstyle": "<->", "color": orange})
ax.text(0, .19, f"FWHM = {2 * hwhm:.3f} Hz", ha="center", color=orange, fontsize=10)
ax.set(xlabel="Offset from resonance (Hz)", ylabel="Normalized absorption", xlim=(-10, 10), ylim=(0, 1.1),
       title="Weak drive, uniform field")
ax.text(.5, -.28, "$A(f)=1/[1+(2\\pi\\Delta f T_2)^2]$", transform=ax.transAxes,
        ha="center", fontsize=10)
for ax in axes:
    ax.spines[["top", "right"]].set_visible(False)
fig.suptitle("Original Bloch-model example: excitation, decay and linewidth", fontsize=16, y=.97)
fig.text(.5, .018, "Teaching calculation • not 1946 data • $T_1=0.800$ s • homogeneous $T_2$ • pulse and weak-CW regimes differ",
         ha="center", fontsize=10, color="#555555")
fig.subplots_adjust(left=.065, right=.98, top=.80, bottom=.29, wspace=.40)
fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100, facecolor="white")
plt.close(fig)
