"""Original modulation/filter spectra; Python 3.14, NumPy, Matplotlib. PNG to cwd."""
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 3, figsize=(11.6, 3.8), layout="constrained", facecolor="white")
triangle = lambda w: np.maximum(1 - np.abs(w), 0)
w = np.linspace(-1.5, 1.5, 1000)
axes[0].plot(w, triangle(w), color="#1565a8", lw=2)
axes[0].set(title="Message spectrum", xlabel=r"$\omega$", ylabel=r"$|\widetilde{s}|/\pi$", xlim=(-1.5, 1.5))
for ax, carrier in [(axes[1], 2), (axes[2], 0.75)]:
    w = np.linspace(-carrier - 1.3, carrier + 1.3, 1800)
    continuous = (triangle(w - carrier) + triangle(w + carrier)) / 2
    ax.plot(w, continuous, color="0.45", lw=2, label=r"Continuous $\widetilde{\phi}/\pi$")
    for sign in [-1, 1]:
        ax.annotate("", (sign * carrier, 1.02), (sign * carrier, 0), arrowprops={"arrowstyle": "->", "color": "#c35419", "lw": 1.6})
    ax.text(0, 1.07, r"Carrier lines: weight $\pi$ each", ha="center", color="#9b3f10", fontsize=9)
    ax.set(xlabel=r"$\omega$", ylabel=r"Continuous spectrum / $\pi$", xlim=(w.min(), w.max()))
axes[1].set_title(r"Separated bands: $\Omega=2$")
ax = axes[2]
inside = np.linspace(-0.75, 0.75, 800)
retained = (triangle(inside - 0.75) + triangle(inside + 0.75)) / 2
ax.fill_between(inside, retained, color="#7bb5df", alpha=0.4)
ax.plot(inside, retained, color="#1565a8", lw=2.5, label=r"Retained $\widetilde{\rho}/\pi$")
for sign in [-1, 1]:
    ax.plot([sign * 0.75] * 2, [0, 0.5], color="#1565a8", ls="--", lw=1)
ax.set_title(r"Overlapping bands: $\Omega=3/4$")
ax.legend(loc="upper center", bbox_to_anchor=(0.5, 0.88), fontsize=8, framealpha=0.97)
for ax in axes:
    ax.set_ylim(-0.025, 1.2)
    ax.axhline(0, color="0.3", lw=0.7)
    ax.grid(alpha=0.15)
fig.savefig("paper-1-q4-modulation-spectra.png", dpi=160, facecolor="white")
plt.close(fig)
