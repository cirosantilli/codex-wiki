"""Plot the index-one profile and mean free path; Python 3.14, NumPy/Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(9, 3.9), dpi=130, facecolor="white")
x = np.linspace(0, 1, 700)
theta = np.sinc(x)
axes[0].plot(x, theta, color="#2166ac", lw=2.3)
axes[0].plot([1, 1.12], [0, 0], color="#2166ac", lw=2.3)
axes[0].set(xlim=(0, 1.12), ylim=(-.03, 1.08), xlabel=r"Radius $r/R$",
            ylabel=r"Density $\rho/\rho_c$", title="Finite centre, linear surface decline")
axes[0].scatter([0, 1], [1, 0], color="#2166ac", s=24, zorder=3)
x_inner = np.linspace(0, .9995, 1200)
axes[1].semilogy(x_inner, 1 / np.sinc(x_inner), color="#b45d00", lw=2.3)
axes[1].axvline(1, color="#555555", ls="--", lw=1)
axes[1].set(xlim=(0, 1.04), ylim=(.85, 2500), xlabel=r"Radius $r/R$",
            ylabel=r"Mean free path $\ell/L$", title="Mean free path diverges at the edge")
axes[1].text(.12, 250, r"$\ell/L=(\pi r/R)/\sin(\pi r/R)$", fontsize=11)
for ax in axes:
    ax.set_facecolor("white")
    ax.grid(alpha=.22)
    ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
            facecolor="white", transparent=False, metadata={"Software": "Matplotlib"})
plt.close(fig)
