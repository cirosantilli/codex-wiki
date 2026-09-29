"""Fair-bit Hamming rate-distortion curve; write matching PNG to cwd."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def main():
    distortion = np.linspace(0, .5, 501)
    entropy = np.zeros_like(distortion)
    mask = distortion > 0
    entropy[mask] = (-distortion[mask] * np.log2(distortion[mask])
                     - (1 - distortion[mask]) * np.log2(1 - distortion[mask]))
    fig, ax = plt.subplots(figsize=(9.4, 4.8), layout="constrained")
    ax.plot(distortion, 1 - entropy, lw=2.6, color="#285f87",
            label="Asymptotic minimum R(D) = 1 − binary entropy(D)")
    ax.plot([.5, .62], [0, 0], lw=2.6, color="#285f87")
    ax.fill_between(distortion, 0, 1 - entropy, color="#b45b59", alpha=.14,
                    label="Rates below the bound cannot meet this distortion")
    points = [(0, 1, "Exact recovery\n1 bit / source symbol", (.035, .91)),
              (.25, 1/3, "Three-bit majority code\nrate 1/3, average error 1/4", (.31, .50)),
              (.5, 0, "Always reconstruct zero\nrate 0, average error 1/2", (.33, .12))]
    for x, y, label, pos in points:
        ax.scatter([x], [y], s=55, c="#bc7328", zorder=4)
        ax.annotate(label, (x, y), xytext=pos, textcoords="data", fontsize=10,
                    arrowprops={"arrowstyle": "->", "color": ".35"})
    exact = 1 + .25*np.log2(.25) + .75*np.log2(.75)
    ax.plot([.25, .25], [exact, 1/3], color="#bc7328", ls="--", lw=1.4)
    ax.scatter([.25], [exact], s=35, color="#285f87", zorder=4)
    ax.set(xlim=(-.015, .62), ylim=(-.055, 1.10),
           xlabel="Allowed average fraction of incorrect source bits D",
           ylabel="Bits per original source symbol",
           title="Lossy compression of independent fair bits")
    ax.grid(alpha=.20)
    ax.legend(loc="upper right", fontsize=9)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
