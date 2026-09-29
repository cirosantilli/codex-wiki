"""Finite-record periodogram dispersion. Tested with Python 3.14.4,
NumPy 2.3.5 and Matplotlib 3.10.7. Writes the PNG basename to caller CWD.
MPLCONFIGDIR, if supplied, is left unchanged.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    rng = np.random.default_rng(200133)
    omega = 2 * np.pi / 5
    bins = np.linspace(0, 7, 48)
    fig, ax = plt.subplots(figsize=(7.5, 4.4), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    for length, color in zip((25, 125, 505), ("#1764aa", "#d46021", "#238553")):
        t = np.arange(1, length + 1)
        x = rng.normal(size=(8000, length))
        c = x @ np.cos(omega * t)
        s = x @ np.sin(omega * t)
        # I=(c²+s²)/(pi*T), and the one-sided white-noise density is 1/pi.
        normalized = (c*c + s*s) / length
        ax.hist(normalized, bins=bins, density=True, histtype="step",
                linewidth=1.7, color=color, label=f"T = {length}")
    v = np.linspace(0, 7, 400)
    ax.plot(v, np.exp(-v), color="#202020", linestyle="--",
            linewidth=2, label="Exp(1) density")
    ax.set(xlim=(0, 7), ylim=(0, 1.12),
           xlabel="Periodogram / one-sided spectral density",
           ylabel="Probability density",
           title="Longer records do not concentrate a raw periodogram")
    ax.axvline(1, color="#888888", linewidth=1, alpha=.65)
    ax.text(1.08, 1.04, "Target value = 1", color="#555555", fontsize=9)
    ax.grid(alpha=.18)
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig("paper-33-periodogram.png", facecolor="white", transparent=False)
    plt.close(fig)

if __name__ == "__main__":
    main()
