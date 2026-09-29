"""Original schematic radiative-shock profile; write PNG to working directory.

The hot and cooled endpoints satisfy exact perfect-gas jump conditions.
The downstream path conserves mass and momentum. Its spatial parametrization
is illustrative, not the solution of a specified radiative cooling law.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

gamma, mach = 5 / 3, 8.0
u_squared = gamma * mach**2  # Upstream rho=p=T=1, so isothermal sound speed=1.
hot_density = (gamma + 1) * mach**2 / ((gamma - 1) * mach**2 + 2)
hot_pressure = (2 * gamma * mach**2 - (gamma - 1)) / (gamma + 1)
hot_temperature = hot_pressure / hot_density
hot_entropy = np.log(hot_pressure / hot_density**gamma)
cooled_density = u_squared
cooled_entropy = -(gamma - 1) * np.log(cooled_density)
cool_x = np.linspace(0, 5, 650)
fraction = (1 - np.exp(-cool_x)) / (1 - np.exp(-5))
density = hot_density + (cooled_density - hot_density) * fraction
temperature = (1 + u_squared) / density - u_squared / density**2
entropy = np.log(temperature / density**(gamma - 1))
fig, axes = plt.subplots(2, 1, figsize=(10.5, 6.5), dpi=100, facecolor="white", sharex=True)
for ax, hot, downstream, final, ylabel in zip(
    axes, [hot_temperature, hot_entropy], [temperature, entropy],
    [1, cooled_entropy], [r"Temperature $T/T_1$", r"Specific entropy $(s-s_1)/c_v$"]
):
    initial = 1 if ax is axes[0] else 0
    ax.plot([-0.85, -0.055], [initial, initial], color="tab:blue", lw=2.5)
    ax.plot([-0.055, 0], [initial, hot], color="tab:red", lw=2.5)
    ax.plot(cool_x, downstream, color="tab:blue", lw=2.5)
    ax.plot([5, 5.7], [final, final], color="tab:blue", lw=2.5)
    ax.axvspan(-0.055, 0, color="tab:red", alpha=0.16)
    ax.axvspan(0, 5, color="tab:orange", alpha=0.06)
    ax.axhline(initial, color="0.5", ls=":", lw=1)
    ax.set(ylabel=ylabel, xlim=(-0.85, 5.7))
    ax.grid(alpha=0.2)
axes[0].annotate("Thin irreversible jump", (0, hot_temperature), (0.65, hot_temperature * 0.85),
                 arrowprops={"arrowstyle": "->"}, fontsize=10)
axes[0].text(2.0, hot_temperature * 0.48, "Radiative cooling + compression", fontsize=10.5)
axes[1].annotate("Gas loses entropy to escaping radiation", (1.5, np.interp(1.5, cool_x, entropy)),
                 (1.1, 1.1), arrowprops={"arrowstyle": "->"}, fontsize=10)
axes[0].set_title(r"Adiabatic jump followed by cooling: $\gamma=5/3$, upstream adiabatic $\mathcal{M}_1=8$")
axes[1].set_xlabel("Downstream distance (schematic units; microscopic jump greatly enlarged)")
fig.text(0.5, 0.025, "Exact endpoint states and downstream mass/momentum balance; no spatial cooling law is assumed.",
         ha="center", fontsize=10)
fig.subplots_adjust(left=0.10, right=0.98, top=0.90, bottom=0.13, hspace=0.14)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white")
