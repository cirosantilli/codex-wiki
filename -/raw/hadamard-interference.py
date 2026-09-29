"""Draw hadamard-interference.png in cwd; Python 3.14, NumPy, Matplotlib.

From the repository root: cd _media && python ../hadamard-interference.py
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    h = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
    zero = np.array([1, 0], dtype=complex)
    phi = np.linspace(0, 2 * np.pi, 601)
    outputs = np.array([h @ np.diag([1, np.exp(1j * p)]) @ h @ zero for p in phi])
    probabilities = np.abs(outputs) ** 2
    error = np.max(np.abs(probabilities[:, 1] - np.sin(phi / 2) ** 2))
    assert error < 1e-14
    assert np.allclose(h @ h @ zero, zero)
    assert np.allclose(h @ np.diag([1, -1]) @ h @ zero, [0, 1])
    assert np.allclose(probabilities.sum(axis=1), 1)
    mixed = np.eye(2) / 2
    for p in [0, np.pi / 3, np.pi / 2, np.pi]:
        u = h @ np.diag([1, np.exp(1j * p)])
        assert np.allclose(u @ mixed @ u.conj().T, mixed)
        state = h @ np.diag([1, np.exp(1j * p)]) @ h @ zero
        print(f"phi/pi={p / np.pi:.6f}: P(1)={abs(state[1]) ** 2:.12f}")
    print(f"Maximum phase-sweep probability error: {error:.3g}")

    blue, orange, ink = "#1765a8", "#bf5900", "#253646"
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.6, 4.5),
                                     gridspec_kw={"width_ratios": [1.3, 1]})
    fig.suptitle(r"Phase becomes a probability: $|0\rangle\ \to H\ \to P_\phi\ \to H$",
                 fontsize=14, y=0.98)
    left.plot(phi / np.pi, probabilities[:, 1], color=orange, lw=2.5,
              label=r"$P(1)=\sin^2(\phi/2)$")
    left.plot(phi / np.pi, probabilities[:, 0], color=blue, lw=2,
              label=r"$P(0)=\cos^2(\phi/2)$")
    left.axhline(0.5, color="#727272", ls="--", lw=1.5,
                 label="Complete dephasing: P(1) = 1/2")
    left.scatter([0, 1 / 3, 1 / 2, 1], [0, 1 / 4, 1 / 2, 1],
                 color=orange, s=30, zorder=4)
    left.set(xlim=(-0.04, 2.04), ylim=(-0.045, 1.045),
             xlabel=r"Relative phase $\phi / \pi$", ylabel="Output probability",
             title="A fringe from coherent recombination")
    left.set_xticks([0, 0.5, 1, 1.5, 2], ["0", "1/2", "1", "3/2", "2"])
    left.set_yticks([0, 0.25, 0.5, 0.75, 1])
    left.grid(alpha=0.2)
    left.legend(loc="upper center", bbox_to_anchor=(0.5, -0.2), frameon=False,
                fontsize=9)

    circle = (1 - np.exp(1j * phi)) / 2
    right.plot(circle.real, circle.imag, color="#c6cdd4", ls=":", lw=1.5)
    right.axhline(0, color="#c6cdd4", lw=0.8)
    right.axvline(0, color="#c6cdd4", lw=0.8)
    a = 0.5 - 0.5j
    for start, end, color, width in [(0j, 0.5 + 0j, blue, 2.5),
                                    (0.5 + 0j, a, orange, 2.5),
                                    (0j, a, ink, 2)]:
        right.annotate("", xy=(end.real, end.imag), xytext=(start.real, start.imag),
                       arrowprops={"arrowstyle": "->", "color": color, "lw": width})
    right.text(0.23, 0.06, r"$1/2$", color=blue, ha="center", fontsize=12)
    right.text(0.56, -0.26, r"$-e^{i\phi}/2=-i/2$", color=orange, fontsize=11)
    right.text(0.0, -0.59, r"$a_1=(1-i)/2$", color=ink, fontsize=11)
    right.scatter([a.real], [a.imag], color=ink, s=25, zorder=4)
    right.set(xlim=(-0.15, 1.16), ylim=(-0.65, 0.65), aspect="equal",
              xlabel="Real part of output-one amplitude",
              ylabel="Imaginary part", title=r"Add complex contributions at $\phi=\pi/2$")
    right.set_xticks([0, 0.5, 1])
    right.set_yticks([-0.5, 0, 0.5])
    right.text(0.5, -0.27, r"$P(1)=|a_1|^2=1/2$", transform=right.transAxes,
               ha="center", fontsize=11)
    fig.subplots_adjust(left=0.075, right=0.98, top=0.82, bottom=0.28, wspace=0.38)
    path = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(path, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print(path)


if __name__ == "__main__":
    main()
