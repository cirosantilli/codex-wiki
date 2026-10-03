"""Original travelling profiles; Python 3.14 and declared root dependencies.

Output PNG basename to caller CWD; do not override MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    xi = np.linspace(-7, 7, 1001)
    nutrient = 1/(1+np.exp(-xi))
    bacteria = nutrient*(1-nutrient)
    fig, ax = plt.subplots(figsize=(8, 4), layout="constrained")
    ax.plot(xi, nutrient, color="#27753c", lw=2, label=r"Nutrient $a$")
    ax.plot(xi, bacteria, color="#1d5ca6", lw=2, label=r"Scaled bacteria $kDb/c^2$")
    ax.annotate("Motion into fresh nutrient", xy=(5, .58), xytext=(1, .58),
                arrowprops={"arrowstyle":"->"}, fontsize=10)
    ax.set(xlabel=r"$\xi=cz/D$", ylabel="Dimensionless concentration",
           ylim=(-.02, 1.05), title=r"Travelling band: $\chi=2D$, $K=1$")
    ax.legend(loc="upper left")
    ax.grid(alpha=.15)
    fig.savefig("paper-2-chemotactic-band.png", dpi=115, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
