"""Plot the fitted teaching-method models; write the PNG to the caller's CWD."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    aptitude = np.array([3, 1, 3, 1, 2, 1, 4, 4, 5, 5, 4, 3, 1, 2, 3, 2, 2, 3, 4, 1, 4], dtype=float)
    score = np.array([6, 4, 5, 3, 4, 3, 6, 8, 9, 7, 9, 8, 5, 7, 6, 7, 7, 7, 8, 5, 7], dtype=float)
    group = np.repeat(np.arange(3), 7)
    design = np.column_stack([np.ones(21), aptitude, group == 1, group == 2])
    coefficients = np.linalg.lstsq(design, score, rcond=None)[0]
    colours = ["#2866a8", "#b8422e", "#388451"]
    markers = ["o", "s", "^"]
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.5), facecolor="white", sharex=True, sharey=True)
    for ax in axes:
        ax.set_facecolor("white")
        for g in range(3):
            selected = group == g
            ax.scatter(aptitude[selected], score[selected], color=colours[g], marker=markers[g], s=48, zorder=3, label=f"Method {'ABC'[g]}")
        ax.set(xlabel="Initial aptitude", ylabel="Final achievement", xlim=(0.7, 5.3), ylim=(2.5, 10.1), xticks=np.arange(1, 6))
        ax.grid(alpha=0.18)
        ax.spines[["top", "right"]].set_visible(False)
    grid = np.linspace(1, 5, 150)
    for g in range(3):
        selected = group == g
        intercept, slope = np.linalg.lstsq(np.column_stack([np.ones(7), aptitude[selected]]), score[selected], rcond=None)[0]
        axes[0].plot(grid, intercept + slope * grid, color=colours[g], linewidth=2)
        common_intercept = coefficients[0] + (coefficients[2] if g == 1 else coefficients[3] if g == 2 else 0)
        axes[1].plot(grid, common_intercept + coefficients[1] * grid, color=colours[g], linewidth=2)
    axes[0].set_title("Separate slopes: interaction model")
    axes[1].set_title("Preferred model: parallel fitted lines")
    axes[0].legend(loc="upper left", frameon=False)
    axes[1].text(1.05, 9.75, "Common slope = 0.743\nB − A = 2.188; C − A = 1.861", va="top", fontsize=9)
    fig.tight_layout()
    fig.savefig("paper-43-teaching-methods.png", dpi=140, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
