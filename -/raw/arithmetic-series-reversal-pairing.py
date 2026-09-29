"""Original reversal pairing for eight terms; emit matching opaque PNG in CWD."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white"})
terms = 7 + 3*np.arange(8)
reverse = terms[::-1]
rows = np.arange(8)
fig, ax = plt.subplots(figsize=(9, 5.5), layout="constrained")
ax.barh(rows, terms, height=0.73, color="#2563eb", label="Original term")
ax.barh(rows, reverse, left=terms, height=0.73, color="#eab308", label="Reversed term")
for row, a, b in zip(rows, terms, reverse):
    ax.text(a/2, row, str(a), ha="center", va="center", color="white", fontsize=12)
    ax.text(a+b/2, row, str(b), ha="center", va="center", color="#422006", fontsize=12)
ax.set_yticks(rows, [f"k = {j}" for j in range(1, 9)])
ax.invert_yaxis()
ax.set_xlim(0, 36.5)
ax.set_xticks([0, 7, 14, 21, 28, 35])
ax.set_xlabel("Every stacked pair has value 35")
ax.spines[["top", "right", "left"]].set_visible(False)
ax.grid(axis="x", alpha=0.2)
ax.set_axisbelow(True)
ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.22), ncol=2, frameon=False)
fig.suptitle(r"Adding the progression to its reverse: $2S_8=8\times35=280$", fontsize=14)
ax.set_title(r"$7+10+13+16+19+22+25+28=140$", fontsize=12, pad=12)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
plt.close(fig)
