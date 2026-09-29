"""Calculated weak-field two-level force; Python 3.14 / matplotlib 3.10.7.

Uses numpy 2.3.5. Run from _media; emits its basename.png.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

u = np.linspace(-2, 2, 1601)
d = -.5
force = 1/(1+4*(d-u)**2) - 1/(1+4*(d+u)**2)
fig, axes = plt.subplots(1, 2, figsize=(9.2, 4.6), facecolor="white", gridspec_kw={"width_ratios": [1.7, 1]})
fig.subplots_adjust(left=.09, right=.98, bottom=.20, top=.76, wspace=.35)
fig.suptitle("Red detuning gives velocity damping", fontsize=17, y=.96)
fig.text(.5, .85, r"$F(u)=[1+4(d-u)^2]^{-1}-[1+4(d+u)^2]^{-1},\quad d=-0.5$", ha="center", fontsize=13)
blue = "#2768a7"
for ax in axes:
    ax.axhline(0, color="#777777", lw=1)
    ax.axvline(0, color="#777777", lw=1)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_xlabel(r"Velocity $u=kv/\Gamma$", fontsize=12)
    ax.set_ylabel(r"Force $F=f/(\hbar k\Gamma s/2)$", fontsize=11)
axes[0].plot(u, force, color=blue, lw=2.5)
axes[0].set(xlim=(-2, 2), ylim=(-1, 1), title="Full calculated model")
axes[0].text(-1.88, .87, r"$u<0$: force to the right", fontsize=11, color=blue)
axes[0].text(.12, -.90, r"$u>0$: force to the left", fontsize=11, color=blue)
axes[0].annotate("Scattering weakens\nat large speed", (1.5, float(1/(1+4*(d-1.5)**2)-1/(1+4*(d+1.5)**2))),
                 xytext=(.45, .40), fontsize=10, arrowprops=dict(arrowstyle="->", color="#555555"))
axes[1].plot(u, force, color=blue, lw=2.5, label="Exact model")
axes[1].plot(u, -2*u, color="#bb591b", ls="--", lw=2, label=r"Tangent $F=-2u$")
axes[1].set(xlim=(-.3, .3), ylim=(-.65, .65), title="Near zero velocity")
axes[1].legend(loc="upper right", fontsize=9, frameon=False)
axes[1].plot(.25, -32/65, "o", color=blue, ms=6)
axes[1].annotate(r"$F(0.25)=-32/65$", (.25, -32/65), xytext=(-.28, -.59), fontsize=10,
                 arrowprops=dict(arrowstyle="->", color="#555555"))
fig.text(.5, .04, "Calculated force, not experimental points. Equal weak beams; no position restoring force.", ha="center", fontsize=10)
fig.savefig(Path(__file__).stem + ".png", dpi=110, facecolor="white")
plt.close(fig)
