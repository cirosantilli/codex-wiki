"""Plot rate continuity and secant growth near a square-root singularity.

Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Write an opaque white PNG
with this script's basename to the current directory.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.0, 4.6), dpi=120,
                                     constrained_layout=True, facecolor="white")
    y = np.unique(np.r_[np.linspace(-0.1, 0.1, 1201), 0.0])
    left.plot(y, 2 * np.sqrt(np.abs(y)), color="#1671a3", lw=2.4)
    left.scatter([0], [0], color="#333333", zorder=5)
    for eps, color, label in [(0.08, "#cf7023", "7.07"),
                              (0.02, "#238758", "14.14")]:
        left.plot([0, eps], [0, 2 * np.sqrt(eps)], ls="--", color=color,
                  lw=1.7, label=f"secant slope {label}")
        left.scatter([eps], [2 * np.sqrt(eps)], color=color, s=28)
    left.set(title=r"The rate is continuous: $f(0)=0$",
             xlabel="state y", ylabel=r"rate $f(y)=2\sqrt{|y|}$",
             xlim=(-0.105, 0.105), ylim=(-0.03, 0.7))
    left.legend(loc="upper center", fontsize=9, framealpha=1)
    eps = np.geomspace(1e-7, 1e-1, 501)
    right.loglog(eps, 2 / np.sqrt(eps), color="#8852a1", lw=2.4)
    for e in [1e-2, 1e-4, 1e-6]:
        slope = 2 / np.sqrt(e)
        right.scatter([e], [slope], color="#333333", s=28, zorder=5)
        right.annotate(f"{slope:.0f}", (e, slope), xytext=(7, 7),
                       textcoords="offset points", fontsize=10)
    right.set(title="No finite Lipschitz bound at zero",
              xlabel=r"positive state $\varepsilon$ (log scale)",
              ylabel=r"secant slope $2/\sqrt{\varepsilon}$ (log scale)",
              xlim=(1e-7, 1e-1), ylim=(4, 1e4))
    right.text(0.06, 0.09, r"As $\varepsilon\downarrow0$, slope $\uparrow\infty$",
               transform=right.transAxes, fontsize=10,
               bbox={"facecolor": "white", "edgecolor": "#dddddd", "pad": 5})
    fig.suptitle("A vanishing rate can still change too sharply for uniqueness", fontsize=12)
    for ax in (left, right):
        ax.set_facecolor("white")
        ax.grid(alpha=0.16)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
