"""Draw the three fractional-power values; Python 3.14, numpy 2.3.5, matplotlib 3.10.7."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    z = np.exp(3j * np.pi / 4)
    roots = np.exp(1j * np.array([np.pi / 2, 7 * np.pi / 6, 11 * np.pi / 6]))
    fig, ax = plt.subplots(figsize=(6.4, 5.2), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    theta = np.linspace(0, 2 * np.pi, 401)
    ax.plot(np.cos(theta), np.sin(theta), color="#999999", linewidth=1)
    ax.axhline(0, color="#bbbbbb", linewidth=0.8)
    ax.axvline(0, color="#bbbbbb", linewidth=0.8)
    labels = [r"$w_0=i$", r"$w_1=-\sqrt{3}/2-i/2$", r"$w_2=\sqrt{3}/2-i/2$"]
    offsets = [(12, 5), (-3, -26), (-98, -26)]
    for k, (w, label, offset) in enumerate(zip(roots, labels, offsets)):
        color = "#bc3529" if k == 2 else "#2474a5"
        ax.plot([z.real, w.real], [z.imag, w.imag], color=color,
                linewidth=2.5 if k == 2 else 1.4,
                linestyle="-" if k == 2 else "--")
        ax.scatter(w.real, w.imag, color=color, s=45, zorder=4)
        ax.annotate(label, (w.real, w.imag), xytext=offset,
                    textcoords="offset points", fontsize=11)
    ax.scatter(z.real, z.imag, color="#222222", s=45, zorder=5)
    ax.annotate(r"$z=e^{3\pi i/4}$", (z.real, z.imag), xytext=(-45, 16),
                textcoords="offset points", fontsize=12)
    ax.set(xlim=(-1.38, 1.38), ylim=(-1.12, 1.35),
           xlabel="Real part", ylabel="Imaginary part",
           title=r"Three values of $z^{2/3}$; red segment is longest")
    ax.set_aspect("equal")
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False, metadata={"Software": "Matplotlib"})
    plt.close(fig)


if __name__ == "__main__":
    main()
