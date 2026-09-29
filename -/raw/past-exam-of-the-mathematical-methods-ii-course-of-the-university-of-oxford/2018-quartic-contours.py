"""Plot quartic contours and the transformed integration cap; output to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
fig, axes = plt.subplots(1, 2, figsize=(11.8, 5), layout="constrained")
x = np.linspace(-1.4, 1.4, 550)
y = np.linspace(-1, 1, 500)
xx, yy = np.meshgrid(x, y)
ff = xx*xx-yy*yy-xx**4-yy**4
ax = axes[0]
levels = [-2, -1, -.25, 0, .1, .2]
cs = ax.contour(xx, yy, ff, levels=levels, colors=["#929292", "#929292", "#888888", "#212d35", "#287895", "#287895"])
ax.clabel(cs, fontsize=9, inline=True)
ax.scatter([-1/np.sqrt(2), 1/np.sqrt(2)], [0, 0], color="#a02e48", label="Maxima: 1/4", zorder=3)
ax.scatter([0], [0], color="#305e44", marker="x", label="Saddle: 0", zorder=3)
ax.set(xlabel="x", ylabel="y", title=r"Contours of $x^2-y^2-x^4-y^4$")
ax.set_aspect("equal")
ax.legend(loc="lower center", fontsize=10)
ax = axes[1]
r = 1/np.sqrt(2)
t = np.linspace(0, 2*np.pi, 600)
ax.plot(r*np.cos(t), r*np.sin(t), color="#305e7a", lw=2)
capx = np.linspace(-.5, .5, 400)
ax.fill_between(capx, .5, np.sqrt(.5-capx*capx), color="#93c4b4", alpha=.7)
ax.plot([-.77, .77], [.5, .5], "--", color="#6b6b6b")
ax.axhline(0, color="#aaaaaa", lw=.8)
ax.axvline(0, color="#aaaaaa", lw=.8)
ax.scatter([-.5, .5], [.5, .5], color="#305e7a", s=22)
ax.annotate(r"$(-1/2,1/2)$", xy=(-.5, .5), xytext=(-.82, .84), fontsize=10, arrowprops={"arrowstyle": "->"})
ax.annotate(r"$(1/2,1/2)$", xy=(.5, .5), xytext=(.24, .84), fontsize=10, arrowprops={"arrowstyle": "->"})
ax.text(-.75, -.86, r"$\mathrm{area}=\pi/8-1/4$; integral = area$/4$")
ax.set(xlim=(-.9, .9), ylim=(-.95, 1), xlabel="X", ylabel="Y", title=r"$X^2+Y^2<1/2,\quad Y>1/2$")
ax.set_aspect("equal")
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=125, facecolor="white")
