"""Original comparison of fixed-composition adiabatic and isothermal shocks."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

mach = np.linspace(1, 10, 501); gamma = 5 / 3
adiabatic = (gamma + 1) / (gamma - 1 + 2 / mach**2)
isothermal = mach**2
fig, ax = plt.subplots(figsize=(9, 5.3), dpi=100, facecolor="white")
ax.plot(mach, adiabatic, lw=2.5, label=r"Adiabatic: $\gamma=5/3$")
ax.plot(mach, isothermal, lw=2.5, label="Isothermal: efficient energy loss")
ax.axhline(4, color="0.4", ls="--", lw=1)
ax.text(6.0, 4.35, "Adiabatic strong-shock limit", color="0.3", fontsize=11)
ax.set(xlabel=r"Upstream Mach number $\mathcal{M}_1$ (own sound-speed convention)",
       ylabel=r"Compression ratio $\rho_2/\rho_1$", yscale="log", xlim=(1, 10), ylim=(0.9, 120),
       title="Cooling permits much larger shock compression")
ax.grid(alpha=0.25, which="both"); ax.legend(loc="upper left")
fig.text(0.5, 0.025, "Each Mach number uses its model's upstream sound speed; compare speeds with care.", ha="center", fontsize=10.5)
fig.subplots_adjust(left=0.105, right=0.98, top=0.89, bottom=0.18)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white")
