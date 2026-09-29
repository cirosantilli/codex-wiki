"""Original radiation-fluid density mode; opaque PNG written to CWD.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def regular_mode(x):
    return np.sinc(x / np.pi) - np.cos(x)


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11.4, 4.2), dpi=100)
    early = np.linspace(0, 2.5, 600)
    axes[0].plot(early, regular_mode(early), lw=2, label="Regular mode")
    outside = np.linspace(0, 1, 200)
    axes[0].plot(outside, outside**2 / 3, "--", lw=1.7,
                 label="Early-time approximation x²/3")
    axes[0].axvline(1, color="#777777", lw=1, ls=":", label="Sound-horizon scale x = 1")
    axes[0].set(xlabel="x = kη/√3", ylabel="Density contrast (arbitrary amplitude)",
                xlim=(0, 2.5), title="Regular growth toward horizon crossing")
    late = np.linspace(1, 30, 1500)
    axes[1].plot(late, regular_mode(late), lw=2, label="Regular mode")
    asymptotic = late[late >= 5]
    axes[1].plot(asymptotic, -np.cos(asymptotic), "--", lw=1.4, alpha=0.8,
                 label="Late-time leading term −cos x")
    axes[1].set(xlabel="x = kη/√3", ylabel="Density contrast (arbitrary amplitude)",
                xlim=(1, 30), title="Acoustic oscillations inside the horizon")
    for ax in axes:
        ax.grid(alpha=0.2)
        ax.legend(fontsize=9)
    fig.suptitle("Radiation-fluid density perturbation: Δ(x) = sin(x)/x − cos(x)", fontsize=13)
    fig.tight_layout()
    fig.savefig(Path.cwd() / "paper-55-radiation-density-mode.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
