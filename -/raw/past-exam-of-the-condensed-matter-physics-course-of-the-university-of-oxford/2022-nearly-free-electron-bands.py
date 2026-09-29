"""Original two-wave dispersion sketch; Python 3.14 and Matplotlib 3.10."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    y = np.linspace(-1, 1, 1201)
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.2), dpi=140,
                             sharex=True, sharey=True, facecolor="white")
    for ax, eps in zip(axes, (0., .25)):
        root = np.sqrt(4 * y**2 + eps**2)
        lower = 1 + y**2 - root
        upper = 1 + y**2 + root
        ax.plot(y, lower, color="#126782", lw=2.4, label="Lower band (filled)")
        ax.plot(y, upper, color="#b65531", lw=2.1, label="Upper band (empty)")
        ax.axvline(0, color=".65", lw=.8, ls=":")
        ax.axhline(1, color=".75", lw=.8, ls=":")
        if eps:
            ax.annotate("", (0, 1 + eps), (0, 1 - eps),
                        arrowprops={"arrowstyle": "<->", "color": "#3e3e3e", "lw": 1.4})
            ax.text(.08, 1.12, r"Gap $2|V_G|$", fontsize=11)
            ax.plot(y, (1 - np.abs(y))**2, color="#126782", lw=1, ls="--", alpha=.6)
        ax.set(xlabel=r"Boundary-centred coordinate $y$", xlim=(-1, 1),
               ylim=(-.15, 4.2), xticks=[-1, -.5, 0, .5, 1],
               title=(r"$V_G=0$: folded free bands" if eps == 0 else
                      r"$|V_G|/E_{\rm ZB}=0.25$: avoided crossing"))
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(alpha=.15)
    axes[0].set_ylabel(r"Energy $E/E_{\rm ZB}$")
    axes[0].legend(loc="upper center", frameon=False, fontsize=10)
    fig.suptitle("Two-wave model on the integration interval −1 ≤ y ≤ 1", fontsize=13)
    fig.tight_layout(rect=(0, 0, 1, .94))
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
