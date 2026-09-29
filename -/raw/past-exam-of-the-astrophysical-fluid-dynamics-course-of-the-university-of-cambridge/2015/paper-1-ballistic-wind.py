"""Original pressure-negligible marginal-escape wind profiles, gamma=5/3."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

x = np.geomspace(1, 100, 501)
fig, ax = plt.subplots(figsize=(9, 5.3), dpi=100, facecolor="white")
for power, name in [(0.5, r"$v/v_e=x^{-1/2}$"), (1.5, r"$\rho/\rho_e=x^{-3/2}$"),
                    (1.0, r"$T/T_e=x^{-1}$"), (2.5, r"$p/p_e=x^{-5/2}$")]:
    ax.loglog(x, x**(-power), lw=2.4, label=name)
ax.set(xlabel=r"Radius $x=r/R_e$", ylabel="Profile divided by its value at the reference radius",
       xlim=(1, 100), ylim=(8e-6, 1.3), title=r"Adiabatic profiles along a ballistic wind, $\gamma=5/3$")
ax.grid(alpha=0.25, which="both"); ax.legend(loc="lower left")
fig.text(0.5, 0.025, "Assumes negligible pressure force; finite enthalpy changes the velocity solution.", ha="center", fontsize=11)
fig.subplots_adjust(left=0.105, right=0.98, top=0.89, bottom=0.18)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white")
