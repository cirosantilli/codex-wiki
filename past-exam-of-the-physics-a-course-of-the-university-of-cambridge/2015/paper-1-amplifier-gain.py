"""Original transfer-function plot; Python 3.14, NumPy and Matplotlib."""
import numpy as np
import matplotlib.pyplot as plt

f = np.geomspace(0.01, 100, 1600)
fc = 1/(2*np.pi)
gain = 1000/np.sqrt(1+(f/fc)**2)
fig, ax = plt.subplots(figsize=(7.7, 5.0), layout="constrained")
ax.loglog(f, gain, color="#175b98", lw=2.5, label="Exact ideal response")
ax.loglog([.01, fc, 100], [1000, 1000, 1000*fc/100], "--", color="#c06c22", lw=1.3, label="Low/high frequency asymptotes")
ax.axvline(fc, color="0.5", ls=":", lw=1)
ax.scatter([fc], [1000/np.sqrt(2)], color="#175b98", zorder=5)
ax.annotate("Corner: 0.159 Hz\nGain: 707.1", xy=(fc, 1000/np.sqrt(2)), xytext=(.45, 900), arrowprops=dict(arrowstyle="->"), fontsize=10)
ax.text(.012, 1200, "DC plateau: 1000", fontsize=10)
ax.text(2, 65, "Slope: -1 on log-log axes\n(-20 dB per decade)", fontsize=10)
ax.scatter([.01, 100], [gain[0], gain[-1]], color="#175b98")
ax.annotate("100 Hz: 1.592", xy=(100, gain[-1]), xytext=(7, 1.9), fontsize=10, arrowprops=dict(arrowstyle="->"))
ax.set(xlim=(.01, 100), ylim=(1, 2000), xlabel="Frequency / Hz", ylabel=r"Voltage gain magnitude $|V_{\rm out}/V_{\rm in}|$", title="Inverting low-pass amplifier")
ax.grid(which="both", alpha=.16)
ax.legend(loc="lower left", fontsize=9)
fig.savefig("paper-1-amplifier-gain.png", dpi=150, facecolor="white")
