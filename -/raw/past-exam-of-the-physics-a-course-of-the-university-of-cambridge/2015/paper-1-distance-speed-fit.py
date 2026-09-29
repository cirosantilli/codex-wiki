"""Original plot of numerical observations and derived fit; no source figure used."""
import numpy as np
import matplotlib.pyplot as plt

d = np.array([50, 650, 800, 900, 1100, 1400, 1600, 1650, 2000.])/1000
v = np.array([40, 170, 380, 500, 750, 780, 730, 1000, 1100.])
h = d@v/(d@d)
s = np.sqrt(np.sum((v-h*d)**2)/(len(d)-1))
se = s/np.sqrt(d@d)
fig, (ax, res) = plt.subplots(2, 1, figsize=(7.8, 6.1), sharex=True, height_ratios=[3, 1], layout="constrained")
x = np.linspace(0, 2.12, 200)
ax.plot(x, h*x, color="#175b98", lw=1.8, label="Fit constrained through origin")
ax.scatter(d, v, s=37, color="#a84a24", zorder=3, label="Numerical observations")
ax.text(.05, .96, rf"$H={h:.1f}\pm {se:.1f}$ km s$^{{-1}}$ Mpc$^{{-1}}$"+"\nUncertainty: estimated standard error", va="top", transform=ax.transAxes, fontsize=10)
ax.set(ylabel=r"Speed / km s$^{-1}$", title="Distance-speed fit with equal speed-error weights", xlim=(0, 2.12), ylim=(0, 1260))
ax.legend(loc="lower right", fontsize=9)
res.axhline(0, color="0.3", lw=1)
res.scatter(d, v-h*d, color="#a84a24", s=29)
res.set(xlabel="Distance / Mpc", ylabel=r"Residual / km s$^{-1}$", ylim=(-210, 180))
for a in [ax, res]:
    a.grid(alpha=.18)
fig.savefig("paper-1-distance-speed-fit.png", dpi=150, facecolor="white")
