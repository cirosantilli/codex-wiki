"""Original contour sketch. Python 3.14; numpy 2.3.5, matplotlib 3.10.7.

Writes paper-3-harmonic-contours.png to the caller's current directory.
Uses Matplotlib's supplied MPLCONFIGDIR without replacing it.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7.6, 6.1), dpi=110, facecolor="white")
ax.set_facecolor("white")
radii = [0.75, 1.4, 2.1, 2.8]
for radius in radii:
    for low, high in [(-np.pi / 2 + .018, np.pi / 2 - .018),
                      (np.pi / 2 + .018, 3 * np.pi / 2 - .018)]:
        angle = np.linspace(low, high, 250)
        ax.plot(radius * np.cos(angle), radius * np.sin(angle),
                color="#24649d", linewidth=1.8)
    ax.scatter([0, 0], [radius, -radius], facecolors="white",
               edgecolors="#24649d", s=24, zorder=5)
for angle in [-np.pi / 3, -np.pi / 6, 0, np.pi / 6, np.pi / 3]:
    length = np.linspace(.065, 3.1, 100)
    for sign in [-1, 1]:
        ax.plot(sign * length * np.cos(angle), sign * length * np.sin(angle),
                color="#b54436", linewidth=1.4)
ax.axvline(0, color="#777777", linewidth=1, linestyle=":")
ax.scatter([0], [0], facecolors="white", edgecolors="black", s=35, zorder=6)
ax.text(.09, 3.0, r"$x=0$ excluded", color="#555555", fontsize=10)
ax.text(1.72, 2.66, r"$\phi=\pi/3$", color="#b54436", fontsize=11)
ax.text(2.69, 1.56, r"$\phi=\pi/6$", color="#b54436", fontsize=11)
ax.text(2.85, .09, r"$\phi=0$", color="#b54436", fontsize=11)
ax.text(-3.05, -1.68, r"same $\phi=\pi/6$", color="#b54436", fontsize=10)
for radius, x in zip(radii, [.43, .57, .78, 1.06]):
    y = -np.sqrt(radius * radius - x * x)
    ax.annotate(rf"$r={radius:g}$", xy=(x, y), xytext=(x + .17, y - .15),
                color="#24649d", fontsize=9,
                arrowprops={"arrowstyle": "-", "color": "#24649d"})
ax.plot([], [], color="#b54436", label=r"$\phi=\arctan(y/x)$: opposite rays")
ax.plot([], [], color="#24649d", label=r"$\psi=-\log r$: circles")
ax.set(xlim=(-3.4, 3.4), ylim=(-3.4, 3.4), xlabel="$x$", ylabel="$y$")
ax.set_aspect("equal")
ax.set_title("Harmonic angle and logarithmic radius")
ax.legend(loc="lower center", bbox_to_anchor=(.5, -.25), frameon=False, fontsize=10)
fig.subplots_adjust(bottom=.21, top=.92, left=.12, right=.94)
fig.savefig("paper-3-harmonic-contours.png", facecolor="white", transparent=False)
plt.close(fig)
