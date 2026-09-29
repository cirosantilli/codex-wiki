"""Original dimensionless Langmuir curve; Python 3.14, NumPy, Matplotlib."""
import numpy as np
import matplotlib.pyplot as plt

p = np.linspace(0, 12, 1200)
theta = p/(1+p)
fig, ax = plt.subplots(figsize=(7.5, 4.6), layout="constrained")
ax.plot(p, theta, color="#175b98", lw=2.5, label=r"$\theta=b_sp/(1+b_sp)$")
low = np.linspace(0, .65, 100)
ax.plot(low, low, "--", color="#b86723", lw=1.5, label=r"Low-pressure tangent: $\theta\simeq b_sp$")
ax.axhline(1, color=".4", ls=":", lw=1.3)
ax.plot([1, 1, 0], [0, .5, .5], ":", color=".5", lw=1)
ax.scatter([1], [.5], color="#175b98", s=35, zorder=4)
ax.annotate("Half coverage:\n$p=1/b_s$", xy=(1, .5), xytext=(2.5, .35), arrowprops=dict(arrowstyle="->"), fontsize=11)
ax.text(6.3, 1.015, r"Saturation: $\theta\to1$", fontsize=10)
ax.set(xlabel=r"Pressure $p/p_{1/2}=b_sp$ at fixed temperature", ylabel=r"Occupied fraction $\theta$", title="Independent-site adsorption isotherm", xlim=(0, 12), ylim=(0, 1.09))
ax.grid(alpha=.16)
ax.legend(loc="lower right", fontsize=9)
fig.savefig("paper-1-adsorption-isotherm.png", dpi=150, facecolor="white")
