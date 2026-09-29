"""Original sextic phase diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Write paper-46-phases.png to the caller's working directory.
"""
import os
import tempfile
os.environ.setdefault("MPLCONFIGDIR", tempfile.mkdtemp(prefix="paper-46-mpl-"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(12, 5.3), facecolor="white", layout="constrained")
ax = fig.add_subplot(121)
u = np.linspace(-1, 1, 400)
r_boundary = np.where(u < 0, 3*u*u/16, 0)
ax.fill_between(u, -.25, r_boundary, color="#d4e5f2", alpha=.9)
ax.fill_between(u, r_boundary, .32, color="#f9ead3", alpha=.9)
ax.plot(u[u < 0], r_boundary[u < 0], color="#b74336", lw=2.8, label="First order: three phases coexist")
ax.plot(u[u >= 0], r_boundary[u >= 0], color="#24664a", lw=2.8, label="Continuous transition")
ax.scatter([0], [0], color="black", s=38, zorder=5)
ax.annotate("Tricritical point", (0, 0), (.18, .09), arrowprops={"arrowstyle":"->"})
ax.text(-.55, -.13, "Ordered: M = ±|M|", ha="center")
ax.text(.37, .23, "Disordered: M = 0", ha="center")
ax.set(xlabel="Quartic control u", ylabel="Thermal control r", title="Zero-field section (v = 1)", xlim=(-1, 1), ylim=(-.25, .32))
ax.legend(loc="upper left", fontsize=8)
ax.grid(alpha=.15)

ax = fig.add_subplot(122, projection="3d")
s, z = np.meshgrid(np.linspace(.001, .43, 50), np.linspace(0, 1, 45))
d = s*z
uw = -(10*s*s/3 + 2*d*d)
rw = 5*s**4 - 2*s*s*d*d/3 + d**4
hw = 8*s**3*(s*s-d*d)/3
for sign, color in [(1, "#d98b45"), (-1, "#679dcc")]:
    ax.plot_surface(uw, rw, sign*hw, color=color, alpha=.64, linewidth=0, shade=False)
se = np.linspace(0, .43, 150)
for sign in [-1, 1]:
    ax.plot(-10*se**2/3, 5*se**4, sign*8*se**5/3, color="#245c42", lw=2.4)
ax.plot(-16*se**2/3, 16*se**4/3, np.zeros_like(se), color="#aa3434", lw=2.2)
us, q = np.meshgrid(np.linspace(-1, .4, 45), np.linspace(0, 1, 15))
bd = np.where(us < 0, 3*us**2/16, 0)
rs = -.18 + q*(bd+.18)
ax.plot_surface(us, rs, np.zeros_like(rs), color="#aaa3bc", alpha=.3, linewidth=0, shade=False)
uc = np.linspace(0, .4, 60)
ax.plot(uc, 0*uc, 0*uc, color="#245c42", lw=2.4)
ax.scatter([0], [0], [0], color="black", s=30)
ax.set(xlabel="u", ylabel="r", zlabel="h", title="First-order sheets and critical edges")
ax.view_init(elev=23, azim=-60)
ax.text2D(.03, .96, "Green: continuous edges; red: three-phase line", transform=ax.transAxes, fontsize=8)
fig.savefig("paper-46-phases.png", dpi=120, facecolor="white", transparent=False)
plt.close(fig)
