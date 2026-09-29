"""Calculated rigid-rotor level populations; no observed data are reproduced."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

h, k, c, u = 6.62607015e-34, 1.380649e-23, 299792458., 1.66053906892e-27
inertia = (12*32/44*u)*(1.53e-10)**2
theta = h*h/(8*np.pi**2*inertia*k)
fig, axs = plt.subplots(1, 2, figsize=(10, 3.6), dpi=150)
for ax, temperature, largest in zip(axs, (300., 8.7), (36, 7)):
    j = np.arange(largest+1)
    population = (2*j+1)*np.exp(-theta*j*(j+1)/temperature)
    smooth = np.linspace(0, largest, 800)
    ax.plot(smooth, (2*smooth+1)*np.exp(-theta*smooth*(smooth+1)/temperature),
            color="#8c99a5", lw=1, label="continuous guide")
    ax.vlines(j, 0, population, color="#226c9c", lw=1.8)
    ax.plot(j, population, "o", color="#226c9c", ms=3)
    maximum = int(j[np.argmax(population)])
    ax.annotate(f"integer maximum: J = {maximum}", (maximum, population[maximum]),
                (8, 10), textcoords="offset points", fontsize=10)
    ax.set(title=f"Carbon monosulfide, T = {temperature:g} K",
           xlabel="rotational quantum number J", ylabel=r"$N_J/N_0$", ylim=(0, max(population)*1.25))
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", alpha=.2)
fig.suptitle(r"Calculated rigid-rotor populations: $\tilde B=0.8252\ \mathrm{cm}^{-1}$", fontsize=13)
fig.tight_layout()
fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
