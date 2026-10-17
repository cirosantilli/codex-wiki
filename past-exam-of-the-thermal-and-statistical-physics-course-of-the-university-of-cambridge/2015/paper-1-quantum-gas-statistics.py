"""Original ideal-gas statistical curves; Python 3.14, NumPy, Matplotlib."""
import numpy as np
import matplotlib.pyplot as plt

fig, (bec, fd) = plt.subplots(1, 2, figsize=(9.4, 4.4), layout="constrained")
t = np.linspace(0, 1.5, 800)
fraction = np.maximum(0, 1-t**1.5)
bec.plot(t, fraction, lw=2.5)
bec.axvline(1, color="0.5", ls=":", lw=1)
bec.text(.1, .18, r"$N_0/N=1-(T/T_c)^{3/2}$", fontsize=11)
bec.set(xlabel=r"Temperature $T/T_c$", ylabel=r"Condensate fraction $N_0/N$", title="Uniform ideal Bose gas in a 3D box", xlim=(0, 1.5), ylim=(0, 1.05))
x = np.linspace(-.6, .6, 1200)
fd.plot(x, (x<0).astype(float), color=".3", ls="--", label="Zero-temperature limit")
for width in [.04, .10, .20]:
    fd.plot(x, 1/(np.exp(x/width)+1), lw=2, label=rf"$k_BT/E_0={width:.2f}$")
fd.set(xlabel=r"Energy offset $(\epsilon-\mu)/E_0$", ylabel="Single-state mean occupation", title="Fermi distribution about fixed chemical potential", xlim=(-.6, .6), ylim=(0, 1.05))
fd.legend(fontsize=8, loc="lower left")
for ax in [bec, fd]:
    ax.grid(alpha=.17)
fig.savefig("paper-1-quantum-gas-statistics.png", dpi=150, facecolor="white")
