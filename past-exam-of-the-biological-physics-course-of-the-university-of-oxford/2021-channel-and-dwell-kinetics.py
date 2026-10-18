"""Original exam illustrations; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.facecolor": "white"})
fig, axes = plt.subplots(1, 3, figsize=(10.8, 3.2), constrained_layout=True)
t = np.linspace(0, 5, 1001)
axes[0].plot(t, .5 * (1 - np.exp(-t)), label="A: 0.5/ms each")
axes[0].plot(t, .5 * (1 - np.exp(-10*t)), label="B: 5/ms each")
axes[0].axhline(.5, color="grey", linestyle="--", linewidth=1)
axes[0].set(xlabel="Time (ms)", ylabel="Open probability", title="Equal endpoints, different speeds", ylim=(0, .56))
axes[0].legend(fontsize=8, loc="lower right")
x = np.linspace(0, 7, 1401)
axes[1].plot(x, 2*(np.exp(-x)-np.exp(-2*x)), label=r"$k_a=2k_b$")
axes[1].plot(x, x*np.exp(-x), label=r"$k_a=k_b$", linestyle="--")
axes[1].set(xlabel=r"Scaled time $k_b t$", ylabel=r"Density $p(t)/k_b$", title="Two sequential stages", ylim=(0, .57))
axes[1].legend(fontsize=9)
for ratio in (1, 2, 8):
    density=x*np.exp(-x) if ratio==1 else ratio/(ratio-1)*(np.exp(-x)-np.exp(-ratio*x))
    axes[2].plot(x,density,label=fr"$k_a/k_b={ratio}$")
axes[2].set(xlabel=r"Scaled time $k_b t$", ylabel=r"Density $p(t)/k_b$", title="A fast stage becomes less visible")
axes[2].legend(fontsize=9)
for ax in axes:
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(alpha=.18)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white", transparent=False)
