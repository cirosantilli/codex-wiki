"""Draw an original ideal rectifier schematic and calculated waveform.

Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media to emit this script's matching PNG basename in the CWD.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Rectangle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "axes.spines.top": False,
                         "axes.spines.right": False})
    fig = plt.figure(figsize=(10, 6.5), dpi=120)
    fig.suptitle("Half-wave rectification: an ideal diode and a resistor load", y=0.965, fontsize=15)
    circuit = fig.add_axes([0.08, 0.56, 0.84, 0.32])
    circuit.set(xlim=(0, 10), ylim=(0, 3))
    circuit.set_aspect("equal")
    circuit.axis("off")
    wire = {"color": "#263238", "lw": 2}
    circuit.plot([1.5, 1.5, 4.2], [1.82, 2.45, 2.45], **wire)
    circuit.plot([5.15, 7.4, 7.4], [2.45, 2.45, 1.85], **wire)
    circuit.plot([7.4, 7.4, 1.5, 1.5], [0.95, 0.3, 0.3, 0.92], **wire)
    circuit.add_patch(Circle((1.5, 1.37), 0.45, fill=False, **wire))
    s = np.linspace(-0.25, 0.25, 100)
    circuit.plot(1.5 + s, 1.37 + 0.13 * np.sin(s * 4 * np.pi), **wire)
    circuit.text(0.7, 2.1, "+", fontsize=16)
    circuit.text(0.7, 0.55, "−", fontsize=16)
    circuit.text(0.2, 1.35, r"$v_S$", ha="center", fontsize=14)
    circuit.add_patch(Polygon([[4.2, 2.1], [4.2, 2.8], [4.95, 2.45]],
                              closed=True, facecolor="white", edgecolor="#263238", lw=2))
    circuit.plot([4.95, 4.95], [2.1, 2.8], **wire)
    circuit.plot([4.95, 5.15], [2.45, 2.45], **wire)
    circuit.text(3.8, 2.1, "A", fontsize=12)
    circuit.text(5.15, 2.1, "K (bar)", fontsize=12)
    circuit.text(4.65, 1.55, "Ideal diode", ha="center")
    circuit.add_patch(Rectangle((7.18, 0.95), 0.44, 0.9, fill=False, **wire))
    circuit.text(6.95, 1.3, r"$R_L=1\,\mathrm{k}\Omega$", ha="right", fontsize=12)
    circuit.text(8.3, 2.2, "+", fontsize=16)
    circuit.text(8.3, 0.6, "−", fontsize=16)
    circuit.text(8.65, 1.35, r"$v_L$", fontsize=14)
    circuit.annotate("", (7.98, 1.05), (7.98, 1.8), arrowprops={"arrowstyle": "->", "lw": 1.5})
    circuit.text(8.1, 1.4, r"$i_L$", fontsize=12)
    circuit.text(4.6, 0.05, r"$v_S=5\sin(\omega t)$ V; zero source resistance; no filter capacitor",
                 ha="center", va="top", fontsize=11)
    wave = fig.add_axes([0.09, 0.13, 0.84, 0.34])
    phase = np.linspace(0, 4 * np.pi, 2401)
    source = 5 * np.sin(phase)
    load = np.maximum(0, source)
    wave.plot(phase / np.pi, source, color="#b75513", lw=2, ls="--", label=r"Source $v_S$")
    wave.plot(phase / np.pi, load, color="#1565a6", lw=2.6, label=r"Load $v_L=\max(0,v_S)$")
    wave.axhline(5 / np.pi, color="#31764c", lw=1.7, ls=":", label=r"Average $5/\pi$ V")
    for left in [1, 3]:
        wave.axvspan(left, left + 1, color="#edf1f5", zorder=-1)
        wave.text(left + 0.5, 3.5, "Diode blocks", ha="center", fontsize=10)
    wave.set(xlim=(0, 4), ylim=(-5.6, 6), ylabel="Voltage (V)",
             xlabel=r"Phase $\omega t/\pi$ (two source cycles)", xticks=[0, 1, 2, 3, 4])
    wave.axhline(0, color="0.6", lw=0.8)
    wave.grid(alpha=0.2)
    wave.legend(loc="lower left", fontsize=10, framealpha=1)
    fig.text(0.5, 0.035, "Calculated ideal output: peak current 5 mA; average voltage 1.59155 V; RMS voltage 2.500 V.",
             ha="center", fontsize=10)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
