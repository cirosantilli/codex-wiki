"""Original rigid-rotor sums, with frozen and converting spin populations."""
import numpy as np
import matplotlib.pyplot as plt

theta = 85.3
temperature = np.linspace(5, 450, 1400)
J = np.arange(41)
level = theta * J * (J + 1)
spatial = 2 * J + 1
weights = spatial[:, None] * np.exp(-level[:, None] / temperature[None, :])

def heat_capacity(w):
    prob = w / np.sum(w, axis=0)
    mean = np.sum(prob * level[:, None], axis=0)
    second = np.sum(prob * level[:, None]**2, axis=0)
    return np.maximum(0, second - mean**2) / temperature**2

even, odd = J % 2 == 0, J % 2 == 1
para = heat_capacity(weights * even[:, None])
ortho = heat_capacity(weights * odd[:, None])
normal = 0.25 * para + 0.75 * ortho
equilibrium = heat_capacity(weights * np.where(even, 1, 3)[:, None])

fig, ax = plt.subplots(figsize=(8.3, 5), constrained_layout=True)
ax.plot(temperature, para, label="para, fixed species", color="#245c9f", lw=1.8)
ax.plot(temperature, ortho, label="ortho, fixed species", color="0.45", lw=1.8)
ax.plot(temperature, normal, label="frozen 3:1 ortho:para", color="#21633d", lw=2.2)
ax.plot(temperature, equilibrium, label="continuously equilibrating", color="#b45309", lw=2.2)
ax.axvline(150, color="0.55", ls=":", lw=1.2)
ax.text(155, 2.08, "150 K", fontsize=10, color="0.35")
ax.axhline(1, color="0.75", lw=0.8, ls="--")
ax.set(xlim=(5, 450), ylim=(0, 2.2), xlabel="Temperature / K",
       ylabel=r"$C_{V,m}^{\rm rot}/R$",
       title="Hydrogen: composition changes alter the heat response")
ax.text(0.98, 0.96, r"Rotational contribution only; add $3/2$ for total gas $C_{V,m}/R$",
        transform=ax.transAxes, ha="right", va="top", fontsize=10)
ax.legend(frameon=False, loc="upper right", bbox_to_anchor=(1, 0.88), fontsize=10)
ax.spines[["top", "right"]].set_visible(False)
ax.grid(alpha=0.15)
fig.savefig("paper-2-hydrogen-heat-capacity.png", dpi=150, facecolor="white")
plt.close(fig)
