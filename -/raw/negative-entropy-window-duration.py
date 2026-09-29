"""Exact negative-window probabilities; Python 3.14 and project plotting versions.
Run from _media to write the matching opaque PNG in the current directory.
"""
from math import comb
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

p, q = 0.75, 0.25
n = np.arange(1, 102, 2)
negative = np.array([sum(comb(int(m), k)*p**k*q**(int(m)-k) for k in range((int(m)+1)//2)) for m in n])
fig, axes = plt.subplots(1, 2, figsize=(10, 4), layout="constrained", facecolor="white")
axes[0].semilogy(n, negative, color="#c54d36", lw=2, label=r"Exact $\Pr(S_n<0)$ (odd $n$)")
axes[0].semilogy(n, (2*np.sqrt(p*q))**n, color="0.4", ls="--", label=r"Upper bound $(2\sqrt{pq})^n$")
axes[0].set(xlabel=r"Window duration in steps $n$", ylabel="Probability of a negative total", title="Long negative totals become rare")
axes[0].legend(fontsize=9)
axes[0].grid(alpha=0.2)
axes[1].plot(n, p*n, color="#2676a8", lw=2, label=r"Positive increments: $np$")
axes[1].plot(n, q*n, color="#c54d36", lw=2, label=r"Negative increments: $nq$")
axes[1].set(xlabel=r"Window duration in steps $n$", ylabel="Expected number of increments", title="Negative increments still accumulate", ylim=(0, 80))
axes[1].legend(fontsize=9, loc="upper left")
axes[1].text(0.04, 0.62, r"Negative fraction stays $q=1/4$" + "\n" + r"Mean total: $n\ln(3)/2>0$", transform=axes[1].transAxes)
axes[1].grid(alpha=0.2)
fig.suptitle("Exact biased-step model, p = 3/4: negative increments versus negative windows", fontsize=13)
fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False)
plt.close(fig)
