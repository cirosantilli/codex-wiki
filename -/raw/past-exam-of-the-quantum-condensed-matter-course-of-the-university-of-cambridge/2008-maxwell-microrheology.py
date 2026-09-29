"""Original Maxwell-compliance prediction, not an experimental MSD dataset."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

kb = 1.380649e-23
temperature = 300.0
radius = 1e-6
mesh = 500e-9
viscosity = 1e-3
modulus = kb * temperature / mesh**3
tau = viscosity / modulus
plateau = kb * temperature / (np.pi * radius * modulus) * 1e12
time = np.geomspace(1e-4, 3, 900)
fig, ax = plt.subplots(figsize=(8.1, 4.5), layout="constrained")
ax.axvspan(1/30, 3, color="gold", alpha=0.10,
           label="lags at least one frame at 30 fps")
ax.loglog(time, plateau*(1+time/tau), color="tab:blue", lw=2.3,
          label="ideal Maxwell compliance prediction")
ax.axhline(plateau, color="0.5", ls="--", lw=1.1, label="elastic plateau scale")
long = time[time >= tau]
ax.loglog(long, plateau*long/tau, color="tab:orange", ls=":", lw=2,
          label="long-time diffusive asymptote")
ax.axvline(tau, color="tab:red", ls="--", lw=1.1)
ax.text(tau*0.82, 2.8, r"$\tau\simeq0.030\,\mathrm{s}$", rotation=90,
        color="tab:red", ha="right", va="top", fontsize=10)
ax.set(xlim=(time[0], time[-1]), ylim=(0.02, 7), xlabel="Lag time (s)",
       ylabel=r"Three-dimensional MSD ($\mu\mathrm{m}^2$)",
       title="Maxwell fluid: intermediate and long time response")
ax.grid(which="both", alpha=0.14)
ax.legend(loc="upper left", fontsize=9)
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
