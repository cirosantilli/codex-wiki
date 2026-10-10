"""Draw an exact Cholesky factorization and two solves; output PNG to CWD."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    a = np.array([[4, 2], [2, 5]])
    lower = np.array([[2, 0], [1, 2]])
    assert np.array_equal(lower @ lower.T, a)
    assert np.array_equal(a @ np.array([1, 2]), np.array([8, 12]))
    fig, ax = plt.subplots(figsize=(10.8, 5.8), dpi=120)
    fig.patch.set_facecolor("white")
    ax.set(xlim=(0, 10.8), ylim=(0, 5.8))
    ax.axis("off")
    ax.text(5.4, 5.48, "One factorization, two triangular solves", ha="center", fontsize=19, weight="bold")

    def matrix(center, label, data):
        ax.text(center, 4.93, label, ha="center", fontsize=19)
        for row in range(2):
            for col in range(2):
                value = data[row, col]
                ax.text(center+(col-.5)*.7, 4.31-row*.65, str(value), ha="center", va="center", fontsize=22, color="#26718b" if value else "#aaaaaa")
        for x, sign in [(center-.73, 1), (center+.73, -1)]:
            ax.plot([x+sign*.14, x, x, x+sign*.14], [4.68, 4.68, 3.27, 3.27], color="#222222", lw=1.7)

    matrix(1.9, r"$A$", a)
    matrix(5.35, r"$L$", lower)
    matrix(8.75, r"$L^T$", lower.T)
    ax.text(3.62, 3.97, "=", fontsize=25, ha="center", va="center")
    ax.text(7.04, 3.97, "×", fontsize=25, ha="center", va="center")
    ax.plot([.4, 10.4], [2.92, 2.92], color="#dddddd")
    ax.text(.6, 2.54, r"Given $b=(8,12)^T$, first solve $Ly=b$:", fontsize=15)
    ax.text(1.1, 1.98, r"$2y_1=8,\quad y_1+2y_2=12$", fontsize=17)
    ax.text(7.1, 1.98, r"$y=(4,4)^T$", fontsize=17, color="#26718b")
    ax.text(.6, 1.34, r"Then solve $L^Tx=y$:", fontsize=15)
    ax.text(1.1, .81, r"$2x_2=4,\quad 2x_1+x_2=4$", fontsize=17)
    ax.text(7.1, .81, r"$x=(1,2)^T$", fontsize=17, color="#26718b")
    ax.text(5.4, .14, "Positive diagonal entries fix the signs of the triangular factor.", ha="center", fontsize=12)
    fig.subplots_adjust(left=.01, right=.99, top=.99, bottom=.01)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
