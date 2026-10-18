"""Plot the two integration curves and their area; output to the cwd."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
x = np.linspace(0, 2.3, 700)
f = np.sqrt(1+x*x)
g = 2/f
fig, ax = plt.subplots(figsize=(8, 4.8), layout="constrained")
ax.plot(x, f, color="#246b84", label=r"$\sqrt{1+x^2}$", lw=2)
ax.plot(x, g, color="#ad6135", label=r"$2/\sqrt{1+x^2}$", lw=2)
ax.fill_between(x, f, g, where=x<=1, color="#96c4b8", alpha=.6)
ax.scatter([1], [np.sqrt(2)], color="#202936", zorder=3)
ax.annotate(r"$(1,\sqrt{2})$", xy=(1, np.sqrt(2)), xytext=(1.24, 1.8), arrowprops={"arrowstyle": "->", "color": "#555555"})
ax.text(.15, 1.51, r"$A=\frac{3\log(1+\sqrt{2})-\sqrt{2}}{2}$")
ax.set(xlabel="x", ylabel="y", xlim=(0, 2.3), ylim=(0, 2.8), title="The shaded area ends at the crossing")
ax.grid(alpha=.2)
ax.legend(loc="upper left")
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white")
