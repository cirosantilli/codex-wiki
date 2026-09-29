"""Original principal-axis sketch of a rotated quadratic surface."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(7.1, 5.4), layout="constrained")
ax = fig.add_subplot(projection="3d")
theta, phi = np.meshgrid(np.linspace(0, np.pi, 45), np.linspace(0, 2*np.pi, 65))
short = 1 / np.sqrt(3)
u = np.cos(theta)
v = short * np.sin(theta) * np.cos(phi)
z = short * np.sin(theta) * np.sin(phi)
ax.plot_surface(u, v, z, color="cornflowerblue", alpha=0.3, linewidth=0,
                shade=False, rstride=2, cstride=2)
for vector, label, color in [([1, 0, 0], "$1$", "tab:red"),
                             ([0, short, 0], r"$1/\sqrt{3}$", "tab:green"),
                             ([0, 0, short], r"$1/\sqrt{3}$", "tab:purple")]:
    vector = np.array(vector)
    ax.plot([-vector[0], vector[0]], [-vector[1], vector[1]],
            [-vector[2], vector[2]], lw=2.4, color=color)
    ax.scatter(*vector, s=25, color=color)
    ax.text(*(1.14*vector), label, color=color, fontsize=12)
ax.set(xlabel="$u$", ylabel="$v$", zlabel="$z$", xlim=(-1.2, 1.2),
       ylim=(-0.8, 0.8), zlim=(-0.8, 0.8),
       title=r"$u^2+3v^2+3z^2=1$"+"\n"+r"$u=(x+y)/\sqrt{2}$, $v=(x-y)/\sqrt{2}$")
ax.set_box_aspect((2.4, 1.6, 1.6))
ax.view_init(elev=21, azim=-55)
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
