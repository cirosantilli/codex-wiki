"""Original square reciprocal lattice and monovalent free-electron disk."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle

fig, ax = plt.subplots(figsize=(7.1, 6), constrained_layout=True)
zone = Rectangle((-1, -1), 2, 2, fc="#eaf1f8", ec="#245c9f", lw=2,
                 label="first Brillouin zone")
disk = Circle((0, 0), np.sqrt(2 / np.pi), fc="#c9dfce", ec="#21633d", lw=2,
              label="occupied disk: half the zone area")
ax.add_patch(zone)
ax.add_patch(disk)
points = np.array([(i, j) for i in [-2, 0, 2] for j in [-2, 0, 2]])
ax.scatter(points[:, 0], points[:, 1], color="0.15", s=25, zorder=4)
ax.axhline(0, color="0.6", lw=0.7, zorder=0)
ax.axvline(0, color="0.6", lw=0.7, zorder=0)
ax.annotate(r"$k_Fa/\pi=\sqrt{2/\pi}$", (0.56, 0.56), (1.02, 1.28),
            arrowprops={"arrowstyle": "-", "color": "#21633d"}, fontsize=11,
            color="#21633d")
ax.text(2, 0.14, r"$(2\pi/a,0)$", ha="center", fontsize=10)
ax.text(0.15, 2.0, r"$(0,2\pi/a)$", ha="left", fontsize=10)
ax.text(0.08, -0.18, r"$\Gamma$", fontsize=12)
ax.text(-0.98, -1.20, r"zone edge: $k_y=-\pi/a$", color="#245c9f", fontsize=10)
ax.set(xlim=(-2.55, 2.55), ylim=(-2.5, 2.55), aspect="equal",
       xticks=[-2, -1, 0, 1, 2], yticks=[-2, -1, 0, 1, 2],
       xlabel=r"$k_xa/\pi$", ylabel=r"$k_ya/\pi$",
       title="One electron per square cell; two spin states per wavevector")
ax.legend(handles=[zone, disk], loc="lower center", frameon=False, fontsize=10)
ax.spines[["top", "right"]].set_visible(False)
fig.savefig("paper-2-fermi-circle.png", dpi=150, facecolor="white")
plt.close(fig)
