"""Exact biased-step probabilities; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
Run from _media to write the matching opaque PNG in the current directory.
"""
from math import comb, log
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

p, q, n = 0.75, 0.25, 9
a = log(p / q)
k = np.arange(n + 1)
s = a * (2 * k - n)
weights = np.array([comb(n, int(j)) * p**int(j) * q**(n-int(j)) for j in k])
fig, axes = plt.subplots(1, 2, figsize=(10, 4), layout="constrained", facecolor="white")
axes[0].bar(s, weights, width=1.35, color=np.where(s < 0, "#c54d36", "#2676a8"))
axes[0].axvline(0, color="0.4", lw=0.8)
axes[0].set(xlabel=r"Dimensionless entropy production $s$", ylabel=r"Probability mass $p_9(s)$", title="Exact distribution: nine independent steps")
axes[0].text(0.03, 0.95, r"$p=3/4,\ q=1/4,\ a=\ln 3$" + "\nOrange: negative total", transform=axes[0].transAxes, va="top")
axes[1].plot(s, s, color="0.5", label=r"Prediction: $\ln[p_9(s)/p_9(-s)]=s$")
axes[1].scatter(s, np.log(weights/weights[::-1]), color="#2676a8", s=35, zorder=3, label="Exact probability ratio")
axes[1].axhline(0, color="0.8", lw=0.8)
axes[1].axvline(0, color="0.8", lw=0.8)
axes[1].set(xlabel=r"Dimensionless entropy production $s$", ylabel=r"$\ln[p_9(s)/p_9(-s)]$", title="Finite same-law fluctuation relation")
axes[1].legend(fontsize=9, loc="upper left")
fig.suptitle("Biased-step model: rare negative totals have nonzero probability", fontsize=13)
fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False)
plt.close(fig)
