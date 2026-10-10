"""Plot original on-off counting and veto examples, not historical observations.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; the output is written to the current directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, (ax, veto) = plt.subplots(1, 2, figsize=(10, 4.6), facecolor="white", layout="constrained")
    ax.bar([0, 1, 2], [1000, 400, 600], color=["#3b7daf", "#9d9d9d", "#d68132"], width=.6)
    ax.errorbar([0, 1, 2], [1000, 400, 600],
                yerr=[np.sqrt(1000), .5*np.sqrt(800), np.sqrt(1200)],
                fmt="none", capsize=6, color="black")
    ax.set_xticks([0, 1, 2], ["On\n100 s", "½ × off\n200 s", "Net source\non − ½ off"])
    ax.set(ylabel="Counts on the 100 s scale", ylim=(0, 1280), title="Invented counts; bars show ±1σ")
    for x, y, label in [(0, 1000, "1000"), (1, 400, "400"), (2, 600, "600")]:
        ax.text(x, y+65, label, ha="center")
    ax.text(.04, .95, "Independent off count = 800\nNet σ = √(1000 + ¼ × 800) = 34.64",
            transform=ax.transAxes, va="top", fontsize=9)

    eb = np.linspace(0, 1, 401)
    for es, color in [(1, "#3b7daf"), (.8, "#d68132"), (.5, "#448459")]:
        s, b = es*750, eb*2000
        veto.plot(eb, s/np.sqrt(s+1.5*b), lw=2.2, color=color,
                  label=f"Source acceptance εs = {es:g}")
    chosen = 600/np.sqrt(1200)
    original = 750/np.sqrt(3750)
    veto.plot(.2, chosen, "o", color="#d68132", ms=8)
    veto.plot(1, original, "o", color="#3b7daf", ms=8)
    veto.annotate("chosen veto: 17.32", (.2, chosen), (.32, 23),
                  arrowprops={"arrowstyle": "->"}, fontsize=10)
    veto.annotate("no veto: 12.25", (1, original), (.53, 8),
                  arrowprops={"arrowstyle": "->"}, fontsize=10)
    veto.set(xlim=(0, 1.04), ylim=(0, 32), xlabel="Background acceptance εb",
             ylabel="Expected S / √[S + (1 + α)B]", title="Selection trades signal for background")
    veto.legend(loc="upper right", fontsize=9)
    fig.suptitle("Chosen model: S₀ = 750, B₀ = 2000, α = ½", fontsize=13)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
