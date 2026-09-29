"""Original hoop constraint and energy diagram; Python 3.14, NumPy, Matplotlib."""
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc

fig, (geometry, energy) = plt.subplots(1, 2, figsize=(9.6, 4.8), layout="constrained", facecolor="white")
ratio = 0.5
theta0 = np.arcsin(ratio)
geometry.add_patch(Circle((0, 0), 1, fill=False, edgecolor="#287cae", lw=2))
geometry.add_patch(Circle((1.3, 2), 0.3, facecolor="#e1e6ea", edgecolor="0.4", lw=1.2))
arc = np.linspace(theta0, np.pi/2, 150)
geometry.plot(np.sin(arc), -np.cos(arc), color="#be6d1c", lw=3)
geometry.plot([1, 1], [0, 2], color="#be6d1c", lw=2)
pulley_arc = np.linspace(0, np.pi, 100)
geometry.plot(1.3 + 0.3*np.cos(pulley_arc), 2 + 0.3*np.sin(pulley_arc), color="#be6d1c", lw=2)
geometry.plot([1.6, 1.6], [2, 0.65], color="#be6d1c", lw=2)
point = [np.sin(theta0), -np.cos(theta0)]
geometry.plot([0, point[0]], [0, point[1]], "--", color="0.35", lw=1.2)
geometry.plot([0, 0], [0, -1.1], ":", color="0.5", lw=1)
geometry.add_patch(Arc((0, 0), 0.65, 0.65, theta1=-90, theta2=-90+np.rad2deg(theta0), color="black"))
geometry.text(0.08, -0.42, r"$\theta$", fontsize=12)
geometry.text(0.34, -0.42, "R", fontsize=11)
geometry.scatter([0], [0], color="black", s=20)
geometry.scatter([point[0]], [point[1]], color="black", s=85, zorder=5)
geometry.text(point[0]+0.15, point[1]-0.04, "M", fontsize=12)
geometry.scatter([1.6], [0.65], color="#287cae", s=65, zorder=5)
geometry.text(1.76, 0.62, "m", fontsize=12)
geometry.annotate("", (1.6, 0.13), (1.6, 0.5), arrowprops={"arrowstyle":"->", "color":"#287cae", "lw":1.5})
geometry.text(1.83, 0.22, r"$R\theta$", color="#287cae", fontsize=11)
geometry.set(xlim=(-1.2, 2.3), ylim=(-1.2, 2.55), title="A larger angle releases wrapped string")
geometry.set_aspect("equal")
geometry.axis("off")
theta = np.linspace(0, np.pi/2, 600)
v = -np.cos(theta)-ratio*theta
minimum = -np.cos(theta0)-ratio*theta0
energy.plot(theta, v, color="#287cae", lw=2, label="Exact potential")
near = np.linspace(theta0-0.35, theta0+0.35, 200)
energy.plot(near, minimum+0.5*np.cos(theta0)*(near-theta0)**2, "--", color="#be6d1c", lw=1.7, label="Quadratic approximation")
energy.scatter([theta0], [minimum], color="black", s=30, zorder=4)
energy.axvline(theta0, color="0.5", ls=":", lw=1)
energy.set(xlim=(0, np.pi/2), xlabel=r"$\theta$", ylabel=r"$V/(MgR)=-\cos\theta-(m/M)\theta$", title=r"Stable equilibrium, example $m/M=1/2$")
energy.set_xticks([0, theta0, np.pi/2], ["0", r"$\theta_0=\pi/6$", r"$\pi/2$"])
energy.grid(alpha=0.17)
energy.legend(fontsize=9, loc="upper left")
fig.savefig("paper-1-q9-hoop-counterweight.png", dpi=165, facecolor="white", bbox_inches="tight")
plt.close(fig)
