"""Python 3.14; NumPy/Matplotlib versions in ../pyproject.toml. Output in CWD."""
from math import erf
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
phi = np.vectorize(lambda x: (1+erf(x/np.sqrt(2)))/2)
s = np.linspace(.001, 2.1, 900)
r, vol, tau, strike, cost = .04, .35, 1, 1, .25
d1 = (np.log(s/strike)+(r+vol**2/2)*tau)/(vol*np.sqrt(tau))
d2 = d1-vol*np.sqrt(tau)
put = strike*np.exp(-r*tau)*phi(-d2)-s*phi(-d1)
call = s*phi(d1)-strike*np.exp(-r*tau)*phi(d2)
h = np.maximum(np.maximum(put, call)-cost, 0)
fig, ax = plt.subplots(figsize=(7.2, 4.3), facecolor="white")
ax.plot(s, put-cost, color="C1", ls="--", label="Put value minus exercise cost")
ax.plot(s, call-cost, color="C2", ls="--", label="Call value minus exercise cost")
ax.plot(s, h, color="C0", lw=2.8, label="Chooser payoff")
ax.axvline(np.exp(-r*tau), color="0.55", ls=":", lw=1)
ax.text(np.exp(-r*tau)+.02, .7, r"$D=K_3e^{-r\tau}$")
ax.axhline(0, color="0.5", lw=.7)
ax.set(xlabel="Stock spot at choice time", ylabel="Value / underlying strike", xlim=(0, 2.1), ylim=(-.28, 1.02), title="Positive exercise cost can create an inaction interval")
ax.spines[["top", "right"]].set_visible(False)
ax.legend(frameon=False, fontsize=9)
fig.tight_layout()
fig.savefig("2009-chooser.png", dpi=150, facecolor="white")
