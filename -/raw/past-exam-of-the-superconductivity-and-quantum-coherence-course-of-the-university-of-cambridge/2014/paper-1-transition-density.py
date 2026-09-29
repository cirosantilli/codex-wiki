"""Original prescribed-cutoff-model density comparison; write PNG to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

hbar, mass, kb = 1.054571817e-34, 9.1093837139e-31, 1.380649e-23
theta_over_k, coupling, bose_integral = 1000.0, 0.3, 2.3
n_theta = (2 * mass * kb * theta_over_k / hbar**2)**1.5 / (3 * np.pi**2)
a = 1.13 * np.exp(-1 / coupling)
cb = 0.5 * (2 / (3 * bose_integral))**(2 / 3)
n = np.geomspace(1e20, 1e29, 600)
u = n / n_theta
tf = theta_over_k * u**(2 / 3)
tc = theta_over_k * a * np.minimum(1, u**(1 / 3))
tb = cb * tf
n_cross = n_theta * (a / cb)**3
t_cross = theta_over_k * a**2 / cb
n_bad = n_theta * a**3
fig, ax = plt.subplots(figsize=(10.5, 6.2), dpi=100, facecolor="white")
ax.loglog(n, tc, lw=2.6, label=r"Asymptotic cutoff-model $T_c$ (fixed $\lambda=0.3$)")
ax.loglog(n, tb, lw=2.5, label=r"Ideal pair condensation $T_B\simeq0.219T_F$")
ax.loglog(n, tf, color="0.5", ls=":", lw=1.6, label=r"Assumed $\mu/k_B\simeq T_F$")
ax.axvspan(n.min(), n_bad, color="tab:red", alpha=0.10)
ax.axvline(n_theta, color="0.5", lw=1, ls="--")
ax.scatter([n_cross], [t_cross], color="black", s=35, zorder=5)
ax.annotate(r"Formal crossing: $n\simeq7.2\times10^{23}\,\mathrm{m}^{-3}$, $T\simeq7.4$ K",
            (n_cross, t_cross), (1.5e24, 0.5), fontsize=10, arrowprops={"arrowstyle": "->"})
ax.text(1.4e20, 2e3, "Shaded: extrapolated\n" + r"$k_BT_c>\mu$;" + "\nweak-coupling\napproximations fail", fontsize=10)
ax.text(1.6e26, 2e3, r"$\mu=\theta$", fontsize=11)
ax.set(xlabel=r"Electron density $n$ ($\mathrm{m}^{-3}$)", ylabel="Temperature (K)",
       title="Three-dimensional parabolic band with a prescribed constant pairing coupling",
       xlim=(1e20, 1e29), ylim=(1e-3, 1e5))
ax.grid(alpha=0.18, which="both")
ax.legend(loc="lower right", fontsize=10)
fig.text(0.5, 0.025, "The asymptotic low-density excess is not a self-consistent prediction for the BCS–BEC crossover.",
         ha="center", fontsize=10.5)
fig.subplots_adjust(left=0.09, right=0.985, top=0.9, bottom=0.15)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white")
