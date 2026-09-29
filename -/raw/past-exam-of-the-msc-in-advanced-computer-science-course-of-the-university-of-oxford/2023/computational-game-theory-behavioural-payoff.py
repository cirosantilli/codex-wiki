"""Independent randomization at a revisited information set; Python 3.14.4.

Uses NumPy 2.3.5 and Matplotlib 3.10.7; writes an opaque PNG to the CWD.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    p = np.linspace(0, 1, 401)
    fig, ax = plt.subplots(figsize=(5.2, 3.3), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    ax.plot(p, 8*p-7*p*p, color="#1c5580", linewidth=2.2, label=r"$U(p)=8p-7p^2$")
    ax.plot([0, 1], [0, 1], linestyle="--", color="#a36b21", linewidth=1.7, label="mixtures of the two pure plans")
    ax.scatter([4/7], [16/7], color="#1c7051", s=50, zorder=3)
    ax.annotate(r"$p=4/7,\quad U=16/7$", (4/7, 16/7), xytext=(0, 12), textcoords="offset points", ha="center", fontsize=11)
    ax.set_xlabel(r"$p=\Pr(D)$ at each visit")
    ax.set_ylabel("Expected payoff")
    ax.set_title("Forgetting the visit changes the value of randomization", fontsize=11)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 2.85)
    ax.legend(loc="lower right", fontsize=9, framealpha=1)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout(pad=0.8)
    fig.savefig(Path.cwd()/(Path(__file__).stem+".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
