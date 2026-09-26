from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


output = Path(Path(__file__).stem + ".png")
X = np.linspace(-5.0, 5.0, 1001)
eta = np.where(X < 0.0, -0.5 + 0.5 * np.exp(X), 0.5 - 0.5 * np.exp(-X))
v = 0.5 * np.exp(-np.abs(X))

fig, (ax_eta, ax_v) = plt.subplots(2, 1, figsize=(7.2, 6.0), sharex=True)
ax_eta.axhline(0.0, color="black", linewidth=0.7)
ax_eta.axvline(0.0, color="black", linewidth=0.7, linestyle=":")
ax_eta.plot(X, eta, color="tab:blue")
ax_eta.set_ylabel(r"$\frac{f}{h(q_1-q_2)}\left(\eta+\frac{h(q_1+q_2)}{2f}\right)$")
ax_eta.set_title(r"Free surface and jet for a PV step with $q_1>q_2$")
ax_eta.set_yticks([-0.5, 0.0, 0.5])

ax_v.axhline(0.0, color="black", linewidth=0.7)
ax_v.axvline(0.0, color="black", linewidth=0.7, linestyle=":")
ax_v.plot(X, v, color="tab:orange")
ax_v.set_xlabel(r"$x/R$")
ax_v.set_ylabel(r"$v/[R(q_1-q_2)]$")
ax_v.set_yticks([0.0, 0.25, 0.5])

fig.tight_layout()
fig.savefig(output, dpi=160, facecolor="white")
