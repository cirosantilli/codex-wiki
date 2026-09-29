"""Plot the stipulated empirical Monod law; save basename PNG to the CWD.

Tested with Python 3.14.4, Matplotlib 3.10.7, NumPy 2.3.5.
Run from _media: MPLCONFIGDIR=/tmp/chemostat-mpl python3 ../monod-growth-and-dilution.py
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    mu_max, k_s, dilution, feed = 1.0, 1.0, 0.5, 9.0
    s = np.linspace(0, 12, 601)
    mu = mu_max * s / (k_s + s)
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(8.8, 4.8), dpi=100, layout="constrained")
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.plot(s, mu, color="#17679b", lw=2.5, label=r"Growth: $\mu(s)=s/(1+s)$")
    ax.axhline(mu_max, color="#7b7b7b", ls=":", lw=1.5,
               label=r"Limiting rate $\mu_{\max}=1$ h$^{-1}$")
    ax.axhline(dilution, color="#c56a16", lw=2, ls="--",
               label=r"Dilution $D=0.5$ h$^{-1}$")
    ax.vlines(k_s, 0, dilution, color="#c56a16", ls=":", lw=1.5)
    ax.scatter([k_s, feed], [dilution, mu_max * feed / (k_s + feed)],
               color=["#c56a16", "#17679b"], s=45, zorder=5)
    ax.annotate(r"$s_*=K_s=1$ g/L", (k_s, dilution), xytext=(2.0, 0.30),
                arrowprops={"arrowstyle": "->", "color": "#c56a16"})
    ax.annotate("Feed: 9 g/L permits\n" + r"$\mu(s_{\rm in})=0.9$ h$^{-1}$",
                (feed, 0.9), xytext=(6.0, 0.67),
                arrowprops={"arrowstyle": "->", "color": "#17679b"})
    ax.set(xlim=(0, 12), ylim=(0, 1.12),
           xlabel=r"Residual nutrient concentration $s$ (g/L)",
           ylabel=r"Growth or dilution rate (h$^{-1}$)",
           title="Monod growth: the pump selects a residual nutrient level")
    ax.legend(loc="lower right", frameon=True, facecolor="white", framealpha=1)
    ax.grid(alpha=0.18)
    destination = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(destination, facecolor="white", transparent=False)
    plt.close(fig)
    print(destination)


if __name__ == "__main__":
    main()
