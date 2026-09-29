"""Original model illustration, not measured data; write matching PNG to CWD.

Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Dependencies: Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7 (repository environment).
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    x = np.linspace(-4.5, 7.0, 1801)
    sigma0 = 0.50  # mm; profiles have unit spatial integral
    times = (0.0, 1.0, 4.0)  # h
    colors = ("#59616d", "#1479b8", "#d66a13")
    cases = ((0.20, 0.0, "Diffusion alone", "Centre fixed; width grows"),
             (0.0, 0.60, "Uniform advection alone", "Centre moves; width fixed"),
             (0.20, 0.60, "Both together", "Centre moves; width grows"))
    fig, axes = plt.subplots(1, 3, figsize=(11.1, 4.1), sharex=True, sharey=True)
    for ax, (diffusivity, speed, title, note) in zip(axes, cases):
        for t, color in zip(times, colors):
            variance = sigma0**2 + 2 * diffusivity * t
            profile = np.exp(-(x - speed*t)**2 / (2*variance)) / np.sqrt(2*np.pi*variance)
            ax.plot(x, profile, color=color, lw=2.2,
                    linestyle="--" if t == 0 else "-", label=f"{t:g} h")
        ax.set(title=title, xlabel="Position x (mm)", xlim=(-4.5, 7), ylim=(0, 0.87))
        ax.set_xticks((-4, -2, 0, 2, 4, 6))
        ax.grid(alpha=0.17)
        ax.text(0.5, -0.30, note, transform=ax.transAxes, ha="center", fontsize=10)
    axes[0].set_ylabel(r"Normalized concentration $C/Q$ (mm$^{-1}$)")
    fig.suptitle("Spreading and bulk transport have different signatures", fontsize=15, y=0.98)
    fig.legend(*axes[0].get_legend_handles_labels(), loc="upper center", ncol=3,
               frameon=False, bbox_to_anchor=(0.5, 0.90))
    fig.text(0.5, 0.015, "Illustrative model, not measured data  |  Initial width 0.50 mm; each curve has area one",
             ha="center", fontsize=10, color="#454c55")
    fig.subplots_adjust(left=0.08, right=0.985, bottom=0.26, top=0.75, wspace=0.15)
    fig.savefig(Path(__file__).stem + ".png", dpi=110, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
