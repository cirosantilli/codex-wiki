"""Original resonant coupled-oscillator example; Python 3.14 / NumPy / Matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

m, k, coupling = 1., 1., .08
wm, wp = np.sqrt(k/m), np.sqrt((k+2*coupling)/m)
difference, average = wp-wm, (wp+wm)/2
t = np.linspace(0, 2*np.pi/difference, 4001)
slow = difference*t/2
fig, axes = plt.subplots(2, 1, figsize=(8.6, 4.7), layout="constrained", sharex=True)
for ax, values, env, label in zip(axes, [np.cos(average*t)*np.cos(slow), np.sin(average*t)*np.sin(slow)], [np.abs(np.cos(slow)), np.abs(np.sin(slow))], [r"$x_1/A$", r"$x_2/A$"]):
    ax.fill_between(t*difference/np.pi, -env, env, color="#d5e8f5")
    ax.plot(t*difference/np.pi, values, color="#145d88", lw=1)
    ax.plot(t*difference/np.pi, env, "--", color="#555555", lw=.8)
    ax.plot(t*difference/np.pi, -env, "--", color="#555555", lw=.8)
    ax.axhline(0, color="0.5", lw=.5)
    ax.set(ylabel=label, ylim=(-1.12, 1.12), xlim=(0, 2))
axes[-1].set_xlabel(r"$t\,\Delta\omega/\pi$ (one envelope exchange at 1)")
fig.suptitle(r"Equal end springs, $m=k=1$, $k_{12}=0.08$; initially only mass 1 displaced", fontsize=12)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
plt.close(fig)
