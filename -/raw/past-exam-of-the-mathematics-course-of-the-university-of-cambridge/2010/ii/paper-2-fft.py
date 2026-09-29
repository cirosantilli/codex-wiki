"""Radix-two inverse FFT network; Python 3.14, Matplotlib 3.10.

Writes only paper-2-fft.png in the caller's current directory.
The caller controls MPLCONFIGDIR.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 6), layout="constrained")
for stage, q in enumerate([2, 4, 8]):
    for block in range(0, 8, q):
        for j in range(q//2):
            top, bottom = block+j, block+j+q//2
            for src in [top, bottom]:
                for dst in [top, bottom]:
                    ax.plot([stage, stage+1], [-src, -dst], color="navy" if src==dst else "steelblue", alpha=0.8, lw=1)
            ax.text(stage+0.13, -bottom+0.08, rf"$\omega_{{{q}}}^{{{j}}}$", fontsize=8, bbox={"facecolor":"white", "edgecolor":"none", "pad":1})
    ax.text(stage+0.5, 0.85, f"Block size {q}", ha="center")
for col in range(4):
    ax.plot([col]*8, [-j for j in range(8)], "ko", ms=4)
for row, index in enumerate([0, 4, 2, 6, 1, 5, 3, 7]):
    ax.text(-0.1, -row, rf"$y_{index}$", ha="right", va="center")
    ax.text(3.1, -row, rf"$x_{row}$", ha="left", va="center")
ax.text(1.5, -8, r"Each butterfly: $(a,b)\mapsto(a+\omega_q^j b,\ a-\omega_q^j b)$", ha="center")
ax.set(xlim=(-0.45, 3.45), ylim=(-8.4, 1.5), title="Eight-point inverse FFT: bit-reversed input, ordered output")
ax.axis("off")
fig.savefig("paper-2-fft.png", dpi=125, facecolor="white", transparent=False)
