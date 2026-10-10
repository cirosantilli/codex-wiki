"""Chosen ideal bands, not measured data; tested with Python 3.14.

Uses NumPy 2.3.5 and Matplotlib 3.10.7. Run from _media to emit the PNG.
Both models are normalized to the same first 2+ excitation energy.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.5), dpi=120, sharey=True)
    rotor, vibrator = axes
    for ax in axes:
        ax.set(xlim=(0, 1), ylim=(-0.35, 7.8), xticks=[])
        ax.spines[["top", "right", "bottom"]].set_visible(False)
        ax.grid(axis="y", color="#e5e7eb", lw=0.7)
        ax.set_yticks(np.arange(0, 8))
    rotor.set_ylabel(r"Excitation energy / $E(2_1^+)$")
    rotor.set_title(r"Axial rotor: $K=0$" + "\n" + r"$E(I)/E(2)=I(I+1)/6$", pad=14)
    vibrator.set_title("Harmonic quadrupole vibrator\n" + r"$E(n)/E(2)=n$", pad=14)
    spins = np.array([0, 2, 4, 6])
    energies = spins * (spins + 1) / 6
    for spin, energy in zip(spins, energies):
        rotor.hlines(energy, 0.19, 0.69, color="#127b88", lw=2.5)
        rotor.text(0.72, energy, f"{spin}" + r"$^+$", va="center")
    for low, high in zip(energies[:-1], energies[1:]):
        rotor.annotate("", xy=(0.27, low + 0.06), xytext=(0.27, high - 0.06),
                       arrowprops={"arrowstyle": "->", "lw": 1.5, "color": "#127b88"})
    vibrator.hlines(0, 0.19, 0.69, color="#be6c24", lw=2.5)
    vibrator.text(0.72, 0, r"$0^+$", va="center")
    vibrator.hlines(1, 0.19, 0.69, color="#be6c24", lw=2.5)
    vibrator.text(0.72, 1, r"$2^+$", va="center")
    for x, spin in zip([0.20, 0.45, 0.70], [0, 2, 4]):
        vibrator.hlines(2, x - 0.09, x + 0.09, color="#be6c24", lw=2.5)
        vibrator.text(x, 2.15, f"{spin}" + r"$^+$", ha="center", va="bottom")
        vibrator.annotate("", xy=(0.45, 1.07), xytext=(x, 1.93),
                          arrowprops={"arrowstyle": "->", "lw": 1.3, "color": "#be6c24"})
    vibrator.annotate("", xy=(0.45, 0.07), xytext=(0.45, 0.93),
                      arrowprops={"arrowstyle": "->", "lw": 1.3, "color": "#be6c24"})
    vibrator.text(0.45, 3.05, "Two-quantum multiplet:\n" + r"$0^+,\ 2^+,\ 4^+$" +
                   "\n\nHigher multiplets omitted", ha="center", color="#5f4938")
    rotor.text(0.64, 5.0, r"$E(4)/E(2)=10/3$", ha="center", color="#127b88", fontsize=14)
    vibrator.text(0.45, 5.0, r"$E(4_1^+)/E(2_1^+)=2$", ha="center", color="#be6c24", fontsize=14)
    fig.suptitle("Rotation and vibration leave different energy patterns", fontsize=16, y=0.98)
    fig.text(0.5, 0.028, "Original ideal-model levels. Arrows: selected E2 decays; widths do not encode strength.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.085, right=0.975, top=0.80, bottom=0.105, wspace=0.20)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white",
                transparent=False, dpi=120)
    plt.close(fig)


if __name__ == "__main__":
    main()
