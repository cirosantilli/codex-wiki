"""Three original normalized Haar contrasts; write an opaque PNG to CWD."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def haar(x, j=0, k=0):
    z = 2**j*x-k
    positive = ((z >= 0) & (z < .5)).astype(float)
    negative = ((z >= .5) & (z < 1)).astype(float)
    return 2**(j/2) * (positive-negative)


def main():
    x = np.linspace(-.08, 1.08, 2321)
    fig, axes = plt.subplots(1, 3, figsize=(10.4, 3.9), dpi=120, sharey=True)
    fig.patch.set_facecolor("white")
    specs = [(0, 0, "#246a9b"), (1, 0, "#bf7135"), (1, 1, "#7c458a")]
    for ax, (j, k, color) in zip(axes, specs):
        y = haar(x, j, k)
        ax.plot(x, y, drawstyle="steps-post", color=color, lw=2.5)
        ax.fill_between(x, 0, y, step="post", color=color, alpha=.15)
        ax.axhline(0, color="#777777", lw=.7)
        title = rf"$\psi_{{{j},{k}}}$: support length " + f"{2**(-j):g}"
        ax.set(xlim=(-.08, 1.08), ylim=(-1.75, 1.75),
               xlabel="x", title=title)
        ax.set_yticks([-np.sqrt(2), -1, 0, 1, np.sqrt(2)],
                      [r"$-\sqrt{2}$", "−1", "0", "1", r"$\sqrt{2}$"])
        ax.spines[["top", "right"]].set_visible(False)
        ax.set_facecolor("white")
        ax.grid(alpha=.12)
    axes[0].set_ylabel("Wavelet value")
    fig.suptitle("Localized contrasts: zero integral and unit squared norm",
                 fontsize=14)
    fig.text(.5, .025,
             "Shrinking the support by 2 raises the amplitude by √2; positive and negative areas cancel.",
             ha="center", fontsize=10)
    fig.tight_layout(rect=(0, .08, 1, .94))
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
