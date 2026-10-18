"""Generate the original pairing-spectrum figure in the current working directory.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Dependencies are declared in the repository pyproject.toml.
"""

from pathlib import Path
import os

os.environ.setdefault("MPLCONFIGDIR", "/tmp/oxford-2025-aqt-matplotlib")

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    root = Path.cwd()
    plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.facecolor": "white"})
    ratio = np.linspace(0, 4, 401)
    e = np.sqrt(1 + ratio ** 2)
    fig, axes = plt.subplots(1, 2, figsize=(9, 3.8), layout="constrained")
    axes[0].plot(ratio, 1 - e, color="#2469a0", label=r"$\varepsilon-E$ (one state)")
    axes[0].plot(ratio, np.ones_like(ratio), color="#666666", ls="--", label=r"$\varepsilon$ (two states)")
    axes[0].plot(ratio, 1 + e, color="#c43134", label=r"$\varepsilon+E$ (one state)")
    axes[0].set(xlabel=r"pairing strength $\Delta/\varepsilon$", ylabel=r"energy / $\varepsilon$", title="Four states, three distinct energies")
    axes[0].legend(fontsize=8, loc="upper left")
    axes[1].plot(ratio, (1 - 1 / e) / 2, color="#2469a0", lw=2, label=r"$v^2=(1-\varepsilon/E)/2$")
    axes[1].axhline(0.5, color="#999999", ls=":", label="strong-pairing limit")
    axes[1].set(xlabel=r"pairing strength $\Delta/\varepsilon$", ylabel="occupied-pair probability", ylim=(-0.02, 0.55), title="The ground state contains an occupied pair")
    axes[1].legend(fontsize=8, loc="lower right")
    for ax in axes:
        ax.set_xlim(0, 4)
        ax.grid(alpha=0.2)
    output = root / "2025-pairing-spectrum.png"
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=135, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
