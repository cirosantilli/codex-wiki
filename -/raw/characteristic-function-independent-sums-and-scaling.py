"""Plot exact characteristic functions of Bernoulli and symmetric sign sums."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(2, 2, figsize=(11, 7.8), layout="constrained")
    fig.set_facecolor("white")
    t = np.linspace(-np.pi, np.pi, 1001)
    phi = 2 / 3 + np.exp(1j * t) / 3
    product = phi ** 3
    for ax, component, name in zip(axes[0], [np.real, np.imag], ["Real", "Imaginary"]):
        ax.plot(t, component(phi), color="#2864a5", lw=2.2, label=r"$\varphi_B(t)$")
        ax.plot(t, component(product), color="#c05b16", lw=2.2, label=r"$\varphi_S(t)=\varphi_B(t)^3$")
        ax.set_title(name + " part: three independent Bernoulli variables", fontsize=12)
        ax.set(xlim=(-np.pi, np.pi), ylim=(-1.05, 1.12), ylabel=name + " part")
        ax.set_xticks([-np.pi, 0, np.pi], [r"$-\pi$", "0", r"$\pi$"])
        ax.legend(loc="lower center" if name == "Real" else "upper left", fontsize=11)

    t = np.linspace(-4, 4, 1201)
    colors = ["#a84079", "#bc7618", "#08765b"]
    for n, color in zip([4, 16, 64], colors):
        axes[1, 0].plot(t, np.cos(t / n) ** n, color=color, lw=2, label=f"n = {n}")
        axes[1, 1].plot(t, np.cos(t / np.sqrt(n)) ** n, color=color, lw=2, label=f"n = {n}")
    axes[1, 0].plot(t, np.ones_like(t), "k--", lw=1.6, label="Limit: 1")
    axes[1, 1].plot(t, np.exp(-t ** 2 / 2), "k--", lw=1.6, label=r"Limit: $e^{-t^2/2}$")
    axes[1, 0].set_title(r"Average $S_n/n$: $\cos(t/n)^n$", fontsize=13)
    axes[1, 1].set_title(r"Unit variance $S_n/\sqrt{n}$: $\cos(t/\sqrt{n})^n$", fontsize=13)
    for index, ax in enumerate(axes[1]):
        ax.set(xlim=(-4, 4), ylim=(-0.04, 1.12), ylabel="Real part (imaginary part = 0)")
        ax.legend(loc="lower center" if index == 0 else "upper right", fontsize=10,
                  ncols=2 if index == 0 else 1)
    for ax in axes.flat:
        ax.set_facecolor("white")
        ax.set_xlabel(r"Frequency parameter $t$")
        ax.axhline(0, color="0.65", lw=0.7)
        ax.axvline(0, color="0.75", lw=0.7)
        ax.grid(alpha=0.16)
    fig.suptitle("Independent sums multiply characteristic functions", fontsize=17)
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
