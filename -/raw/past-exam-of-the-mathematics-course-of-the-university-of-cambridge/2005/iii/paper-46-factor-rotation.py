"""Original two-factor sketch; Python 3.14.4 / NumPy 2.3.5 / Matplotlib 3.10.7.
Output the basename PNG to CWD; respect the caller's MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def main():
    loadings = np.array([[.85, .10], [.80, .15], [.10, .85], [.15, .80]])
    specific = 1 - np.sum(loadings**2, axis=1)
    covariance = loadings @ loadings.T + np.diag(specific)
    angle = np.pi/4
    rotation = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
    rotated = loadings @ rotation
    assert np.allclose(rotated @ rotated.T, loadings @ loadings.T)
    colors = ["#176aa0", "#599bbd", "#b85518", "#df9661"]
    fig, axes = plt.subplots(1, 3, figsize=(12, 4.5), dpi=100, facecolor="white", constrained_layout=True)
    for ax, matrix, title in zip(axes[:2], [loadings, rotated], ["An interpretable factor orientation", "Equivalent loadings after rotation"]):
        theta = np.linspace(0, 2*np.pi, 300)
        ax.plot(np.cos(theta), np.sin(theta), color="0.75", lw=1)
        for i, ((x, y), color) in enumerate(zip(matrix, colors)):
            ax.annotate("", xy=(x,y), xytext=(0,0), arrowprops={"arrowstyle": "->", "color": color, "lw": 2})
            offset = [(7, 7), (-10, -18), (5, 8), (9, -17)][i]
            ax.annotate(f"X{i+1}", xy=(x,y), xytext=offset, textcoords="offset points", color=color, fontsize=11)
        ax.axhline(0, color="0.75", lw=.7)
        ax.axvline(0, color="0.75", lw=.7)
        ax.set(xlim=(-1.1, 1.1), ylim=(-1.1, 1.1), xlabel="Factor 1 loading", ylabel="Factor 2 loading", title=title)
        ax.set_aspect("equal")
    values = np.linalg.eigvalsh(covariance)[::-1]
    axes[2].plot(range(1,5), values, "o-", color="#4d5763", lw=2)
    axes[2].set(xticks=range(1,5), xlabel="Component number", ylabel="Eigenvalue", title="Scree plot of the same covariance", ylim=(0, max(values)*1.2))
    axes[2].spines[["top", "right"]].set_visible(False)
    fig.suptitle("Factor rotation preserves covariance and communalities", fontsize=15)
    fig.savefig(Path.cwd() / "paper-46-factor-rotation.png", facecolor="white", transparent=False)
    plt.close(fig)

if __name__ == "__main__":
    main()
