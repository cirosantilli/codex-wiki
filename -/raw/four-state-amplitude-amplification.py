"""Draw four-state-amplitude-amplification.png in cwd; Python 3.14, NumPy, Matplotlib.

From the repository root: cd _media && python ../four-state-amplitude-amplification.py
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    h = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
    uniform = np.kron(h, h) @ np.array([1, 0, 0, 0])
    oracle = np.diag([1, 1, 1, -1])
    flipped = oracle @ uniform
    diffusion = 2 * np.outer(uniform, uniform) - np.eye(4)
    amplified = diffusion @ flipped
    stages = np.array([uniform, flipped, amplified])
    assert np.allclose(uniform, [0.5] * 4)
    assert np.allclose(flipped, [0.5, 0.5, 0.5, -0.5])
    assert np.isclose(flipped.mean(), 0.25)
    assert np.allclose(amplified, [0, 0, 0, 1])
    assert np.allclose(amplified, 2 * flipped.mean() - flipped)
    assert np.allclose(np.sum(stages ** 2, axis=1), 1)
    assert np.allclose(diffusion.T @ diffusion, np.eye(4))
    # The formula must describe arbitrary input amplitudes, including complex ones.
    probe = np.array([1 + 2j, -3j, 2 - 1j, -0.25 + 0.5j])
    assert np.allclose(diffusion @ probe, 2 * probe.mean() - probe)
    for title, values in zip(["Prepared", "Phase flipped", "Amplified"], stages):
        print(f"{title}: amplitudes={values.round(12).tolist()}, "
              f"norm_squared={np.dot(values, values):.12f}, "
              f"marked_probability={values[3] ** 2:.12f}")
    print(f"Mean after oracle: {flipped.mean():.12f}")

    blue, orange = "#1765a8", "#bf5900"
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 3, figsize=(9.6, 4.1), sharey=True)
    fig.suptitle("Four states, one marked answer: one Grover iteration", fontsize=14, y=0.97)
    titles = [r"Prepare $H^{\otimes 2}|00\rangle$", "Flip the marked phase",
              r"Reflect: $a_x\mapsto 2\overline{a}-a_x$"]
    summaries = ["Each outcome has probability 1/4",
                 "Probabilities still all 1/4",
                 "Marked outcome has probability 1"]
    for ax, values, title, summary in zip(axes, stages, titles, summaries):
        visible = values.copy()
        visible[np.abs(visible) < 1e-14] = 0
        ax.bar(np.arange(4), visible, color=[blue, blue, blue, orange], width=0.64)
        ax.axhline(0, color="#4c5964", lw=0.9)
        ax.set_xticks(np.arange(4), [r"$|00\rangle$", r"$|01\rangle$",
                                   r"$|10\rangle$", r"$|11\rangle$"])
        ax.set(xlim=(-0.55, 3.55), ylim=(-0.73, 1.17), title=title)
        ax.grid(axis="y", alpha=0.15)
        ax.set_axisbelow(True)
        for i, value in enumerate(visible):
            ax.text(i, value + (0.05 if value >= 0 else -0.06), f"{value:g}",
                    ha="center", va="bottom" if value >= 0 else "top", fontsize=11)
        ax.text(0.5, -0.21, summary, transform=ax.transAxes, ha="center", fontsize=9)
    axes[0].set_ylabel("Real probability amplitude (signed)")
    axes[0].set_yticks([-0.5, 0, 0.25, 0.5, 1])
    axes[1].axhline(flipped.mean(), color="#727272", ls="--", lw=1.4)
    axes[1].text(-0.35, 0.29, r"Mean $\overline{a}=1/4$", color="#505050", fontsize=9,
                 bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})
    fig.text(0.5, 0.035, r"Orange marks $|11\rangle$. The dashed mean is an amplitude, not a probability.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.075, right=0.985, top=0.78, bottom=0.27, wspace=0.2)
    path = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(path, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print(path)


if __name__ == "__main__":
    main()
