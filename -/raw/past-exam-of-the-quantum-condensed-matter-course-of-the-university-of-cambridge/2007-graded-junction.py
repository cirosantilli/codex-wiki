"""Original depletion-model band diagram and field for a graded p-n junction."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1.8, 1.8, 700)
s = np.clip(x, -1, 1)
potential = 0.5 + 0.75 * s - 0.25 * s**3
field = np.where(abs(x) <= 1, x**2 - 1, 0)
fig, (bands, electric) = plt.subplots(2, 1, figsize=(8.1, 6.2), sharex=True,
                                     layout="constrained", height_ratios=[1.5, 1])
bands.plot(x, 1.8 - 1.6 * potential, color="#245b9f", lw=2.2, label=r"$E_c$")
bands.plot(x, -0.2 - 1.6 * potential, color="#a34828", lw=2.2, label=r"$E_v$")
bands.axhline(0, color="0.2", ls="--", lw=1.3, label=r"equilibrium $\mu$")
bands.set(ylim=(-2.1, 2.1), ylabel="Electron energy (illustrative units)",
          title="Linearly graded p-n junction in equilibrium")
bands.text(-1.72, 1.93, "p-type", fontsize=11)
bands.text(1.72, 1.93, "n-type", ha="right", fontsize=11)
bands.legend(loc="lower left", fontsize=10)
electric.plot(x, field, color="#6c4394", lw=2.2)
electric.fill_between(x, field, 0, color="#ece4f4")
electric.axhline(0, color="0.5", lw=0.8)
electric.annotate("largest field magnitude", xy=(0, -1), xytext=(0.25, -0.68),
                  arrowprops={"arrowstyle": "->", "lw": 0.9}, fontsize=10)
electric.set(xlim=(-1.8, 1.8), ylim=(-1.2, 0.25), xlabel=r"Position $x/d$",
             ylabel=r"$E_x\,/\,[q\alpha d^2/(2\varepsilon_s)]$")
electric.set_xticks([-1, 0, 1], [r"$-1$ (edge)", "0", r"$+1$ (edge)"])
for ax in [bands, electric]:
    for edge in [-1, 1]:
        ax.axvline(edge, color="0.5", ls=":", lw=1)
    ax.grid(alpha=0.13)
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
