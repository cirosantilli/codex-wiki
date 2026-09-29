"""Plot solved string profiles after reflection; output to the cwd."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
def triangle(s):
    return np.maximum(0., 1-np.abs(s-1))
x = np.linspace(0, 4.5, 901)
fig, axes = plt.subplots(2, 1, figsize=(9, 5.7), sharex=True, layout="constrained")
ys = [triangle(x-1)/2, (triangle(x-2)-triangle(x))/2]
for ax, y, label in zip(axes, ys, [r"$t=L/c$", r"$t=2L/c$"]):
    ax.axhline(0, lw=.8, color="#777777")
    ax.plot(x, y, color="#256d84", lw=2.8)
    ax.axvline(0, color="#343434", lw=3)
    ax.fill_between(x, 0, y, alpha=.17, color="#256d84")
    ax.set(ylim=(-.7, .7), yticks=[-.5, 0, .5], ylabel=r"$y/a$", title=label)
    ax.grid(alpha=.16)
axes[1].set(xlabel=r"$x/L$", xlim=(0, 4.5), xticks=range(5))
fig.suptitle("The incident displacement reflects with reversed sign", fontsize=14)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=125, facecolor="white")
