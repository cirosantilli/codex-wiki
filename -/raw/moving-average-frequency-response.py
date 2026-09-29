"""Finite sums give exact moving-average frequency response and cancellation."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, (ax, phasor) = plt.subplots(1, 2, figsize=(11.6, 5.4), layout="constrained")
    frequencies = np.linspace(0, .5, 1501)
    for m, color in [(3, "#6b61a2"), (5, "#167e8d"), (9, "#c26030")]:
        response = np.exp(-2j * np.pi * frequencies[:, None] * np.arange(m)).mean(axis=1)
        assert np.isclose(response[0], 1)
        assert np.isclose(abs(response[-1]), 1 / m)
        assert np.max(abs(response)) <= 1 + 1e-12
        assert abs(np.mean(np.exp(-2j * np.pi * np.arange(m) / m))) < 1e-14
        ax.plot(frequencies, abs(response), color=color, lw=2.3, label=f"M = {m}")
    ax.scatter([.2], [0], color="#167e8d", s=45, zorder=4)
    ax.annotate("M = 5: first zero at f = 1/5", (.2, 0), xytext=(.24, .43),
                arrowprops={"arrowstyle": "->", "color": "#405660"}, fontsize=10)
    ax.set(xlabel="Frequency f (cycles per sample)", ylabel=r"Amplitude gain $|H(2\pi f)|$",
           xlim=(0, .5), ylim=(-.025, 1.08))
    ax.set_title("Longer windows narrow the main pass region", fontsize=14)
    ax.grid(alpha=.18)
    ax.legend(frameon=False)
    ax.spines[["top", "right"]].set_visible(False)
    contributions = np.exp(-2j * np.pi * np.arange(5) / 5)
    vertices = np.r_[0j, np.cumsum(contributions)]
    assert abs(vertices[-1]) < 1e-14
    colors = ["#167e8d", "#c26030", "#6b61a2", "#3c9468", "#526b92"]
    for j, color in enumerate(colors):
        start, end = vertices[j:j+2]
        phasor.annotate("", xy=(end.real, end.imag), xytext=(start.real, start.imag),
                        arrowprops={"arrowstyle": "->", "color": color, "lw": 2.5})
        midpoint = (start + end) / 2
        normal = 1j * (end - start)
        label = midpoint + .13 * normal
        phasor.text(label.real, label.imag, f"j = {j}", color=color, ha="center", va="center", fontsize=10)
    phasor.scatter([0], [0], color="#24343e", s=35)
    phasor.annotate("Start = finish", (0, 0), xytext=(-35, 16),
                    textcoords="offset points", fontsize=10)
    phasor.set_aspect("equal")
    phasor.set(xlim=(-.62, 1.54), ylim=(-1.84, .7))
    phasor.set_axis_off()
    phasor.set_title("At f = 1/5, five phase vectors sum to zero", fontsize=13)
    phasor.text(.45, -1.76, r"$H(2\pi/5)=\frac{1}{5}\sum_{j=0}^4e^{-2\pi i j/5}=0$",
                ha="center", fontsize=14)
    fig.suptitle("Moving-average filtering is a sum of delayed phase contributions", fontsize=16)
    fig.get_layout_engine().set(rect=(0, .055, 1, .945))
    fig.text(.5, .02, "The side lobes show why averaging is not an ideal frequency cutoff.",
             ha="center", fontsize=11)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=100, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
