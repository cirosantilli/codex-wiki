"""Homology sketches. Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Writes only paper-42-homology-sequences.png to the caller's working directory.
The caller may supply MPLCONFIGDIR; this script leaves it unchanged.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7.8, 5.6), layout="constrained")
fig.patch.set_facecolor("white")
ax.set_facecolor("white")
for transition, color, style, name in [
    (4 / 3, "#2457a7", "-", "Solar CNO"),
    (8 / 3, "#a54913", "--", "CNO / 256"),
]:
    mass = np.geomspace(0.7, transition, 100)
    lum = mass ** (11 / 2)
    temp = lum ** 0.25
    ax.plot(np.log10(temp), np.log10(lum), color=color, linestyle=style,
            linewidth=2.5, label=f"{name}: pp")
    mass = np.geomspace(transition, 8, 120)
    radius = (mass / transition) ** (4 / 7)
    lum = transition ** (11 / 2) * (mass / transition) ** (73 / 14)
    temp = (lum / radius ** 2) ** 0.25
    ax.plot(np.log10(temp), np.log10(lum), color=color, linestyle=style,
            linewidth=1.9, label=f"{name}: CNO")
    ax.plot(np.log10(transition ** (11 / 8)), np.log10(transition ** (11 / 2)),
            "o", color=color, markersize=7)
    ax.annotate(f"Transition: {transition:.2f} solar masses",
                (np.log10(transition ** (11 / 8)), np.log10(transition ** (11 / 2))),
                xytext=(12, -22 if transition < 2 else 12), textcoords="offset points",
                fontsize=9, color=color)
ax.invert_xaxis()
ax.set_xlabel(r"$\log_{10}(T_{\rm eff}/T_{{\rm eff},\odot})$  (hotter to the left)")
ax.set_ylabel(r"$\log_{10}(L/L_\odot)$")
ax.set_title("Idealized radiative homology: pp and CNO branches")
ax.grid(alpha=0.22)
ax.legend(loc="upper right", fontsize=9)
fig.savefig("paper-42-homology-sequences.png", dpi=140, facecolor="white", transparent=False)
plt.close(fig)
