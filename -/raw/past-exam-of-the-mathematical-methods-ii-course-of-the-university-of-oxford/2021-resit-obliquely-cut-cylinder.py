"""Draw the solution geometry; tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
fig = plt.figure(figsize=(8, 6), dpi=120, facecolor="white")
ax = fig.add_subplot(projection="3d", facecolor="white")
theta = np.linspace(0, 2 * np.pi, 161)
s = np.linspace(-3, 2, 35)
th, offset = np.meshgrid(theta, s)
x, y = 2 * np.cos(th), 2 * np.sin(th)
ax.plot_surface(x, y, x + offset, color="#65a5c6", alpha=0.17, linewidth=0)
th, rho = np.meshgrid(theta, np.linspace(0, 2, 24))
x, y = rho * np.cos(th), rho * np.sin(th)
for offset, color in [(-3, "#d99c39"), (2, "#4f9b65")]:
    ax.plot_surface(x, y, x + offset, color=color, alpha=0.48, linewidth=0)
    ax.plot(2 * np.cos(theta), 2 * np.sin(theta), 2 * np.cos(theta) + offset,
            color=color, linewidth=2.3)
for angle in np.linspace(0, 2 * np.pi, 9)[:-1]:
    x0, y0 = 2 * np.cos(angle), 2 * np.sin(angle)
    ax.plot([x0, x0], [y0, y0], [x0 - 3, x0 + 2], color="#44758b", alpha=0.35)
ax.text(0, 0, 2.55, r"upper cap: $z=x+2$", ha="center", color="#246638")
ax.text(0, 0, -3.8, r"lower cap: $z=x-3$", ha="center", color="#8b5a0c")
ax.set(xlabel="$x$", ylabel="$y$", zlabel="$z$", xlim=(-2.7, 2.7),
       ylim=(-2.7, 2.7), zlim=(-5.5, 4.5), title=r"Obliquely cut cylinder: $x^2+y^2\leq4$")
ax.set_box_aspect((1, 1, 1.5))
ax.view_init(elev=23, azim=-125)
fig.subplots_adjust(left=0.02, right=0.92, bottom=0.10, top=0.91)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
            facecolor="white", transparent=False)
plt.close(fig)
