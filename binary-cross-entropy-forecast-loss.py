"""Binary expected log loss at fixed true probability; output PNG to cwd."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def main():
    r = .25
    q = np.linspace(.002, .998, 1201)
    event_loss = -np.log2(q)
    nonevent_loss = -np.log2(1-q)
    expected = r*event_loss + (1-r)*nonevent_loss
    optimum = -r*np.log2(r) - (1-r)*np.log2(1-r)
    fig, ax = plt.subplots(figsize=(9.6, 4.8), layout="constrained")
    ax.plot(q, event_loss, color="#b5702b", lw=1.8, label="Event occurs: −log₂ q")
    ax.plot(q, nonevent_loss, color="#777777", lw=1.8, label="No event: −log₂(1−q)")
    ax.plot(q, expected, color="#315f86", lw=2.7,
            label="Average = 1/4 event loss + 3/4 nonevent loss")
    ax.axvline(r, color="#315f86", ls="--", lw=1.2)
    ax.scatter([r, .5, .01], [optimum, 1, -.25*np.log2(.01)-.75*np.log2(.99)],
               color="#315f86", s=45, zorder=5)
    ax.annotate("Truthful q = 1/4\nminimum ≈ 0.8113 bits", (r, optimum),
                xytext=(.32, 2.45), arrowprops={"arrowstyle":"->", "color":".3"}, fontsize=10)
    ax.annotate("q = 0.01\naverage ≈ 1.6718 bits", (.01, -.25*np.log2(.01)-.75*np.log2(.99)),
                xytext=(.10, 3.75), arrowprops={"arrowstyle":"->", "color":".3"}, fontsize=10)
    ax.set(xlim=(0, 1), ylim=(0, 5.8), xlabel="Reported event probability q",
           ylabel="Logarithmic loss in bits",
           title="The event truly occurs with probability r = 1/4")
    ax.grid(alpha=.20)
    ax.legend(loc="upper right", fontsize=9)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
