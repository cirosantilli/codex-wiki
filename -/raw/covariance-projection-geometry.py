"""Render a covariance ellipse and exact variance of directional projections."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    sigma = np.array([[1.0, 0.8], [0.8, 1.0]])
    values, vectors = np.linalg.eigh(sigma)
    assert np.allclose(values, [0.2, 1.8])
    root = (vectors * np.sqrt(values)) @ vectors.T
    assert np.allclose(root @ root.T, sigma)
    phi = np.linspace(0, 2 * np.pi, 601)
    ellipse = root @ np.vstack([np.cos(phi), np.sin(phi)])
    assert np.allclose(np.sum(ellipse * (np.linalg.inv(sigma) @ ellipse), axis=0), 1)
    theta = np.linspace(0, np.pi, 401)
    directions = np.vstack([np.cos(theta), np.sin(theta)])
    projected = np.sum(directions * (sigma @ directions), axis=0)
    assert np.allclose(projected, 1 + 0.8 * np.sin(2 * theta))
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 5.2), dpi=120, facecolor="white")
    ax = axes[0]
    ax.plot(*ellipse, color="#206a9d", lw=3)
    ax.fill(*ellipse, color="#206a9d", alpha=0.1)
    colors = ["#be7521", "#2f8a68"]
    for value, vector, color in zip(values, vectors.T, colors):
        tip = np.sqrt(value) * vector
        ax.plot([-tip[0], tip[0]], [-tip[1], tip[1]], color=color, lw=2)
        ax.annotate("", xy=tip, xytext=(0, 0),
                    arrowprops={"arrowstyle": "->", "lw": 2, "color": color})
    ax.text(0.58, 1.08, r"Long semiaxis: $\sqrt{1.8}$", color=colors[1], fontsize=11, ha="center")
    ax.text(-0.65, 0.87, r"Short semiaxis: $\sqrt{0.2}$", color=colors[0], fontsize=11, ha="center")
    ax.axhline(0, color="#b4bcc2", lw=1)
    ax.axvline(0, color="#b4bcc2", lw=1)
    ax.set(xlim=(-1.35, 1.35), ylim=(-1.35, 1.35), xlabel="First coordinate", ylabel="Second coordinate",
           title=r"Covariance ellipse: $x^T\Sigma^{-1}x=1$", aspect="equal")
    ax.grid(color="#e7eaed")
    ax = axes[1]
    ax.plot(np.degrees(theta), projected, color="#206a9d", lw=3)
    for degrees, value, color in [(45, 1.8, colors[1]), (135, 0.2, colors[0])]:
        ax.scatter(degrees, value, s=70, color=color, zorder=4)
        ax.axvline(degrees, color=color, lw=1, linestyle=":")
        label_position = (15, 2.02) if degrees == 45 else (75, 0.08)
        ax.annotate(f"{degrees}°: variance {value:g}", xy=(degrees, value),
                    xytext=label_position, color=color, fontsize=11, ha="left",
                    arrowprops={"arrowstyle": "->", "color": color})
    ax.set(xlim=(0, 180), ylim=(0, 2.1), xticks=[0, 45, 90, 135, 180],
           xlabel=r"Projection angle $\theta$ (degrees)", ylabel="Projected variance",
           title=r"$a^T\Sigma a=1+0.8\sin(2\theta)$")
    ax.grid(color="#e7eaed")
    for ax in axes:
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Unit coordinate variances, covariance 0.8: ninefold directional variance ratio", fontsize=14)
    fig.subplots_adjust(left=0.065, right=0.985, top=0.82, bottom=0.13, wspace=0.25)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
