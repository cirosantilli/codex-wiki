"""Internal-wave fields and envelope. Output PNG basename to caller CWD.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
import os
import tempfile

if "MPLCONFIGDIR" not in os.environ:
    os.environ["MPLCONFIGDIR"] = tempfile.mkdtemp(prefix="paper-72-mpl-")

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10.2, 7.5), layout="constrained")
grid = fig.add_gridspec(2, 2, height_ratios=(1.4, 0.7))
axes = [fig.add_subplot(grid[0, 0]), fig.add_subplot(grid[0, 1])]
v = np.linspace(-np.pi, np.pi, 150)
X, Z = np.meshgrid(v, v)
theta = -X - Z
q = np.linspace(-2.8, 2.8, 12)
QX, QZ = np.meshgrid(q, q)
qt = -QX - QZ
for ax, field, arrows, title in [
    (axes[0], np.sin(theta), np.sin(qt), r"Pressure $p/A$ and velocity $\mathbf{u}/(\omega A)$"),
    (axes[1], -np.cos(theta), np.cos(qt), r"Buoyancy $\sigma/(N^2A)$ and displacement $\mathbf{\xi}/A$"),
]:
    mesh = ax.pcolormesh(X, Z, field, cmap="coolwarm", vmin=-1, vmax=1, shading="auto", rasterized=True)
    ax.contour(X, Z, theta, levels=np.arange(-6, 7, 2), colors="white", alpha=0.6, linewidths=0.7)
    ax.quiver(QX, QZ, -arrows, arrows, color="#15191f", pivot="mid", scale=22, width=0.005)
    ax.set(xlabel="x (wave-number units)", ylabel="z", title=title, aspect="equal", xlim=(-np.pi, np.pi), ylim=(-np.pi, np.pi))
    fig.colorbar(mesh, ax=ax, shrink=0.8, ticks=(-1, 0, 1))
axes[0].arrow(-0.4, -1.2, -1.2, -1.2, color="#2b6544", width=0.035, head_width=0.17, length_includes_head=True, zorder=8)
axes[0].text(-0.45, -1.1, r"$\mathbf{c}_p$", color="#2b6544", fontsize=12, bbox={"facecolor":"white", "alpha":0.7, "edgecolor":"none"}, zorder=9)
axes[0].arrow(-0.4, 1.2, -1.2, 1.2, color="#533b7c", width=0.035, head_width=0.17, length_includes_head=True, zorder=8)
axes[0].text(-0.45, 0.8, r"$\mathbf{c}_g$", color="#533b7c", fontsize=12, bbox={"facecolor":"white", "alpha":0.7, "edgecolor":"none"}, zorder=9)
axes[1].text(0.02, 0.02, r"$k=m=-1,\ N=\sqrt{2},\ \omega=1,\ t=0$", transform=axes[1].transAxes, fontsize=9, bbox={"facecolor":"white", "alpha":0.85, "edgecolor":"none"})
ax = fig.add_subplot(grid[1, :])
s = np.linspace(0, 3, 500)
retarded = np.clip(2-s, 0, 1)
amp = 6*retarded**5-15*retarded**4+10*retarded**3
ax.plot(s, amp, color="#1760a3", lw=2.5)
ax.axvline(1, color="#7c8796", ls=":")
ax.axvline(2, color="#7c8796", ls=":")
ax.set(xlabel=r"Slow height $Z/c_{gz}$", ylabel=r"Envelope $A/\epsilon$", title=r"Upward-radiating boundary wave at $T=2$: representative smooth ramp", xlim=(0, 3), ylim=(-0.08, 1.2))
ax.text(0.25, 1.07, "Fully established")
ax.text(1.18, 1.07, "Transition")
ax.text(2.2, 1.07, "Unreached")
ax.grid(alpha=0.2)
fig.savefig("paper-72-wave.png", dpi=125, facecolor="white", transparent=False)
plt.close(fig)
