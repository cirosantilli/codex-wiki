"""Original joint-register quantum Fourier probabilities; write PNG to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(11, 4.7), dpi=100, facecolor="white")
for ax, Q, N, r in [(axes[0], 16, 15, 4), (axes[1], 32, 21, 6)]:
    state = np.zeros((Q, N), complex)
    for x in range(Q):
        state[x, pow(2, x, N)] = 1 / np.sqrt(Q)
    # NumPy's inverse transform has the positive phase used in the paper.
    transformed = np.fft.ifft(state, axis=0) * np.sqrt(Q)
    probability = np.sum(abs(transformed)**2, axis=1)
    assert np.isclose(probability.sum(), 1)
    ax.bar(np.arange(Q), probability, color="tab:blue", width=0.78, zorder=3)
    for target in np.arange(r) * Q / r:
        ax.axvline(target, color="tab:red", ls=":", lw=1.3, alpha=0.75)
    ax.set(xlabel=r"Measured first-register integer $k$", ylabel="Probability",
           title=f"N={N}, a=2, order r={r}, register size Q={Q}",
           xlim=(-0.7, Q - 0.3), ylim=(0, 0.28))
    ax.grid(axis="y", alpha=0.22, zorder=0)
fig.text(0.5, 0.035, "Red dotted lines: reciprocal-period grid ℓQ/r. Nondividing periods give peaks near that grid.",
         ha="center", fontsize=10.5)
fig.subplots_adjust(left=0.075, right=0.985, top=0.88, bottom=0.19, wspace=0.23)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white")
