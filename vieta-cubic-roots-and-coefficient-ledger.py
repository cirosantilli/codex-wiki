"""Original cubic roots and signed elementary-symmetric coefficient ledger."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white"})
fig = plt.figure(figsize=(10, 5.8), layout="constrained")
gs = fig.add_gridspec(2, 1, height_ratios=[1.2, 1])
ax = fig.add_subplot(gs[0])
x = np.linspace(-3, 6, 600)
ax.plot(x, (x+2)*(x-1)*(x-5), color="#2563eb", lw=2)
ax.axhline(0, color="#64748b", lw=1)
ax.scatter([-2, 1, 5], [0, 0, 0], color="#c2410c", zorder=3)
for r in [-2, 1, 5]:
    ax.annotate(str(r), (r, 0), xytext=(r, 10), ha="center", color="#c2410c")
ax.set(xlim=(-3, 6), ylim=(-44, 46), xlabel="x", ylabel="p(x)", title=r"$p(x)=(x+2)(x-1)(x-5)=x^3-4x^2-7x+10$")
ax.spines[["top", "right"]].set_visible(False)
ax.grid(alpha=0.2)
table = fig.add_subplot(gs[1])
table.set(xlim=(0, 1), ylim=(0, 1)); table.axis("off")
for xx, text in [(0.03, "Root choices"), (0.3, "Symmetric calculation"), (0.66, "Value"), (0.83, "Coefficient")]:
    table.text(xx, 0.91, text, weight="bold")
rows = [("One at a time", r"$-2+1+5$", r"$e_1=4$", r"$-e_1=-4$"),
        ("Pairs of positions", r"$(-2)(1)+(-2)(5)+(1)(5)$", r"$e_2=-7$", r"$+e_2=-7$"),
        ("All three", r"$(-2)(1)(5)$", r"$e_3=-10$", r"$-e_3=10$")]
for yy, row in zip([0.67, 0.42, 0.17], rows):
    table.axhspan(yy-0.09, yy+0.12, color="#eff6ff" if yy != 0.42 else "#fff7ed")
    for xx, text in zip([0.03, 0.3, 0.66, 0.83], row): table.text(xx, yy, text, va="center", fontsize=11)
fig.suptitle("Root combinations determine the alternating coefficient signs", fontsize=15)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
plt.close(fig)
