"""Plot stipulated binomial models, not historical neutrino data."""

from math import comb
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


N, a, r, b, qb = 40, .90, .05, .10, .40
qs = [(1 - b) * r + b * qb, (1 - b) * (a + r) / 2 + b * qb, qb]
names = ["Muon-associated signal", "Equal selected e/μ mixture", "Background only"]
colors = ["#16659a", "#b35d15", "#737373"]
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(11, 5.8), dpi=120, facecolor="white", gridspec_kw={"width_ratios": [1, 1.12]})
fig.suptitle("Track or shower? A chosen classification model", fontsize=16, weight="bold", y=.96)
fig.text(.5, .875, "N = 40 selected events • a = 0.90, r = 0.05, b = 0.10, qᵦ = 0.40", ha="center")
fig.text(.5, .825, "Teaching inputs throughout; no historical counts or measured efficiencies", ha="center", fontsize=10, color="#555555")

y = np.arange(3)
track = N * (1 - np.array(qs))
shower = N * np.array(qs)
ax0.barh(y, track, color="#c7e0ef", label="Track labels")
ax0.barh(y, shower, left=track, color="#f3c591", label="Shower labels")
for i, (t, s) in enumerate(zip(track, shower)):
    ax0.text(t / 2, i, f"{t:g}", ha="center", va="center", weight="bold")
    ax0.text(t + s / 2, i, f"{s:g}", ha="center", va="center", weight="bold", fontsize=10)
ax0.set(yticks=y, yticklabels=["Muon signal", "Equal mixture", "Background"], xlim=(0, 40), xlabel="Expected count", title="Expected labels at fixed sample size")
ax0.invert_yaxis()
ax0.legend(loc="lower center", bbox_to_anchor=(.5, -.34), frameon=False, ncol=2, fontsize=10)
ax0.spines[["top", "right"]].set_visible(False)

ks = np.arange(N + 1)
for q, name, color in zip(qs, names, colors):
    pmf = np.array([comb(N, int(k)) * q**k * (1 - q)**(N - k) for k in ks])
    assert abs(pmf.sum() - 1) < 1e-12
    assert abs(ks @ pmf - N * q) < 1e-12
    ax1.plot(ks, pmf, "o-", ms=3, lw=1.6, label=f"{name} (q = {q:g})", color=color)
ax1.set(xlabel="Shower count K", ylabel="Probability P(K = k)", title="Independent labels: binomial sampling", xlim=(-.5, 35), ylim=(0, .24))
ax1.axvspan(-.5, 5.5, color="#e8edf2", alpha=.6, zorder=0)
ax1.text(2.4, .227, "K ≤ 5", ha="center", fontsize=10)
ax1.legend(loc="lower center", bbox_to_anchor=(.50, -.43), frameon=False, fontsize=9)
ax1.spines[["top", "right"]].set_visible(False)
fig.subplots_adjust(left=.13, right=.98, bottom=.26, top=.71, wspace=.43)
fig.savefig(Path(__file__).stem + ".png", facecolor="white")
plt.close(fig)
