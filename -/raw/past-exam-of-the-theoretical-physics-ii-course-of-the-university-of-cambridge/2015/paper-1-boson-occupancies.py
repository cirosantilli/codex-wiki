"""Original two-mode occupation distributions; Python 3.14, numpy, matplotlib."""

import math
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


fig, axes = plt.subplots(1, 2, figsize=(10, 3.9), constrained_layout=True,
                         facecolor="white")
n = np.arange(3)
axes[0].bar(n-.23, [.5, 0, .5], .22, color="#1764a0", label="Identical bosons")
axes[0].bar(n, [0, 1, 0], .22, color="#197c54", label="Identical fermions")
axes[0].bar(n+.23, [.25, .5, .25], .22, color="#c55412", label="Distinguishable")
axes[0].set(title="One particle per input", xticks=n,
            xlabel=r"Output occupation $n_1$ ($n_2=2-n_1$)", ylabel="Probability")
axes[0].legend(fontsize=8)
N = 4
n = np.arange(2*N+1)
p = np.zeros(2*N+1)
for j in range(N+1):
    p[2*j] = math.comb(2*j, j)*math.comb(2*(N-j), N-j)/4**N
classical = np.array([math.comb(2*N, int(i))/4**N for i in n])
axes[1].bar(n-.18, p, .35, color="#1764a0", label="Twin-Fock bosons")
axes[1].bar(n+.18, classical, .35, color="#c55412",
            label="Independent distinguishable particles")
axes[1].set(title=r"Illustrative $|4,4\rangle$ input",
            xlabel=r"Output occupation $n_1$ ($n_2=8-n_1$)", xticks=n)
axes[1].set_ylim(0, .37)
axes[1].legend(fontsize=8)
for ax in axes:
    ax.set_ylim(bottom=0)
    ax.grid(axis="y", alpha=.2)
    ax.set_axisbelow(True)
    ax.spines[["top", "right"]].set_visible(False)
fig.savefig("paper-1-boson-occupancies.png", dpi=160, facecolor="white")
plt.close(fig)
