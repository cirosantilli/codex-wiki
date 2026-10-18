"""Original fixed-band equal-phase wave superpositions, plotted at t=0."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

xi = np.linspace(-12, 12, 6001)
k0, halfwidth = 18., 1.
fig, axes = plt.subplots(3, 1, figsize=(8.8, 6.1), layout="constrained", sharex=True)
envelopes = [np.cos(halfwidth*xi), np.cos(np.linspace(-halfwidth, halfwidth, 9)[:, None]*xi).mean(axis=0), np.sinc(halfwidth*xi/np.pi)]
labels = ["Two endpoint waves: periodic beats", "Nine equally spaced components: recurring groups", "Continuous flat band: sinc envelope"]
for ax, env, label in zip(axes, envelopes, labels):
    ax.plot(xi, env*np.cos(k0*xi), color="#246e99", lw=.8)
    ax.plot(xi, np.abs(env), color="#c34e38", lw=1.3, label="envelope magnitude")
    ax.plot(xi, -np.abs(env), color="#c34e38", lw=1.3)
    ax.axhline(0, color="0.5", lw=.5)
    ax.set(ylabel="Re(y)/B", ylim=(-1.14, 1.14), title=label, xlim=(-12, 12))
axes[0].legend(fontsize=8, loc="upper right")
axes[-1].set_xlabel(r"$K\xi$ with $K=1$; same bandwidth and normalized peak in all panels")
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
plt.close(fig)
