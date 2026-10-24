"""Python 3.14; NumPy/Matplotlib versions are recorded in ../pyproject.toml. Output in CWD."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
x = np.linspace(0, 2.6, 500)
fig, ax = plt.subplots(figsize=(7.2, 4.3), facecolor="white")
ax.plot(x, np.minimum(x, 1), lw=2.6, label="Total debt / face value")
ax.plot(x, np.maximum(x-1, 0), lw=2.6, label="Total equity / face value")
ax.axvline(1, color="0.55", ls="--", lw=1)
ax.text(1.03, 1.72, "Debt fully repaid", color="0.3")
ax.set(xlabel="Terminal company value / debt face value", ylabel="Payoff / debt face value", xlim=(0, 2.6), ylim=(-.04, 1.9), title="Debt and equity split the company value")
ax.spines[["top", "right"]].set_visible(False)
ax.legend(loc="upper left", frameon=False)
fig.tight_layout()
fig.savefig("2009-capital-structure-payoffs.png", dpi=150, facecolor="white")
