"""Exact polynomial sampling counterexample; writes a PNG to the cwd."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def main():
    t = np.linspace(0, 2 * np.pi, 1001)
    samples = np.arange(5) * np.pi / 2
    values = np.exp(1j * samples)
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.6), layout="constrained")
    axes[0].plot(np.cos(t), np.sin(t), color="#315f86", lw=2, label="Outline of both full curves")
    axes[0].plot(values.real, values.imag, "o--", color="#ba5933", lw=2, label="Four samples, joined")
    for j in range(4):
        axes[0].annotate(f"j={j}", (values[j].real, values[j].imag),
                         xytext=(-27 if j == 0 else 8, 7), textcoords="offset points")
    axes[0].scatter([0], [0], color="black", s=22)
    axes[0].set(aspect="equal", xlim=(-1.3, 1.3), ylim=(-1.3, 1.3),
                xlabel="Real part", ylabel="Imaginary part", title="Identical samples; different full traversals")
    axes[0].legend(loc="lower center", bbox_to_anchor=(0.5, -0.32), frameon=False, fontsize=9)
    axes[1].plot(t / (2*np.pi), t / (2*np.pi), color="#315f86", lw=2, label="z: one turn")
    axes[1].plot(t / (2*np.pi), 5*t / (2*np.pi), color="#24824c", lw=2, label="z⁵: five turns")
    axes[1].step(samples / (2*np.pi), samples / (2*np.pi), where="post", color="#ba5933", ls="--",
                 label="Shortest sampled increments")
    axes[1].scatter(samples / (2*np.pi), samples / (2*np.pi), color="#ba5933", s=24, zorder=5)
    axes[1].set(xlabel="Boundary parameter t / (2π)", ylabel="Continuous argument / (2π)",
                title="Whole turns disappear between sparse samples", xlim=(0, 1), ylim=(-0.15, 5.25))
    axes[1].legend(loc="upper left", fontsize=9)
    axes[1].grid(alpha=0.2)
    fig.suptitle("Boundary sampling cannot certify winding without control between samples", fontsize=13)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
