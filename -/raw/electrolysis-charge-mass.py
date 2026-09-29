"""Calculated current-area and copper-mass models, never experimental data.

Tested with Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Writes its PNG basename to CWD; run from _media with MPLBACKEND=Agg.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

F = 96485.3321233100184  # N_A e; displayed precision is rounded.
M_CU = 63.546  # g/mol, conventional value used in the KIT teaching practical.
Z = 2
Q_EQUAL = 600.0
assert 1.0 * 10 * 60 == 0.5 * 20 * 60 == Q_EQUAL
assert abs(M_CU * Q_EQUAL / (Z * F) - .19758236387305083) < 1e-14

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
fig, (left, right) = plt.subplots(1, 2, figsize=(10, 4.8), dpi=120, facecolor="white")
blue, copper, ink = "#237b9b", "#bb7447", "#243544"
fig.suptitle("Charge counts electrons; stoichiometry counts copper atoms", fontsize=15, weight="bold", color=ink, y=.96)
fig.text(.5, .875, "CALCULATED MODEL • no measured currents or masses", ha="center", color=ink, fontsize=10)

left.fill_between([0, 10], 0, 1, color=blue, alpha=.13)
left.fill_between([0, 20], 0, .5, color=copper, alpha=.15)
left.plot([0, 10, 10, 22], [1, 1, 0, 0], color=blue, lw=2.5, label="1 A for 10 min")
left.plot([0, 20, 20, 22], [.5, .5, 0, 0], color=copper, lw=2.5, ls="--", label="0.5 A for 20 min")
left.set(xlim=(0, 22), ylim=(0, 1.2), xlabel="Time (min)", ylabel="Assumed current (A)", title="Different durations, equal charge")
left.text(10.9, 1.03, "Both areas = 600 C", ha="center", color=ink)
left.text(10.9, .16, r"$Q=\int I(t)\,dt$ (time in seconds)", ha="center", color=ink, fontsize=10)
left.legend(loc="upper right", bbox_to_anchor=(1, .79), fontsize=10, frameon=False)
left.set_xticks([0, 5, 10, 15, 20])

q = np.linspace(0, 900, 301)
m_ideal = M_CU * q / (Z * F)
right.plot(q, m_ideal, color=blue, lw=2.5, label=r"Ideal: $\eta=1$")
right.plot(q, .8 * m_ideal, color=copper, lw=2.5, ls="--", label=r"Assumed: $\eta=0.8$")
right.axvline(Q_EQUAL, color="#aeb9c2", lw=1, ls=":")
right.text(460, .228, r"$m=\eta M_{\mathrm{Cu}}Q/(2F)$", ha="center", color=ink, fontsize=12)
right.text(260, .035, "At 600 C: 0.19758 g (ideal)", color=ink, fontsize=9)
right.set(xlim=(0, 900), ylim=(0, .31), xlabel="Transported charge (C)", ylabel="Retained copper mass (g)", title="Two electrons per deposited Cu atom")
right.legend(loc="upper left", fontsize=10, frameon=False)
right.set_xticks([0, 300, 600, 900])
for ax in (left, right):
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(alpha=.15)
fig.text(.5, .055, "80% line assumes same-direction side reactions and complete retention of deposited copper.", ha="center", fontsize=10, color=ink)
fig.subplots_adjust(left=.075, right=.975, bottom=.19, top=.745, wspace=.3)
fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
plt.close(fig)
