"""Original finite-micelle mass-action distributions.

Python 3.14, numpy, matplotlib. Every energy and concentration is an
illustrative dimensionless choice, not inferred exam data. Set mu_1^0=0,
mu_alpha^0/kT=-8+[(alpha-40)^2/(2*4^2)+offset]/alpha for alpha>=2.
The offset makes the aggregate and monomer molecular populations equal
at x_1=exp(-8), using the finite displayed size range.
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


alpha = np.arange(2, 101)
centre, width = 40., 4.
reference = np.exp(-8.)
penalty = (alpha-centre)**2/(2*width**2)
offset = np.log(np.sum(alpha*np.exp(-penalty))/reference)
fig, axes = plt.subplots(1, 2, figsize=(10, 3.8), constrained_layout=True,
                         facecolor="white", sharey=True)
for ax, factor, title in zip(axes, [0.5, 1.04],
                             ["Below the crossover", "Above the crossover"]):
    x1 = factor*reference
    xa = alpha*np.exp(alpha*(np.log(x1)+8)-penalty-offset)
    total = x1+np.sum(xa)
    ax.semilogy(alpha, xa, lw=2.2, color="#1764a0", label="In aggregates")
    ax.vlines(1, 1e-20, x1, color="#c55412", lw=2)
    ax.scatter([1], [x1], color="#c55412", zorder=3, label="Monomers")
    ax.set(xlim=(-1, 85), ylim=(1e-20, 2e-3),
           xlabel=r"Aggregation number $\alpha$", title=title)
    fraction = np.sum(xa)/total
    displayed = f"{100*fraction:.1f}%" if fraction >= .001 else f"{100*fraction:.2e}%"
    ax.text(.96, .75, f"Aggregated molecules:\n{displayed}",
            transform=ax.transAxes, ha="right", fontsize=10,
            bbox={"facecolor": "white", "alpha": .85, "edgecolor": "none"})
    ax.grid(alpha=.17)
    ax.spines[["top", "right"]].set_visible(False)
axes[0].set_ylabel(r"Molecular fraction $x_\alpha$ (log scale)")
axes[0].legend(loc="lower left", fontsize=9)
fig.suptitle("Illustrative finite-size mass-action model; no measured surfactant parameters",
             fontsize=11)
fig.savefig("paper-1-aggregate-distribution.png", dpi=160, facecolor="white")
plt.close(fig)
