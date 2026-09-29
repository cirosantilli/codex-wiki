"""Original Apollonius loci and harmonic potential; Python 3.14, NumPy, Matplotlib."""
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

fig, (family, potential) = plt.subplots(1, 2, figsize=(10.4, 4.5), layout="constrained", facecolor="white")
for ratio, color in [(0.25, "#287cae"), (0.5, "#38864c"), (2, "#b85121"), (4, "#8b4f9e")]:
    centre = (1 + ratio**2) / (1 - ratio**2)
    radius = 2 * ratio / abs(1 - ratio**2)
    family.add_patch(Circle((centre, 0), radius, fill=False, lw=1.8, color=color, label=rf"$\lambda={ratio:g}$"))
family.axvline(0, color="black", ls="--", lw=1.2, label=r"$\lambda=1$")
family.scatter([-1, 1], [0, 0], color="black", s=25)
family.text(-1, -0.23, "-a", ha="center")
family.text(1, -0.23, "a", ha="center")
family.set(xlim=(-3.3, 3.3), ylim=(-2.3, 2.3), xlabel="x / a", ylabel="y / a", title="Distance-ratio circles and the exceptional line")
family.legend(fontsize=8, ncols=3, loc="upper center")
family.set_aspect("equal")
family.grid(alpha=0.15)
d, radius = 2, 1
a = np.sqrt(d*d - radius*radius)
tau = np.arccosh(d / radius)
x = np.linspace(0, 5, 501)
y = np.linspace(-3, 3, 501)
xx, yy = np.meshgrid(x, y)
dist_plus = np.hypot(xx - a, yy)
dist_minus = np.hypot(xx + a, yy)
values = np.log(dist_plus / dist_minus) / tau
values = np.ma.masked_where((xx - d)**2 + yy**2 <= radius**2, values)
contours = potential.contour(xx, yy, values, levels=[-0.9, -0.7, -0.5, -0.3, -0.1], cmap="viridis", linewidths=1.5)
potential.clabel(contours, fontsize=8, fmt="%.1f")
potential.add_patch(Circle((d, 0), radius, facecolor="#d8dde2", edgecolor="black", lw=1.4, zorder=3))
potential.text(d, 0, r"$V=-V_0$", ha="center", fontsize=12, zorder=4)
potential.axvline(0, color="black", lw=1.5)
potential.text(0.08, 2.6, "V = 0", fontsize=10)
potential.set(xlim=(-0.06, 5), ylim=(-3, 3), xlabel="x / R", ylabel="y / R", title=r"Contours of $V/V_0$, example $d/R=2$")
potential.set_aspect("equal")
fig.savefig("paper-1-q7-circle-line-potential.png", dpi=165, facecolor="white", bbox_inches="tight")
plt.close(fig)
