"""Original toy bench layout and calculated phase measurement, not acquired data.

Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python ../reactance-bench-phase-sensing.py
Writes reactance-bench-phase-sensing.png to CWD.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
import numpy as np


def main():
    L, C, R, Rs, Vrms, f = 10e-3, 1e-6, 100.0, 10.0, 1.0, 500.0
    w = 2 * np.pi * f
    x = w * L - 1 / (w * C)
    phase = np.arctan2(x, R + Rs)
    Irms = Vrms / np.hypot(R + Rs, x)
    t = np.linspace(0, 4e-3, 1201)
    va = np.sqrt(2) * Vrms * np.sin(w * t)
    vb = np.sqrt(2) * Irms * Rs * np.sin(w * t - phase)
    ta, tb = 1 / f, 1 / f + phase / w
    blue, green = "#2855a5", "#177352"
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    fig = plt.figure(figsize=(10.4, 7.7), layout="constrained")
    gs = fig.add_gridspec(3, 1, height_ratios=[1.35, 1, 1])
    circuit, a, b = (fig.add_subplot(gs[k]) for k in range(3))
    fig.suptitle("Measure current with a return-side resistor\n"
                 "Toy L = 10 mH, C = 1 μF, R = 100 Ω, Rₛ = 10 Ω; f = 500 Hz\n"
                 "Layout + ideal predictions • no measured data", fontsize=13)
    circuit.set(xlim=(-0.5, 10.5), ylim=(-0.7, 3.2), aspect="equal")
    circuit.axis("off")
    circuit.add_patch(Circle((0.6, 1.25), 0.42, fill=False, linewidth=1.8))
    s = np.linspace(-0.3, 0.3, 100)
    circuit.plot(0.6 + s, 1.25 + 0.12 * np.sin(2 * np.pi * (s + 0.3) / 0.6), color="black")
    circuit.plot([0.6, 0.6, 1.4], [1.67, 2.15, 2.15], color="black")
    circuit.plot([0.6, 0.6, 9.6], [0.83, 0.1, 0.1], color="black")
    circuit.text(1.25, 1.15, "Sine\ngenerator", fontsize=10)
    circuit.text(0.65, 0.48, "−", ha="left")
    circuit.text(0.65, 1.85, "+", ha="left")
    # Rectangles denote explicitly labeled ideal series components.
    for start, end, label in [(1.7, 3.5, "L = 10 mH"), (4.0, 5.8, "C = 1 μF"), (6.3, 8.1, "R = 100 Ω")]:
        circuit.add_patch(Rectangle((start, 1.85), end-start, 0.6, facecolor="white", edgecolor="black", linewidth=1.5))
        circuit.text((start+end)/2, 2.15, label, ha="center", va="center", fontsize=10)
    for start, end in [(1.4, 1.7), (3.5, 4.0), (5.8, 6.3), (8.1, 9.6)]:
        circuit.plot([start, end], [2.15, 2.15], color="black")
    circuit.plot([9.6, 9.6], [2.15, 1.65], color="black")
    circuit.add_patch(Rectangle((9.3, 0.6), 0.6, 1.05, facecolor="white", edgecolor="black", linewidth=1.5))
    circuit.plot([9.6, 9.6], [0.6, 0.1], color="black")
    circuit.text(8.8, 1.08, "Rₛ\n10 Ω", ha="right", va="center", fontsize=10)
    circuit.text(9.9, 1.47, "+", ha="left", fontsize=10)
    circuit.text(9.9, 0.45, "−", ha="left", fontsize=10)
    for px, py, label, color in [(1.4, 2.15, "A: loaded voltage", blue), (9.6, 1.78, "B: vₛ = Rₛ i", green)]:
        circuit.plot(px, py, "o", color=color, markersize=5)
        circuit.annotate(label, xy=(px, py), xytext=(px, 2.8), ha="center", color=color,
                         arrowprops={"arrowstyle": "-", "color": color}, fontsize=10)
    circuit.annotate("i", xy=(5.8, 1.35), xytext=(4.2, 1.35), va="center",
                     arrowprops={"arrowstyle": "->", "color": "black"})
    circuit.text(4.7, -0.4, "Common return: both scope grounds + generator return", ha="center", fontsize=10)
    circuit.plot([4.7, 4.7], [0.1, -0.06], color="black")
    for dy, halfwidth in [(-0.06, .18), (-0.13, .12), (-0.2, .06)]:
        circuit.plot([4.7-halfwidth, 4.7+halfwidth], [dy, dy], color="black")
    a.plot(t * 1000, va, color=blue, linewidth=2)
    b.plot(t * 1000, vb * 1000, color=green, linewidth=2)
    a.set(ylabel="Channel A (V)", ylim=(-1.8, 1.8), yticks=[-1.4, 0, 1.4])
    b.set(ylabel="Channel B (mV)", ylim=(-66, 92), yticks=[-46, 0, 46], xlabel="Time (ms)")
    a.text(0.05, 0.9, "Vᵣₘₛ = 1.00 V  •  peak = 1.414 V", transform=a.transAxes, color=blue, fontsize=10)
    b.text(0.05, 0.9, f"Vₛ,ᵣₘₛ = {1000*Irms*Rs:.2f} mV  •  Iᵣₘₛ = {1000*Irms:.3f} mA", transform=b.transAxes, color=green, fontsize=10)
    for ax in (a, b):
        ax.set_xlim(0, 4)
        ax.axhline(0, color="0.4", linewidth=0.8)
        ax.axvline(ta * 1000, color=blue, linestyle=":")
        ax.axvline(tb * 1000, color=green, linestyle=":")
        ax.grid(alpha=0.17)
    b.annotate("", xy=(ta*1000, 69), xytext=(tb*1000, 69),
               arrowprops={"arrowstyle": "<->", "color": "0.2"})
    b.text(2.08, 69, f"Current rises {1000*(ta-tb):.4f} ms earlier\nφ = {np.degrees(phase):.2f}°", fontsize=10, va="center")
    fig.savefig(Path.cwd() / "reactance-bench-phase-sensing.png", dpi=105,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
