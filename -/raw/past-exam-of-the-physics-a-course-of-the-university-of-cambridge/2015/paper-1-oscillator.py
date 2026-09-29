"""Original analytical diagram; tested with Python 3.14, NumPy and Matplotlib."""
from math import factorial
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.hermite import hermval

x = np.linspace(-4, 4, 1500)
fig, ax = plt.subplots(figsize=(8.1, 5.6), layout="constrained")
ax.plot(x, x*x/2, color="0.25", lw=1.8, label=r"$V/(\hbar\omega)=\xi^2/2$")
for n in range(5):
    energy = n + 0.5
    coeff = np.zeros(n+1)
    coeff[n] = 1
    psi = hermval(x, coeff)*np.exp(-x*x/2)/np.sqrt(2**n*factorial(n)*np.sqrt(np.pi))
    color = plt.cm.viridis(0.12+0.16*n)
    ax.axhline(energy, color=color, lw=0.8, ls="--", alpha=0.65)
    ax.plot(x, energy+0.63*psi, color=color, lw=2)
    t = np.sqrt(2*n+1)
    ax.scatter([-t, t], [energy, energy], s=22, color=color, zorder=5)
    ax.text(3.05, energy+0.12, f"n={n}: {n} nodes", fontsize=8, color=color)
ax.text(-3.75, 5.25, "Dots: classical turning points; curves: rescaled amplitudes", fontsize=8, va="top")
ax.annotate("", xy=(2.8, 1.5), xytext=(2.8, 2.5), arrowprops=dict(arrowstyle="<->", color="0.2"))
ax.text(2.87, 2, r"$\hbar\omega$", fontsize=10, va="center")
ax.set(xlim=(-4, 4), ylim=(-0.1, 5.4), xlabel=r"Position $\xi=x/\ell_0$", ylabel=r"Energy / $\hbar\omega$; wavefunctions offset", title="Oscillator eigenstates and equal energy spacing")
ax.legend(loc="lower right", fontsize=9)
fig.savefig("paper-1-oscillator.png", dpi=150, facecolor="white")
