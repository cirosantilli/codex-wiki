"""Original dipole-limit patterns, not copied source figures; Python 3.14."""
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 1000)
mu = np.cos(theta)
electric = (1+mu**2)/2
pec = 5*(1+mu**2)/8-mu
fig = plt.figure(figsize=(9.0, 4.7), layout="constrained")
ax = fig.add_subplot(1, 2, 1, projection="polar")
ax.plot(theta, electric, lw=2, label="Electric dipole only")
ax.plot(theta, pec, lw=2, label="Electric + magnetic (PEC)")
ax.set_theta_zero_location("E")
ax.set_thetagrids([45, 90, 135, 225, 270, 315])
ax.set_rmax(2.4)
ax.set_rticks([.5, 1, 1.5, 2])
ax.set_title("Unpolarized differential scattering\nradius = cross section / $k^4a^6$", fontsize=11, pad=17)
ax.text(0, 2.4, "Forward", ha="left", va="center", fontsize=9)
ax.text(np.pi, 2.4, "Backward", ha="right", va="center", fontsize=9)
ax.legend(loc="lower center", bbox_to_anchor=(.5, -.24), fontsize=8)
right = fig.add_subplot(1, 2, 2)
angle = np.linspace(0, 180, 900)
z = np.cos(np.deg2rad(angle))
right.plot(angle, (1+z*z)/2, lw=2, label="Electric only")
right.plot(angle, 5*(1+z*z)/8-z, lw=2, label="PEC: both dipoles")
right.scatter([180, 180], [1, 2.25], color=["C0", "C1"], zorder=5)
right.annotate("Backward intensity ratio: 9/4\nRange ratio: sqrt(3/2)", xy=(180, 2.25), xytext=(20, 1.8), fontsize=9, arrowprops=dict(arrowstyle="->"))
right.set(xlabel="Scattering angle / degrees", ylabel=r"$(d\sigma/d\Omega)/(k^4a^6)$", title="Leading Rayleigh-limit response", xlim=(0, 180), ylim=(0, 2.55))
right.grid(alpha=.18)
fig.savefig("paper-1-radar-scattering.png", dpi=150, facecolor="white")
