"""Render two exact two-point Jensen inequalities, with a fixed mean, to cwd."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    d = np.linspace(0, 2, 401)
    mean = 2.0
    square_average = ((mean - d) ** 2 + (mean + d) ** 2) / 2
    exp_average = (np.exp(mean - d) + np.exp(mean + d)) / 2
    assert np.allclose(square_average - mean**2, d**2)
    assert np.allclose(exp_average, np.exp(mean) * np.cosh(d))
    assert np.isclose(0.25 * 1**2 + 0.75 * 3**2 - (0.25 * 1 + 0.75 * 3)**2, 0.75)
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.2), dpi=120, facecolor="white")
    curves = [(square_average, mean**2, r"$f(x)=x^2$", r"$E[f(X)]=4+d^2$"),
              (exp_average, np.exp(mean), r"$f(x)=e^x$", r"$E[f(X)]=e^2\cosh d$")]
    for ax, (average, baseline, title, label) in zip(axes, curves):
        ax.plot(d, average, color="#206a9d", lw=3, label=label)
        ax.axhline(baseline, color="#be7521", lw=2, linestyle="--",
                   label=r"$f(E[X])=f(2)$")
        ax.fill_between(d, baseline, average, color="#206a9d", alpha=0.12)
        height = float(np.interp(1, d, average))
        ax.plot([1, 1], [baseline, height], color="#2f8a68", lw=3)
        ax.scatter([1, 1], [baseline, height], color=["#be7521", "#206a9d"],
                   s=45, zorder=4)
        ax.annotate(f"At d = 1, gap = {height - baseline:.3f}",
                    xy=(1, (baseline + height) / 2), xytext=(0.08, 0.78),
                    textcoords="axes fraction", fontsize=11,
                    arrowprops={"arrowstyle": "->", "color": "#2f8a68"})
        ax.set(xlim=(0, 2), ylim=(0, max(average) * 1.17),
               title=title, xlabel="Half-spread d", ylabel="Function value / average")
        ax.legend(loc="upper left", frameon=False, fontsize=11)
        ax.grid(color="#e5e9eb")
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Two equally likely inputs: 2 − d and 2 + d; their mean stays 2", fontsize=15)
    fig.subplots_adjust(left=0.065, right=0.985, top=0.84, bottom=0.13, wspace=0.24)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
