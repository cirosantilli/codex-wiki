"""Write inverse-problem-blur-and-regularization.png into cwd.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media; only NumPy, Matplotlib and the standard library are used.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    a = np.array([[0.55, 0.45], [0.45, 0.55]])
    truth = np.array([1.0, 0.0])
    clean = a @ truth
    noisy = clean + np.array([0.01, -0.01])
    alpha = 0.01
    direct = np.linalg.solve(a, noisy)
    regularized = np.linalg.solve(a.T @ a + alpha * np.eye(2), a.T @ noisy)
    np.testing.assert_allclose(clean, [0.55, 0.45])
    np.testing.assert_allclose(direct, [1.1, -0.1])
    np.testing.assert_allclose(regularized, [803 / 1010, 197 / 1010])
    np.testing.assert_allclose(np.linalg.cond(a), 10)

    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.9), facecolor="white")
    fig.subplots_adjust(left=0.075, right=0.975, bottom=0.23, top=0.76, wspace=0.32)
    fig.suptitle("Two pixels: inversion amplifies contrast noise", y=0.98, fontsize=16)
    fig.text(0.5, 0.875, "A = [[0.55, 0.45], [0.45, 0.55]]    clean data (0.55, 0.45) → noisy data (0.56, 0.44)", ha="center")
    colors = ["#1765a8", "#bf5b16"]

    ax = axes[0]
    estimates = np.stack([truth, direct, regularized])
    groups = np.arange(3)
    for j in range(2):
        xs = groups + (j - 0.5) * 0.32
        bars = ax.bar(xs, estimates[:, j], width=0.30, color=colors[j], label=f"Pixel {j + 1}")
        for bar, value in zip(bars, estimates[:, j]):
            ax.text(bar.get_x() + bar.get_width() / 2, value + (0.035 if value >= 0 else -0.055), f"{value:.3f}", ha="center", va="bottom" if value >= 0 else "top", fontsize=10)
    ax.axhline(0, color="#555555", lw=0.8)
    ax.set_xticks(groups, ["True image", "Direct inverse", "Tikhonov\nα = 0.01"])
    ax.set_ylim(-0.26, 1.35)
    ax.set_ylabel("Reconstructed pixel value")
    ax.set_title("Less noise amplification, more bias")
    ax.legend(loc="upper right", frameon=False, fontsize=10)
    ax.set_axisbelow(True)
    ax.grid(axis="y", color="#e3e7eb")

    ax = axes[1]
    sigma = np.geomspace(0.005, 2, 400)
    attenuation = sigma**2 / (sigma**2 + alpha)
    ax.semilogx(sigma, attenuation, color="#5c378c", lw=2.4)
    for s, text, offset in [(0.1, "Difference mode\nσ = 0.1: retain 50%", (12, -40)), (1.0, "Mean mode\nσ = 1: retain 99.01%", (-225, -10))]:
        phi = s**2 / (s**2 + alpha)
        ax.plot([s, s], [0, phi], color="#999999", ls="--", lw=1)
        ax.scatter(s, phi, s=55, color="#5c378c", zorder=3)
        ax.annotate(text, (s, phi), xytext=offset, textcoords="offset points", fontsize=10, arrowprops={"arrowstyle": "->", "color": "#555555"} if s == 1 else None)
    ax.set_ylim(0, 1.13)
    ax.set_xlim(sigma[0], sigma[-1])
    ax.set_xlabel("Singular value σ (log scale)")
    ax.set_ylabel("Fraction of exact solution retained")
    ax.set_title(r"Attenuation $\phi_\alpha(\sigma)=\sigma^2/(\sigma^2+\alpha)$")
    ax.grid(color="#e3e7eb")
    for ax in axes:
        ax.set_facecolor("white")
        ax.spines[["top", "right"]].set_visible(False)
    fig.text(0.5, 0.045, "Penalty convention: ‖Ax − y‖² + α‖x‖².    Here α = 0.01 equals λ² with λ = 0.1.", ha="center", fontsize=11)
    fig.savefig(Path.cwd() / "inverse-problem-blur-and-regularization.png", dpi=110, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
