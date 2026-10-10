"""Original complex-root geometry and coefficient-ratio checks; output to CWD."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white"})
fig, (ax, notes) = plt.subplots(1, 2, figsize=(9.6, 4.7), layout="constrained", gridspec_kw={"width_ratios": [1.15, 1]})
ax.axhline(0, color="#64748b", lw=1); ax.axvline(0, color="#64748b", lw=1)
theta = np.linspace(-np.pi/2, np.pi/2, 301)
ax.plot(np.sqrt(2.5)*np.cos(theta), np.sqrt(2.5)*np.sin(theta), color="#cbd5e1", lw=1.5)
for yy, color, label in [(0.5, "#2563eb", r"$r_+=3/2+i/2$"), (-0.5, "#c2410c", r"$r_-=3/2-i/2$")]:
    ax.annotate("", (1.5, yy), (0, 0), arrowprops={"arrowstyle": "->", "color": color, "lw": 2})
    ax.scatter([1.5], [yy], color=color, zorder=3)
    ax.text(1.55, yy + (0.13 if yy > 0 else -0.22), label, color=color, fontsize=11)
ax.plot([1.5, 1.5], [-0.5, 0.5], "--", color="#64748b", lw=1)
ax.set(xlim=(-0.2, 2.8), ylim=(-1.15, 1.15), xlabel="Real part", ylabel="Imaginary part", title="Roots mirror across the real axis")
ax.set_aspect("equal"); ax.grid(alpha=0.2); ax.spines[["top", "right"]].set_visible(False)
notes.axis("off")
lines = [(0.87, r"$p(x)=2x^2-6x+5$"), (0.71, r"$r_++r_-=3=-(-6)/2$"),
         (0.55, r"$r_+r_-=|r_+|^2=5/2$"), (0.38, r"$(-6)^2-4(2)(5)=-4$"),
         (0.24, "No real roots; both complex roots count."),
         (0.09, "Scaling every coefficient by a nonzero\nfactor preserves the roots and these ratios.")]
for yy, label in lines: notes.text(0.01, yy, label, fontsize=12 if yy > 0.3 else 10.5, va="center")
fig.suptitle("Real coefficients can encode nonreal roots", fontsize=15)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
plt.close(fig)
