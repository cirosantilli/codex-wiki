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
h = np.maximum(put-cost, 0)
threshold = np.interp(cost, put[::-1], s[::-1])
fig, ax = plt.subplots(figsize=(7.2, 4.3), facecolor="white")
ax.plot(s, put, color="0.65", ls="--", label="Underlying put value")
ax.plot(s, h, lw=2.6, label="Call-on-put payoff")
ax.axvline(threshold, color="0.5", ls=":", lw=1)
ax.text(threshold+.025, .17, r"$s_*$")
ax.set(xlabel="Stock spot at compound-option expiry", ylabel="Value / underlying strike", xlim=(0, 2.1), ylim=(-.025, 1.03), title="Pay to acquire the put only at low stock spots")
ax.spines[["top", "right"]].set_visible(False)
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig("2009-call-on-put.png", dpi=150, facecolor="white")
