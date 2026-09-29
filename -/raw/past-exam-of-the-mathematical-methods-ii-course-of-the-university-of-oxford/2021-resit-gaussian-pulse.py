"""Draw a translating Gaussian pulse; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 13, "figure.facecolor": "white"})
fig, ax = plt.subplots(figsize=(8, 3.8), dpi=120, facecolor="white")
x = np.linspace(-6, 4, 1001)
ax.plot(x, np.exp(-x * x), color="#206895", lw=2.5, label=r"$t_1=0$")
ax.plot(x, np.exp(-(x + 3) ** 2), color="#b45621", lw=2.5,
        linestyle="--", label=r"$t_2=3x_0/v$")
ax.annotate("", (-3, 1.17), (0, 1.17), arrowprops={"arrowstyle": "->", "lw": 2, "color": "#333333"})
ax.text(-1.5, 1.23, r"$v(t_2-t_1)=3x_0$", ha="center")
ax.set(xlabel=r"$x/x_0$", ylabel=r"$y/A$", xlim=(-6, 4), ylim=(-0.05, 1.45),
       title=r"$y=Ae^{-(x+vt)^2/x_0^2}$, with $v>0$ and $x_0>0$")
ax.legend(loc="upper right", frameon=False)
ax.grid(alpha=0.17)
fig.tight_layout()
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
            facecolor="white", transparent=False)
plt.close(fig)
